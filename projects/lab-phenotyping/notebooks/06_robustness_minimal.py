from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.impute import KNNImputer
from sklearn.metrics import silhouette_score
from sklearn.preprocessing import RobustScaler


@dataclass
class Paths:
    project_root: Path
    data_raw: Path
    data_processed: Path
    outputs_robustness: Path
    tables_dir: Path
    supplementary_dir: Path


def resolve_paths() -> Paths:
    root = Path(__file__).resolve().parents[1]
    outputs_robustness = root / "outputs" / "robustness"
    tables_dir = root / "tables"
    supplementary_dir = root / "supplementary"

    outputs_robustness.mkdir(parents=True, exist_ok=True)
    tables_dir.mkdir(parents=True, exist_ok=True)
    supplementary_dir.mkdir(parents=True, exist_ok=True)

    return Paths(
        project_root=root,
        data_raw=root / "data" / "raw",
        data_processed=root / "data" / "processed",
        outputs_robustness=outputs_robustness,
        tables_dir=tables_dir,
        supplementary_dir=supplementary_dir,
    )


def clip_iqr(df: pd.DataFrame, cols: list[str], k: float = 3.0) -> pd.DataFrame:
    out = df.copy()
    for col in cols:
        q1 = out[col].quantile(0.25)
        q3 = out[col].quantile(0.75)
        iqr = q3 - q1
        lo = q1 - k * iqr
        hi = q3 + k * iqr
        out[col] = out[col].clip(lo, hi)
    return out


def load_if_exists(path: Path) -> pd.DataFrame | None:
    if not path.exists():
        return None
    return pd.read_csv(path, low_memory=False)


def run_no_age_sensitivity(
    features: pd.DataFrame,
    clusters: pd.DataFrame | None,
    out_dir: Path,
) -> dict[str, object]:
    vars_with_age = ["LEUCO", "PLAQ", "CREATININA", "UREIA", "PCR", "TGO", "TGP", "idade"]
    vars_without_age = ["LEUCO", "PLAQ", "CREATININA", "UREIA", "PCR", "TGO", "TGP"]

    missing_cols = [col for col in vars_with_age if col not in features.columns]
    if missing_cols:
        raise ValueError(f"Missing required columns for no-age sensitivity: {missing_cols}")

    df = features.copy()
    x = df[vars_without_age].copy()
    x = clip_iqr(x, vars_without_age)
    for col in vars_without_age:
        x[col] = np.log1p(x[col])

    imputer = KNNImputer(n_neighbors=5)
    x_imp = imputer.fit_transform(x)
    scaler = RobustScaler()
    x_scaled = scaler.fit_transform(x_imp)

    scores = []
    for k in range(2, 7):
        km = KMeans(n_clusters=k, random_state=42, n_init=100)
        labels = km.fit_predict(x_scaled)
        scores.append({"k": k, "silhouette": float(silhouette_score(x_scaled, labels))})
    pd.DataFrame(scores).to_csv(out_dir / "no_age_silhouette_scores.csv", index=False)

    km = KMeans(n_clusters=3, random_state=42, n_init=200)
    df["cluster_no_age"] = km.fit_predict(x_scaled)

    no_age_dist = (
        df["cluster_no_age"].value_counts().sort_index().rename_axis("cluster_no_age").reset_index(name="count")
    )
    no_age_dist["pct"] = (no_age_dist["count"] / len(df) * 100).round(4)
    no_age_dist.to_csv(out_dir / "no_age_cluster_distribution.csv", index=False)

    profile_rows: list[dict[str, object]] = []
    for cluster_value, sub_df in df.groupby("cluster_no_age"):
        for col in vars_with_age:
            series = sub_df[col].dropna()
            if series.empty:
                continue
            profile_rows.append(
                {
                    "cluster_no_age": int(cluster_value),
                    "variable": col,
                    "count": int(series.shape[0]),
                    "median": float(series.median()),
                    "q1": float(series.quantile(0.25)),
                    "q3": float(series.quantile(0.75)),
                }
            )
    no_age_profile = pd.DataFrame(profile_rows)
    no_age_profile.to_csv(out_dir / "no_age_cluster_profile_summary.csv", index=False)

    comparison_rows: list[dict[str, object]] = []
    if clusters is not None and "cluster" in clusters.columns and "numero_do_atendimento" in clusters.columns:
        current_dist = (
            clusters["cluster"].value_counts().sort_index().rename_axis("cluster").reset_index(name="count")
        )
        current_dist["pct"] = (current_dist["count"] / len(clusters) * 100).round(4)
        current_dist.to_csv(out_dir / "current_cluster_distribution.csv", index=False)

        merged = df.merge(
            clusters[["numero_do_atendimento", "cluster"]].drop_duplicates(),
            on="numero_do_atendimento",
            how="left",
        )
        if merged["cluster"].notna().any():
            for cluster_value, sub_df in merged.groupby("cluster_no_age"):
                comparison_rows.append(
                    {
                        "cluster_no_age": int(cluster_value),
                        "dominant_current_cluster": sub_df["cluster"].mode(dropna=True).iloc[0]
                        if sub_df["cluster"].dropna().any()
                        else None,
                        "median_age": float(sub_df["idade"].median()),
                        "median_pcr": float(sub_df["PCR"].median()),
                        "median_creatinina": float(sub_df["CREATININA"].median()),
                        "median_ureia": float(sub_df["UREIA"].median()),
                    }
                )
    pd.DataFrame(comparison_rows).to_csv(out_dir / "no_age_cluster_comparison.csv", index=False)

    # Heuristic check for persistence of inflammatory-renal phenotype in no-age rerun.
    inflammatory_renal_score = (
        no_age_profile[no_age_profile["variable"].isin(["PCR", "CREATININA", "UREIA"])]
        .groupby("cluster_no_age")["median"]
        .mean()
    )
    persistent_cluster = (
        int(inflammatory_renal_score.idxmax()) if not inflammatory_renal_score.empty else None
    )

    return {
        "rows": len(df),
        "silhouette_k3": float(
            pd.DataFrame(scores).loc[pd.DataFrame(scores)["k"] == 3, "silhouette"].iloc[0]
        ),
        "inflammatory_renal_like_cluster_no_age": persistent_cluster,
    }


def run_repeated_encounter_analysis(
    dataset_expandido: pd.DataFrame,
    clusters: pd.DataFrame | None,
    out_dir: Path,
) -> dict[str, object]:
    required = {"numero_do_atendimento", "data_de_entrada"}
    missing = required - set(dataset_expandido.columns)
    if missing:
        raise ValueError(f"Missing required columns for repeated-encounter analysis: {sorted(missing)}")

    if "patient_id" not in dataset_expandido.columns:
        raise ValueError("patient_id column is required for repeated-encounter analysis")

    df = dataset_expandido.copy()
    df["data_de_entrada"] = pd.to_datetime(df["data_de_entrada"], errors="coerce")

    encounter_patient = (
        df.sort_values("data_de_entrada")
        .groupby("numero_do_atendimento", as_index=False)[["patient_id", "data_de_entrada"]]
        .first()
    )

    total_encounters = int(encounter_patient["numero_do_atendimento"].nunique())
    unique_patients = int(encounter_patient["patient_id"].nunique())

    encounters_per_patient = (
        encounter_patient.groupby("patient_id")["numero_do_atendimento"]
        .nunique()
        .rename("encounters")
        .reset_index()
    )

    repeated_patient_count = int((encounters_per_patient["encounters"] > 1).sum())
    repeated_encounters = int(
        encounters_per_patient.loc[encounters_per_patient["encounters"] > 1, "encounters"].sum()
        - repeated_patient_count
    )

    encounters_per_patient["encounter_bin"] = pd.cut(
        encounters_per_patient["encounters"],
        bins=[0, 1, 2, 5, 10, np.inf],
        labels=["1", "2", "3-5", "6-10", ">10"],
        right=True,
    )
    encounter_dist = (
        encounters_per_patient["encounter_bin"].value_counts(dropna=False).sort_index().reset_index()
    )
    encounter_dist.columns = ["encounters_per_patient_bin", "patient_count"]
    encounter_dist["pct_of_patients"] = (
        encounter_dist["patient_count"] / len(encounters_per_patient) * 100
    ).round(4)
    encounter_dist.to_csv(out_dir / "encounters_per_patient_distribution.csv", index=False)

    summary = pd.DataFrame(
        [
            {
                "total_encounters": total_encounters,
                "unique_patients": unique_patients,
                "repeated_patient_count": repeated_patient_count,
                "repeated_encounters_beyond_first": repeated_encounters,
            }
        ]
    )
    summary.to_csv(out_dir / "repeated_encounter_summary.csv", index=False)

    if clusters is not None and {"numero_do_atendimento", "cluster"}.issubset(clusters.columns):
        cluster_df = clusters[["numero_do_atendimento", "cluster"]].drop_duplicates().copy()

        all_prev = (
            cluster_df["cluster"].value_counts().sort_index().rename_axis("cluster").reset_index(name="count")
        )
        all_prev["analysis_set"] = "all_encounters"
        all_prev["pct"] = (all_prev["count"] / len(cluster_df) * 100).round(4)

        first_encounter = (
            encounter_patient.sort_values("data_de_entrada")
            .groupby("patient_id", as_index=False)
            .first()[["patient_id", "numero_do_atendimento"]]
        )
        first_prev = (
            first_encounter.merge(cluster_df, on="numero_do_atendimento", how="left")
            ["cluster"]
            .value_counts()
            .sort_index()
            .rename_axis("cluster")
            .reset_index(name="count")
        )
        first_prev["analysis_set"] = "first_encounter_only"
        first_prev["pct"] = (first_prev["count"] / first_prev["count"].sum() * 100).round(4)

        cluster_prev = pd.concat([all_prev, first_prev], ignore_index=True)
        cluster_prev.to_csv(out_dir / "cluster_prevalence_all_vs_first_encounter.csv", index=False)

    return {
        "total_encounters": total_encounters,
        "unique_patients": unique_patients,
        "repeated_patients": repeated_patient_count,
        "repeated_encounters_beyond_first": repeated_encounters,
    }


def run_testing_intensity_analysis(
    dataset_expandido: pd.DataFrame,
    features_emergency: pd.DataFrame | None,
    out_dir: Path,
) -> dict[str, object]:
    vars_keep = [
        "PCR",
        "LEUCO",
        "PLAQ",
        "CREATININA",
        "UREIA",
        "TGO",
        "TGP",
        "FOSFATASE_ALCALINA",
        "BILIRRUBINA",
        "SODIO",
        "POTASSIO",
        "GLICOSE",
        "LDH",
        "CPK",
        "TAP",
    ]

    needed = {"numero_do_atendimento", "exame_padronizado"}
    missing = needed - set(dataset_expandido.columns)
    if missing:
        raise ValueError(f"Missing required columns for testing-intensity analysis: {sorted(missing)}")

    df = dataset_expandido.copy()
    df = df[df["exame_padronizado"].isin(vars_keep)].copy()

    peak = (
        df.groupby(["numero_do_atendimento", "exame_padronizado"], as_index=False)["valor_num"]
        .max()
    )
    features_before = (
        peak.pivot_table(
            index="numero_do_atendimento",
            columns="exame_padronizado",
            values="valor_num",
            aggfunc="first",
        )
        .reset_index()
    )
    features_before["n_exames"] = features_before[[c for c in vars_keep if c in features_before.columns]].notna().sum(axis=1)

    encounters_before = int(features_before["numero_do_atendimento"].nunique())
    encounters_after = int((features_before["n_exames"] >= 6).sum())

    summary = pd.DataFrame(
        [
            {
                "encounters_before_filter": encounters_before,
                "encounters_after_filter": encounters_after,
                "excluded_encounters": encounters_before - encounters_after,
                "retained_pct": round(encounters_after / encounters_before * 100, 4)
                if encounters_before
                else None,
            }
        ]
    )
    summary.to_csv(out_dir / "testing_intensity_filter_summary.csv", index=False)

    bucket = pd.cut(
        features_before["n_exames"],
        bins=[0, 3, 5, 7, 10, np.inf],
        labels=["1-3", "4-5", "6-7", "8-10", ">10"],
        right=True,
    )
    n_exam_dist = bucket.value_counts(dropna=False).sort_index().reset_index()
    n_exam_dist.columns = ["n_exames_bin", "encounter_count"]
    n_exam_dist["pct"] = (n_exam_dist["encounter_count"] / len(features_before) * 100).round(4)
    n_exam_dist.to_csv(out_dir / "testing_intensity_distribution.csv", index=False)

    char_rows: list[dict[str, object]] = []
    for label, sub_df in {
        "pre_filter_all": features_before,
        "post_filter_ge6": features_before[features_before["n_exames"] >= 6].copy(),
        "excluded_lt6": features_before[features_before["n_exames"] < 6].copy(),
    }.items():
        row: dict[str, object] = {
            "group": label,
            "encounters": int(sub_df["numero_do_atendimento"].nunique()),
            "median_n_exames": float(sub_df["n_exames"].median()) if not sub_df.empty else None,
        }
        if features_emergency is not None and "numero_do_atendimento" in features_emergency.columns:
            merged = sub_df.merge(
                features_emergency[["numero_do_atendimento", "idade", "sexo", "codigo_da_unidade"]].drop_duplicates(),
                on="numero_do_atendimento",
                how="left",
            )
            if "idade" in merged.columns:
                row["median_idade"] = float(merged["idade"].median()) if merged["idade"].notna().any() else None
            if "sexo" in merged.columns:
                row["female_pct"] = round((merged["sexo"] == "F").mean() * 100, 4) if merged["sexo"].notna().any() else None
            if "codigo_da_unidade" in merged.columns:
                row["adult_emergency_pct"] = round(merged["codigo_da_unidade"].isin([5, 6]).mean() * 100, 4)
                row["pediatric_emergency_pct"] = round((merged["codigo_da_unidade"] == 4).mean() * 100, 4)
        char_rows.append(row)
    pd.DataFrame(char_rows).to_csv(out_dir / "testing_intensity_group_characteristics.csv", index=False)

    return {
        "encounters_before_filter": encounters_before,
        "encounters_after_filter": encounters_after,
    }


def write_summary_markdown(
    out_dir: Path,
    supplementary_dir: Path,
    statuses: list[str],
    no_age: dict[str, object] | None,
    repeated: dict[str, object] | None,
    testing: dict[str, object] | None,
) -> None:
    lines = [
        "# Minimal Robustness Execution Summary",
        "",
        "This report contains aggregate-only robustness outputs.",
        "",
        "## Execution Status",
        "",
    ]
    lines.extend([f"- {item}" for item in statuses])

    lines.extend(["", "## No-age sensitivity", ""])
    if no_age is None:
        lines.append("- Not executed.")
    else:
        lines.append(f"- Rows analyzed: `{no_age['rows']}`")
        lines.append(f"- Silhouette at k=3 without age: `{no_age['silhouette_k3']:.4f}`")
        lines.append(
            f"- No-age cluster with strongest inflammatory-renal signature: `{no_age['inflammatory_renal_like_cluster_no_age']}`"
        )

    lines.extend(["", "## Repeated encounters", ""])
    if repeated is None:
        lines.append("- Not executed.")
    else:
        lines.append(f"- Total encounters: `{repeated['total_encounters']}`")
        lines.append(f"- Unique patients: `{repeated['unique_patients']}`")
        lines.append(f"- Repeated patients: `{repeated['repeated_patients']}`")
        lines.append(
            f"- Repeated encounters beyond first: `{repeated['repeated_encounters_beyond_first']}`"
        )

    lines.extend(["", "## Testing intensity filter", ""])
    if testing is None:
        lines.append("- Not executed.")
    else:
        lines.append(f"- Encounters before filter: `{testing['encounters_before_filter']}`")
        lines.append(f"- Encounters after filter: `{testing['encounters_after_filter']}`")

    text = "\n".join(lines)
    (out_dir / "robustness_minimal_summary.md").write_text(text, encoding="utf-8")
    (supplementary_dir / "robustness_minimal_summary.md").write_text(text, encoding="utf-8")


def main() -> None:
    paths = resolve_paths()

    features_path = paths.data_processed / "features_24h_peak_emergency.csv"
    clusters_path = paths.data_processed / "clusters_kmeans_robust_final_with_care_setting.csv"
    expandido_path = paths.data_processed / "dataset_laboratorial_expandido.csv"

    features = load_if_exists(features_path)
    clusters = load_if_exists(clusters_path)
    dataset_expandido = load_if_exists(expandido_path)

    statuses: list[str] = []
    no_age_result: dict[str, object] | None = None
    repeated_result: dict[str, object] | None = None
    testing_result: dict[str, object] | None = None

    if features is None:
        statuses.append(f"Missing input: `{features_path}`")
    if clusters is None:
        statuses.append(f"Missing input: `{clusters_path}`")
    if dataset_expandido is None:
        statuses.append(f"Missing input: `{expandido_path}`")

    try:
        if features is not None:
            no_age_result = run_no_age_sensitivity(features, clusters, paths.outputs_robustness)
            statuses.append("No-age sensitivity executed.")
        else:
            statuses.append("No-age sensitivity skipped due to missing features dataset.")
    except Exception as exc:  # pragma: no cover - defensive status capture
        statuses.append(f"No-age sensitivity failed: {exc}")

    try:
        if dataset_expandido is not None:
            repeated_result = run_repeated_encounter_analysis(
                dataset_expandido,
                clusters,
                paths.outputs_robustness,
            )
            statuses.append("Repeated-encounter analysis executed.")
        else:
            statuses.append("Repeated-encounter analysis skipped due to missing expanded dataset.")
    except Exception as exc:  # pragma: no cover
        statuses.append(f"Repeated-encounter analysis failed: {exc}")

    try:
        if dataset_expandido is not None:
            testing_result = run_testing_intensity_analysis(
                dataset_expandido,
                features,
                paths.outputs_robustness,
            )
            statuses.append("Testing-intensity analysis executed.")
        else:
            statuses.append("Testing-intensity analysis skipped due to missing expanded dataset.")
    except Exception as exc:  # pragma: no cover
        statuses.append(f"Testing-intensity analysis failed: {exc}")

    write_summary_markdown(
        paths.outputs_robustness,
        paths.supplementary_dir,
        statuses,
        no_age_result,
        repeated_result,
        testing_result,
    )


if __name__ == "__main__":
    main()
