# Final Exploration Summary

This report contains aggregate-only exploratory outputs.

## Input Notes

- clusters file loaded: `clusters_kmeans_robust_final_with_care_setting.csv`
- features file loaded: `features_24h_peak_final_units_fixed.csv`
- merged clusters and features on encounter identifier

## Missing or unresolved items

- No critical expected columns were missing from the executed summaries.

## Cluster identity used in outputs

- Cluster `0` interpreted as `inflammatory_renal`
- Cluster `1` interpreted as `hepatic_like`
- Cluster `2` interpreted as `basal`

## What strengthens the paper

- The basal phenotype remains the largest group, representing `58.86%` of encounters in the final clustered dataset.
- The cluster profiles are clinically legible in original laboratory units, especially the inflammatory-renal and hepatic-like contrasts.
- Sex distribution is not uniform across clusters, supporting a biologically non-random structure.
- Sex-by-cluster association is quantifiable with Cramer's V=`0.149`.
- Age-group composition differs across clusters with Cramer's V=`0.301`.

## What weakens the paper

- The final analytic cohort still reflects selected multimarker-rich encounters rather than the full care population.
- Several supportive variables outside the core eight-variable panel remain highly incomplete, limiting broader biological interpretation.
- Care-setting association remains limited in magnitude (Cramer's V=`0.052`), which constrains broader contextual claims.

## What should enter the main manuscript

- Original-units cluster summary table for the core analytic variables.
- Concise completeness paragraph for the final analytic variables.
- A short Results and Discussion note on sex redistribution across clusters.
- A more explicit biological interpretation of the basal and hepatic-like phenotypes.

## What should remain supplementary

- Full categorical distribution tables by sex, age group, and care setting.
- The standardized cluster heatmap.
- Extended completeness outputs beyond the core analytic variables.