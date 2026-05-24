# Reproducible Literature Search Protocol

## Topic

**Multimodal clinical-laboratory intelligence for hematology**

## Purpose

This protocol is designed to evaluate whether integrating peripheral blood smear morphology with structured hematology/laboratory data, analyzer flags, CBC parameters, and reasoning-aware AI represents a strong, novel, and feasible PhD direction.

This is a **search protocol only**. It does **not** summarize or synthesize results yet.

## Protocol Metadata

- Protocol version: `v1.0`
- Draft date: `2026-05-24`
- Prepared for: doctoral positioning within `PPGCC/UFSC`
- Candidate profile anchor: leukocyte classification, hematology computer vision, dataset construction, Vision Transformers, YOLO, stain augmentation, domain generalization, clinical laboratory practice

## Review Question Framework

### Preferred framework: PCC

#### Population / Problem / Context

Human hematology and clinical laboratory medicine, especially:

- peripheral blood smear
- blood cell morphology
- complete blood count
- leukocyte differential
- hematologic diagnostics
- clinical hematology workflows
- real-world laboratory data

#### Concept

Computational methods for multimodal clinical-laboratory intelligence, including:

- artificial intelligence
- machine learning
- deep learning
- multimodal learning
- data fusion
- image + tabular integration
- foundation-model-related methods
- large language models
- knowledge-grounded reasoning
- agentic AI
- clinical decision support
- interpretability, uncertainty, robustness, and domain generalization

#### Context / Application

Laboratory medicine and hematology decision support in clinically realistic settings, especially:

- diagnostic support
- morphology-assisted interpretation
- analyzer-assisted review
- integrated interpretation of smear + CBC + flags + metadata
- real-world or practice-oriented validation

## Primary Review Question

What computational approaches have been used in hematology and clinical laboratory medicine to integrate peripheral blood smear morphology with structured laboratory data, CBC parameters, analyzer outputs, or reasoning-aware AI for diagnostic support?

## Secondary Questions

1. How often are image and structured laboratory modalities combined in hematology AI?
2. Which tasks are most common: classification, triage, abnormality detection, case-level diagnosis, laboratory decision support, or report assistance?
3. Are reasoning-oriented approaches, knowledge-grounded AI, or LLM-based methods already present in hematology/laboratory settings?
4. How are robustness, domain shift, calibration, interpretability, and uncertainty handled?
5. Where are the main literature gaps that support a doctoral project?

## Search Logic Overview

The search is built from concept blocks that can be combined differently depending on database coverage and interface limitations.

### Block A. Hematology / laboratory domain

- hematology
- hematologic tests
- clinical laboratory techniques
- laboratory medicine
- clinical laboratory
- complete blood count
- hemogram
- leukocyte differential
- blood cell count

### Block B. Peripheral blood smear / cell morphology

- blood smear
- peripheral blood smear
- peripheral blood film
- blood film
- smear review
- leukocyte morphology
- white blood cell morphology
- hematologic cell morphology
- digital microscopy / microscopy when relevant

### Block C. Structured laboratory data / CBC / analyzer flags

- complete blood count
- CBC
- full blood count
- FBC
- hemogram
- hematology analyzer
- analyzer flag
- instrument flag
- laboratory parameter
- blood count parameter
- structured laboratory data

### Block D. AI / ML / deep learning

- artificial intelligence
- machine learning
- deep learning
- neural networks
- computer vision
- transformers
- vision transformer
- YOLO
- predictive modeling

### Block E. Multimodal learning / data fusion

- multimodal
- multimodal learning
- multimodal AI
- data fusion
- multimodal fusion
- multi-source data
- image and tabular
- image and laboratory data
- cross-modal

### Block F. Reasoning systems / LLMs / knowledge-grounded AI

- reasoning
- reasoning-aware AI
- large language model
- large language models
- foundation model
- foundation models
- clinical reasoning
- knowledge graph
- retrieval-augmented generation
- RAG
- agentic AI
- multi-agent
- decision support

### Block G. Robustness / domain shift / interpretability / uncertainty

- domain generalization
- domain adaptation
- domain shift
- robustness
- uncertainty
- uncertainty estimation
- calibration
- explainability
- interpretability
- out-of-distribution
- OOD

## Recommended Search Sequence

The search should be run in three passes per database:

1. **Broad / high sensitivity**
   Capture the full candidate space across hematology, laboratory medicine, multimodal AI, and reasoning-oriented systems.
2. **Focused / high specificity**
   Prioritize papers clearly combining morphology or blood smear data with structured laboratory data.
3. **Exploratory / cutting-edge**
   Capture recent work on LLMs, foundation models, agentic systems, knowledge graphs, and reasoning-aware hematology/laboratory AI.

## Controlled Vocabulary Strategy

### PubMed / MEDLINE

Use verified MeSH where available, then combine with Title/Abstract free text to avoid missing newly indexed or not-yet-indexed studies.

### SciELO / BVS

Use DeCS descriptors where relevant, but maintain multilingual free-text terms in Portuguese, English, and Spanish because title/abstract indexing varies.

### Embase

Use Emtree explosion where the preferred term is verified or strongly expected from MeSH-to-Emtree mapping. Where the exact preferred Emtree term is uncertain, mark the descriptor as **to verify in the Embase thesaurus** before final execution.

### Scopus / Web of Science / IEEE Xplore / ACM Digital Library

These are primarily searched with structured free text. Controlled vocab may be absent or less central.

## Time Window

### Primary window

- Last 5 years: `2021-2026`

### Secondary allowance

- Seminal older studies may be retained if they are methodologically foundational, especially for:
  - multimodal fusion concepts
  - clinical decision support in laboratory medicine
  - peripheral smear automation
  - knowledge-grounded biomedical AI

## Language

Include:

- English
- Portuguese
- Spanish

Primary screening language is expected to be English, but Portuguese and Spanish are important for SciELO/BVS capture and Latin American laboratory/hematology work.

## Study Types Eligible for Retrieval

- original research articles
- conference papers, especially in IEEE/ACM for computational methods
- systematic reviews and scoping reviews
- benchmark and dataset papers
- methods papers
- clinically oriented AI evaluation studies

## Inclusion Criteria

Include studies that meet at least one of the following:

1. AI/ML applied to hematology or clinical laboratory medicine.
2. Peripheral blood smear or blood-cell morphology used in a computational pipeline.
3. Structured laboratory data used for hematology-related prediction, triage, or decision support.
4. Multimodal integration of image data plus tabular/laboratory/clinical metadata.
5. Clinical decision support, reasoning, LLM, knowledge graph, or agentic AI applied to hematology or laboratory interpretation.
6. Studies discussing robustness, domain shift, uncertainty, calibration, or interpretability in this context.

## Exclusion Criteria

Exclude:

1. Purely veterinary or non-human studies unless methodologically exceptional and clearly relevant.
2. Generic medical AI with no hematology or laboratory relevance.
3. Radiology-only multimodal AI unless it contributes a transferable multimodal method that is unusually relevant.
4. Genomics-only or omics-only studies with no laboratory morphology or CBC/laboratory interpretation relevance.
5. Pure wet-lab hematology without computational methods.
6. Pure image classification papers outside hematology unless used as background for multimodal methodology.

## Screening Workflow

### Stage 1. Title/abstract screening

Label each record:

- `directly relevant`
- `adjacent but useful`
- `background only`
- `exclude`

### Stage 2. Full-text screening

Apply the same labels, but record reasons for exclusion where possible.

### Stage 3. Evidence mapping

Map included studies by:

- modality
- task
- data combination strategy
- AI family
- validation type
- clinical realism
- robustness handling

## Reproducibility Notes

1. Record the exact search date for every database run.
2. Export the full query string used in each database.
3. Save the number of retrieved records before deduplication.
4. Save database-specific filters separately from the raw query.
5. Record any query adaptation made due to interface syntax limits.
6. Record whether conference abstracts were included or excluded in Embase/Scopus/IEEE/ACM.

## Key Risk in This Search

The phrase **multimodal** is often used narrowly in radiology or imaging-platform contexts and may not capture **image + structured laboratory data**. For that reason, the protocol intentionally combines:

- multimodal/free-text terms
- explicit data fusion terms
- explicit image + tabular/laboratory combinations
- explicit reasoning and decision support terms

## Expected Output of the Search Phase

The search should help answer:

- Is the topic novel enough?
- Is morphology + CBC/laboratory integration already established or still underdeveloped?
- Are reasoning-aware and LLM-based hematology/laboratory systems emerging or sparse?
- Does the literature support a doctoral positioning centered on multimodal clinical-laboratory intelligence?

## Controlled Vocabulary Status Note

This protocol uses three statuses:

- `verified`: confirmed from an official thesaurus source
- `provisional`: highly likely term, but should be checked before final execution
- `free-text only`: no controlled term confidently verified, so use text words

See:

- `database_search_strings.md`
- `screening_criteria.md`
- `extraction_form.md`
- `candidate_topics/multimodal_hematology_search_strategy.md`
