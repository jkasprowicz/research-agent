# Data Quality Flags

This audit contains aggregate-only outputs and does not expose patient-level records.

## Input File Availability

- `raw_base`: `present`
- `clusters_with_care_setting`: `present`
- `dataset_expandido`: `present`
- `features_24h_peak_emergency`: `present`

## High Missingness Flags

- `clusters_with_care_setting` / `GLICOSE`: `97.10%` missing
- `clusters_with_care_setting` / `TAP`: `71.34%` missing
- `clusters_with_care_setting` / `FOSFATASE_ALCALINA`: `60.26%` missing
- `clusters_with_care_setting` / `POTASSIO`: `58.40%` missing
- `clusters_with_care_setting` / `SODIO`: `58.00%` missing
- `clusters_with_care_setting` / `LDH`: `56.84%` missing
- `clusters_with_care_setting` / `CPK`: `53.87%` missing
- `clusters_with_care_setting` / `BILIRRUBINA`: `51.92%` missing
- `clusters_with_care_setting` / `TGP`: `23.98%` missing
- `dataset_expandido` / `idade`: `26.56%` missing
- `features_24h_peak_emergency` / `GLICOSE`: `98.99%` missing
- `features_24h_peak_emergency` / `TAP`: `71.07%` missing
- `features_24h_peak_emergency` / `FOSFATASE_ALCALINA`: `59.85%` missing
- `features_24h_peak_emergency` / `POTASSIO`: `58.22%` missing
- `features_24h_peak_emergency` / `SODIO`: `57.44%` missing
- `features_24h_peak_emergency` / `LDH`: `56.16%` missing
- `features_24h_peak_emergency` / `CPK`: `53.38%` missing
- `features_24h_peak_emergency` / `BILIRRUBINA`: `51.39%` missing
- `features_24h_peak_emergency` / `TGP`: `24.17%` missing
- `raw_base` / `Telefone do Paciente`: `98.92%` missing
- `raw_base` / `RG`: `91.91%` missing
- `raw_base` / `Código Controle`: `84.30%` missing
- `raw_base` / `Celular do Paciente`: `70.91%` missing
- `raw_base` / `Endereço do Paciente`: `70.43%` missing

## Numeric Range Flags

- `dataset_expandido` / `idade` has minimum value `-0.9`
- `dataset_expandido` / `valor_do_resultado` has minimum value `-16.98`
- `dataset_expandido` / `valor_num` has minimum value `-16.98`
- `raw_base` / `Valor do Resultado` has minimum value `-188.0`

## Dataset-Level Notes

- `raw_base`: `9097700` rows, `22` columns
- `clusters_with_care_setting`: `26414` rows, `24` columns
- `dataset_expandido`: `1394229` rows, `12` columns
- `features_24h_peak_emergency`: `25785` rows, `22` columns

## Repeated Encounter Flags

- `raw_base`: encounter identifier not available or file missing.
- `clusters_with_care_setting`: unique encounters=`26414`, repeated encounter rows beyond first occurrence=`0`
- `dataset_expandido`: unique encounters=`120216`, repeated encounter rows beyond first occurrence=`1274013`
- `features_24h_peak_emergency`: unique encounters=`25785`, repeated encounter rows beyond first occurrence=`0`