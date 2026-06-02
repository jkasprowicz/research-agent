# Revised Positioning Report

## Scope of this re-evaluation

This report re-evaluates the doctoral positioning from first principles using the **entire currently available local corpus** in:

- `/Users/joaokasprowicz/Documents/Projects/research-agent/projects/phd-positioning/literature/pdfs`
- `/Users/joaokasprowicz/Documents/Projects/research-agent/projects/phd-positioning/dissertation/dissertation.pdf`

It does **not** try to preserve the current proposal. It asks what the corpus actually supports when the papers are grouped by the real computational problem they solve.

An important caveat remains: the local PDF corpus is still a **curated subset**, not the whole search landscape. The search audit already showed that analyzer/CBC workflow papers and broader laboratory decision-support literature are underrepresented relative to the retrieved record pool. Therefore, the conclusions below should be read as **evidence-weighted from the full current corpus**, not as a final statement about the entire external literature.

---

## 1. Corpus-wide literature map by actual task

## A. Morphology-only systems

Representative papers:

- Asghar et al. (2024)
- Kasprowicz dissertation (2026)
- Katz et al. (2021)
- Katz et al. (2025)
- Kimura et al. (2019)
- de Almeida et al. (2023)

What these papers are actually solving:

- isolated cell classification
- digital blood-film visualization and preclassification
- morphology characterization at cell or smear level
- disease screening from morphology-derived features alone

What they are **not** solving well:

- laboratory workflow decisions
- case-level interpretation with structured laboratory context
- integration of morphology with analyzer flags and CBC data in routine use

Overall maturity:

- very mature for `cell classification`
- moderately mature for `morphology characterization`
- emerging but already populated for `disease prediction from morphology`

## B. Analyzer/CBC-driven systems

Representative papers:

- Haider et al. (2019)
- Hayes et al. (2025)

What these papers are actually solving:

- early flagging of high-risk disease patterns from CBC/analyzer parameters
- reduction or optimization of manual smear review
- rule-based or ML-based laboratory triage

What they are **not** solving well:

- image-aware morphology reasoning
- explicit linking between observed morphology and structured laboratory signals
- broad disease-level interpretation

Overall maturity:

- narrow but practically strong
- more operational than mechanistic
- strongest for `review triage` and `premicroscopic flagging`

## C. Morphology + CBC systems

Representative papers:

- de Almeida et al. (2023)
- Kimura et al. (2021)
- Horiuchi et al. (2026)
- M3MIL abstract

What these papers are actually solving:

- disease screening or disease discrimination using morphology-derived features plus blood counts
- case-level prediction rather than isolated-cell prediction
- multimodal risk or diagnosis assistance in restricted disease settings

What they are **not** solving well:

- robust routine deployment across laboratories
- workflow-aware decision support around smear review
- broad, general-purpose hematology support
- strong prospective validation in real clinical operations

Overall maturity:

- scientifically promising
- less saturated than image-only classification
- still thin in terms of clinically realistic, workflow-anchored implementations

## D. Blood-film decision support systems

Representative papers:

- PROSER
- Kratz et al. (2019)
- Kim et al. (2025)
- Katz et al. (2021)

What these papers are actually solving:

- digital workflow support
- interpretation support
- structured access to context during smear review
- platform-level support for pathologists or laboratory professionals

What they are **not** solving well:

- learned multimodal inference from image + CBC in a single model
- rigorous comparison of modality-specific versus multimodal performance
- robust computational support for case prioritization under real workload constraints

Overall maturity:

- operationally relevant
- computationally underdeveloped compared with image classification
- highly aligned with real laboratory practice

---

## 2. Explicit comparison of the four system families

| System family | Real task solved | What is already solved | Main limitations in current corpus | Strategic implication |
|---|---|---|---|---|
| Morphology-only systems | cell classification, morphology characterization, some disease screening | isolated-cell leukocyte classification is already strong; digital morphology platforms work as decision-support visualization; morphology-derived disease signals can be extracted | weak laboratory context; weak workflow endpoints; limited case-level reasoning; risk of incrementalism | not a strong primary PhD identity by itself |
| Analyzer/CBC-driven systems | premicroscopic flagging, manual review triage | narrow triage tasks are already feasible and clinically useful | morphology is absent; interpretability depends on handcrafted parameters; often task-specific and narrow | strong source of workflow realism, but incomplete as a thesis core |
| Morphology + CBC systems | disease prediction, case-level discrimination, multimodal assistance | multimodal disease-assist models already exist for selected diseases and show high performance | evidence base is still small; external robustness is limited; real deployment logic is underdeveloped | strongest technical bridge beyond the master's |
| Blood-film decision support systems | interpretation support, digital review workflow, report assistance | context-aware support tools and digital review environments already exist | mostly rule-based or platform-centric; little learned multimodal inference; limited rigorous CS contribution if copied directly | strong application frame, but needs a sharper computational kernel |

---

## 3. What is already solved

Across the corpus, the following areas are already substantially solved or at least no longer strategically attractive as a doctoral core:

### 3.1 Isolated-cell leukocyte classification

This is the most mature branch in the corpus. The scoping review by Asghar et al. shows a dense image-classification literature, and the master's dissertation already makes a strong contribution inside this branch with:

- a 14-class leukocyte dataset
- explicit coverage of immature and atypical cells
- comparison of CNN and ViT families
- stain-augmentation strategy for domain robustness

Another thesis centered on “automatic leukocyte classification” would be scientifically weak and too close to the master's.

### 3.2 Digital blood-smear viewing and AI-assisted preclassification

Katz et al. (2021), Kratz et al. (2019), and Kim et al. (2025) collectively show that digital morphology analyzers already support:

- full-field visualization
- AI-based preclassification
- workflow acceleration
- remote review and standardization

This means a doctoral project should not be framed as “digitizing smear review” in general. That is already underway.

### 3.3 Narrow disease classifiers from peripheral smear morphology

Kimura et al. (2019), Kimura et al. (2021), de Almeida et al. (2023), and Horiuchi et al. (2026) show that disease-oriented peripheral-smear AI is not hypothetical. The literature already contains systems for:

- MDS versus aplastic anemia
- Ph-negative MPN differentiation
- disease-associated cytomorphology discovery
- case-level assistance from morphology-derived features and CBC

Therefore, a proposal claiming novelty merely because it predicts disease from smear data would overstate the gap.

### 3.4 Rule-based smear interpretation support

PROSER shows that blood-film interpretation support can be operationalized using EHR and laboratory context plus structured morphology entry. This does not solve multimodal machine inference, but it does mean that “supporting smear interpretation with contextual data” is already partly solved at the workflow level.

---

## 4. What remains unsolved

The strongest unsolved problems in the current corpus are not in raw image classification. They are in the gap between algorithmic morphology and real laboratory decision-making.

### 4.1 Case-level multimodal inference with clear incremental value over single-modality baselines

The literature suggests that multimodal systems can help, but the evidence is still narrow and disease-specific. What remains open is a rigorous demonstration that:

- morphology-derived signals alone are insufficient in important cases
- CBC/analyzer signals alone are insufficient in important cases
- combining both improves case-level performance in a measurable and clinically useful way

This needs to be shown task-by-task, not assumed.

### 4.2 Workflow-aware support rather than abstract prediction

Many papers optimize classification metrics, but few are anchored to a concrete laboratory decision such as:

- which cases require prioritized smear review
- which cases should trigger additional human attention
- which patterns justify a structured interpretive alert
- which cases are discordant between morphology and structured lab context

This is where the corpus still feels open.

### 4.3 Robustness across real-world variability

The dissertation addresses stain variability for leukocyte classification, but the broader multimodal literature still leaves major open questions about:

- different smear quality conditions
- different analyzers
- different class distributions in routine laboratory traffic
- rare or atypical cells
- external generalization of case-level models

This is one of the clearest ways to preserve continuity while moving into a higher-level task.

### 4.4 Interpretable multimodal support that maps to laboratory reasoning

The current literature has pieces of interpretability:

- morphotypes in de Almeida et al.
- explicit morphological characteristics in Horiuchi et al.
- rule-based phrase generation in PROSER

But it does not yet provide a strong framework for interpretable multimodal support where a case-level output can be explained in terms of:

- morphology-derived evidence
- CBC/analyzer evidence
- concordance or discordance between modalities
- suggested laboratory follow-up logic

### 4.5 Realistic retrospective data integration in routine laboratory settings

The literature contains proof-of-concept systems, but much less on how to build a computationally rigorous system from retrospective real laboratory data using:

- peripheral smear images
- CBC parameters
- analyzer flags or research parameters
- structured metadata from routine workflow

That is especially relevant for a working researcher with access to actual laboratory processes.

---

## 5. Where multimodal integration adds measurable value

The corpus does **not** support multimodality as a buzzword by itself. It supports multimodality when the task is one in which morphology and structured laboratory data are complementary.

The clearest cases are:

### 5.1 Disease-level discrimination when morphology alone is ambiguous

de Almeida et al. and Horiuchi et al. show that morphology-derived patterns and blood counts together can improve discrimination for diseases such as MDS and related conditions. The measurable value comes from combining:

- cell appearance or smear-level morphometrics
- abundance patterns
- CBC-derived context

This is stronger than image-only classification because the target is a **case**, not a cell.

### 5.2 Early triage when full microscopy is expensive

Analyzer/CBC-driven studies such as Haider et al. and Hayes et al. show that structured laboratory signals can support early flagging and review prioritization. Multimodal integration becomes valuable when morphology-derived evidence can refine or validate what analyzer-driven triage already suggests.

This is likely one of the most practical value-add settings.

### 5.3 Interpretation support in complex blood-film review

PROSER shows the operational importance of contextual information beyond the CBC. A multimodal learning system would add value only if it can help translate:

- morphology-derived evidence
- CBC/analyzer patterns
- structured laboratory context

into a transparent support output for the reviewer.

This is more promising than generic diagnostic automation because it maps to real workflow.

### 5.4 Robustness checks between modalities

A particularly strong but still underdeveloped use of multimodality is not just “more features,” but **cross-modal consistency**:

- Do smear-derived findings match CBC expectations?
- Do analyzer flags align with visible morphology?
- Are there cases where one modality contradicts the other and should trigger manual attention?

This kind of multimodal discordance logic is highly compatible with laboratory decision support and still weakly explored in the current corpus.

---

## 6. Which contribution type is strongest?

The four candidate contribution types are not equally supported by the literature.

## A. Disease prediction

Strengths:

- already represented by several papers
- publication-friendly
- technically clear

Weaknesses:

- already partially solved in the corpus
- easy to drift into benchmark-style work
- can look like an extension of image-based diagnosis papers already published

Verdict:

- viable, but not the strongest distinguishing identity

## B. Review triage

Strengths:

- operationally important
- clearly relevant to laboratory workflows
- feasible with retrospective data

Weaknesses:

- can become too narrow or too service-oriented
- may underuse the candidate's morphology and vision expertise if based mostly on CBC/analyzer data

Verdict:

- excellent as a **subproblem** or first paper
- probably too narrow as the entire thesis identity

## C. Interpretation support

Strengths:

- clinically realistic
- naturally multimodal
- aligned with PROSER-like workflow logic

Weaknesses:

- easy to become rule-based informatics rather than Computer Science research
- difficult to show strong algorithmic novelty unless the computational core is carefully designed

Verdict:

- strong framing layer, but not sufficient alone

## D. Workflow-aware laboratory decision support

Strengths:

- absorbs the practical strengths of triage and interpretation support
- allows a real multimodal computational core
- aligns with laboratory practice rather than abstract prediction
- keeps morphology central without remaining at cell-classification level
- offers room for robustness, uncertainty, and interpretability contributions

Weaknesses:

- needs strict scope control
- can become vague if not tied to one or two concrete decision tasks

Verdict:

- **best-supported primary contribution type**

### Final answer on contribution type

The strongest contribution supported by the current corpus is:

**d) workflow-aware laboratory decision support**

with:

- **b) review triage** as the most feasible operational entry point
- **c) interpretation support** as the most natural extension

The weakest primary choice is a broad disease-prediction thesis, because that area is already partially occupied and risks looking like a direct escalation of image-based disease classifiers.

---

## 7. Comparison against the master's dissertation

The master's dissertation sits firmly in the `morphology-only / isolated-cell` part of the field.

What the master's already solved well:

- high-quality leukocyte classification
- explicit inclusion of immature and atypical leukocyte classes
- comparison of CNN and ViT architectures
- robustness gains via stain-oriented augmentation
- public dataset and experimental infrastructure

What would now be merely incremental:

- another leukocyte classifier
- another cell-level architecture comparison
- another stain-augmentation paper without task escalation
- another image-only study framed as “hematology AI”

What remains scientifically open beyond the master's:

- moving from isolated-cell recognition to case-level inference
- integrating morphology with CBC/analyzer context
- defining workflow-relevant targets
- quantifying multimodal benefit over image-only baselines
- modeling uncertainty and generalization in routine retrospective data

The correct transition is therefore **not** from leukocyte classification to generic multimodal AI. It is from:

`morphology intelligence at the cell level`

to:

`workflow-aware multimodal support at the case level`

---

## 8. Is the current proposal positioned correctly?

## Short answer

Partly, but it is still too broad in wording and not yet anchored enough to the strongest evidence-backed task.

## Where it is correct

- It is correct to move away from image-only leukocyte classification.
- It is correct to keep morphology as the anchor.
- It is correct to emphasize multimodality, robustness, and real laboratory data.

## Where it is too weak

- “Multimodal clinical-laboratory intelligence” is too broad as a primary identity.
- The proposal risks sounding larger than the evidence base.
- If framed too generally, it may appear to promise universal hematology support without sufficient literature support.

## Is it too focused on image classification?

The current wording tries to avoid that, but the risk remains if the project is still understood as:

- extract features from smear images
- add CBC
- predict disease

That framing is too close to what the corpus already contains.

## Is it already partially solved in the literature?

Yes, partially.

The literature already contains:

- morphology-only disease classifiers
- morphology + CBC diagnostic-assist models
- analyzer-driven flagging systems
- blood-film interpretation support tools

Therefore, the proposal should not claim novelty at the level of “using smear images and CBC together.”

## What would be a stronger positioning?

A stronger positioning is:

**robust and interpretable workflow-aware laboratory decision support for peripheral blood smear review, integrating morphology-derived evidence with CBC/analyzer context at the case level**

This is stronger because it:

- preserves continuity with the master's
- avoids the saturated cell-classification niche
- avoids inflated claims about broad multimodal intelligence
- distinguishes itself from narrow disease classifiers by centering the laboratory decision process
- remains computational, publishable, and feasible

---

## 9. Recommended revised positioning

## Core thesis identity

The most evidence-supported doctoral identity is:

**Computational methods for workflow-aware multimodal decision support in peripheral blood smear analysis**

In domain language:

**from morphology intelligence to case-level laboratory decision support in hematology**

## What the PhD should be about

The thesis should investigate how morphology-derived evidence from peripheral blood smears can be integrated with CBC parameters and analyzer-derived structured signals to support a narrow set of laboratory decisions under real-world conditions.

## What the PhD should not be about

It should not be framed as:

- universal hematology diagnosis
- generic multimodal clinical AI
- agentic hematology systems
- LLM-centered reasoning
- another leukocyte classifier

## Best task focus

The strongest task axis is:

1. **review triage / prioritization**
2. **discordance-aware case support**
3. **structured interpretation support**

Disease prediction may still appear as a sub-study, but it should not be the sole identity of the thesis.

---

## 10. Recommended research questions

The literature currently supports questions such as:

1. **To what extent does combining smear-derived morphology with CBC and analyzer signals improve case-level support over morphology-only or CBC-only baselines?**
2. **Which laboratory decisions benefit most from multimodal integration: review triage, suspicious-case prioritization, or interpretation support?**
3. **How can multimodal hematology models be made robust to real-world variability in smear quality, staining, cell distribution, and laboratory workflow?**
4. **How can case-level outputs be explained in terms that remain meaningful to laboratory professionals, including morphology-derived evidence, CBC context, and cross-modal concordance or discordance?**

---

## 11. Closest competing works

The closest works in the current corpus are:

### Horiuchi et al. (2026)

Closest because it directly combines morphology-derived features with CBC for case-level diagnostic assistance.

Why it matters:

- strongest multimodal disease-assist paper in the current corpus
- shows the thesis cannot claim novelty simply for combining morphology and CBC

### de Almeida et al. (2023)

Closest because it demonstrates computational morphology linked to disease-associated cytomorphologies and shows that adding blood counts can improve predictive performance.

Why it matters:

- raises the bar for morphology-derived disease inference
- supports interpretability through morphotypes

### PROSER (2023)

Closest because it shows real workflow relevance for blood-film interpretation support.

Why it matters:

- proves the operational need for context-aware laboratory support
- also warns that interpretation support can become mostly informatics unless the computational contribution is clear

### Haider et al. (2019) and Hayes et al. (2025)

Closest because they represent the triage side of laboratory decision support using structured analyzer/CBC information.

Why they matter:

- show that review prioritization is a legitimate scientific target
- highlight the practical value of narrowing the task

---

## 12. Risks in the current positioning

The current positioning still carries five major risks:

### 12.1 Overselling multimodality

The corpus supports multimodality for narrow tasks, not for a broad “intelligence” thesis identity.

### 12.2 Understating prior art

The literature already contains morphology + CBC decision-assist papers. Any novelty claim must move to:

- workflow target
- robustness
- real-world validation
- interpretability
- cross-modal support logic

### 12.3 Remaining too close to the master's

If the project still centers on classification or disease prediction from smear images, reviewers can reasonably say it is a scaled-up master's.

### 12.4 Becoming too broad for a working researcher

A thesis spanning disease prediction, interpretation support, workflow deployment, and general multimodal reasoning would likely be too wide.

### 12.5 Losing the Computer Science contribution

If the project drifts too far toward descriptive laboratory workflow or rule-based reporting, the CS contribution may weaken.

---

## 13. Final conclusion

The re-evaluation of the **entire current corpus** changes the emphasis more than the direction.

The literature does support moving beyond morphology-only systems. However, it does **not** most strongly support a broad thesis framed as generic multimodal clinical-laboratory intelligence.

What the corpus most strongly supports is a narrower and more defensible position:

**a PhD on robust, interpretable, workflow-aware laboratory decision support for peripheral blood smear analysis, integrating morphology-derived evidence with CBC and analyzer context at the case level**

This is the best compromise between:

- continuity with the master's
- publishability
- feasibility
- Computer Science relevance
- laboratory realism

If the positioning is revised along this line, the thesis can remain clearly hematology-centered while avoiding both saturation and overreach.
