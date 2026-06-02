# Literature Repositioning Review

## Premise of this review

This review intentionally ignores prior positioning decisions and re-evaluates the doctoral direction from first principles, using only the locally available literature corpus in:

`/Users/joaokasprowicz/Documents/Projects/research-agent/projects/phd-positioning/literature/pdfs`

and the completed master's dissertation:

`/Users/joaokasprowicz/Documents/Projects/research-agent/projects/phd-positioning/dissertation/dissertation.pdf`

The purpose is not to defend the current proposal. The purpose is to determine what the available literature actually supports.

## Corpus actually available

The available paper set is small but strategically informative. It contains:

- 1 review on hematological cytomorphology and digital transition
- 1 scoping review on WBC image classification
- 1 digital morphology system validation paper
- 1 peripheral blood computational morphology paper with disease association
- 1 morphology + CBC diagnostic assistance paper
- 1 smear-review optimization paper using CBC/analyzer-derived features
- 1 rule-based clinical decision support paper for PBS interpretation
- 1 multimodal abstract using smear images + CBC + chemistry for mortality risk

This is not a comprehensive field survey. It is a high-value strategic subset. The conclusions below must therefore be interpreted as **evidence-weighted from the available corpus**, not as a claim that no additional external literature exists.

---

## 1. Structured literature map

## A. Image-based hematology

### What the corpus supports

This is the most mature and saturated part of the field.

- **Asghar et al. (2024)** maps the image-only WBC classification literature.
- **Kasprowicz dissertation (2026)** belongs here.
- **Horiuchi et al. (2026)** begins here with image recognition before adding CBC.

### Real computational task

Mostly:

- cell classification
- morphology detection
- abnormal-cell recognition

Not yet:

- genuine case-level reasoning
- full diagnostic support

## B. Digital morphology

### What the corpus supports

- **Katz et al. (2021)** validates a digital morphology platform against manual microscopy.
- **Zini (2024)** frames digital morphology as part of the ongoing modernization of hematology.

### Real computational task

- digital review support
- semi-automated morphology workflow
- pre-classification for human review

This literature is not mainly about new model design. It is about workflow-level digitalization and operational comparability.

## C. Leukocyte classification

### What the corpus supports

- **Asghar et al. (2024)**
- **Kasprowicz dissertation (2026)**
- **Kasprowicz & Silva (2026)** as summarized by the dissertation and prior outputs

### Real computational task

- isolated-cell classification
- fine-grained leukocyte categorization
- robustness under staining variation

This area is clearly active but scientifically crowded.

## D. Disease classification from morphology

### What the corpus supports

- **de Almeida et al. (2023)** moves from cell characterization to disease-associated cytomorphologies and disease discrimination.
- **Horiuchi et al. (2026)** uses morphology outputs, then combines them with CBC for diagnostic assistance.

### Real computational task

- disease screening
- disease classification
- subtype discrimination

Important nuance: this is already beyond “another classifier,” but still not necessarily a full decision-support system.

## E. Multimodal learning

### What the corpus supports

True multimodal learning is present, but only sparsely.

- **Horiuchi et al. (2026)** is the strongest full paper in the local corpus for morphology + CBC.
- **M3MIL abstract** is the strongest explicit image + laboratory multimodal model, but only as a conference abstract.
- **de Almeida et al. (2023)** incorporates blood counts alongside morphology-derived features, but the center of gravity is still computational cytomorphology.

### Real computational task

- multimodal disease prediction
- multimodal risk prediction

Not yet strongly supported:

- robust multimodal reasoning systems
- broad multimodal hematology platforms

## F. Image + CBC approaches

### What the corpus supports

- **Horiuchi et al. (2026)** directly supports this category.
- **M3MIL abstract** supports it in an emerging way.

### Real computational task

- disease prediction from morphology + CBC
- case-level risk prediction

This is one of the clearest open but plausible spaces in the corpus.

## G. Image + laboratory data approaches

### What the corpus supports

- **Horiuchi et al. (2026)**: image-derived morphology + CBC
- **M3MIL abstract**: smear images + CBC + chemistry
- **PROSER**: not image-learning multimodality, but laboratory-context integration around smear interpretation

### Real computational task

- integrated diagnostic assistance
- structured interpretation support
- case-level risk modeling

The literature supports this as a real direction, but not yet as a mature, saturated field.

## H. Image + clinical data approaches

### What the corpus supports

- **PROSER** uses EHR and lab context, but manual morphology entry, not learned image features.
- **M3MIL** uses hospital mortality outcome with smear + labs.

### Real computational task

- contextualized interpretation support
- risk prediction

There is only weak-to-moderate support here in the local corpus.

## I. Diagnostic support systems

### What the corpus supports

- **PROSER** is the clearest example.
- **Horiuchi et al. (2026)** claims diagnostic assistance, but the actual method is better described as model-based disease assistance from morphology + CBC.

### Real computational task

- report drafting support
- structured interpretation support
- diagnostic assistance

This category is present, but mostly in narrow and operational forms rather than as rich AI reasoning systems.

## J. Foundation models

### What the corpus supports

Almost nothing directly.

- No true foundation-model paper is present in the local PDF corpus.
- Transformers appear in the master's context, but not as biomedical foundation models in this literature set.

### Real implication

The available literature **does not support** a thesis positioned around foundation models.

## K. Medical agents

### What the corpus supports

Nothing meaningful in the local corpus.

- No medical agent paper is present.
- No autonomous multi-step agent system for hematology is demonstrated.

### Real implication

The local evidence **does not support** an agent-centered PhD.

## L. Explainable AI

### What the corpus supports

- **de Almeida et al. (2023)** provides interpretable disease-associated morphotypes.
- **Horiuchi et al. (2026)** uses identifiable morphological characteristics.
- **Katz et al. (2021)** supports pre-classification in a decision-support mode, but not deep explainability.
- **Zini (2024)** explicitly highlights interpretability concerns with black-box AI in morphology.

### Real computational task

- morphology characterization
- interpretable disease association
- operator-facing AI support

Explainability is present, but not yet richly formalized in the local corpus.

## M. Clinical decision support systems

### What the corpus supports

- **PROSER** is the only direct CDS paper in the local corpus.
- **Hayes et al. (2025)** is a workflow triage decision system, though veterinary.

### Real computational task

- support for review decisions
- support for interpretation drafting
- reduction of manual workload

This is a meaningful but still narrow evidence base.

---

## 2. Per-paper extraction

## 2.1 Zini (2024) — *Hematological cytomorphology: Where we are*

- **Objective:** Review the current role of morphology from optical microscopy to digital/AI-assisted hematology.
- **Inputs:** Narrative review of historical and current hematology practice.
- **Outputs:** Conceptual synthesis of where morphology stands in modern hematology.
- **Level of reasoning:** Conceptual/expository, not algorithmic.
- **Clinical task:** Framing the role of morphology in diagnosis and workflow.
- **Model type:** None.
- **Limitations:** Not an experimental AI paper; does not validate a computational method.
- **Future work:** Wider spread of AI-based preclassification, especially beyond simple PB settings.
- **Real problem being solved:** Not solving a prediction problem; it clarifies why morphology remains operationally important.

## 2.2 Asghar et al. (2024) — *Classification of white blood cells... scoping review*

- **Objective:** Review machine learning and deep learning techniques for WBC classification from blood smear images.
- **Inputs:** Prior WBC classification studies.
- **Outputs:** Field-level summary of methods, datasets, performance patterns, and limitations.
- **Level of reasoning:** Literature synthesis.
- **Clinical task:** Automated WBC categorization from images.
- **Model type:** Review of ML/DL, especially CNN-based methods.
- **Limitations:** Review is confined to WBC image classification and does not move into case-level hematology.
- **Future work:** Better datasets, stronger interdisciplinary collaboration, continued DL growth.
- **Real problem being solved:** Isolated-cell image classification mapping.

## 2.3 Katz et al. (2021) — *Evaluation of Scopio Labs X100 Full Field PBS*

- **Objective:** Validate a digital full-field smear system with AI-based morphological analysis against manual microscopy.
- **Inputs:** Digitized peripheral blood smear images.
- **Outputs:** WBC classification, platelet estimation, RBC morphology agreement, reproducibility metrics.
- **Level of reasoning:** Pre-classification / workflow support.
- **Clinical task:** Digital smear review in decision-support mode.
- **Model type:** Proprietary AI-assisted digital morphology platform.
- **Limitations:** Focuses on validation against manual review, not on new disease inference or rich multimodal reasoning.
- **Future work:** Broader digital adoption and improved difficult morphology analysis, especially RBC issues.
- **Real problem being solved:** Digital morphology workflow validation.

## 2.4 de Almeida et al. (2023) — *Computational analysis of peripheral blood smears detects disease-associated cytomorphologies*

- **Objective:** Detect and characterize large-scale cell morphologies in PBS and use them for disease-related inference.
- **Inputs:** Peripheral blood smear images; WBC and RBC detections; blood counts.
- **Outputs:** Morphometric features, computational morphotypes, disease discrimination, genetic subtype prediction.
- **Level of reasoning:** From morphology characterization to disease classification.
- **Clinical task:** Disease detection/classification and subtype association from blood morphology.
- **Model type:** Detection + feature characterization + machine learning over morphometric summaries / morphotypes.
- **Limitations:** Cell detection and feature extraction can be improved; some cell types underrepresented; not a general clinical reasoning system.
- **Future work:** Better cell detection, more learned features, improved RBC handling, deeper models.
- **Real problem being solved:** Disease prediction from morphology, partly enhanced by blood counts.

## 2.5 Horiuchi et al. (2026) — *Application of CNN Image Analysis and Machine Learning to Basic Blood Tests...*

- **Objective:** Build image recognition of peripheral blood cells and combine those outputs with CBC data for diagnostic assistance.
- **Inputs:** Cell images; identified cell types; recognized morphological characteristics; CBC parameters.
- **Outputs:** Image recognition outputs; disease-assistance predictions.
- **Level of reasoning:** Multimodal disease prediction / diagnostic assistance.
- **Clinical task:** Detection and assistance for leukemia, malignant lymphoid conditions, MDS-related morphology, etc.
- **Model type:** CNN-based image recognition plus downstream machine learning using CBC + morphology outputs.
- **Limitations:** Still largely centered on predefined morphology recognition; concern about multi-cell images; broader diagnostic generalization remains limited.
- **Future work:** Better handling of complex images and broader practical deployment.
- **Real problem being solved:** Narrow case-level disease prediction from morphology-derived features plus CBC.

## 2.6 Hayes et al. (2025) — *Development of criteria to optimize manual smear review...*

- **Objective:** Reduce unnecessary manual smear review while preserving acceptable sensitivity.
- **Inputs:** Automated CBC results paired with manual smear review outcomes.
- **Outputs:** Review/no-review recommendations.
- **Level of reasoning:** Triage decision support.
- **Clinical task:** Smear review prioritization.
- **Model type:** Ensemble machine learning combined with expert-derived criteria.
- **Limitations:** Veterinary/nonhuman setting; depends on local infrastructure and criteria design; not directly a morphology-learning system.
- **Future work:** More interpretable models and broader rule design for review decisions.
- **Real problem being solved:** Workflow triage from structured analyzer/CBC data.

## 2.7 Iscoe et al. (2023) — *PROSER*

- **Objective:** Support peripheral blood smear interpretation through structured EHR- and lab-aware report assistance.
- **Inputs:** Demographics, laboratory values, medication data, pathologist-entered morphology findings.
- **Outputs:** Structured display of relevant information and drafted smear interpretation text.
- **Level of reasoning:** Rule-based diagnostic support.
- **Clinical task:** PBS interpretation support and report drafting.
- **Model type:** Web-based CDS using rule-based logic over structured data and user-entered morphology.
- **Limitations:** Quality-improvement deployment rather than formal predictive validation; depends on data warehouse update quality; does not learn morphology from images.
- **Future work:** Evaluate impact on outcomes and training more quantitatively.
- **Real problem being solved:** Clerical and interpretive support for smear reporting.

## 2.8 Webb et al. (M3MIL abstract)

- **Objective:** Predict hospital mortality and identify underlying syndromes using smear images and laboratory values.
- **Inputs:** Digitized peripheral blood smear images, CBCs, blood chemistry panels.
- **Outputs:** Mortality risk and attention-weighted syndrome-associated morphology signals.
- **Level of reasoning:** Multimodal risk prediction.
- **Clinical task:** Acute decompensation / mortality risk prediction.
- **Model type:** Multimodal, multiencoder, multiple-instance learning.
- **Limitations:** Conference abstract only; no full paper-level methodological transparency in the local corpus.
- **Future work:** Not fully visible in the abstract, but clearly broader validation and fuller syndrome modeling would be needed.
- **Real problem being solved:** Multimodal outcome prediction from smear + labs, not direct hematologic diagnosis.

---

## 3. Maturity ladder

### Level 0 — Cell classification

- **Asghar et al. (2024)** as a map of this space
- **Master's dissertation (2026)**
- **Kasprowicz & Silva (2026)** by trajectory summary

### Level 1 — Morphology characterization

- **Katz et al. (2021)** pre-classification and morphology review support
- **de Almeida et al. (2023)** cell/rule-independent morphotype characterization
- **Horiuchi et al. (2026)** 24 morphological characteristics recognition

### Level 2 — Disease prediction from morphology

- **de Almeida et al. (2023)** disease and subtype discrimination from morphology-derived features
- **Horiuchi et al. (2026)** disease-support predictions based on image recognition outputs

### Level 3 — Multimodal disease prediction

- **Horiuchi et al. (2026)** morphology-derived outputs + CBC
- **M3MIL abstract** smear images + CBC + chemistry for mortality risk

### Level 4 — Diagnostic support systems

- **PROSER** rule-based interpretation support
- **Hayes et al. (2025)** review triage support

### Level 5 — Clinical reasoning systems

- **No strong paper in the local corpus**

### Level 6 — Medical agents

- **No paper in the local corpus**

---

## 4. Where the master's dissertation sits on the ladder

## What the dissertation already solves

The dissertation clearly occupies **Level 0**, with partial movement toward **Level 1**.

It already solves:

- isolated-cell leukocyte classification
- fine-grained morphology-aware cell categorization
- comparison of modern architectures
- robustness improvement via domain-aware staining augmentation
- external generalization testing across datasets

It also partially enters Level 1 because it is not only “normal leukocyte counting”; it includes immature and atypical classes and explicitly treats morphology variation as a learning problem.

## What would now be incremental

From the dissertation’s standpoint, the following would now be scientifically incremental:

- another architecture comparison on the same cell-classification task
- another dataset-only expansion with no shift in inference level
- another paper whose core output is still only single-cell class labels

## What would be genuinely novel relative to the dissertation

Relative to the dissertation, novelty would require moving into at least one of:

- case-level aggregation
- disease-level prediction from morphology
- integration of morphology with structured laboratory evidence
- workflow-level decision support
- multimodal robustness beyond image-only pipelines

## What remains scientifically open

The most credible open spaces, given the local corpus, are:

- narrow multimodal disease or case-level prediction using morphology + CBC
- workflow-level support for smear review prioritization using morphology + analyzer/CBC evidence
- robust multimodal systems under real laboratory variability

The corpus does **not** support a claim that the next open frontier is a broad clinical reasoning system or medical agent.

---

## 5. Closest competing works

The closest papers to the candidate’s current direction are:

1. **Horiuchi et al. (2026)**  
   Closest full-paper competitor for morphology-derived features + CBC diagnostic support.

2. **de Almeida et al. (2023)**  
   Strongest paper for moving from morphology characterization to disease-level inference with blood-count-aware modeling.

3. **PROSER (2023)**  
   Closest operational diagnostic support paper, though rule-based and not image-learning multimodal.

4. **M3MIL abstract**  
   Strongest explicit multimodal case-level model in concept, but currently only an abstract.

5. **Hayes et al. (2025)**  
   Useful competitor in workflow triage logic, though veterinary and structured-data-centered.

---

## 6. True state of the art, based on this corpus

The corpus supports the following interpretation:

### Mature

- isolated-cell WBC classification
- digital morphology pre-classification
- narrow disease prediction from morphology-derived features

### Emerging but not yet mature

- morphology + CBC multimodal disease support
- workflow-level smear review decision support with AI/ML
- multimodal risk prediction from smear + lab data

### Weakly supported or unsupported in the local corpus

- clinical reasoning systems over multimodal hematology data
- foundation-model-centered hematology systems
- medical agents for hematology

This matters because it means the literature does **not** justify a broad thesis identity such as:

- “multimodal biomedical reasoning in hematology”
- “agentic laboratory AI”
- “foundation models for clinical-laboratory intelligence”

At least not from the evidence currently available here.

---

## 7. Is the current proposal positioned correctly?

## Short answer

**Partly yes in direction, but too broad in formulation.**

## What the current proposal gets right

- It correctly moves away from another image-only leukocyte classifier.
- It correctly identifies case-level integration as more promising than isolated-cell recognition.
- It correctly treats robustness and interpretability as scientifically serious axes.

## What the current proposal gets wrong or overstates

- It overgeneralizes from a small evidence base into a broad “multimodal clinical-laboratory intelligence” identity.
- It implies a wider state-of-the-art maturity for multimodal hematology than the local corpus really supports.
- It risks sounding closer to a platform vision than to a sharply scoped PhD problem.

## Is it too focused on image classification?

Not in declared intent.  
But it is still **too morphology-centered in its rhetorical skeleton** if the actual aim is broader case-level support. It needs a more explicit task anchor than “integrate modalities.”

## Is it already partially solved in the literature?

Yes, partially.

The broad idea “combine morphology with blood/lab data for diagnostic assistance” is **not new anymore**.

What remains open is not the broad claim itself, but narrower questions such as:

- which case-level tasks most benefit from morphology + CBC integration?
- how should such integration be done robustly under real laboratory variability?
- how can multimodal outputs support review or triage decisions in a way that is operationally useful?

So the literature does **not** support a novelty claim at the level of:

> “No one has yet integrated peripheral smear morphology with laboratory data.”

That claim would be too strong.

---

## 8. Strongest research gap supported by the corpus

The strongest gap that is simultaneously publishable, feasible, aligned with Computer Science, aligned with laboratory medicine, and plausibly supported by available data is:

## **Robust case-level laboratory decision support from peripheral smear morphology plus CBC/analyzer data for narrowly defined hematology tasks**

### Why this is the strongest gap

- It is beyond Level 0 cell classification.
- It is not yet saturated in the local corpus.
- It stays close to available data types: smear images, CBC, analyzer signals.
- It supports clear Computer Science contribution: multimodal fusion, calibration, uncertainty, robustness, task design.
- It is more feasible than a broad reasoning/agent thesis.

### What task types fit best

The literature most strongly supports tasks such as:

- smear-review prioritization
- suspicious-case triage
- disease screening in narrow categories
- morphology-versus-analyzer discordance detection

These are better supported than an open-ended “hematology intelligence platform.”

---

## 9. Recommended PhD positioning

## Recommended positioning

The strongest evidence-based positioning is:

**Robust multimodal decision support for case-level peripheral blood smear interpretation, integrating morphology-derived features with CBC and analyzer data**

This is stronger than the current broader wording because it:

- names a narrower real task family
- better reflects the actual maturity of the literature
- is easier to defend as a Computer Science doctorate
- is more obviously feasible within a PhD

## What should be revised

The current proposal should be **repositioned, not fully replaced**.

### Keep

- hematology as the domain anchor
- morphology as the starting asset
- robustness as a core axis
- multimodality as an expansion beyond the master's

### Revise

- move from broad “clinical-laboratory intelligence” language to narrower case-level decision-support language
- define one or two central tasks explicitly
- avoid implying that medical reasoning systems are the natural next step

### Replace

Any residual framing that suggests:

- general multimodal reasoning in hematology
- foundation-model identity
- agentic laboratory systems

Those directions are not supported by the available corpus.

---

## 10. Recommended research questions

The strongest research questions from this literature are:

1. **Does integrating morphology-derived information from peripheral blood smears with CBC and analyzer flags improve case-level triage or suspicious-case detection compared with unimodal approaches?**

2. **Which multimodal fusion strategies are most robust under real laboratory variability when combining smear morphology with CBC/analyzer data?**

3. **How can multimodal hematology models be calibrated and interpreted so that they support review decisions rather than merely produce black-box predictions?**

These are stronger than broad questions about “clinical reasoning” or “multimodal intelligence” because they are more tightly supported by existing work.

---

## 11. Recommended thesis title candidates

1. **Robust Multimodal Decision Support for Peripheral Blood Smear Interpretation Using Morphology, CBC, and Analyzer Data**

2. **Case-Level Hematology AI: Integrating Peripheral Smear Morphology with CBC and Analyzer Signals for Review Prioritization**

3. **Multimodal Triage and Decision Support in Laboratory Hematology from Peripheral Smear Morphology and Structured Blood Data**

4. **From Leukocyte Classification to Case-Level Hematology Decision Support: Robust Multimodal AI with Smear Morphology and CBC Data**

These are all narrower and more evidence-faithful than titles implying broad laboratory intelligence.

---

## 12. Risks in the current proposal

The current proposal has five main risks:

1. **Overbreadth risk**  
   “Clinical-laboratory multimodal intelligence” can sound broader than the literature actually supports.

2. **Novelty inflation risk**  
   The broad idea of morphology + lab integration is already partially present in the literature.

3. **Task ambiguity risk**  
   Without a central task, the proposal can look conceptually attractive but operationally vague.

4. **Reasoning drift risk**  
   If the text drifts toward reasoning systems or agents, it leaves the evidence-supported zone.

5. **Platform illusion risk**  
   The proposal can sound like a long-term research agenda instead of a sharply scoped PhD.

---

## Final conclusion

The literature in the local corpus does **not** support returning to another image-only classification thesis, but it also does **not** support a broad thesis identity around agentic, reasoning-heavy, or foundation-model-based hematology intelligence.

The strongest evidence-based middle ground is:

**a narrowly scoped, robust, case-level multimodal hematology PhD centered on decision support tasks that integrate peripheral smear morphology with CBC and analyzer data**

That means the current proposal should be **revised and tightened**, not merely refined cosmetically and not replaced by a trend-driven alternative.

The most defensible next step is not:

- another leukocyte classifier
- a generic multimodal platform
- a medical agent thesis

It is:

**task-focused multimodal decision support in peripheral blood hematology, with robustness and interpretability as the main Computer Science contributions.**
