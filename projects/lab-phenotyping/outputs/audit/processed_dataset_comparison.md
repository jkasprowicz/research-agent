# Processed Dataset Comparison

This report contains aggregate-only comparisons across the processed datasets.

## Dataset Summary

### dataset_expandido
- Path: `/Users/joaokasprowicz/Documents/Projects/research-agent/projects/lab-phenotyping/data/processed/dataset_laboratorial_expandido.csv`
- Exists: `True`
- Rows: `1394229`
- Columns: `12`

### features_24h_peak_emergency
- Path: `/Users/joaokasprowicz/Documents/Projects/research-agent/projects/lab-phenotyping/data/processed/features_24h_peak_emergency.csv`
- Exists: `True`
- Rows: `25785`
- Columns: `22`

### clusters_with_care_setting
- Path: `/Users/joaokasprowicz/Documents/Projects/research-agent/projects/lab-phenotyping/data/processed/clusters_kmeans_robust_final_with_care_setting.csv`
- Exists: `True`
- Rows: `26414`
- Columns: `24`

## Encounter-Level Aggregate Comparison

### dataset_expandido
- Unique encounters (aggregate count only): `120216`
- Repeated encounter rows beyond first occurrence: `1274013`
- Unique patients (if `patient_id` exists): `135757`
- Repeated patient rows beyond first occurrence: `1258472`

### features_24h_peak_emergency
- Unique encounters (aggregate count only): `25785`
- Repeated encounter rows beyond first occurrence: `0`
- Unique patients (if `patient_id` exists): `None`
- Repeated patient rows beyond first occurrence: `None`

### clusters_with_care_setting
- Unique encounters (aggregate count only): `26414`
- Repeated encounter rows beyond first occurrence: `0`
- Unique patients (if `patient_id` exists): `None`
- Repeated patient rows beyond first occurrence: `None`

## Shared Columns

### dataset_expandido vs features_24h_peak_emergency
- Shared columns: `4`
- Column names: `codigo_da_unidade, idade, numero_do_atendimento, sexo`

### dataset_expandido vs clusters_with_care_setting
- Shared columns: `4`
- Column names: `codigo_da_unidade, idade, numero_do_atendimento, sexo`

### features_24h_peak_emergency vs clusters_with_care_setting
- Shared columns: `22`
- Column names: `BILIRRUBINA, CPK, CREATININA, FOSFATASE_ALCALINA, GLICOSE, LDH, LEUCO, LEUCO_original, PCR, PLAQ, PLAQ_original, POTASSIO, SODIO, TAP, TGO, TGP, UREIA, codigo_da_unidade, idade, n_exames, numero_do_atendimento, sexo`

## Potential Inconsistency Checks

- `dataset_expandido`: rows=`1394229`, unique_encounters=`120216`, repeated_encounter_rows=`1274013`
- `features_24h_peak_emergency`: rows=`25785`, unique_encounters=`25785`, repeated_encounter_rows=`0`
- `clusters_with_care_setting`: rows=`26414`, unique_encounters=`26414`, repeated_encounter_rows=`0`
