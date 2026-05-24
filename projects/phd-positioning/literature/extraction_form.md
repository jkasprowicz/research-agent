# Data Extraction Form

## Purpose

This extraction form is designed for evidence mapping after screening. It focuses on whether the literature supports a doctoral direction in:

**multimodal clinical-laboratory intelligence for hematology**

## Recommended Format

Use this as a spreadsheet schema or markdown table template.

## Core Fields

| Field | Description |
|---|---|
| Record ID | Internal unique identifier |
| Citation | Full citation in preferred style |
| DOI / URL | DOI or stable link |
| Year | Publication year |
| Journal / Conference | Venue |
| Database Source | PubMed, Scopus, Embase, SciELO, Web of Science, IEEE Xplore, ACM DL |
| Country / Setting | Country or geographic context if clear |
| Study Type | Original study, review, benchmark, dataset paper, conference paper, methods paper |

## Relevance Fields

| Field | Description |
|---|---|
| Screening Label | directly relevant / adjacent but useful / background only |
| Relevance to PhD Proposal | 1-3 sentence note |
| Why Included | Main reason the paper matters |

## Domain Fields

| Field | Description |
|---|---|
| Hematology Task | Leukocyte classification, smear review, diagnostic support, CBC interpretation, anomaly detection, etc. |
| Clinical Context | Peripheral blood smear, CBC, clinical laboratory workflow, analyzer review, hematology service, etc. |
| Human / Non-human | Human, mixed, non-human |
| Target Use Case | Triage, classification, diagnosis support, report aid, prediction, reasoning, etc. |

## Data / Modality Fields

| Field | Description |
|---|---|
| Modality Used | Image, tabular laboratory data, text, metadata, multimodal |
| Image Source | Peripheral blood smear, microscopy, scanner, digital morphology system, etc. |
| Structured Data Type | CBC, differential count, analyzer flags, metadata, laboratory information system variables, etc. |
| Text Data Type | Reports, comments, clinical notes, guidelines, literature, knowledge base |
| Dataset Type | Single-center, multi-center, public, private, retrospective, prospective |
| Dataset Size | Samples, images, cases, patients, records |
| Label Source | Experts, analysts, pathologists, automated labels, chart review |
| Code/Data Availability | Open code, open data, partial, not available |

## Method Fields

| Field | Description |
|---|---|
| AI Method | ML, DL, CNN, ViT, multimodal transformer, LLM, KG+LLM, rule-based+ML, etc. |
| Multimodal Strategy | Early fusion, late fusion, joint embedding, cross-attention, retrieval augmentation, none |
| Reasoning Component | None, rule-based, KG-based, LLM, agentic, hybrid |
| Decision Support Component | Explicit CDS, triage logic, report assistance, alerting, ranking, none |
| Robustness Strategy | Domain adaptation, augmentation, calibration, uncertainty, OOD, none |
| Interpretability Strategy | Saliency, attention, SHAP, feature importance, rule traceability, none |

## Validation Fields

| Field | Description |
|---|---|
| Validation Type | Internal split, cross-validation, external validation, prospective, simulation only |
| External Validation | Yes / No |
| Multi-center Validation | Yes / No |
| Real-world Laboratory Data | Yes / No / unclear |
| Comparator | Manual review, existing model, analyzer, clinician, baseline ML, none |
| Main Metrics | Accuracy, F1, AUROC, sensitivity, specificity, calibration, etc. |

## Findings / Interpretation Fields

| Field | Description |
|---|---|
| Main Contribution | Short summary of what the paper actually contributes |
| Main Limitation | Most important limitation |
| Gap Addressed | What problem it claims to solve |
| Residual Gap | What remains unsolved after this paper |
| PhD Relevance Category | novelty support / feasibility support / methods support / gap support / background |

## Suggested Extra Fields for This Doctoral Topic

| Field | Description |
|---|---|
| Smear + CBC Integration | Yes / No / partial |
| Analyzer Flags Used | Yes / No |
| Case-level Reasoning | Yes / No |
| LLM or Foundation Model Used | Yes / No |
| Knowledge Graph Used | Yes / No |
| Agentic Workflow Used | Yes / No |
| Domain Shift Discussed | Yes / No |
| Uncertainty Discussed | Yes / No |
| Interpretable for Clinical Use | Yes / No / partial |

## Minimal Markdown Template

```md
- Record ID:
- Citation:
- DOI / URL:
- Year:
- Journal / Conference:
- Database Source:
- Screening Label:
- Hematology Task:
- Clinical Context:
- Modality Used:
- Structured Data Type:
- Dataset Type:
- Dataset Size:
- AI Method:
- Multimodal Strategy:
- Reasoning Component:
- Decision Support Component:
- Validation Type:
- External Validation:
- Real-world Laboratory Data:
- Interpretability Strategy:
- Robustness Strategy:
- Main Contribution:
- Main Limitation:
- Gap Addressed:
- Residual Gap:
- Relevance to PhD Proposal:
```

## Suggested Coding Conventions

To keep extraction reproducible:

- use `yes / no / unclear`
- use controlled short labels for modality and method
- distinguish `image-only`, `tabular-only`, and `true multimodal`
- distinguish `case-level reasoning` from `cell-level classification`

## Primary Questions the Extraction Should Answer

1. Is image + laboratory data integration already common in hematology?
2. Are analyzer flags and CBC parameters being used meaningfully?
3. Are reasoning systems or LLMs already present in laboratory hematology?
4. How much of the field remains image-only?
5. Are robustness and domain shift handled seriously enough to support a new thesis contribution?
