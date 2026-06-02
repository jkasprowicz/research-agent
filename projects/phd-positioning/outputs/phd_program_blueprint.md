# PhD Program Blueprint

## Working thesis identity

**From morphology intelligence to workflow-aware multimodal laboratory decision support in hematology**

## Core thesis premise

This doctoral program unifies the three strongest ranked opportunities:

- `C1` multimodal smear review triage and prioritization
- `B2` multimodal discordance modeling
- `E2` longitudinal review-trigger prediction

The thesis is built around a single claim:

**peripheral blood smear review can be supported more effectively when morphology-derived evidence is integrated with CBC, Sysmex parameters, analyzer flags, and longitudinal laboratory context at the case level, especially for triage, suspicious-case detection, and review escalation.**

This creates one coherent narrative:

1. establish a robust multimodal baseline for case-level triage
2. show that cross-modal discordance carries added value beyond raw prediction
3. show that longitudinal context improves review-trigger decisions
4. consolidate the components into a workflow-aware decision-support framework

This is a doctoral program, not a universal platform. It stays focused on:

- peripheral blood smear workflow
- real retrospective laboratory data
- actionable support for review decisions
- interpretable and robust multimodal modeling

---

## Program structure

The recommended program contains **4 publishable studies**. This is the best balance between coherence, publication potential, and feasibility for a working professional.

### Study 1

**Multimodal case-level triage for peripheral blood smear review**

### Study 2

**Discordance-aware multimodal modeling for suspicious-case detection**

### Study 3

**Longitudinal prediction of smear review triggers**

### Study 4

**Integrated workflow-aware laboratory decision support framework**

An optional fifth study can be added only if the program is ahead of schedule:

### Optional Study 5

**Robustness and external temporal validation of multimodal hematology decision support**

This optional paper should be treated as a bonus, not as part of the core PhD dependency chain.

---

## Coherent thesis narrative

The thesis should tell a single story:

### Phase 1: Static multimodal support

Image-only morphology systems and analyzer/CBC-only triage systems are both incomplete. The first study demonstrates that combining smear-derived and structured laboratory information supports case-level review prioritization better than either modality alone.

### Phase 2: Why multimodality matters

The second study moves beyond performance comparison and asks a more scientific question: when do modalities disagree, and can discordance itself identify suspicious, uncertain, or high-priority cases? This gives the thesis a stronger Computer Science contribution than simply building a better classifier.

### Phase 3: Temporal workflow intelligence

The third study adds the dimension that is missing from most of the current literature: time. Review needs are often not static. A case may become suspicious because of trajectory, not only because of one isolated smear and one isolated CBC. This study brings longitudinal laboratory intelligence into the thesis.

### Phase 4: Workflow-oriented synthesis

The fourth study consolidates the evidence into a task-focused framework for real laboratory decision support. The emphasis is not autonomous diagnosis; it is support for:

- whether to review
- how urgently to review
- why a case deserves escalation

That final synthesis gives the thesis conceptual unity.

---

## Realistic datasets

The program should be designed around **three linked retrospective datasets**, each progressively richer.

## Dataset A: Static smear-review cohort

Purpose:

- support Study 1 and part of Study 2

Expected contents:

- Cellavision peripheral blood smear images
- CBC results from the same case episode
- Sysmex analyzer parameters
- Sysmex research parameters if available
- analyzer flags
- review outcome labels from historical practice

Typical unit:

- one laboratory case episode

Likely labels:

- reviewed vs not reviewed
- normal vs abnormal review outcome
- high-priority vs routine review proxy

Complexity:

- moderate

## Dataset B: Discordance-enriched adjudication cohort

Purpose:

- support Study 2

Expected contents:

- all Dataset A modalities
- expert review outcome
- subset of cases selected for disagreement or ambiguity
- optional manual adjudication of suspicious multimodal mismatch patterns

Typical unit:

- one case episode with enriched expert ground truth

Likely labels:

- concordant vs discordant
- low-risk vs suspicious discordance
- escalation-worthy discordance

Complexity:

- moderate to high

## Dataset C: Longitudinal patient-laboratory cohort

Purpose:

- support Study 3 and Study 4

Expected contents:

- repeated CBCs
- repeated Sysmex parameters
- repeated flags
- linked smear-review episodes when present
- patient identifier for retrospective linkage
- timestamps
- selected encounter context

Typical unit:

- patient timeline with repeated laboratory events

Likely labels:

- future smear review within a predefined window
- review escalation within a predefined window
- abnormal follow-up review proxy

Complexity:

- high

---

## Realistic ethics requirements

The program should be split into ethics layers to reduce startup risk.

## Ethics layer 1: retrospective laboratory data only

Supports:

- Study 1

Includes:

- smear images
- CBC
- Sysmex outputs
- analyzer flags
- historical review decisions

Risk:

- lowest

## Ethics layer 2: retrospective expert adjudication subset

Supports:

- Study 2

Includes:

- all of layer 1
- targeted expert re-review of selected cases

Risk:

- moderate

## Ethics layer 3: longitudinal patient linkage

Supports:

- Study 3
- Study 4

Includes:

- patient-level retrospective linkage across multiple timepoints
- selected encounter information

Risk:

- moderate to high

## Ethics layer 4: hospital outcomes, if needed

Supports:

- optional secondary analyses only

Recommendation:

- do not make hospital outcomes a dependency of the core thesis

This is important for feasibility. The main thesis should survive even if access to outcomes is delayed or restricted.

---

## Recommended timeline for a working professional

This blueprint assumes approximately **48 months** of doctoral work under full-time employment, with a conservative pace.

## Year 1

- finalize thesis framing and advisor alignment
- obtain Ethics layer 1 approval
- build Dataset A
- define review-related endpoints
- complete Study 1

## Year 2

- submit Study 1
- obtain Ethics layer 2 approval if needed as amendment
- build Dataset B
- complete Study 2

## Year 3

- submit Study 2
- obtain Ethics layer 3 approval
- build Dataset C
- complete Study 3

## Year 4

- submit Study 3
- integrate results across studies
- complete Study 4
- write thesis
- optional robustness/validation paper only if time and data allow

This sequence is realistic because the first paper does not depend on the most difficult data linkage step.

---

## Study-by-study design

## Study 1. Multimodal case-level triage for peripheral blood smear review

### Objective

Develop and evaluate a case-level model that combines smear-derived morphology with CBC, Sysmex parameters, and analyzer flags to support peripheral blood smear review triage.

### Inputs

- Cellavision smear images
- CBC results
- Sysmex analyzer parameters
- Sysmex research parameters when available
- analyzer flags

### Outputs

- probability of manual smear review need
- probability of abnormal review outcome
- ranking score for review prioritization

### Core question

Does multimodal integration improve triage performance over:

- image-only baselines
- CBC/analyzer-only baselines

### Main contribution

- establish the thesis baseline
- show the first measurable value of multimodal integration

### Relationship with previous studies

- starting study
- creates the core multimodal dataset and baseline models

### Target publication venue

Preferred:

- `International Journal of Laboratory Hematology`
- `Diagnostics`
- `Clinical Chemistry and Laboratory Medicine`

Alternative computing-oriented venue:

- `Computers in Biology and Medicine`

### Why this study comes first

- highest feasibility
- clear labels
- strong translational value
- no need for the hardest longitudinal linkage at the beginning

---

## Study 2. Discordance-aware multimodal modeling for suspicious-case detection

### Objective

Quantify and model discordance between morphology-derived evidence and structured laboratory signals, and evaluate whether discordance improves detection of suspicious or escalation-worthy cases.

### Inputs

- outputs from morphology branch
- CBC and Sysmex structured data
- analyzer flags
- selected expert-adjudicated cases

### Outputs

- discordance score
- uncertainty score
- suspicious-case or escalation prediction
- explainable case-level evidence profile

### Core question

When morphology and structured laboratory context disagree, does that disagreement identify cases that deserve manual attention better than standard multimodal prediction alone?

### Main contribution

- deeper scientific explanation of why multimodality matters
- stronger Computer Science identity through multimodal uncertainty and consistency analysis

### Relationship with previous studies

- builds directly on Study 1
- uses the multimodal baseline as a reference point
- should reuse feature pipelines or encoders when possible

### Target publication venue

Preferred:

- `Artificial Intelligence in Medicine`
- `Journal of Biomedical Informatics`
- `Computers in Biology and Medicine`

Alternative:

- `NPJ Digital Medicine` if the experimental quality is high enough

### Why this study matters

- this is the study most likely to move the thesis beyond “a better predictor”
- it creates a distinctive scientific identity

---

## Study 3. Longitudinal prediction of smear review triggers

### Objective

Develop temporal models that use repeated laboratory trajectories to predict future smear review need or escalation before a static threshold-based system would do so.

### Inputs

- serial CBC results
- serial Sysmex parameters
- serial analyzer flags
- timestamps
- linked smear-review events
- optional sparse image episode summaries

### Outputs

- probability of review trigger within a future time window
- escalation-risk score
- temporal explanation of trigger patterns

### Core question

Do longitudinal laboratory trajectories improve review-trigger prediction compared with single-timepoint multimodal assessment?

### Main contribution

- introduces temporal intelligence into the thesis
- leverages a rare asset that many morphology papers do not have

### Relationship with previous studies

- conceptually extends Study 1 from static to temporal triage
- can use discordance concepts from Study 2 as temporal features

### Target publication venue

Preferred:

- `Journal of Biomedical Informatics`
- `Artificial Intelligence in Medicine`
- `IEEE Journal of Biomedical and Health Informatics`

Alternative:

- `BMC Medical Informatics and Decision Making`

### Why this study matters

- strongest use of the richer laboratory ecosystem
- especially valuable for differentiating the thesis from existing morphology + CBC papers

---

## Study 4. Integrated workflow-aware laboratory decision support framework

### Objective

Synthesize the findings of Studies 1 to 3 into a unified framework for workflow-aware laboratory decision support in peripheral blood smear analysis.

### Inputs

- static multimodal case data
- discordance features
- longitudinal trigger features
- laboratory workflow labels

### Outputs

- unified conceptual and computational framework
- ablation comparing static, discordance-aware, and longitudinal models
- decision-support policy for review priority and escalation support

### Core question

What combination of static multimodal evidence, discordance analysis, and longitudinal context provides the most useful support for smear-review workflow?

### Main contribution

- thesis-level synthesis
- defines the doctoral contribution as a coherent decision-support framework rather than a collection of separate models

### Relationship with previous studies

- integrates Studies 1, 2, and 3
- should not require an entirely new dataset
- should emphasize comparative evaluation and framework design

### Target publication venue

Preferred:

- `Journal of Biomedical Informatics`
- `Artificial Intelligence in Medicine`
- `NPJ Digital Medicine`

Alternative:

- strong journal extension of the thesis core if one of the earlier studies appears in a more domain-specific venue

### Why this study closes the thesis well

- it converts the program from a sequence of papers into a doctoral argument
- it explicitly answers what kind of laboratory AI support is genuinely useful

---

## Optional Study 5. Robustness and temporal validation

### Objective

Evaluate robustness of the final workflow-aware framework across:

- time periods
- staining variability
- analyzer drift
- subgroup distributions

### Inputs

- historical temporal split cohorts
- multimodal data from prior studies

### Outputs

- robustness metrics
- calibration analysis
- failure-mode characterization

### Relationship with previous studies

- extension study only
- should reuse the final framework

### Target publication venue

- `Computers in Biology and Medicine`
- `Artificial Intelligence in Medicine`
- `International Journal of Laboratory Hematology`

### Recommendation

- do only if core studies are already secure

---

## Minimum viable doctoral program

If time, approvals, or linkage quality become limiting, the thesis can still succeed with a **minimum viable 3-study path**:

1. Study 1 as the baseline multimodal triage paper
2. Study 2 as the distinctive scientific paper on discordance
3. Study 4 as the synthesis/framework paper

In that scenario, Study 3 becomes a high-value extension rather than a core dependency.

This fallback matters for a working professional.

---

## Strongest publication sequence

Recommended publication order:

1. Study 1
2. Study 2
3. Study 3
4. Study 4

Why this order works:

- Paper 1 establishes feasibility and early output
- Paper 2 creates conceptual differentiation
- Paper 3 adds originality through temporal modeling
- Paper 4 consolidates the thesis contribution

---

## Core methodological boundaries

To preserve coherence, the program should **not** expand into:

- universal hematology diagnosis
- generic LLM-based interpretation
- fully autonomous agents
- unrestricted outcome prediction disconnected from smear workflow
- large-scale foundation-model pretraining as a thesis dependency

These may become future directions, but they should not define the core doctoral program.

---

## Final recommended thesis statement

The strongest unified doctoral program is:

**a four-study research program on workflow-aware multimodal laboratory decision support for peripheral blood smear analysis, centered on triage, discordance-aware suspicious-case detection, and longitudinal review-trigger prediction using Cellavision morphology, CBC, Sysmex analyzer information, and retrospective laboratory records.**

This program is:

- coherent
- publication-oriented
- methodologically mature
- realistic for a working professional
- clearly beyond morphology-only systems
- clearly beyond simple image+CBC disease prediction
