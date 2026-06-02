# LEAC Feasibility Assessment

## Scope of this assessment

This assessment evaluates the doctoral program blueprint against the **actually documented data assets** currently visible in the local LEAC-related workspace, not against idealized future access assumptions.

Primary evidence used:

- `/Users/joaokasprowicz/Documents/Projects/research-agent/projects/phd-positioning/outputs/phd_program_blueprint.md`
- `/Users/joaokasprowicz/Documents/Projects/research-agent/projects/lab-phenotyping/outputs/audit/processed_dataset_comparison.md`
- `/Users/joaokasprowicz/Documents/Projects/research-agent/projects/lab-phenotyping/outputs/audit/data_quality_flags.md`
- `/Users/joaokasprowicz/Documents/Projects/research-agent/projects/lab-phenotyping/outputs/final_exploration/final_exploration_summary.md`
- `/Users/joaokasprowicz/Documents/Projects/research-agent/projects/lab-phenotyping/outputs/robustness/robustness_minimal_summary.md`
- the documented columns in:
  - `base_laboratorial_consolidada.csv`
  - `dataset_laboratorial_expandido.csv`
  - `features_24h_peak_emergency.csv`
  - `clusters_kmeans_robust_final_with_care_setting.csv`

## Critical distinction

At the moment, the workspace **does document a strong retrospective structured laboratory base**, but it does **not yet document** a verified, linkable multimodal research dataset containing:

- Cellavision image identifiers or exported image tables
- manual smear review outcomes
- Sysmex analyzer flags
- Sysmex research parameters
- explicit blood-film review workflow labels

Therefore, the current program must be judged against two layers:

1. **Verified assets now**
2. **Presumed assets that may exist operationally at LEAC but are not yet evidenced in the current workspace**

This distinction is the key to the whole feasibility assessment.

---

## 1. What is actually verified in the current LEAC-adjacent data environment

## Verified structured laboratory base

From the documented outputs in `lab-phenotyping`, the following are currently supported by evidence:

- raw consolidated laboratory base with `9,097,700` rows
- processed laboratory-expanded subset with `1,394,229` rows
- `120,216` total encounters in the processed expanded set
- `81,629` unique patients in the repeated-encounter robustness summary
- `21,295` repeated patients
- `38,587` repeated encounters beyond first
- emergency-focused analytic cohort with `25,785` encounter-level rows
- filtered testing-intensity cohort with `41,084` encounters

## Verified variables

The current structured data visibly include:

- encounter identifier
- hashed patient identifier in the expanded dataset
- timestamp (`data_de_entrada`)
- age
- sex
- unit code / care setting proxies
- CBC-derived values such as:
  - leukocytes
  - platelets
  - Hb / Ht
  - differential fractions in the expanded mapping logic
- selected chemistry/inflammatory variables:
  - creatinine
  - urea
  - LDH
  - PCR
  - sodium
  - potassium
  - glucose
  - TGO/TGP
  - bilirubin
  - alkaline phosphatase
  - CPK
  - TAP

## Not yet verified in the workspace

The following are **assumed in the blueprint** but **not yet evidenced** in the currently inspected data artifacts:

- Cellavision image export linked by encounter
- manual smear review decision labels
- abnormal review outcome labels
- Sysmex analyzer flags
- Sysmex research parameters
- platelet research parameters
- RBC research parameters beyond basic CBC surrogates
- explicit clinical encounter context beyond basic unit/care-setting fields
- hospital outcomes linked to hematology episodes

---

## 2. Global feasibility judgment

## Strongest currently verified asset

The strongest documented asset is the **longitudinal structured laboratory base**.

This supports:

- temporal modeling
- encounter-level aggregation
- patient-level repeated-measure analysis
- retrospective risk stratification from laboratory trajectories

## Weakest currently verified asset

The weakest point is the **absence of a documented linkable multimodal smear-review dataset** containing:

- image linkage
- review labels
- analyzer flags
- research parameters

This directly threatens Studies 1 and 2, and indirectly threatens Study 4.

## Immediate conclusion

As of the currently documented assets:

- **Study 3 is the most feasible**
- **Study 1 is the most important unverified dependency**
- **Study 2 is the most fragile from a data perspective**
- **Study 4 is feasible only if at least Studies 1 and 3 survive**

---

## 3. Study-by-study feasibility

## Study 1. Multimodal case-level triage for peripheral blood smear review

### Blueprint dependence

Requires:

- Cellavision smear images
- CBC
- Sysmex analyzer parameters
- Sysmex research parameters
- analyzer flags
- historical review outcomes

### Required variables

Minimum required:

- `numero_do_atendimento` or equivalent case key
- timestamp for the CBC/smear episode
- core CBC values
- smear image linkage key
- review-performed label or equivalent proxy
- abnormal-review or escalation label

Preferred additional variables:

- analyzer abnormal flags
- research parameters
- platelet-specific and RBC-specific structured outputs

### What is currently verified

Verified:

- encounter-level structured laboratory values
- CBC-like variables
- timestamps

Not verified:

- images
- review labels
- flags
- research parameters

### Expected sample size

#### Verified sample size now

- `0` fully documented multimodal smear-review cases in the current inspected artifacts

#### Practical planning envelope

- upper bound for structured case episodes is `120,216` encounters
- emergency-focused high-density subset is `25,785` encounters

But this upper bound is **not the usable Study 1 sample** unless image and review linkage are confirmed.

### Expected number of positive cases

For the actual Study 1 endpoint, there is **no verified positive-case count yet**, because no documented review label or smear-review event table was found.

### Labeling burden

High.

If historical review labels are not already stored, the study would require one of:

- retrospective workflow reconstruction
- proxy labeling from LIS routing logic
- manual expert re-review subset creation

### Ethics complexity

High.

This study requires the first truly multimodal linkage layer:

- structured lab data
- image data
- workflow labels
- possibly expert adjudication

### Technical risk

Very high.

Main risks:

- image-case linkage may not be recoverable cleanly
- review events may not be encoded in analyzable form
- analyzer flags may exist operationally but not historically extractable
- “multimodal” may collapse to “tabular-only with optional images”

### Feasibility verdict

**Feasible only if a hidden operational dataset exists and can be exported. Not currently supported by the documented workspace alone.**

---

## Study 2. Discordance-aware multimodal modeling for suspicious-case detection

### Blueprint dependence

Requires:

- everything in Study 1
- plus higher-quality labels for suspicious or discordant cases
- ideally expert adjudication

### Required variables

Minimum required:

- all Study 1 variables
- branch-specific morphology outputs
- branch-specific structured-lab outputs
- gold-standard label for suspicious discordance or escalation-worthiness

Preferred:

- explicit expert comments
- follow-up review outcome
- clinical rationale for escalation

### What is currently verified

Verified:

- only the tabular backbone needed for one side of the discordance comparison

Not verified:

- morphology side at case level
- review decision labels
- adjudicated discordance labels

### Expected sample size

#### Verified sample size now

- `0` documented discordance-ready multimodal cases

#### Practical planning envelope

Even if Study 1 becomes viable, the usable Study 2 sample will be smaller because discordance analysis usually requires:

- cleaner linkage
- higher-quality labels
- adjudication subset

Operationally, this likely becomes a subset study rather than a full-cohort study.

### Expected number of positive cases

No verified count is currently possible.

The positive class here is not “abnormal CBC.” It is something more specific:

- suspicious discordance
- escalation-worthy discordance
- uncertainty-worthy discordance

That event definition does not yet exist in the documented datasets.

### Labeling burden

Very high.

This is the most annotation-intensive study in the program because it likely needs:

- case selection
- multimodal comparison logic
- expert adjudication
- quality control on ambiguous cases

### Ethics complexity

High to very high.

Compared with Study 1, it adds:

- secondary expert review
- possibly richer interpretive context

### Technical risk

Very high.

Main risks:

- the target label may be too subjective
- discordance may be scientifically interesting but operationally rare
- insufficient adjudicated sample could reduce the study to a pilot

### Feasibility verdict

**This is the weakest study in the current blueprint from a data-availability standpoint.**

It is the most likely to fail unless LEAC already has:

- accessible image linkage
- accessible review outputs
- accessible analyzer flags
- an expert willing to support targeted adjudication

---

## Study 3. Longitudinal prediction of smear review triggers

### Blueprint dependence

Requires:

- repeated patient-linked laboratory data
- timestamps
- preferably repeated analyzer outputs
- ideally review-trigger events

### Required variables

Minimum required for a viable temporal version:

- `patient_id`
- `numero_do_atendimento`
- timestamp
- repeated CBC / core lab measures

Preferred:

- repeated analyzer flags
- repeated research parameters
- smear-review trigger or escalation outcome

### What is currently verified

Verified:

- patient linkage in the expanded dataset
- timestamps
- repeated encounters
- substantial longitudinal structure

Quantitatively verified:

- `120,216` encounters
- `81,629` unique patients
- `21,295` repeated patients
- `38,587` repeated encounters beyond first

### Expected sample size

#### Verified usable scale

For a longitudinal structured-lab study, the current documented base already supports a serious sample:

- full repeated-encounter pool: up to `120,216` encounters
- repeated-patient pool: `21,295` patients
- repeated-encounter excess volume: `38,587`
- more intensity-enriched filtered cohort: `41,084` encounters

### Expected number of positive cases

This depends on the endpoint.

#### If the endpoint remains exactly as written in the blueprint

`future smear review within a time window`

then the positive-case count is **not yet verifiable**, because no documented smear-review event label was found.

#### If the study is pragmatically reframed to a structured-lab temporal endpoint

such as:

- future repeated urgent evaluation
- future intensified testing
- future abnormal multimarker state

then thousands of positive events are plausible inside the currently documented repeated-encounter structure.

### Labeling burden

Low to moderate if reframed to structured-lab temporal endpoints.

High if it remains dependent on explicit smear-review triggers.

### Ethics complexity

Moderate.

This is the cleanest study ethically because it can be built on retrospective tabular linkage without necessarily requiring images, expert rereview, or hospital outcomes.

### Technical risk

Moderate.

Main risks:

- endpoint definition
- irregular measurement intervals
- missingness
- cohort selection bias toward emergency-rich episodes

But these are manageable methodological risks, not existential data risks.

### Feasibility verdict

**This is the most feasible study in the current program, provided the endpoint is defined using currently documented structured-laboratory events or proxies.**

As originally phrased around smear-review triggers, it is still partially exposed to missing workflow labels.

---

## Study 4. Integrated workflow-aware laboratory decision support framework

### Blueprint dependence

Requires:

- successful Study 1 baseline
- preferably successful Study 2 discordance layer
- preferably successful Study 3 longitudinal layer

### Required variables

This study does not primarily require new raw variables. It requires successful delivery of:

- one valid static multimodal cohort
- one valid temporal cohort
- one comparable decision target space

### What is currently verified

Verified:

- enough longitudinal structured data exists to support the temporal side

Not verified:

- enough multimodal workflow data exists to support the static image-linked side

### Expected sample size

No independent sample size of its own.

It inherits sample viability from prior studies.

### Expected number of positive cases

Inherited from prior studies.

### Labeling burden

Low if earlier studies are completed successfully.

High if this study needs to compensate for weak earlier outputs by creating new labels.

### Ethics complexity

Moderate to high, depending on whether earlier studies already secured multimodal linkage approvals.

### Technical risk

Moderate to high.

The risk is not raw-data scarcity per se. The risk is **program fragility**:

- if Study 1 fails, Study 4 becomes mostly temporal/tabular
- if Study 2 fails, the framework loses part of its conceptual novelty

### Feasibility verdict

**Conditionally feasible.**

This is not the study most likely to fail first, but it is highly dependent on whether the earlier multimodal studies survive.

---

## 4. Weakest point of the program

The weakest point is **not** simply “ethics” and **not** simply “sample size.”

The weakest point is:

**the unverified existence of a clean, encounter-linked multimodal blood-smear workflow dataset joining Cellavision data, structured CBC/Sysmex data, and historical review outcomes.**

Everything else follows from that.

Without this linkage layer:

- Study 1 loses its multimodal character
- Study 2 becomes nearly impossible
- Study 4 loses its intended thesis-level synthesis

By contrast, the longitudinal tabular backbone is already much better supported.

---

## 5. Study most likely to fail because of data availability

## First place: Study 2

Why:

- it depends on all the unverified assets of Study 1
- it additionally requires an adjudicated target that does not currently exist in documented form
- the positive class is narrower and more subjective than in the other studies

## Second place: Study 1

Why:

- it requires image linkage and review labels not yet documented in the current data artifacts
- it may still be possible operationally, but this is not yet evidenced

## Least likely to fail: Study 3

Why:

- the workspace already demonstrates a real longitudinal retrospective lab base
- repeated encounters and repeated patients are documented at useful scale
- it can be rescued with endpoint reframing even if smear-review labels are unavailable

---

## 6. Program-level realism summary

## What the current LEAC-adjacent data clearly supports

- a strong retrospective **tabular longitudinal laboratory study**
- emergency-rich encounter modeling
- repeated-patient temporal analysis
- multimarker laboratory state modeling

## What it may support, but is not yet evidenced

- image-linked smear-review triage
- analyzer-flag-aware multimodal case modeling
- expert-adjudicated discordance analysis

## What should be considered high-risk assumptions

- that historical Cellavision exports are recoverable and linkable
- that review decisions are stored in structured form
- that Sysmex research parameters are historically queryable
- that analyzer flags are archived in a clean research-friendly format

---

## 7. Recommended interpretation of feasibility

### If the blueprint is evaluated strictly against currently verified assets

The program is **too multimodal too early**.

A more realistic interpretation is:

- Study 3 is immediately viable
- Study 1 is a contingent feasibility milestone, not a guaranteed Year 1 paper
- Study 2 should be treated as optional until the multimodal linkage is proven

### If LEAC operationally does have image and workflow exports that are simply not documented here

Then the blueprint may still stand, but only after a fast feasibility sprint confirms:

1. image-case linkage
2. review-label availability
3. flag availability
4. research-parameter extractability

Without those four confirmations, the current blueprint overestimates real-world readiness.

---

## 8. Final verdict

The blueprint is **scientifically strong but operationally asymmetric** against the currently documented LEAC data.

The documented data strongly support the **longitudinal structured-laboratory axis**.

The documented data do **not yet** strongly support the **full multimodal smear-review axis** that Studies 1 and 2 assume.

Therefore:

- the **most feasible study** is Study 3
- the **most likely study to fail because of data availability** is Study 2
- the **critical feasibility milestone for the whole PhD** is proving the existence of a linkable multimodal Cellavision/CBC/Sysmex/review dataset

If that milestone is not met early, the doctoral program should pivot toward a stronger structured-laboratory and longitudinal core.
