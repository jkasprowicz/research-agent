# Screening Criteria

## Purpose

This file standardizes title/abstract and full-text screening for the doctoral topic:

**Multimodal clinical-laboratory intelligence for hematology**

## Screening Labels

Each record should receive exactly one of the following labels:

### 1. `directly relevant`

Use when the paper clearly matches the doctoral topic or can directly support the proposal.

Typical cases:

- peripheral blood smear AI combined with CBC, laboratory parameters, analyzer outputs, or structured data
- multimodal hematology AI
- laboratory decision support systems for hematology
- reasoning-aware AI in laboratory medicine
- knowledge-graph or LLM applications specifically tied to hematology/laboratory interpretation
- robust or interpretable hematology AI with clinically realistic laboratory context

### 2. `adjacent but useful`

Use when the paper is not directly on the target topic but contributes methods, framing, or relevant precedent.

Typical cases:

- blood smear AI without structured data integration
- laboratory AI using tabular CBC data but without image integration
- multimodal medical AI outside hematology with transferable methods
- clinical decision support or knowledge-grounded medical AI relevant to later thesis framing
- domain adaptation, uncertainty, or interpretability methods applicable to hematology

### 3. `background only`

Use when the paper provides conceptual or disciplinary background but is unlikely to support the core novelty argument.

Typical cases:

- classic hematology or blood smear workflow descriptions
- general reviews on laboratory medicine
- general reviews on multimodal AI or LLMs with no hematology/laboratory specificity
- purely descriptive laboratory process papers without computational content

### 4. `exclude`

Use when the paper does not materially contribute to the doctoral topic.

Typical cases:

- veterinary-only studies without methodological value
- radiology-only multimodal AI
- genomics-only studies with no laboratory morphology/CBC relevance
- generic medical AI with no hematology/laboratory connection
- non-computational laboratory papers
- purely clinical treatment papers

## Title/Abstract Screening Rules

Assign `directly relevant` if the title/abstract clearly contains:

1. a hematology or clinical laboratory setting, and
2. AI/ML or decision support, and
3. at least one of the following:
   - blood smear / morphology
   - CBC / hemogram / laboratory parameters
   - multimodal / data fusion
   - reasoning / knowledge graph / LLM / agentic AI
   - robustness / uncertainty / interpretability in hematology AI

Assign `adjacent but useful` if only two of the three are clearly present but the paper still looks strategically useful.

Assign `background only` if the paper is foundational context but does not appear to advance the doctoral theme itself.

Assign `exclude` if it fails the hematology/laboratory relevance test or the computational relevance test.

## Full-Text Inclusion Criteria

Include as `directly relevant` or `adjacent but useful` if the full text shows one or more of the following:

### Hematology / laboratory relevance

- human hematology diagnostics
- peripheral blood smear review
- complete blood count interpretation
- leukocyte differential or blood cell morphology
- laboratory workflow, analyzer, or pathology review context

### Computational relevance

- artificial intelligence or machine learning method
- multimodal fusion strategy
- image + structured/tabular data integration
- knowledge-grounded or reasoning-based approach
- clinical decision support logic
- validation of robustness, calibration, uncertainty, or interpretability

### Doctoral positioning relevance

- supports the novelty of multimodal hematology AI
- identifies gaps in integrated morphology + laboratory reasoning
- strengthens feasibility arguments
- helps define methodological architecture for the PhD

## Full-Text Exclusion Criteria

Exclude at full text if:

1. The setting is not hematology or clinical laboratory medicine.
2. The computational component is trivial or absent.
3. The paper is entirely about radiology, pathology outside blood/laboratory context, or genomics-only analytics.
4. The paper does not contribute to multimodal, decision support, reasoning, or laboratory intelligence framing.
5. The paper is duplicate, inaccessible without enough metadata, or non-scholarly.

## Priority Ranking During Screening

When triaging volume, prioritize this order:

1. image + CBC/lab data integration in hematology
2. blood smear AI with analyzer/CBC or case-level interpretation
3. laboratory decision support in hematology
4. hematology LLM / knowledge graph / reasoning systems
5. robustness / interpretability / uncertainty in hematology AI
6. adjacent multimodal or clinical decision support methods

## Suggested Reasons for Exclusion

Record one short reason where possible:

- no hematology context
- no laboratory context
- no computational method
- radiology-only
- genomics-only
- veterinary-only
- no multimodal or decision-support relevance
- commentary/editorial only
- duplicate

## Notes for Borderline Cases

### Include if likely useful

- image-only hematology AI papers with strong discussion of clinical workflow, robustness, or decision support
- tabular hematology prediction papers using CBC and analyzer data
- multimodal medical AI papers with a very transferable fusion strategy
- reasoning/LLM healthcare papers if they explicitly address structured clinical data and decision support

### Exclude unless exceptional

- general computer vision classification papers
- microscopy studies unrelated to hematology
- LLM papers with no clinical/laboratory use case
- biomedical knowledge graph papers with no practical diagnostic or clinical reasoning application

## Minimal Screening Form

Use these fields during review:

- record ID
- citation
- database source
- title/abstract label
- full-text label
- exclusion reason if excluded
- short note on relevance to PhD
