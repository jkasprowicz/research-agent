from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

import pandas as pd


CHUNK_SIZE = 100_000
NUMERIC_RATIO_THRESHOLD = 0.80


@dataclass
class DatasetSpec:
    label: str
    path: Path
    sep: str = ","
    chunksize: int = CHUNK_SIZE


def project_root() -> Path:
    return Path(__file__).resolve().parents[1]


def output_dir() -> Path:
    out = project_root() / "outputs" / "audit"
    out.mkdir(parents=True, exist_ok=True)
    return out


def dataset_specs() -> list[DatasetSpec]:
    root = project_root()
    return [
        DatasetSpec(
            label="raw_base",
            path=root / "data" / "raw" / "base_laboratorial_consolidada.csv",
            sep=";",
        ),
        DatasetSpec(
            label="clusters_with_care_setting",
            path=root / "data" / "processed" / "clusters_kmeans_robust_final_with_care_setting.csv",
        ),
        DatasetSpec(
            label="dataset_expandido",
            path=root / "data" / "processed" / "dataset_laboratorial_expandido.csv",
        ),
        DatasetSpec(
            label="features_24h_peak_emergency",
            path=root / "data" / "processed" / "features_24h_peak_emergency.csv",
        ),
    ]


def read_sample(spec: DatasetSpec, nrows: int = 1_000) -> pd.DataFrame:
    return pd.read_csv(
        spec.path,
        sep=spec.sep,
        nrows=nrows,
        low_memory=False,
    )


def iter_chunks(spec: DatasetSpec) -> Iterable[pd.DataFrame]:
    return pd.read_csv(
        spec.path,
        sep=spec.sep,
        chunksize=spec.chunksize,
        low_memory=False,
    )


def detect_numeric_columns(sample: pd.DataFrame) -> set[str]:
    numeric_cols: set[str] = set()
    for col in sample.columns:
        non_null = sample[col].dropna()
        if non_null.empty:
            continue
        converted = pd.to_numeric(non_null, errors="coerce")
        ratio = converted.notna().mean()
        if ratio >= NUMERIC_RATIO_THRESHOLD:
            numeric_cols.add(col)
    return numeric_cols


def analyze_dataset(spec: DatasetSpec) -> tuple[pd.DataFrame, pd.DataFrame, dict[str, object]]:
    sample = read_sample(spec)
    columns = list(sample.columns)
    numeric_cols = detect_numeric_columns(sample)

    row_count = 0
    non_null_counts = {col: 0 for col in columns}
    numeric_non_null = {col: 0 for col in numeric_cols}
    numeric_min = {col: None for col in numeric_cols}
    numeric_max = {col: None for col in numeric_cols}

    for chunk in iter_chunks(spec):
        chunk.columns = chunk.columns.str.strip()
        row_count += len(chunk)

        for col in columns:
            series = chunk[col]
            non_null_counts[col] += int(series.notna().sum())

        for col in numeric_cols:
            numeric_values = pd.to_numeric(chunk[col], errors="coerce")
            valid = numeric_values.dropna()
            numeric_non_null[col] += int(valid.shape[0])
            if valid.empty:
                continue

            col_min = float(valid.min())
            col_max = float(valid.max())

            if numeric_min[col] is None or col_min < numeric_min[col]:
                numeric_min[col] = col_min
            if numeric_max[col] is None or col_max > numeric_max[col]:
                numeric_max[col] = col_max

    missingness_rows = []
    for col in columns:
        non_null = non_null_counts[col]
        missing = row_count - non_null
        missingness_rows.append(
            {
                "dataset": spec.label,
                "variable": col,
                "row_count": row_count,
                "non_null_count": non_null,
                "missing_count": missing,
                "missing_pct": round((missing / row_count) * 100, 4) if row_count else None,
            }
        )

    range_rows = []
    for col in sorted(numeric_cols):
        range_rows.append(
            {
                "dataset": spec.label,
                "variable": col,
                "numeric_non_null_count": numeric_non_null[col],
                "min_value": numeric_min[col],
                "max_value": numeric_max[col],
            }
        )

    summary = {
        "dataset": spec.label,
        "path": str(spec.path),
        "exists": True,
        "rows": row_count,
        "columns": len(columns),
        "column_names": columns,
        "numeric_columns": sorted(numeric_cols),
    }

    return (
        pd.DataFrame(missingness_rows),
        pd.DataFrame(range_rows),
        summary,
    )


def aggregate_cluster_outputs(spec: DatasetSpec, out: Path) -> dict[str, object]:
    df = pd.read_csv(spec.path, low_memory=False)

    outputs: dict[str, object] = {}

    if "cluster" in df.columns:
        cluster_counts = df["cluster"].value_counts(dropna=False).sort_index().reset_index()
        cluster_counts.columns = ["cluster", "count"]
        cluster_counts["pct"] = (cluster_counts["count"] / len(df) * 100).round(4)
        cluster_counts.to_csv(out / "cluster_distribution.csv", index=False)
        outputs["cluster_distribution"] = cluster_counts

        numeric_cols = [
            col
            for col in df.columns
            if col != "cluster" and pd.api.types.is_numeric_dtype(df[col])
        ]
        profile_rows: list[dict[str, object]] = []
        for cluster_value, sub_df in df.groupby("cluster", dropna=False):
            for col in numeric_cols:
                series = sub_df[col].dropna()
                if series.empty:
                    continue
                profile_rows.append(
                    {
                        "cluster": cluster_value,
                        "variable": col,
                        "count": int(series.shape[0]),
                        "median": float(series.median()),
                        "q1": float(series.quantile(0.25)),
                        "q3": float(series.quantile(0.75)),
                        "mean": float(series.mean()),
                    }
                )
        pd.DataFrame(profile_rows).to_csv(out / "cluster_profile_summary.csv", index=False)

    if "care_setting" in df.columns:
        care_counts = df["care_setting"].value_counts(dropna=False).sort_index().reset_index()
        care_counts.columns = ["care_setting", "count"]
        care_counts["pct"] = (care_counts["count"] / len(df) * 100).round(4)
        care_counts.to_csv(out / "care_setting_distribution.csv", index=False)
        outputs["care_setting_distribution"] = care_counts

    return outputs


def load_identifier_stats(spec: DatasetSpec) -> dict[str, int | float | None]:
    if not spec.path.exists():
        return {
            "rows": None,
            "unique_encounters": None,
            "repeated_encounter_rows": None,
            "unique_patients": None,
            "repeated_patient_rows": None,
        }

    sample = read_sample(spec, nrows=50)
    has_encounter = "numero_do_atendimento" in sample.columns
    has_patient = "patient_id" in sample.columns

    rows = 0
    encounter_counts: dict[str, int] = {}
    patient_counts: dict[str, int] = {}

    for chunk in iter_chunks(spec):
        rows += len(chunk)
        if has_encounter:
            ids = chunk["numero_do_atendimento"].dropna().astype(str)
            for value, count in ids.value_counts().items():
                encounter_counts[value] = encounter_counts.get(value, 0) + int(count)
        if has_patient:
            ids = chunk["patient_id"].dropna().astype(str)
            for value, count in ids.value_counts().items():
                patient_counts[value] = patient_counts.get(value, 0) + int(count)

    repeated_encounter_rows = None
    unique_encounters = None
    if has_encounter:
        unique_encounters = len(encounter_counts)
        repeated_encounter_rows = sum(
            count - 1 for count in encounter_counts.values() if count > 1
        )

    repeated_patient_rows = None
    unique_patients = None
    if has_patient:
        unique_patients = len(patient_counts)
        repeated_patient_rows = sum(
            count - 1 for count in patient_counts.values() if count > 1
        )

    return {
        "rows": rows,
        "unique_encounters": unique_encounters,
        "repeated_encounter_rows": repeated_encounter_rows,
        "unique_patients": unique_patients,
        "repeated_patient_rows": repeated_patient_rows,
    }


def aggregate_age_distribution(specs: list[DatasetSpec], out: Path) -> None:
    rows: list[dict[str, object]] = []
    age_bins = [0, 18, 40, 60, 200]
    age_labels = ["<18", "18-39", "40-59", ">=60"]

    for spec in specs:
        if not spec.path.exists():
            continue

        sample = read_sample(spec, nrows=100)
        if "idade" not in sample.columns:
            continue

        values: list[pd.Series] = []
        bucket_counts = {label: 0 for label in age_labels}
        total_non_null = 0

        for chunk in iter_chunks(spec):
            ages = pd.to_numeric(chunk["idade"], errors="coerce").dropna()
            if ages.empty:
                continue
            values.append(ages)
            total_non_null += int(ages.shape[0])
            categorized = pd.cut(ages, bins=age_bins, labels=age_labels, right=False)
            counts = categorized.value_counts(dropna=False)
            for label in age_labels:
                bucket_counts[label] += int(counts.get(label, 0))

        if not values:
            continue

        full_ages = pd.concat(values, ignore_index=True)
        rows.append(
            {
                "dataset": spec.label,
                "non_null_age_count": total_non_null,
                "median_age": float(full_ages.median()),
                "q1_age": float(full_ages.quantile(0.25)),
                "q3_age": float(full_ages.quantile(0.75)),
                "min_age": float(full_ages.min()),
                "max_age": float(full_ages.max()),
                "<18_count": bucket_counts["<18"],
                "<18_pct": round(bucket_counts["<18"] / total_non_null * 100, 4),
                "18_39_count": bucket_counts["18-39"],
                "18_39_pct": round(bucket_counts["18-39"] / total_non_null * 100, 4),
                "40_59_count": bucket_counts["40-59"],
                "40_59_pct": round(bucket_counts["40-59"] / total_non_null * 100, 4),
                "ge_60_count": bucket_counts[">=60"],
                "ge_60_pct": round(bucket_counts[">=60"] / total_non_null * 100, 4),
            }
        )

    pd.DataFrame(rows).to_csv(out / "age_distribution_summary.csv", index=False)


def aggregate_processed_comparison(
    specs: list[DatasetSpec],
    dataset_summaries: list[dict[str, object]],
    out: Path,
) -> None:
    summary_by_label = {item["dataset"]: item for item in dataset_summaries}

    comparison_lines = [
        "# Processed Dataset Comparison",
        "",
        "This report contains aggregate-only comparisons across the processed datasets.",
        "",
        "## Dataset Summary",
        "",
    ]

    for label in [
        "dataset_expandido",
        "features_24h_peak_emergency",
        "clusters_with_care_setting",
    ]:
        summary = summary_by_label.get(label)
        if not summary:
            continue
        comparison_lines.extend(
            [
                f"### {label}",
                f"- Path: `{summary['path']}`",
                f"- Exists: `{summary['exists']}`",
                f"- Rows: `{summary.get('rows', 'n/a')}`",
                f"- Columns: `{summary.get('columns', 'n/a')}`",
                "",
            ]
        )

    comparison_lines.extend(
        [
            "## Encounter-Level Aggregate Comparison",
            "",
        ]
    )

    for label in [
        "dataset_expandido",
        "features_24h_peak_emergency",
        "clusters_with_care_setting",
    ]:
        spec = next((item for item in specs if item.label == label), None)
        if spec is None:
            continue
        id_stats = load_identifier_stats(spec)
        comparison_lines.extend(
            [
                f"### {label}",
                f"- Unique encounters (aggregate count only): `{id_stats['unique_encounters']}`",
                f"- Repeated encounter rows beyond first occurrence: `{id_stats['repeated_encounter_rows']}`",
                f"- Unique patients (if `patient_id` exists): `{id_stats['unique_patients']}`",
                f"- Repeated patient rows beyond first occurrence: `{id_stats['repeated_patient_rows']}`",
                "",
            ]
        )

    common_columns = {}
    labels = [
        "dataset_expandido",
        "features_24h_peak_emergency",
        "clusters_with_care_setting",
    ]
    for i, left_label in enumerate(labels):
        left_cols = set(summary_by_label.get(left_label, {}).get("column_names", []))
        for right_label in labels[i + 1 :]:
            right_cols = set(summary_by_label.get(right_label, {}).get("column_names", []))
            common_columns[(left_label, right_label)] = sorted(left_cols & right_cols)

    comparison_lines.extend(
        [
            "## Shared Columns",
            "",
        ]
    )
    for (left_label, right_label), cols in common_columns.items():
        comparison_lines.extend(
            [
                f"### {left_label} vs {right_label}",
                f"- Shared columns: `{len(cols)}`",
                f"- Column names: `{', '.join(cols) if cols else 'none'}`",
                "",
            ]
        )

    comparison_lines.extend(
        [
            "## Potential Inconsistency Checks",
            "",
        ]
    )
    for label in labels:
        spec = next((item for item in specs if item.label == label), None)
        if spec is None:
            continue
        stats = load_identifier_stats(spec)
        comparison_lines.append(
            f"- `{label}`: rows=`{stats['rows']}`, "
            f"unique_encounters=`{stats['unique_encounters']}`, "
            f"repeated_encounter_rows=`{stats['repeated_encounter_rows']}`"
        )
    comparison_lines.append("")

    (out / "processed_dataset_comparison.md").write_text(
        "\n".join(comparison_lines),
        encoding="utf-8",
    )


def write_quality_flags(
    specs: list[DatasetSpec],
    dataset_summaries: list[dict[str, object]],
    missingness_df: pd.DataFrame,
    ranges_df: pd.DataFrame,
    out: Path,
) -> None:
    lines = [
        "# Data Quality Flags",
        "",
        "This audit contains aggregate-only outputs and does not expose patient-level records.",
        "",
        "## Input File Availability",
        "",
    ]

    for spec in specs:
        lines.append(f"- `{spec.label}`: `{'present' if spec.path.exists() else 'missing'}`")

    high_missing = missingness_df[missingness_df["missing_pct"] >= 20].copy()
    high_missing = high_missing.sort_values(["dataset", "missing_pct"], ascending=[True, False])

    lines.extend(
        [
            "",
            "## High Missingness Flags",
            "",
        ]
    )
    if high_missing.empty:
        lines.append("- No variables with missingness >= 20% among the files successfully audited.")
    else:
        for _, row in high_missing.iterrows():
            lines.append(
                f"- `{row['dataset']}` / `{row['variable']}`: "
                f"`{row['missing_pct']:.2f}%` missing"
            )

    negative_ranges = ranges_df[
        ranges_df["min_value"].notna() & (ranges_df["min_value"] < 0)
    ].sort_values(["dataset", "variable"])

    lines.extend(
        [
            "",
            "## Numeric Range Flags",
            "",
        ]
    )
    if negative_ranges.empty:
        lines.append("- No negative minima detected among numeric variables audited.")
    else:
        for _, row in negative_ranges.iterrows():
            lines.append(
                f"- `{row['dataset']}` / `{row['variable']}` has minimum value `{row['min_value']}`"
            )

    lines.extend(
        [
            "",
            "## Dataset-Level Notes",
            "",
        ]
    )
    for summary in dataset_summaries:
        lines.append(
            f"- `{summary['dataset']}`: `{summary.get('rows', 'n/a')}` rows, "
            f"`{summary.get('columns', 'n/a')}` columns"
        )

    lines.extend(
        [
            "",
            "## Repeated Encounter Flags",
            "",
        ]
    )
    for spec in specs:
        stats = load_identifier_stats(spec)
        if stats["unique_encounters"] is None:
            lines.append(f"- `{spec.label}`: encounter identifier not available or file missing.")
            continue
        lines.append(
            f"- `{spec.label}`: unique encounters=`{stats['unique_encounters']}`, "
            f"repeated encounter rows beyond first occurrence=`{stats['repeated_encounter_rows']}`"
        )

    (out / "data_quality_flags.md").write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    out = output_dir()
    specs = dataset_specs()

    all_missingness: list[pd.DataFrame] = []
    all_ranges: list[pd.DataFrame] = []
    dataset_summaries: list[dict[str, object]] = []

    for spec in specs:
        if not spec.path.exists():
            dataset_summaries.append(
                {
                    "dataset": spec.label,
                    "path": str(spec.path),
                    "exists": False,
                    "rows": None,
                    "columns": None,
                    "column_names": [],
                    "numeric_columns": [],
                }
            )
            continue

        missingness_df, ranges_df, summary = analyze_dataset(spec)
        all_missingness.append(missingness_df)
        all_ranges.append(ranges_df)
        dataset_summaries.append(summary)

    missingness_out = pd.concat(all_missingness, ignore_index=True) if all_missingness else pd.DataFrame(
        columns=["dataset", "variable", "row_count", "non_null_count", "missing_count", "missing_pct"]
    )
    ranges_out = pd.concat(all_ranges, ignore_index=True) if all_ranges else pd.DataFrame(
        columns=["dataset", "variable", "numeric_non_null_count", "min_value", "max_value"]
    )

    missingness_out.to_csv(out / "missingness_by_variable.csv", index=False)
    ranges_out.to_csv(out / "variable_ranges.csv", index=False)
    aggregate_age_distribution(specs, out)

    cluster_spec = next(
        (spec for spec in specs if spec.label == "clusters_with_care_setting" and spec.path.exists()),
        None,
    )
    if cluster_spec is not None:
        aggregate_cluster_outputs(cluster_spec, out)
    else:
        pd.DataFrame(columns=["cluster", "count", "pct"]).to_csv(
            out / "cluster_distribution.csv", index=False
        )
        pd.DataFrame(columns=["cluster", "variable", "count", "median", "q1", "q3", "mean"]).to_csv(
            out / "cluster_profile_summary.csv", index=False
        )
        pd.DataFrame(columns=["care_setting", "count", "pct"]).to_csv(
            out / "care_setting_distribution.csv", index=False
        )
    if not (out / "age_distribution_summary.csv").exists():
        pd.DataFrame(
            columns=[
                "dataset",
                "non_null_age_count",
                "median_age",
                "q1_age",
                "q3_age",
                "min_age",
                "max_age",
                "<18_count",
                "<18_pct",
                "18_39_count",
                "18_39_pct",
                "40_59_count",
                "40_59_pct",
                "ge_60_count",
                "ge_60_pct",
            ]
        ).to_csv(out / "age_distribution_summary.csv", index=False)

    aggregate_processed_comparison(specs, dataset_summaries, out)
    write_quality_flags(specs, dataset_summaries, missingness_out, ranges_out, out)


if __name__ == "__main__":
    main()
