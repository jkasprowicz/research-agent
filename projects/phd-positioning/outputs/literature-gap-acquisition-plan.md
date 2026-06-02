# Literature Gap Acquisition Plan

## Purpose

This acquisition plan is based primarily on:

- [literature-search-audit.md](</Users/joaokasprowicz/Documents/Projects/research-agent/projects/phd-positioning/outputs/literature-search-audit.md>)

Its goal is to define the **minimum additional literature set** needed before rewriting the doctoral proposal again.

The guiding principle is not completeness. It is **positioning efficiency**.

The priority is to strengthen the branches that were underrepresented in the current PDF corpus:

1. digital morphology analyzers
2. CBC/analyzer-driven triage systems
3. disease-level peripheral smear AI
4. blood-film interpretation support systems
5. human workflow integration
6. laboratory decision support systems

---

## Tier 1 — Mandatory for PhD positioning

These are the papers most likely to change how the doctorate should be framed.

## 1. Digital morphology analyzers in hematology: ICSH review and recommendations

- **DOI:** `10.1111/ijlh.13042`
- **Why it matters:** This is likely the strongest standards-oriented anchor for digital morphology analyzer use in hematology. It can help separate what is already routine workflow support from what remains a true research contribution.
- **Relation to Horiuchi et al.:** Horiuchi is a model-building and diagnostic-assistance paper. This ICSH review likely clarifies the operational baseline that Horiuchi is extending beyond.
- **Relation to the current PhD proposal:** Essential if the thesis wants to claim clinical realism and laboratory integration. It grounds the project in actual hematology workflow expectations rather than in model-centric framing alone.
- **Expected impact on project positioning:** High. It will likely force a cleaner distinction between:
  - digital morphology workflow support already available
  - new multimodal inference contributions still scientifically open

## 2. Real-World Application of Digital Morphology Analyzers: Practical Issues and Challenges in Clinical Laboratories

- **DOI:** `10.3390/diagnostics15060677`
- **Why it matters:** Likely one of the best practical papers for understanding deployment frictions, workflow constraints, and what laboratories actually struggle with after adopting digital morphology tools.
- **Relation to Horiuchi et al.:** Horiuchi shows a diagnostic-assist direction; this paper likely shows whether that direction is aligned with actual operational bottlenecks.
- **Relation to the current PhD proposal:** Very important for deciding whether the thesis should be framed more as disease prediction, review prioritization, or workflow-aware support.
- **Expected impact on project positioning:** High. It may shift the proposal from broad “multimodal intelligence” wording toward narrower workflow-aware decision support.

## 3. Early pre-microscopic differentiation of acute promyelocytic leukaemia: The convergence of cell population data and artificial intelligence tools

- **DOI:** `10.1111/bjh.16638`
- **Why it matters:** This is a strong example of analyzer/CBC-driven pre-microscopic prediction in a clinically urgent hematology setting.
- **Relation to Horiuchi et al.:** Horiuchi integrates morphology-derived image outputs with CBC. This paper may show the complementary or competing logic of structured-data-first triage before microscopic review.
- **Relation to the current PhD proposal:** Crucial if the thesis is going to use analyzer flags and CBC as more than passive covariates.
- **Expected impact on project positioning:** High. It may push the proposal toward:
  - review prioritization
  - suspicious-case flagging
  - morphology-plus-analyzer discordance tasks
  instead of broader generic multimodal diagnosis.

## 4. Cell Population Data–Driven Acute Promyelocytic Leukemia Flagging Through Artificial Neural Network Predictive Modeling

- **DOI:** `10.1016/j.tranon.2019.09.009`
- **Why it matters:** Another important example of analyzer-driven hematology prediction using structured instrument outputs.
- **Relation to Horiuchi et al.:** Horiuchi is image-plus-CBC; this paper likely shows what can already be done without image learning, which is exactly the comparison the PhD needs.
- **Relation to the current PhD proposal:** Important for testing whether image data truly add value beyond analyzer/CBC-derived models.
- **Expected impact on project positioning:** High. It can sharpen the central thesis question into:
  - when does morphology improve structured-data prediction?

## 5. The Use and Effectiveness of an Online Diagnostic Support System for Blood Film Interpretation: Comparative Observational Study

- **DOI:** `10.2196/20815`
- **Why it matters:** This is one of the clearest missing comparators to PROSER in the blood-film interpretation support branch.
- **Relation to Horiuchi et al.:** Horiuchi focuses more on predictive assistance from learned features; this paper likely focuses more on interpretive support and human workflow.
- **Relation to the current PhD proposal:** Essential if the thesis wants to claim novelty in decision support rather than only in multimodal prediction.
- **Expected impact on project positioning:** High. It may show that “support system” language needs to be used more carefully and narrowly.

## 6. A Novel Automated Image Analysis System Using Deep Convolutional Neural Networks to Diagnose MDS

- **DOI:** `10.1182/blood-2019-129524`
- **Why it matters:** Strong candidate for disease-level peripheral smear AI that goes beyond cell classification.
- **Relation to Horiuchi et al.:** Horiuchi is broader in disease-assist scope and explicitly multimodal; this paper likely clarifies how far morphology-only disease diagnosis has already gone.
- **Relation to the current PhD proposal:** Important for deciding whether disease prediction from morphology alone is already too mature to be a central novelty claim.
- **Expected impact on project positioning:** High. It may force the proposal to emphasize multimodal value and robustness more strongly.

## 7. Next-generation morphology, a novel multilayer morphometric digital analysis, reveals both the basic topology and new trends of myelodysplasia of peripheral blood specimens

- **DOI:** `10.1111/bjh.70110`
- **Why it matters:** Likely a strong morphology-characterization / disease-association paper closer to the de Almeida branch than to simple leukocyte classification.
- **Relation to Horiuchi et al.:** Horiuchi uses explicit morphology recognition plus CBC; this paper likely deepens the disease-level morphology-analysis branch.
- **Relation to the current PhD proposal:** Important for evaluating whether the right niche is disease-level morphometry, multimodal support, or workflow decision support.
- **Expected impact on project positioning:** High. It can help determine whether the proposed thesis should stay disease-oriented or move more clearly toward laboratory decision support.

---

## Tier 2 — Important supporting literature

These papers are less likely to overturn the positioning, but they can materially strengthen the proposal.

## 8. Performance comparison of two automated digital morphology analyzers for leukocyte differential in patients with malignant hematological diseases: Mindray MC-80 and Sysmex DI-60

- **DOI:** `10.1111/ijlh.14227`
- **Why it matters:** Useful for understanding the comparative operational landscape of digital morphology analyzers in difficult hematology contexts.
- **Relation to Horiuchi et al.:** Horiuchi is closer to algorithmic diagnostic assistance; this paper likely clarifies where platform-level analyzer performance ends and model-level contribution begins.
- **Relation to the current PhD proposal:** Helps avoid overstating novelty in digital morphology workflow.
- **Expected impact on project positioning:** Moderate to high.

## 9. Exploring artificial intelligence techniques for morphological analysis of digital images of peripheral blood cells: MC-80 versus HemaVision

- **DOI:** `10.1016/j.cca.2024.118809`
- **Why it matters:** Another practical digital morphology comparator with direct workflow relevance.
- **Relation to Horiuchi et al.:** Likely useful for distinguishing image analysis platform evaluation from real multimodal diagnostic modeling.
- **Relation to the current PhD proposal:** Supports more realistic framing around what new computational value the thesis adds beyond analyzer platforms.
- **Expected impact on project positioning:** Moderate.

## 10. Advantages of AI-based whole blood film scanning for blast detection in markedly leucopenic blood films

- **DOI:** `10.1007/s00277-025-06473-0`
- **Why it matters:** Strong example of disease-relevant peripheral blood AI focused on a narrow but clinically urgent task.
- **Relation to Horiuchi et al.:** Horiuchi is broader and multimodal; this paper may show how competitive narrow morphology-only disease screening can be.
- **Relation to the current PhD proposal:** Helpful if the proposal wants to define a narrower central task rather than an overly broad platform claim.
- **Expected impact on project positioning:** Moderate to high.

## 11. A deep learning model (ALNet) for the diagnosis of acute leukaemia lineage using peripheral blood cell images

- **DOI:** `10.1016/j.cmpb.2021.105999`
- **Why it matters:** Important disease-level morphology-only comparator.
- **Relation to Horiuchi et al.:** Helps isolate what multimodal integration adds over image-only disease diagnosis.
- **Relation to the current PhD proposal:** Supports more rigorous baseline design.
- **Expected impact on project positioning:** Moderate.

## 12. Artificial intelligence of digital morphology analyzers improves the efficiency of manual leukocyte differentiation of peripheral blood

- **DOI:** `10.1186/s12911-023-02153-z`
- **Why it matters:** Strong human-workflow integration paper.
- **Relation to Horiuchi et al.:** Less about disease classification, more about operational efficiency and human review.
- **Relation to the current PhD proposal:** Important if the proposal leans toward review prioritization or workflow support.
- **Expected impact on project positioning:** Moderate.

## 13. OPTIMIZING PLATELET COUNT VALIDATION: AN INTEGRATED APPROACH WITH DXH 900 AND SCOPIO X100

- **DOI:** `10.1515/cclm-2025-8054`
- **Why it matters:** Likely useful as a model of structured integration between analyzer outputs and digital morphology tools.
- **Relation to Horiuchi et al.:** Horiuchi combines model-derived morphology outputs with CBC; this paper may show a more operational integration route.
- **Relation to the current PhD proposal:** Helps if the thesis wants to justify analyzer-plus-morphology integration as a real laboratory need.
- **Expected impact on project positioning:** Moderate.

## 14. Deep Learning-Driven 24-Hour Mortality Risk Assessment through Peripheral Blood Smear Morphology in Hospitalized Cancer Patients

- **DOI:** `10.1182/blood-2024-208716`
- **Why it matters:** Adjacent to M3MIL as a risk-prediction branch.
- **Relation to Horiuchi et al.:** Horiuchi is diagnostic-assist in hematologic disease; this is outcome-risk prediction from smear morphology.
- **Relation to the current PhD proposal:** Useful mainly to decide whether risk-prediction positioning should be excluded or retained as a secondary line.
- **Expected impact on project positioning:** Moderate.

---

## Tier 3 — Optional background reading

These papers are useful for context but are not necessary before rewriting the proposal.

## 15. Artificial Intelligence RBC Recognition Program for Schistocyte Screening in Cytopenic Patients

- **DOI:** `10.1182/blood-2023-174225`
- **Why it matters:** Narrow morphology-screening application for RBC abnormalities.
- **Relation to Horiuchi et al.:** More task-specific and likely image-centric.
- **Relation to the current PhD proposal:** Helpful if RBC morphology becomes part of future scope, but not essential now.
- **Expected impact on project positioning:** Low to moderate.

## 16. Leukocyte deep learning classification assessment using Shapley additive explanations algorithm

- **DOI:** `10.1111/ijlh.14031`
- **Why it matters:** Explicit interpretability paper in leukocyte classification.
- **Relation to Horiuchi et al.:** Provides explainability contrast to broader disease-assistance modeling.
- **Relation to the current PhD proposal:** Helpful for interpretability framing, but not central enough to block proposal rewriting.
- **Expected impact on project positioning:** Low to moderate.

## 17. Comparative Evaluation of Five Multimodal Large Language Models for Medical Laboratory Image Recognition: Impact of Prompting Strategies on Diagnostic Accuracy

- **DOI:** `10.3390/diagnostics16091258`
- **Why it matters:** Useful only to understand the current LLM branch and avoid overstating or understating its relevance.
- **Relation to Horiuchi et al.:** Horiuchi is classical multimodal diagnostic assistance; this paper belongs to a newer multimodal-LLM branch.
- **Relation to the current PhD proposal:** Mainly useful if you want evidence-based reasons to keep LLMs outside the thesis core.
- **Expected impact on project positioning:** Low.

## 18. Hilab System Device in an Oncological Hospital: A New Clinical Approach for Point of Care CBC Test, Supported by the Internet of Things and Machine Learning

- **DOI:** `10.3390/diagnostics13101695`
- **Why it matters:** Broader laboratory AI context.
- **Relation to Horiuchi et al.:** More device/system oriented than morphology + CBC disease assistance.
- **Relation to the current PhD proposal:** Useful context, not core.
- **Expected impact on project positioning:** Low.

---

## Minimum acquisition set before rewriting the proposal

If only the smallest defensible expansion of the corpus is possible, acquire these **7 papers first**:

1. `10.1111/ijlh.13042` — ICSH review on digital morphology analyzers
2. `10.3390/diagnostics15060677` — real-world digital morphology analyzer challenges
3. `10.1111/bjh.16638` — pre-microscopic APL differentiation from analyzer/CBC data
4. `10.1016/j.tranon.2019.09.009` — cell population data–driven APL flagging
5. `10.2196/20815` — online blood-film diagnostic support system
6. `10.1182/blood-2019-129524` — CNN-based MDS diagnosis
7. `10.1111/bjh.70110` — next-generation morphology / myelodysplasia peripheral blood analysis

This is the smallest additional set likely to answer the most important unresolved positioning questions:

- Is the real gap multimodal diagnosis, review triage, or decision support?
- How much is already solved by analyzer/CBC systems without image learning?
- How much is already solved by morphology-only disease models?
- Is the strongest thesis identity disease prediction or workflow-aware laboratory support?

---

## Recommended acquisition sequence

### Phase 1 — Positioning-critical

Acquire and read:

1. `10.1111/ijlh.13042`
2. `10.3390/diagnostics15060677`
3. `10.1111/bjh.16638`
4. `10.1016/j.tranon.2019.09.009`

### Phase 2 — Disease-level comparator branch

Acquire and read:

5. `10.1182/blood-2019-129524`
6. `10.1111/bjh.70110`
7. `10.1007/s00277-025-06473-0`

### Phase 3 — Decision-support comparator branch

Acquire and read:

8. `10.2196/20815`
9. `10.1186/s12911-023-02153-z`
10. `10.1515/cclm-2025-8054`

---

## Final recommendation

Before rewriting the doctoral proposal again, the literature base should be expanded just enough to cover:

- **digital morphology workflow**
- **analyzer/CBC triage**
- **disease-level peripheral smear AI**
- **blood-film interpretation support**

That does **not** require a broad new review. It requires a **targeted acquisition of 7 to 10 papers**.

The current corpus is strong enough to reject a return to simple leukocyte classification, but not yet broad enough to determine with confidence whether the best final positioning is:

- multimodal disease prediction
- laboratory triage support
- blood-film interpretation support
- or a narrower hybrid of these

This acquisition plan is the minimum step needed to resolve that uncertainty.
