# Robustness Execution Round 1

## Scope

This round implemented the minimum high-value robustness analyses recommended in [robustness_analysis_round1.md](/Users/joaokasprowicz/.codex/worktrees/9965/research-agent/projects/lab-phenotyping/reviews/robustness_analysis_round1.md):

1. no-age sensitivity analysis
2. repeated-encounter analysis
3. testing-intensity / `n_exames >= 6` filter analysis

The goal was to implement the smallest set of analyses that materially improves publication defensibility without overengineering the project.

## What Was Implemented

### 1. Minimal robustness execution script

Created:

- [06_robustness_minimal.py](/Users/joaokasprowicz/.codex/worktrees/9965/research-agent/projects/lab-phenotyping/notebooks/06_robustness_minimal.py)

This script is designed to run locally against:

- `data/processed/features_24h_peak_emergency.csv`
- `data/processed/clusters_kmeans_robust_final_with_care_setting.csv`
- `data/processed/dataset_laboratorial_expandido.csv`

### 2. Output locations

The script creates and uses:

- `projects/lab-phenotyping/outputs/robustness/`
- `projects/lab-phenotyping/tables/`
- `projects/lab-phenotyping/supplementary/`

### 3. Aggregate-only reporting

The implementation respects the project’s privacy constraint:

- no patient-level rows are exported
- only aggregate counts, summaries, and cluster-level tables are produced

## Analyses Implemented in Code

### A. No-age sensitivity analysis

Implemented behavior:

- reruns the clustering pipeline without `idade`
- preserves the main preprocessing logic:
  - clipping
  - `log1p`
  - KNN imputation
  - robust scaling
- recalculates silhouette scores for `k=2..6`
- reruns `k=3`
- exports:
  - `no_age_silhouette_scores.csv`
  - `no_age_cluster_distribution.csv`
  - `no_age_cluster_profile_summary.csv`
  - `no_age_cluster_comparison.csv`

Scientific purpose:

- evaluate whether age is structurally dominating the clustering solution
- assess whether an inflammatory-renal-like phenotype persists after removing age

### B. Repeated-encounter analysis

Implemented behavior:

- quantifies:
  - total encounters
  - unique patients
  - repeated patients
  - repeated encounters beyond first occurrence
  - encounters-per-patient distribution
- evaluates cluster prevalence in:
  - all encounters
  - first encounter only
- exports:
  - `repeated_encounter_summary.csv`
  - `encounters_per_patient_distribution.csv`
  - `cluster_prevalence_all_vs_first_encounter.csv`

Scientific purpose:

- test whether phenotype prevalence may be distorted by recurring patients

### C. Testing-intensity / filter analysis

Implemented behavior:

- reconstructs pre-filter encounter-level feature density from `dataset_laboratorial_expandido.csv`
- quantifies:
  - encounters before `n_exames >= 6`
  - encounters after filter
  - excluded encounters
  - retention percentage
- characterizes testing-intensity bins
- if `features_24h_peak_emergency.csv` is available, also summarizes:
  - median age
  - sex distribution
  - adult emergency share
  - pediatric emergency share
- exports:
  - `testing_intensity_filter_summary.csv`
  - `testing_intensity_distribution.csv`
  - `testing_intensity_group_characteristics.csv`

Scientific purpose:

- evaluate whether the analytic cohort is best interpreted as a multimarker-rich selected cohort rather than a general emergency population

## Execution Outcome in This Worktree

The script was executed successfully and produced:

- [robustness_minimal_summary.md](/Users/joaokasprowicz/.codex/worktrees/9965/research-agent/projects/lab-phenotyping/outputs/robustness/robustness_minimal_summary.md)
- [robustness_minimal_summary.md](/Users/joaokasprowicz/.codex/worktrees/9965/research-agent/projects/lab-phenotyping/supplementary/robustness_minimal_summary.md)

However, the local processed datasets required for the numeric analyses were not present in this worktree at execution time.

Therefore:

- the robustness framework is implemented
- the script runs
- the output directories are created
- the execution summary is generated
- but the numerical robustness outputs were not materialized because the required input CSVs were missing

## Current Blocker

Missing local inputs at execution time:

- `projects/lab-phenotyping/data/processed/features_24h_peak_emergency.csv`
- `projects/lab-phenotyping/data/processed/clusters_kmeans_robust_final_with_care_setting.csv`
- `projects/lab-phenotyping/data/processed/dataset_laboratorial_expandido.csv`

Because of that, the following analyses were skipped in execution:

- no-age sensitivity
- repeated-encounter analysis
- testing-intensity analysis

## What Is Ready Immediately Once Local Data Are Available

As soon as the local processed CSVs are present in the expected project paths, rerunning:

```bash
python3 projects/lab-phenotyping/notebooks/06_robustness_minimal.py
```

should generate the minimal robustness package without further code changes.

## Scientific Value of This Round

Even though the numeric outputs could not be computed in this worktree, this round still improves the project materially because:

1. the exact minimal robustness design is now encoded and reproducible
2. the analyses are aligned with the highest-priority publication risks
3. the output footprint is privacy-safe and supplement-ready
4. the project now has a clear path from conceptual robustness concerns to executable aggregate analyses

## Recommended Next Step

Place the processed CSVs in:

- `projects/lab-phenotyping/data/processed/`

and rerun:

```bash
python3 projects/lab-phenotyping/notebooks/06_robustness_minimal.py
```

Then the next review round should interpret:

- whether age materially changes phenotype structure
- whether first-encounter prevalence differs from all-encounter prevalence
- how selective the `n_exames >= 6` cohort actually is
