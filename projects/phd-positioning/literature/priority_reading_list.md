# Priority Reading List

## Purpose

This reading list prioritizes the papers most useful for doctoral positioning based on the initial evidence mapping.

It is intentionally selective. It does **not** attempt to list every relevant paper.

## Reading Strategy

Read in this order:

1. papers that define the true competitive space
2. papers that show clinically realistic workflow integration
3. papers that show how generalization/robustness is being handled
4. papers that show whether LLM/reasoning work is credible or still mostly exploratory

## Category Definitions

### `foundational`

Papers that define the field, its workflow context, datasets, or methodological baseline.

### `directly competitive`

Papers that come closest to the proposed doctoral niche:

- smear morphology + laboratory data
- workflow support
- analyzer integration
- case-level multimodal reasoning

### `adjacent`

Important neighboring work that informs methods, robustness, or translational framing, but does not directly compete with the exact proposed thesis.

### `low relevance`

Papers retrieved by the broad search that are not strategically useful for the core doctoral argument.

## Priority Tier 1: Read First

These are the most important first reads.

| Priority | Paper | Category | Why it matters |
|---|---|---|---|
| 1 | `Identifying Hospitalized Patients with Acute Decompensation Risk from Peripheral Blood Smears and Laboratory Results using Multimodal, Multiencoder, Multiple Instance Learning (M3MIL)` — `10.1093/ajcp/aqaf121.430` | directly competitive | Closest visible match to morphology + laboratory-results integration and case-level multimodal inference |
| 2 | `PROSER: A Web-Based Peripheral Blood Smear Interpretation Support Tool Utilizing Electronic Health Record Data` — `10.1093/ajcp/aqad024` | directly competitive | One of the clearest signals of smear interpretation support linked to structured clinical data |
| 3 | `Development of criteria to optimize manual smear review of automated complete blood counts using a machine learning model` — `10.1111/vcp.13400` | directly competitive | Strong workflow-level example linking AI to CBC-driven smear review logic |
| 4 | `diagnostic algorithm for the detection of blasts in peripheral blood based on morphological flags from the integrated sysmex Xn-9100 system` — `10.23736/S1825-859X.24.00257-3` | directly competitive | Very relevant example of analyzer-flag + morphology integration |
| 5 | `Application of Convolutional Neural Network Image Analysis and Machine Learning to Basic Blood Tests for Intelligent Diagnostic Assistance` — `10.1111/ijlh.14550` | directly competitive | Likely one of the strongest direct signals for morphology + basic blood test integration |
| 6 | `DeepHeme, a high-performance, generalizable deep ensemble for bone marrow morphometry and hematologic diagnosis` — `10.1126/scitranslmed.adq2162` | adjacent | Important for understanding what robust, generalizable hematology AI looks like at a higher maturity level |
| 7 | `Computational analysis of peripheral blood smears detects disease-associated cytomorphologies` — `10.1038/s41467-023-39676-y` | adjacent | Strong evidence that peripheral smear morphology can support broader disease-associated inference beyond simple cell classification |
| 8 | `Evaluation of Scopio Labs X100 Full Field PBS: The first high-resolution full field viewing of peripheral blood specimens combined with artificial intelligence-based morphological analysis` — `10.1111/ijlh.13681` | foundational | Important workflow baseline for digital morphology integration |

## Priority Tier 2: Core Foundations

These shape the field and should be read early after Tier 1.

| Paper | Category | Why it matters |
|---|---|---|
| `Hematological cytomorphology: Where we are` — `10.1111/ijlh.14330` | foundational | Useful high-level map of where morphology is now |
| `Digital pathology and artificial intelligence as the next chapter in diagnostic hematopathology` — `10.1053/j.semdp.2023.02.001` | foundational | Places hematology AI in broader diagnostic maturation context |
| `Classification of white blood cells (leucocytes) from blood smear imagery using machine and deep learning models: A global scoping review` — `10.1371/journal.pone.0292026` | foundational | Good overview of the saturated image-only space |
| `A large multi-focus dataset for white blood cell classification` — `10.1038/s41597-024-03938-1` | foundational | Important for dataset landscape |
| `A Large-Scale Peripheral Blood Cell Dataset for Automated Hematological Analysis` — `10.1038/s41597-026-06761-y` | foundational | Important for benchmark evolution and scale |
| `1 Million Segmented Red Blood Cells With 240 K Classified in 9 Shapes and 47 K Patches of 25 Manual Blood Smears` — `10.1038/s41597-024-03570-z` | foundational | Important for RBC-side data scale and morphology infrastructure |

## Priority Tier 3: Robustness and Generalization

These matter because your doctoral direction should not stop at integration; it should also be robust.

| Paper | Category | Why it matters |
|---|---|---|
| `Contrastive Representation Learning for Cross-Domain Blood Cell Image Classification With Denoising Mechanism` — `10.1109/JBHI.2025.3585548` | adjacent | Strong domain-shift relevance |
| `Domain-incremental white blood cell classification with privacy-aware continual learning` — `10.1038/s41598-025-08024-z` | adjacent | Important for longitudinal/generalizable deployment logic |
| `FL-W3S: Cross-domain federated learning for weakly supervised semantic segmentation of white blood cells` — `10.1016/j.ijmedinf.2025.105806` | adjacent | Valuable for privacy + cross-domain thinking |
| `Transferable automatic hematological cell classification: Overcoming data limitations with self-supervised learning` — `10.1016/j.cmpb.2024.108560` | adjacent | Good bridge between morphology and generalization |
| `Automatic normalized digital color staining in the recognition of abnormal blood cells using generative adversarial networks` — `10.1016/j.cmpb.2023.107629` | adjacent | Relevant to stain variability and domain robustness |

## Priority Tier 4: LLM / Reasoning / Emerging Systems

Read these after the multimodal and workflow core, not before.

| Paper | Category | Why it matters |
|---|---|---|
| `Artificial intelligence in hematology: Evaluating a large language model for morphology-based diagnostics` — `10.4103/ijpm.ijpm_1191_25` | adjacent | Shows current maturity level of LLM morphology support |
| `COMPARATIVE EFFECTIVENESS OF HEMATOLOGISTS WITH LARGE LANGUAGE MODELS IN HEMATOLOGIC DIAGNOSIS` — `10.1016/j.htct.2025.104218` | adjacent | Useful for separating signal from hype |
| `MDS-1223: Benchmarking Few-Shot GPT-4o Against Supervised Fine-Tuning for Morphologic Identification of Peripheral Blood Smears` — `10.1016/S2152-2650(25)02070-1` | adjacent | Important as a trend marker, but likely not enough alone for a thesis |
| `Comparative Evaluation of Five Multimodal Large Language Models for Medical Laboratory Image Recognition: Impact of Prompting Strategies on Diagnostic Accuracy` — `10.3390/diagnostics16091258` | adjacent | Useful for the exploratory reasoning layer |
| `ChatGPT's innovative application in blood morphology recognition` — `10.1097/JCMA.0000000000001071` | low relevance | Good as a signal of trend emergence, but probably not a strong scientific anchor |

## Lower-Priority but Still Useful

These are worth reading selectively depending on the thesis angle you choose.

### If you emphasize analyzer/workflow integration

- `Artificial intelligence and the blood film: Performance of the MC-80 digital morphology analyzer in samples with neoplastic and reactive cell types` — `10.1111/ijlh.14160`
- `Performance comparison of two automated digital morphology analyzers for leukocyte differential in patients with malignant hematological diseases: Mindray MC-80 and Sysmex DI-60` — `10.1111/ijlh.14227`
- `Real-World Application of Digital Morphology Analyzers: Practical Issues and Challenges in Clinical Laboratories` — `10.3390/diagnostics15060677`

### If you emphasize morphology-to-diagnosis expansion

- `AI-based detection of neutrophil dysplasia: an accessible and sensitive model for MDS diagnosis from peripheral blood` — `10.1007/s00277-025-06533-5`
- `Detection of acute promyelocytic leukemia in peripheral blood and bone marrow with annotation-free deep learning` — `10.1038/s41598-023-29160-4`
- `A new convolutional neural network predictive model for the automatic recognition of hypogranulated neutrophils in myelodysplastic syndromes` — `10.1016/j.compbiomed.2021.104479`

## Topics to Deprioritize in Reading

These appeared frequently in the search but are not the best investment for your immediate doctoral positioning.

### `low relevance`

- generic multimodal oncology or immune profiling papers with no laboratory hematology task
- non-hematology pathology foundation-model papers
- repeated image-classification architecture papers with no workflow, structured data, or robustness contribution
- general “AI in cancer” reviews

## Final Reading Recommendation

If you read only eight papers first, read:

1. `M3MIL`
2. `PROSER`
3. `Development of criteria to optimize manual smear review of automated CBCs using a machine learning model`
4. `diagnostic algorithm for blast detection based on morphological flags from integrated Sysmex XN-9100`
5. `Application of CNN image analysis and machine learning to basic blood tests for intelligent diagnostic assistance`
6. `DeepHeme`
7. `Computational analysis of peripheral blood smears detects disease-associated cytomorphologies`
8. `Evaluation of Scopio Labs X100 Full Field PBS`

That reading set will give you the clearest picture of:

- what is already competitive
- what is still missing
- where your doctoral positioning can be strongest
