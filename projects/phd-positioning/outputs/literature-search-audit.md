# Literature Search Audit

## Scope of this audit

This audit reconstructs the search landscape using:

- `/Users/joaokasprowicz/Documents/Projects/research-agent/projects/phd-positioning/literature/raw_search_results/embase/records.ris`
- `/Users/joaokasprowicz/Documents/Projects/research-agent/projects/phd-positioning/literature/raw_search_results/pubmed/pubmed.csv`

and compares the search yield against the final local PDF corpus in:

- `/Users/joaokasprowicz/Documents/Projects/research-agent/projects/phd-positioning/literature/pdfs`

The goal is to determine whether the final corpus is representative of the search landscape or whether relevant branches were unintentionally excluded during screening.

## 1. Reconstructed search landscape

## Raw retrieval

- **PubMed records:** `2,733`
- **Embase records:** `1,972`
- **Total raw records retrieved:** `4,705`

## Deduplication

Using exact DOI matching when available and normalized title matching otherwise:

- **Duplicates removed:** `368`
- **Unique records after deduplication:** `4,337`

This reconstructed count is consistent with the earlier strategic mapping and can be treated as the effective screened pool.

## PDF retention

Useful PDFs retained in the final local corpus:

1. `Hematological cytomorphology: Where we are`
2. `Classification of white blood cells (leucocytes) from blood smear imagery using machine and deep learning models: A global scoping review`
3. `Evaluation of Scopio Labs X100 Full Field PBS`
4. `Computational analysis of peripheral blood smears detects disease-associated cytomorphologies`
5. `Application of Convolutional Neural Network Image Analysis and Machine Learning to Basic Blood Tests for Intelligent Diagnostic Assistance`
6. `Development of criteria to optimize manual smear review of automated complete blood counts using a machine learning model`
7. `PROSER: A Web-Based Peripheral Blood Smear Interpretation Support Tool Utilizing Electronic Health Record Data`
8. `Identifying Hospitalized Patients with Acute Decompensation Risk from Peripheral Blood Smears and Laboratory Results using Multimodal, Multiencoder, Multiple Instance Learning (M3MIL)` (conference abstract)

Therefore:

- **Total PDFs retained:** `8`

## Reconstructed screening funnel

There is no complete manual screening log in the local files, so the following counts are **inferred** from the raw search files and the retained PDF corpus:

- **Total records retrieved:** `4,705`
- **Total unique records screened (inferred):** `4,337`
- **Total records excluded (inferred):** `4,329`
- **Total PDFs retained:** `8`

This means the final corpus represents about:

- **0.18% of raw retrieved records**
- **0.18% of deduplicated unique records**

This is an extremely selective final corpus.

---

## 2. What the final PDF corpus actually represents

The retained PDF set is not random. It is highly curated around a narrow conceptual spine:

- image-based hematology background
- digital morphology
- morphology + CBC
- blood smear interpretation support
- one explicit multimodal risk-prediction abstract

In practice, the retained set strongly represents:

- **peripheral blood smear morphology**
- **digital morphology workflow**
- **morphology + CBC integration**
- **smear interpretation support**

It weakly represents:

- **general pathology AI**
- **bone marrow / hematopathology AI**
- **AI for analyzer-driven workflow optimization**
- **broader laboratory medicine AI**

It effectively does not represent:

- **foundation models**
- **medical AI agents**
- **retrieval-augmented systems**
- **large-language-model-based laboratory systems**

---

## 3. Thematic comparison: retained PDFs vs. relevant search-result records absent from the PDF corpus

## A. Papers present in the PDF corpus

### Strongest represented branches

1. **Image-based hematology / leukocyte classification**
   - `Asghar et al. (2024)`

2. **Digital morphology and operational workflow**
   - `Katz et al. (2021)`
   - `Zini (2024)`

3. **Disease-associated morphology**
   - `de Almeida et al. (2023)`

4. **Image + CBC / image + laboratory data**
   - `Horiuchi et al. (2026)`
   - `M3MIL` abstract

5. **Clinical / laboratory decision support**
   - `PROSER`
   - `Hayes et al.`

### Interpretation

The final corpus is reasonably coherent for a **narrowly defined peripheral-blood-smear multimodal hematology niche**.

## B. Relevant papers present in search results but absent from the PDF corpus

Below are branches and representative papers that appear relevant in the search results but were not retained in the final PDF corpus.

### 1. Digital morphology analyzers and workflow support

Potentially relevant absent works:

- `Digital morphology analyzers in hematology: ICSH review and recommendations` — `10.1111/ijlh.13042`
- `Real-World Application of Digital Morphology Analyzers: Practical Issues and Challenges in Clinical Laboratories` — `10.3390/diagnostics15060677`
- `Performance comparison of two automated digital morphology analyzers for leukocyte differential in patients with malignant hematological diseases: Mindray MC-80 and Sysmex DI-60` — `10.1111/ijlh.14227`
- `Exploring artificial intelligence techniques for morphological analysis of digital images of peripheral blood cells: MC-80 versus HemaVision` — `10.1016/j.cca.2024.118809`

### Why this matters

This branch is highly relevant if the doctoral problem is framed as workflow-aware laboratory AI. The final corpus currently underrepresents this branch.

### 2. CBC/analyzer-driven pre-microscopic prediction and triage

Potentially relevant absent works:

- `Early pre-microscopic differentiation of acute promyelocytic leukaemia: The convergence of cell population data and artificial intelligence tools` — `10.1111/bjh.16638`
- `Pre-microscopic prediction of acute promyelocytic leukemia through complete blood cell count (CBC) based derived factor` — `10.1111/bjh.15854`
- `Cell Population Data–Driven Acute Promyelocytic Leukemia Flagging Through Artificial Neural Network Predictive Modeling` — `10.1016/j.tranon.2019.09.009`
- `OPTIMIZING PLATELET COUNT VALIDATION: AN INTEGRATED APPROACH WITH DXH 900 AND SCOPIO X100` — `10.1515/cclm-2025-8054`

### Why this matters

If the target problem includes analyzer flags, pre-review triage, or structured laboratory support, this is a major missing branch. The final corpus includes one veterinary smear-review paper, but it seems to under-sample the human analyzer/CBC workflow literature.

### 3. Disease-level peripheral smear AI beyond simple leukocyte classification

Potentially relevant absent works:

- `A Novel Automated Image Analysis System Using Deep Convolutional Neural Networks to Diagnose MDS` — `10.1182/blood-2019-129524`
- `Advantages of AI-based whole blood film scanning for blast detection in markedly leucopenic blood films` — `10.1007/s00277-025-06473-0`
- `A deep learning model (ALNet) for the diagnosis of acute leukaemia lineage using peripheral blood cell images` — `10.1016/j.cmpb.2021.105999`
- `Distinguishing Reactive Lymphocytes From Blasts Using Fractal Chromatin Patterns` — `10.1111/ijlh.14541`
- `Next-generation morphology, a novel multilayer morphometric digital analysis, reveals both the basic topology and new trends of myelodysplasia of peripheral blood specimens` — `10.1111/bjh.70110`

### Why this matters

The retained corpus has one strong paper in this branch (`de Almeida`) and one hybrid diagnostic-assist paper (`Horiuchi`), but the disease-classification branch still looks thinner than it probably should be.

### 4. Broader decision support for blood film interpretation

Potentially relevant absent works:

- `The Use and Effectiveness of an Online Diagnostic Support System for Blood Film Interpretation: Comparative Observational Study` — `10.2196/20815`
- `THE IMPACT OF COMPUTER-ASSISTED AUTOMATIC ALGORITHMS IN THE DIAGNOSIS OF ANEMIA IN PRIMARY CARE` — `10.1515/cclm-2023-7042`
- `1679 An Optical Character Recognition (OCR) based Complete Blood Count (CBC) Reporting Tool Enables Automated Peripheral Blood Smear Report Generation and improves Turn Around Time (TAT)` — `10.1016/j.labinv.2025.105982`

### Why this matters

`PROSER` is retained and important, but it is not enough alone to represent the full blood-film interpretation support branch.

### 5. Explainable / interpretable morphology AI

Potentially relevant absent works:

- `Leukocyte deep learning classification assessment using Shapley additive explanations algorithm` — `10.1111/ijlh.14031`

### Why this matters

Interpretability is a claimed positioning axis in the doctoral project, but the final corpus contains relatively little explicit XAI literature.

### 6. Multimodal and multimodal-LLM / laboratory-image AI

Potentially relevant absent works:

- `Comparative Evaluation of Five Multimodal Large Language Models for Medical Laboratory Image Recognition: Impact of Prompting Strategies on Diagnostic Accuracy` — `10.3390/diagnostics16091258`

### Why this matters

If the goal is to assess whether LLM or multimodal-LLM branches are truly relevant or overhyped, then excluding all of them makes the final corpus less representative of the *current* broader AI landscape. On the other hand, if the goal is a **strictly non-LLM peripheral smear thesis**, this exclusion may be appropriate.

### 7. Foundation models, medical agents, retrieval-augmented systems

Observed in search results:

- some **foundation-model** records were retrieved
- effectively no meaningful **medical agent** literature was retained
- many generic **retrieval** records appeared, but these were mostly broad spillover rather than true hematology-specific RAG systems

### Why this matters

The final corpus is not representative of these branches at all. Whether that is a problem depends on the intended claim:

- If the claim is “this corpus represents peripheral-smear hematology AI,” the exclusion is mostly acceptable.
- If the claim is “this corpus represents the current state of the art in AI relevant to doctoral positioning,” then these branches are underrepresented or absent.

---

## 4. Quantitative branch impression

The automated thematic scan of the deduplicated set suggests:

- `hematology ai`-like records were abundant (`1373` matched a broad hematology-AI pattern)
- `pathology ai` records were also substantial (`637`)
- `laboratory medicine ai`-like records were nontrivial (`306`)
- `image + laboratory data` records were much smaller (`31`)
- `clinical decision support`-like records were modest (`39`)
- `laboratory decision support`-like records were smaller still (`17`)

The retained PDF corpus over-sampled the narrow image+lab / decision-support niche relative to the whole search set and under-sampled the broader adjacent branches.

This is not necessarily wrong. It depends on the intended goal of the corpus.

---

## 5. Was the final corpus representative?

## Short answer

### Representative of the broad search landscape?

**No.**

The raw search landscape was much broader and included:

- generic pathology AI
- broader laboratory medicine AI
- analyzer and CBC workflow papers
- disease-focused peripheral smear papers
- digital morphology analyzer evaluation and implementation papers
- some foundation-model and multimodal-LLM spillover

The final PDF corpus captures only a small and highly selective subset of those branches.

### Representative of the narrow proposed niche?

**Partly yes.**

It does represent a coherent narrow niche:

- peripheral smear morphology
- digital morphology
- morphology + CBC
- smear interpretation support

But even for that niche, it appears to miss some relevant branches:

1. **human CBC/analyzer pre-microscopic prediction and flagging**
2. **additional blood-film interpretation support systems**
3. **more disease-level peripheral smear AI**
4. **digital morphology analyzer implementation / practical issues literature**

---

## 6. Likely screening effects

The screening appears to have favored papers that were:

- clearly centered on peripheral blood smear morphology
- easy to map onto the emerging doctoral niche
- available and interpretable from title/DOI-level strategic triage

The screening appears to have disfavored papers that were:

- broader workflow or analyzer papers without explicit multimodal language
- digital morphology platform evaluation literature beyond one anchor paper
- blood-film support tools that were not “AI-heavy” enough
- conference abstracts and niche lab-operations papers

Some of these exclusions were probably intentional and defensible. Others look more like **under-sampling of adjacent but strategically useful literature**.

---

## 7. Main conclusion

The final local PDF corpus is **not fully representative of the current search landscape**.

It is best described as:

**a narrow, strategy-driven corpus for peripheral-smear-centered multimodal hematology positioning**

rather than:

**a representative corpus of the state of the art across hematology AI, laboratory medicine AI, digital morphology, and clinical decision support**

## Most important likely omissions

If the goal is to have a more representative state-of-the-art basis for doctoral positioning, the following branches should have stronger representation than they currently do:

1. **digital morphology analyzers and practical workflow literature**
2. **human CBC/analyzer-based review triage and pre-microscopic disease flagging**
3. **additional disease-level smear AI beyond the single strongest examples**
4. **more than one blood-film interpretation support system**

## Less important omissions

The absence of foundation-model, medical-agent, and retrieval-augmented literature is less concerning **if** the intended thesis remains firmly outside those spaces. It becomes concerning only if the project wants to make broader claims about “current AI trends” or to argue that those directions were considered and rejected on evidence grounds.

---

## 8. Final audit verdict

### If the intended use of the corpus is:

**“support a narrowly focused peripheral-smear multimodal hematology thesis”**

Then the corpus is:

- **directionally useful**
- **strategically coherent**
- **but somewhat under-inclusive**

### If the intended use of the corpus is:

**“represent the current state of the art in relevant AI branches for doctoral positioning”**

Then the corpus is:

- **too selective**
- **not fully representative**
- **missing some important adjacent branches**

## Bottom line

Important branches of the literature were likely **underrepresented or excluded** during screening, especially around:

- analyzer/CBC-driven decision support
- digital morphology workflow
- disease-level smear AI
- blood-film interpretation support

The final corpus is therefore best treated as a **curated niche corpus**, not as a comprehensive or fully representative state-of-the-art corpus.
