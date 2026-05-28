# Multimodal Expansion Strategy

## Strategic principle

The doctoral expansion should be **morphology-first, multimodal-second, reasoning-later**.

This means:

- morphology remains the anchor modality;
- multimodal integration is the core scientific expansion;
- broader reasoning layers are optional and only justified after the multimodal base is mature.

## 1. Expansion logic

The project should not expand by adding many unrelated data sources at once. It should expand by gradually increasing the inferential richness of the same hematology problem.

Recommended progression:

1. leukocyte morphology in isolated cells;
2. morphology aggregated at smear or case level;
3. morphology integrated with CBC and analyzer-derived structured data;
4. multimodal support for laboratory triage or review;
5. optional structured reasoning layer.

## 2. How additional morphology domains can be incorporated

### 2.1 Erythrocyte abnormalities

**How to incorporate:** as a secondary morphology channel when directly relevant to the case-level task.  
**Why it fits:** erythrocyte morphology strengthens the move from leukocyte-only recognition to whole-smear reasoning. It is especially useful when the task involves anemia patterns, dysplasia suspicion, or smear-review prioritization.

**Best role in the PhD:** controlled expansion after the initial leukocyte-centered multimodal core is stable.

### 2.2 Platelet morphology

**How to incorporate:** as targeted features or categories when platelet abnormalities are relevant to triage, analyzer discrepancy, or abnormal smear review.

**Best role in the PhD:** selective inclusion, not a separate thesis line. Platelets should enter when they improve case-level inference, not to create a parallel platelet-only project.

### 2.3 Immature cells

**How to incorporate:** as a high-priority continuity domain.  
**Why it fits:** immature cells are already part of the master's scientific seriousness and are highly relevant for escalation from isolated-cell classification to case-level warning signals.

**Best role in the PhD:** core thesis material, especially for tasks involving suspicion of hematologic abnormality, review prioritization, or multimodal discordance detection.

### 2.4 Morphologic abnormalities

**How to incorporate:** not only as cell classes, but as interpretable abnormality signals that can be aggregated at case level.

Examples:

- toxic granulation;
- hypolobulation or hyperlobulation;
- anisopoikilocytosis-related signals;
- atypical lymphoid morphology;
- blast-like or dysplastic patterns.

**Best role in the PhD:** gradual and task-driven. Morphologic abnormalities should be introduced where they strengthen interpretability and case-level relevance.

### 2.5 Analyzer flags

**How to incorporate:** as structured, machine-generated signals that complement morphology and CBC.

Examples:

- immature granulocyte flags;
- blast or abnormal cell alerts;
- platelet-clump-related alerts;
- instrument review recommendations.

**Best role in the PhD:** core thesis material. Analyzer flags are a natural bridge between morphology and structured laboratory intelligence.

### 2.6 Structured laboratory data

**How to incorporate:** as the central non-image modality in the thesis.

Priority variables:

- CBC parameters;
- differential counts;
- hemoglobin, hematocrit, red-cell indices;
- platelet count and platelet-related indices;
- selected metadata linked to review logic;
- analyzer abnormal flags.

**Best role in the PhD:** core thesis material. This is the main mechanism that turns the project from morphology AI into multimodal hematology intelligence.

## 3. Recommended staged expansion

### Stage 1. Core multimodal thesis

Integrate:

- leukocyte-centered morphology;
- immature and atypical cell signals;
- CBC parameters;
- analyzer flags;
- essential structured laboratory metadata.

This stage is the actual thesis core.

### Stage 2. Controlled morphology broadening

Add, only if justified by data quality and publication value:

- erythrocyte abnormalities;
- platelet morphology;
- broader abnormality descriptors.

This should happen only if the additions improve case-level tasks and remain manageable.

### Stage 3. Optional interpretive extension

Add, only after the multimodal models are stable:

- rule-based support;
- retrieval over structured laboratory knowledge;
- limited explanation assistance.

This stage is optional and should never delay the core thesis.

## 4. What to avoid during expansion

- Expanding to all blood-cell lineages at once from the start.
- Turning the project into a complete digital hematopathology platform.
- Introducing genomics, flow cytometry, bone marrow, or molecular pathology as major data streams.
- Building a generic medical reasoning agent with weak connection to smear review.
- Promising prospective deployment-grade clinical software during the PhD.

## 5. Best expansion framing

The best wording is:

> The doctoral project begins from leukocyte-centered morphology, especially clinically relevant immature and atypical patterns, and expands toward case-level multimodal inference by integrating morphology with CBC parameters, analyzer flags, and structured laboratory data. Additional morphology domains such as erythrocyte and platelet abnormalities may be incorporated only when they directly strengthen the central case-level laboratory decision-support tasks.

## Bottom line

The right expansion is not “more data everywhere.”  
It is **better inference over the same hematology reality**.
