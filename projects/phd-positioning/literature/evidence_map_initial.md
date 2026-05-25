# Initial Evidence Map

## Scope

This document is a first-pass strategic synthesis of the exported search results from:

- `raw_search_results/pubmed/pubmed.csv`
- `raw_search_results/embase/records.ris`

It is not a full review and does not summarize every paper individually. Its purpose is to identify the shape of the field, the true competitive core, and the most important gaps for doctoral positioning.

## Data Quality and Interpretation Notes

### Search yield

- Raw PubMed records: `2,733`
- Raw Embase records: `1,972`
- Total raw records: `4,705`

### Deduplication

- Unique studies after exact DOI/title deduplication: `4,337`
- Cross-database duplicate studies: `309`
- PubMed-only studies after deduplication: `2,424`
- Embase-only studies after deduplication: `1,604`

### Important caveat

The search was intentionally high-sensitivity. As a result, a large proportion of the yield is broad spillover from:

- general oncology AI
- pathology foundation-model literature
- multimodal immune profiling
- single-cell and multi-omics studies
- non-hematology microscopy

That broad spillover is useful for context, but it is **not** the true doctoral competitive set.

Another important limitation is that the exported PubMed CSV does not contain abstracts. The initial mapping therefore relies heavily on:

- title
- citation metadata
- DOI
- Embase abstracts/keywords when the same paper appeared in both databases

## Overall Shape of the Literature

The retrieved literature separates into two very different zones:

## Zone 1. High-volume but only partially relevant

This is the largest part of the search yield. It includes:

- generic white blood cell image classification
- leukemia image classification benchmarks
- digital pathology and bone marrow image AI
- broad multimodal cancer or immune-cell profiling
- laboratory analyzer validation studies

This zone is important because it shows where the field is active, but much of it is not directly competitive with the proposed PhD.

## Zone 2. Small but strategically critical

This is the area that matters most for the PhD proposal:

- smear morphology + structured laboratory data
- morphology + CBC integration
- analyzer flags + AI-assisted decision support
- workflow-level hematology intelligence
- LLM/diagnostic reasoning applied to morphology or laboratory interpretation
- domain generalization and real-world robustness in hematology AI

This second zone is much smaller, more fragmented, and much less mature.

## Dominant Thematic Clusters

## 1. Leukocyte / blood-cell image classification and detection

This is the dominant core cluster within the actually relevant hematology subset.

Typical features:

- peripheral blood smear or single-cell image input
- CNN / ViT / YOLO comparisons
- segmentation + classification pipelines
- synthetic augmentation or stain normalization
- benchmark-style reporting

This cluster is active, crowded, and technically mature enough that pure model-comparison work is increasingly low-yield scientifically.

## 2. Acute leukemia / blast / dysplasia morphology AI

This is the second major cluster.

Typical focus:

- AML / ALL detection
- blast classification
- bone marrow or peripheral smear morphology
- dysplasia detection
- weakly supervised or generalizable morphology models

This area remains clinically important and still scientifically active, especially when it moves beyond easy classes and into difficult abnormal morphology.

## 3. Digital morphology analyzers and laboratory workflow support

This is one of the most strategically important clusters for your PhD positioning.

Typical focus:

- Scopio, CellaVision, Sysmex, Mindray, HemaVision, Sight OLO
- AI-assisted smear review
- manual review reduction
- analyzer comparison
- platelet estimation
- differential count support
- practical workflow integration

This cluster is less algorithmically flashy than image-classification papers, but it is more clinically realistic.

## 4. Bone marrow and digital hematopathology AI

This is a strong neighboring field rather than your exact core.

Typical focus:

- whole-slide bone marrow analysis
- dysplasia detection
- cell counting in marrow aspirates
- hematopathology digital workflows

This literature matters because it shows how hematology AI matures when it becomes case-level, workflow-level, and clinically integrated.

## 5. CBC / analyzer / laboratory parameter modeling

This cluster is present but clearly smaller than image-only morphology work.

Typical focus:

- analyzer parameters
- CBC-derived prediction
- rules for smear review
- morphology analyzer output integration
- pre-microscopic flagging

This is the cluster that most directly supports the doctoral idea of structured laboratory intelligence.

## 6. LLM / reasoning / decision support in hematology

This cluster exists, but it is still early and sparse.

The most visible strands are:

- ChatGPT or GPT-4 smear/morphology recognition studies
- LLM versus hematologist comparisons
- multimodal LLM image recognition studies
- blood-film interpretation support tools
- EHR-linked or web-based support tools

The number of studies is still modest, and much of the work looks exploratory rather than mature.

## Specific Buckets Relevant to the Proposed PhD

## Multimodal hematology studies

The broad search retrieved many papers with the word `multimodal`, but most are **not** true multimodal clinical-laboratory hematology studies.

Most false-positive multimodal records are:

- oncology multi-omics
- immune-cell profiling
- multimodal pathology foundation-model work
- multimodal therapy case reports

The **true multimodal hematology** subset appears to be small.

The strongest directly relevant examples found in the export set include:

- `Identifying Hospitalized Patients with Acute Decompensation Risk from Peripheral Blood Smears and Laboratory Results using Multimodal, Multiencoder, Multiple Instance Learning (M3MIL)`  
  DOI: `10.1093/ajcp/aqaf121.430`
- `AI Based Multi-modal Parameter of Peripheral Blood Cells (MMPBC) Predicts Survival Risk in Critically Ill Children: a Multicenter, Retrospective Cohort Study`
- `Application of Convolutional Neural Network Image Analysis and Machine Learning to Basic Blood Tests for Intelligent Diagnostic Assistance`  
  DOI: `10.1111/ijlh.14550`
- `PROSER: A Web-Based Peripheral Blood Smear Interpretation Support Tool Utilizing Electronic Health Record Data`  
  DOI: `10.1093/ajcp/aqad024`

Strategic conclusion:

The literature contains **signals**, not saturation, for true multimodal hematology intelligence.

## Morphology + CBC integration

This is one of the clearest underdeveloped spaces in the search set.

Relevant examples include:

- `Development of criteria to optimize manual smear review of automated complete blood counts using a machine learning model`  
  DOI: `10.1111/vcp.13400`
- `diagnostic algorithm for the detection of blasts in peripheral blood based on morphological flags from the integrated sysmex Xn-9100 system`  
  DOI: `10.23736/S1825-859X.24.00257-3`
- `Application of Convolutional Neural Network Image Analysis and Machine Learning to Basic Blood Tests for Intelligent Diagnostic Assistance`  
  DOI: `10.1111/ijlh.14550`
- `Identifying Hospitalized Patients with Acute Decompensation Risk from Peripheral Blood Smears and Laboratory Results using Multimodal, Multiencoder, Multiple Instance Learning (M3MIL)`  
  DOI: `10.1093/ajcp/aqaf121.430`

Strategic conclusion:

This is much less crowded than image-only morphology and much more directly aligned with a defensible doctoral niche.

## Robustness / domain shift studies

This is an active but still methodologically incomplete cluster.

Relevant examples include:

- `Contrastive Representation Learning for Cross-Domain Blood Cell Image Classification With Denoising Mechanism`  
  DOI: `10.1109/JBHI.2025.3585548`
- `Domain-incremental white blood cell classification with privacy-aware continual learning`  
  DOI: `10.1038/s41598-025-08024-z`
- `FL-W3S: Cross-domain federated learning for weakly supervised semantic segmentation of white blood cells`  
  DOI: `10.1016/j.ijmedinf.2025.105806`
- `Transferable automatic hematological cell classification: Overcoming data limitations with self-supervised learning`  
  DOI: `10.1016/j.cmpb.2024.108560`
- `DeepHeme, a high-performance, generalizable deep ensemble for bone marrow morphometry and hematologic diagnosis`  
  DOI: `10.1126/scitranslmed.adq2162`

Strategic conclusion:

Robustness is active, but mostly still inside image-centric pipelines. The integration of robustness with multimodal laboratory intelligence remains largely open.

## Laboratory reasoning systems

This cluster is present but small.

Most relevant examples include:

- `PROSER: A Web-Based Peripheral Blood Smear Interpretation Support Tool Utilizing Electronic Health Record Data`  
  DOI: `10.1093/ajcp/aqad024`
- `The use and effectiveness of an online diagnostic support system for blood film interpretation: Comparative observational study`  
  DOI: `10.2196/20815`
- `Decision support system for the classification of Downey cells as a prediagnostic tool`  
  DOI: `10.1515/tjb-2023-0035`
- `Decision tree-enabled establishment and validation of intelligent verification rules for blood analysis results`

Strategic conclusion:

Reasoning and support systems exist, but they are still relatively disconnected from modern multimodal AI.

## Agentic / LLM laboratory studies

This area is clearly emerging, but not yet mature.

Most relevant examples include:

- `Artificial intelligence in hematology: Evaluating a large language model for morphology-based diagnostics`  
  DOI: `10.4103/ijpm.ijpm_1191_25`
- `COMPARATIVE EFFECTIVENESS OF HEMATOLOGISTS WITH LARGE LANGUAGE MODELS IN HEMATOLOGIC DIAGNOSIS`  
  DOI: `10.1016/j.htct.2025.104218`
- `MDS-1223: Benchmarking Few-Shot GPT-4o Against Supervised Fine-Tuning for Morphologic Identification of Peripheral Blood Smears`  
  DOI: `10.1016/S2152-2650(25)02070-1`
- `Comparative Evaluation of Five Multimodal Large Language Models for Medical Laboratory Image Recognition: Impact of Prompting Strategies on Diagnostic Accuracy`  
  DOI: `10.3390/diagnostics16091258`
- `ChatGPT's innovative application in blood morphology recognition`  
  DOI: `10.1097/JCMA.0000000000001071`

Strategic conclusion:

This area has visibility, but it currently looks more exploratory and benchmark-driven than translationally mature.

## Recurring Datasets

The most repeatedly visible datasets and platforms in the export set are:

- `CellaVision DM96` or related CellaVision workflows
- `BCCD`
- `LISC`
- `ALL-IDB`
- `Raabin-WBC`
- `PBC`
- `C-NMC`

These patterns suggest that the literature is still heavily anchored in public image benchmarks plus vendor-linked analyzer or workflow studies.

## Recurring Methodological Limitations

The same weaknesses appear repeatedly across the relevant records:

1. Image-only designs with no structured laboratory integration.
2. Cell-level classification rather than case-level diagnostic inference.
3. Benchmark dependence on a small set of reused public datasets.
4. Limited representation of rare, immature, atypical, or clinically difficult cells.
5. Limited external validation and weak interlaboratory generalization.
6. Heavy focus on accuracy/F1 with less attention to calibration, uncertainty, and decision thresholds.
7. Conference abstracts or early-stage evaluations with incomplete methodological detail.

## Recurring Clinical Limitations

1. Single-center retrospective cohorts.
2. Weak embedding in actual laboratory decision pathways.
3. Limited connection to analyzer outputs, CBC context, or reflex-smear workflows.
4. Limited demonstration of reduced manual workload or improved diagnostic throughput.
5. Sparse evidence for prospective deployment or multi-site robustness.

## Initial Strategic Interpretation

The evidence map supports a strong distinction between:

- a **saturated image-classification literature**
- and a **much thinner multimodal clinical-laboratory intelligence literature**

That distinction is the most important signal for doctoral positioning.
