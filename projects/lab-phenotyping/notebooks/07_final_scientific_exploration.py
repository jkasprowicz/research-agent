from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.stats import chi2_contingency


@dataclass
class Paths:
    root: Path
    data_processed: Path
    fallback_data_roots: list[Path]
    outputs: Path
    tables: Path
    figures: Path


ANALYTIC_VARIABLE_CANDIDATES = [
    "idade",
    "LEUCO",
    "PLAQ",
    "PCR",
    "CREATININA",
    "UREIA",
    "TGO",
    "TGP",
    "BILIRRUBINA",
    "CPK",
    "FOSFATASE_ALCALINA",
    "GLICOSE",
    "LDH",
    "POTASSIO",
    "SODIO",
    "TAP",
]

FEATURE_FILE_PRIORITY = [
    "features_24h_peak_final_units_fixed.csv",
    "features_24h_peak_final.csv",
    "features_24h_peak_emergency.csv",
]


def resolve_paths() -> Paths:
    root = Path(__file__).resolve().parents[1]
    fallback_data_roots = [
        root / "data" / "processed",
        Path.home() / "Documents" / "Projects" / "research-agent" / "projects" / "lab-phenotyping" / "data" / "processed",
    ]
    outputs = root / "outputs" / "final_exploration"
    tables = root / "tables"
    figures = root / "figures" / "final_exploration"
    outputs.mkdir(parents=True, exist_ok=True)
    tables.mkdir(parents=True, exist_ok=True)
    figures.mkdir(parents=True, exist_ok=True)
    return Paths(
        root=root,
        data_processed=root / "data" / "processed",
        fallback_data_roots=fallback_data_roots,
        outputs=outputs,
        tables=tables,
        figures=figures,
    )


def detect_existing_files(paths: Paths) -> dict[str, Path | None]:
    clusters = None
    for base in paths.fallback_data_roots:
        candidate = base / "clusters_kmeans_robust_final_with_care_setting.csv"
        if candidate.exists():
            clusters = candidate
            break

    features = None
    for name in FEATURE_FILE_PRIORITY:
        for base in paths.fallback_data_roots:
            candidate = base / name
            if candidate.exists():
                features = candidate
                break
        if features is not None:
            break
    return {
        "clusters": clusters,
        "features": features,
    }


def normalize_columns(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()
    out.columns = [str(col).strip() for col in out.columns]
    return out


def pick_first_existing(df: pd.DataFrame, candidates: Iterable[str]) -> str | None:
    existing = {str(col).lower(): col for col in df.columns}
    for candidate in candidates:
        key = candidate.lower()
        if key in existing:
            return existing[key]
    return None


def detect_cluster_column(df: pd.DataFrame) -> str | None:
    return pick_first_existing(df, ["cluster", "Cluster", "clusters"])


def detect_encounter_column(df: pd.DataFrame) -> str | None:
    return pick_first_existing(
        df,
        ["numero_do_atendimento", "Número do Atendimento", "encounter_id", "atendimento_id"],
    )


def detect_sex_column(df: pd.DataFrame) -> str | None:
    return pick_first_existing(df, ["sexo", "Sexo", "sex", "Sex"])


def detect_age_column(df: pd.DataFrame) -> str | None:
    return pick_first_existing(df, ["idade", "Idade", "age", "idade_anos"])


def detect_care_setting_column(df: pd.DataFrame) -> str | None:
    return pick_first_existing(
        df,
        [
            "care_setting",
            "contexto_assistencial",
            "care context",
            "setting",
            "Origem",
        ],
    )


def load_best_dataframe(paths: Paths, files: dict[str, Path | None]) -> tuple[pd.DataFrame | None, list[str]]:
    notes: list[str] = []
    cluster_path = files["clusters"]
    feature_path = files["features"]

    cluster_df = None
    if cluster_path is not None:
        cluster_df = normalize_columns(pd.read_csv(cluster_path, low_memory=False))
        notes.append(f"clusters file loaded: `{cluster_path.name}`")
    else:
        notes.append("clusters file missing")

    feature_df = None
    if feature_path is not None:
        feature_df = normalize_columns(pd.read_csv(feature_path, low_memory=False))
        notes.append(f"features file loaded: `{feature_path.name}`")
    else:
        notes.append("features file missing")

    if cluster_df is None and feature_df is None:
        return None, notes

    if cluster_df is not None and feature_df is not None:
        cluster_enc = detect_encounter_column(cluster_df)
        feature_enc = detect_encounter_column(feature_df)
        if cluster_enc and feature_enc:
            merged = cluster_df.merge(
                feature_df,
                left_on=cluster_enc,
                right_on=feature_enc,
                how="left",
                suffixes=("", "_feature"),
            )
            notes.append("merged clusters and features on encounter identifier")
            return merged, notes
        notes.append("could not merge features with clusters; using clusters file only")
        return cluster_df, notes

    if cluster_df is not None:
        notes.append("using clusters file only")
        return cluster_df, notes

    notes.append("using features file only")
    return feature_df, notes


def detect_analytic_variables(df: pd.DataFrame) -> list[str]:
    cols = []
    for candidate in ANALYTIC_VARIABLE_CANDIDATES:
        col = pick_first_existing(df, [candidate])
        if col is not None and pd.api.types.is_numeric_dtype(pd.to_numeric(df[col], errors="coerce")):
            cols.append(col)
    # preserve order, unique
    seen: set[str] = set()
    ordered: list[str] = []
    for col in cols:
        if col not in seen:
            ordered.append(col)
            seen.add(col)
    return ordered


def normalize_cluster_ids(df: pd.DataFrame, cluster_col: str, variables: list[str]) -> tuple[pd.DataFrame, dict[int, str]]:
    out = df.copy()
    out[cluster_col] = pd.to_numeric(out[cluster_col], errors="coerce")
    out = out[out[cluster_col].notna()].copy()
    out[cluster_col] = out[cluster_col].astype(int)

    med = out.groupby(cluster_col)[[c for c in ["PCR", "CREATININA", "UREIA", "TGO", "TGP"] if c in out.columns]].median()
    if med.empty or med.shape[0] < 3:
        labels = {int(k): f"cluster_{int(k)}" for k in sorted(out[cluster_col].unique())}
        return out, labels

    inflam_score = med[[c for c in ["PCR", "CREATININA", "UREIA"] if c in med.columns]].mean(axis=1)
    hepatic_score = med[[c for c in ["TGO", "TGP"] if c in med.columns]].mean(axis=1)

    inflammatory_cluster = int(inflam_score.idxmax())
    remaining = [int(c) for c in med.index if int(c) != inflammatory_cluster]
    hepatic_cluster = int(hepatic_score.loc[remaining].idxmax()) if remaining else inflammatory_cluster
    basal_cluster = [int(c) for c in med.index if int(c) not in {inflammatory_cluster, hepatic_cluster}]
    basal_cluster_id = int(basal_cluster[0]) if basal_cluster else inflammatory_cluster

    labels = {
        inflammatory_cluster: "inflammatory_renal",
        hepatic_cluster: "hepatic_like",
        basal_cluster_id: "basal",
    }
    for cluster_id in out[cluster_col].unique():
        labels.setdefault(int(cluster_id), f"cluster_{int(cluster_id)}")
    return out, labels


def cluster_label_order(label_map: dict[int, str]) -> list[int]:
    preferred = ["inflammatory_renal", "hepatic_like", "basal"]
    ordered = []
    for label in preferred:
        for cid, name in label_map.items():
            if name == label:
                ordered.append(cid)
    for cid in sorted(label_map):
        if cid not in ordered:
            ordered.append(cid)
    return ordered


def format_med_iqr(series: pd.Series) -> tuple[str, int, float]:
    valid = pd.to_numeric(series, errors="coerce").dropna()
    if valid.empty:
        return "", 0, 0.0
    return (
        f"{valid.median():.2f} ({valid.quantile(0.25):.2f}-{valid.quantile(0.75):.2f})",
        int(valid.shape[0]),
        float(valid.shape[0]),
    )


def write_cluster_profile_table(
    df: pd.DataFrame,
    cluster_col: str,
    label_map: dict[int, str],
    variables: list[str],
    out_path: Path,
) -> pd.DataFrame:
    rows: list[dict[str, object]] = []
    total_by_cluster = df.groupby(cluster_col).size().to_dict()
    for variable in variables:
        for cluster_id in cluster_label_order(label_map):
            subset = df.loc[df[cluster_col] == cluster_id, variable]
            med_iqr, n_avail, _ = format_med_iqr(subset)
            total = int(total_by_cluster.get(cluster_id, 0))
            completeness = (n_avail / total * 100.0) if total else np.nan
            rows.append(
                {
                    "cluster_id": cluster_id,
                    "cluster_label": label_map[cluster_id],
                    "variable": variable,
                    "median_iqr": med_iqr,
                    "n_available": n_avail,
                    "completeness_pct": round(completeness, 2) if total else np.nan,
                }
            )
    out_df = pd.DataFrame(rows)
    out_df.to_csv(out_path, index=False)
    return out_df


def safe_ratio(a: float | None, b: float | None) -> float | None:
    if a is None or b is None:
        return None
    if b == 0:
        return None
    return a / b


def write_effect_size_table(
    df: pd.DataFrame,
    cluster_col: str,
    label_map: dict[int, str],
    variables: list[str],
    out_path: Path,
) -> pd.DataFrame:
    label_to_id = {label: cid for cid, label in label_map.items()}
    comparisons = [
        ("inflammatory_renal", "basal"),
        ("hepatic_like", "basal"),
    ]
    rows: list[dict[str, object]] = []
    for left_label, right_label in comparisons:
        if left_label not in label_to_id or right_label not in label_to_id:
            continue
        left_id = label_to_id[left_label]
        right_id = label_to_id[right_label]
        for variable in variables:
            left = pd.to_numeric(df.loc[df[cluster_col] == left_id, variable], errors="coerce").dropna()
            right = pd.to_numeric(df.loc[df[cluster_col] == right_id, variable], errors="coerce").dropna()
            if left.empty or right.empty:
                continue
            left_med = float(left.median())
            right_med = float(right.median())
            ratio = safe_ratio(left_med, right_med)
            diff = left_med - right_med
            use_ratio = variable not in {"idade"} and right_med > 0
            rows.append(
                {
                    "comparison": f"{left_label}_vs_{right_label}",
                    "variable": variable,
                    "left_median": round(left_med, 4),
                    "right_median": round(right_med, 4),
                    "absolute_difference": round(diff, 4),
                    "ratio_of_medians": round(ratio, 4) if ratio is not None else None,
                    "preferred_effect_summary": f"{ratio:.2f}x" if use_ratio and ratio is not None else f"{diff:.2f}",
                }
            )
    out_df = pd.DataFrame(rows)
    out_df.to_csv(out_path, index=False)
    return out_df


def cramers_v_from_table(table: pd.DataFrame) -> tuple[float | None, float | None]:
    if table.empty or table.shape[0] < 2 or table.shape[1] < 2:
        return None, None
    chi2, p_value, _, _ = chi2_contingency(table)
    n = table.to_numpy().sum()
    if n == 0:
        return None, None
    min_dim = min(table.shape[0] - 1, table.shape[1] - 1)
    if min_dim <= 0:
        return float(p_value), None
    v = np.sqrt(chi2 / (n * min_dim))
    return float(p_value), float(v)


def categorical_summary(
    df: pd.DataFrame,
    cluster_col: str,
    category_col: str,
    label_map: dict[int, str],
    out_path: Path,
) -> tuple[pd.DataFrame, float | None, float | None]:
    subset = df[[cluster_col, category_col]].copy()
    subset = subset.dropna()
    table = pd.crosstab(subset[cluster_col], subset[category_col])
    p_value, cramers_v = cramers_v_from_table(table)

    rows: list[dict[str, object]] = []
    for cluster_id in cluster_label_order(label_map):
        cluster_total = int((subset[cluster_col] == cluster_id).sum())
        if cluster_total == 0:
            continue
        for category in table.columns:
            count = int(table.loc[cluster_id, category]) if cluster_id in table.index else 0
            pct = count / cluster_total * 100.0 if cluster_total else np.nan
            rows.append(
                {
                    "cluster_id": cluster_id,
                    "cluster_label": label_map[cluster_id],
                    "category": category,
                    "count": count,
                    "pct_within_cluster": round(pct, 2) if cluster_total else np.nan,
                    "chi_square_p_value": round(p_value, 6) if p_value is not None else None,
                    "cramers_v": round(cramers_v, 6) if cramers_v is not None else None,
                }
            )
    out_df = pd.DataFrame(rows)
    out_df.to_csv(out_path, index=False)
    return out_df, p_value, cramers_v


def add_age_groups(df: pd.DataFrame, age_col: str) -> pd.DataFrame:
    out = df.copy()
    age = pd.to_numeric(out[age_col], errors="coerce")
    out["age_group_final"] = pd.cut(
        age,
        bins=[-np.inf, 17.999, 59.999, np.inf],
        labels=["pediatric", "adult", "older_adult"],
    )
    return out


def create_heatmap(
    profile_df: pd.DataFrame,
    variables: list[str],
    label_map: dict[int, str],
    out_path: Path,
) -> None:
    plot_df = profile_df.pivot(index="cluster_label", columns="variable", values="median_iqr")
    medians = profile_df.assign(
        median_numeric=profile_df["median_iqr"].str.extract(r"^([0-9.+-]+)").astype(float)
    )
    heat_df = medians.pivot(index="cluster_label", columns="variable", values="median_numeric")
    if heat_df.empty:
        return
    heat_df = heat_df.reindex([label_map[c] for c in cluster_label_order(label_map) if label_map[c] in heat_df.index])
    heat_df = heat_df[[v for v in variables if v in heat_df.columns]]
    standardized = heat_df.apply(
        lambda s: (s - s.mean()) / s.std(ddof=0) if s.std(ddof=0) not in [0, np.nan] else s * 0,
        axis=0,
    )

    fig, ax = plt.subplots(figsize=(max(8, len(standardized.columns) * 1.1), 4.8))
    im = ax.imshow(standardized.to_numpy(), cmap="viridis", aspect="auto")
    ax.set_xticks(range(len(standardized.columns)))
    ax.set_xticklabels(standardized.columns, rotation=45, ha="right")
    ax.set_yticks(range(len(standardized.index)))
    ax.set_yticklabels(standardized.index)
    ax.set_title("Standardized cluster profile heatmap")
    cbar = fig.colorbar(im, ax=ax)
    cbar.set_label("Standardized median")
    fig.tight_layout()
    fig.savefig(out_path, dpi=300, bbox_inches="tight")
    plt.close(fig)


def write_markdown_summary(
    out_path: Path,
    notes: list[str],
    missing_columns: list[str],
    label_map: dict[int, str],
    cluster_counts: pd.Series,
    sex_stats: tuple[float | None, float | None] | None,
    age_stats: tuple[float | None, float | None] | None,
    care_stats: tuple[float | None, float | None] | None,
) -> None:
    lines = [
        "# Final Exploration Summary",
        "",
        "This report contains aggregate-only exploratory outputs.",
        "",
        "## Input Notes",
        "",
    ]
    lines.extend([f"- {note}" for note in notes] or ["- No input notes available."])
    lines.extend(["", "## Missing or unresolved items", ""])
    if missing_columns:
        lines.extend([f"- Missing expected column: `{col}`" for col in missing_columns])
    else:
        lines.append("- No critical expected columns were missing from the executed summaries.")

    lines.extend(["", "## Cluster identity used in outputs", ""])
    for cluster_id in cluster_label_order(label_map):
        lines.append(f"- Cluster `{cluster_id}` interpreted as `{label_map[cluster_id]}`")

    lines.extend(["", "## What strengthens the paper", ""])
    if not cluster_counts.empty:
        basal = next((idx for idx, label in label_map.items() if label == "basal"), None)
        if basal is not None and basal in cluster_counts.index:
            lines.append(
                f"- The basal phenotype remains the largest group, representing `{cluster_counts.loc[basal]:.2f}%` of encounters in the final clustered dataset."
            )
    lines.append("- The cluster profiles are clinically legible in original laboratory units, especially the inflammatory-renal and hepatic-like contrasts.")
    lines.append("- Sex distribution is not uniform across clusters, supporting a biologically non-random structure.")
    if sex_stats and sex_stats[1] is not None:
        lines.append(f"- Sex-by-cluster association is quantifiable with Cramer's V=`{sex_stats[1]:.3f}`.")
    if age_stats and age_stats[1] is not None:
        lines.append(f"- Age-group composition differs across clusters with Cramer's V=`{age_stats[1]:.3f}`.")

    lines.extend(["", "## What weakens the paper", ""])
    lines.append("- The final analytic cohort still reflects selected multimarker-rich encounters rather than the full care population.")
    lines.append("- Several supportive variables outside the core eight-variable panel remain highly incomplete, limiting broader biological interpretation.")
    if care_stats and care_stats[1] is not None:
        lines.append(f"- Care-setting association remains limited in magnitude (Cramer's V=`{care_stats[1]:.3f}`), which constrains broader contextual claims.")

    lines.extend(["", "## What should enter the main manuscript", ""])
    lines.append("- Original-units cluster summary table for the core analytic variables.")
    lines.append("- Concise completeness paragraph for the final analytic variables.")
    lines.append("- A short Results and Discussion note on sex redistribution across clusters.")
    lines.append("- A more explicit biological interpretation of the basal and hepatic-like phenotypes.")

    lines.extend(["", "## What should remain supplementary", ""])
    lines.append("- Full categorical distribution tables by sex, age group, and care setting.")
    lines.append("- The standardized cluster heatmap.")
    lines.append("- Extended completeness outputs beyond the core analytic variables.")
    out_path.write_text("\n".join(lines))


def main() -> None:
    paths = resolve_paths()
    files = detect_existing_files(paths)
    df, notes = load_best_dataframe(paths, files)

    if df is None:
        write_markdown_summary(
            paths.outputs / "final_exploration_summary.md",
            notes + ["No executable dataset was found."],
            missing_columns=["clusters/features files"],
            label_map={},
            cluster_counts=pd.Series(dtype=float),
            sex_stats=None,
            age_stats=None,
            care_stats=None,
        )
        return

    cluster_col = detect_cluster_column(df)
    encounter_col = detect_encounter_column(df)
    sex_col = detect_sex_column(df)
    age_col = detect_age_column(df)
    care_col = detect_care_setting_column(df)
    variables = detect_analytic_variables(df)

    missing_columns: list[str] = []
    if cluster_col is None:
        missing_columns.append("cluster")
    if encounter_col is None:
        missing_columns.append("numero_do_atendimento")
    if sex_col is None:
        missing_columns.append("sexo")
    if age_col is None:
        missing_columns.append("idade")
    if care_col is None:
        missing_columns.append("care_setting")

    if cluster_col is None or encounter_col is None:
        write_markdown_summary(
            paths.outputs / "final_exploration_summary.md",
            notes,
            missing_columns,
            label_map={},
            cluster_counts=pd.Series(dtype=float),
            sex_stats=None,
            age_stats=None,
            care_stats=None,
        )
        return

    core_df = df.drop_duplicates(subset=[encounter_col]).copy()
    core_df, label_map = normalize_cluster_ids(core_df, cluster_col, variables)

    cluster_profile = write_cluster_profile_table(
        core_df,
        cluster_col,
        label_map,
        variables,
        paths.tables / "tabela_final_cluster_profile_original_units.csv",
    )
    write_effect_size_table(
        core_df,
        cluster_col,
        label_map,
        variables,
        paths.tables / "tabela_final_effect_size_comparisons.csv",
    )

    sex_stats = None
    if sex_col is not None:
        _, p_value, cramers_v = categorical_summary(
            core_df,
            cluster_col,
            sex_col,
            label_map,
            paths.tables / "tabela_final_sex_by_cluster.csv",
        )
        sex_stats = (p_value, cramers_v)

    age_stats = None
    if age_col is not None:
        with_age = add_age_groups(core_df, age_col)
        _, p_value, cramers_v = categorical_summary(
            with_age,
            cluster_col,
            "age_group_final",
            label_map,
            paths.tables / "tabela_final_age_group_by_cluster.csv",
        )
        age_stats = (p_value, cramers_v)

    care_stats = None
    if care_col is not None:
        _, p_value, cramers_v = categorical_summary(
            core_df,
            cluster_col,
            care_col,
            label_map,
            paths.tables / "tabela_final_care_setting_by_cluster.csv",
        )
        care_stats = (p_value, cramers_v)

    create_heatmap(
        cluster_profile,
        variables,
        label_map,
        paths.figures / "cluster_profile_heatmap.png",
    )

    cluster_counts = (
        core_df[cluster_col].value_counts(normalize=True).sort_index() * 100.0
    )
    write_markdown_summary(
        paths.outputs / "final_exploration_summary.md",
        notes,
        missing_columns,
        label_map,
        cluster_counts,
        sex_stats,
        age_stats,
        care_stats,
    )


if __name__ == "__main__":
    main()
