# Doctoral Positioning Strategy for PPGCC/UFSC

## Executive Positioning

Your trajectory is already more coherent than it may seem at first glance. The master's did not produce only a technical image classification project. It produced a research identity with four strong pillars:

1. A real clinical-laboratory problem with clear diagnostic relevance.
2. Construction and curation of a clinically grounded dataset.
3. Rigorous experimental comparison of modern AI architectures.
4. Explicit concern with robustness, domain shift, interpretability, and real-world feasibility.

This is important because it means your best doctoral transition is not a jump from "leukocyte classification" to an unrelated trendy AI topic. The natural doctoral expansion is from:

`cell-level hematology AI` -> `trustworthy clinical-laboratory intelligence` -> `multimodal and reasoning-aware biomedical systems`

That path preserves continuity, increases publication potential, and makes the transition look scientifically mature rather than opportunistic.

## Material Analyzed

The analysis below was based on the non-empty materials available in `projects/phd-positioning/`, especially:

- `dissertation/dissertation.pdf`
- `publications/pdfs/1519 (2).pdf`
- `publications/pdfs/s11760-026-05309-2 (5).pdf`
- `profile/current_research_identity.md`
- `edital/ppgcc_2026_2.pdf`

## 1. Master's Trajectory Analysis

### What the master's actually demonstrates

Your dissertation and publications show that your master's was not only a model-comparison exercise. It included:

- a clinically meaningful problem in hematology diagnostics
- a systematic review with PRISMA and protocol registration
- construction of a local dataset with specialist-reviewed annotation
- comparison of CNN-style and Transformer-style models
- attention to class imbalance and clinically difficult classes
- domain-specific augmentation for staining variability
- external generalization analysis on public datasets
- discussion of limits for real clinical deployment
- public release of data/code, which strengthens scientific credibility

### Strongest scientific assets

#### 1. Rare combination of domain and technical depth

You are not an AI researcher trying to enter healthcare from the outside. You are a biomedical scientist and laboratory professional who can formulate clinically relevant questions and understand the operational reality of hematology. That is a major differentiator.

#### 2. Dataset-building credibility

The Leukocyte-UNIVALI dataset is a strategic asset. Creating, annotating, validating, documenting, and releasing a clinically grounded dataset is more valuable long-term than having only a single high-performing model paper.

#### 3. Focus on difficult and clinically relevant morphology

Your work is not centered only on easy mature leukocyte classes. It explicitly includes immature and atypical cells, blast-related morphology, artifacts, and interlaboratory staining variation. That gives your trajectory stronger clinical seriousness.

#### 4. Methodological maturity

Your work already shows:

- systematic review competence
- supervised DL experimentation
- model comparison
- statistical testing
- k-fold validation
- external evaluation
- interpretability concerns
- reproducibility/open science

This is a stronger doctoral foundation than many applicants who only have one narrow model paper.

#### 5. Realistic translational instinct

Your dissertation repeatedly returns to robustness, domain shift, workflow integration, and prospective validation. That is exactly the kind of instinct that can mature into a strong doctoral identity.

### Unique differentiators

- Clinical laboratory background, not only generic health informatics.
- Experience with peripheral blood smear morphology, which is specialized and harder to fake than generic "medical AI".
- Ability to connect microscopic image interpretation with diagnostic workflow reality.
- Early evidence of open-science practices through public dataset/code availability.
- A profile that can speak to both laboratory medicine and computational intelligence.

### Methodological strengths

- clinically motivated problem formulation
- dataset design and annotation workflow
- comparative experimental design
- domain-aware augmentation strategy
- external validation logic
- attention to interpretability and real deployment limitations
- good instinct for benchmarking without overstating claims

### Themes with strongest continuity potential

The strongest continuity themes are:

1. Clinical-laboratory AI for hematology.
2. Multimodal biomedical intelligence combining morphology with structured laboratory data.
3. Trustworthy/interpretable AI for laboratory decision support.
4. Domain adaptation, robustness, and interlaboratory generalization in diagnostic AI.
5. Reasoning systems grounded in laboratory data, if introduced gradually and not as a hard topic switch.

### Themes that should probably be abandoned or deprioritized

These are not bad topics in general, but they are strategically weak for your positioning:

#### 1. Pure benchmark-chasing on leukocyte image classification

Another thesis centered only on "testing newer models on the same image task" would look incremental and easy to saturate.

#### 2. Generic LLM/agentic AI without laboratory grounding

If you jump directly to generic medical chatbots, multi-agent LLMs, or RAG systems without keeping the laboratory/hematology anchor, the transition may look artificial.

#### 3. Digital twins as a primary doctoral theme right now

Digital twins remain attractive conceptually, but for your current trajectory they are too broad and can easily become vague. They are better treated as a later long-term evolution, not the core PhD identity.

#### 4. Purely theoretical AI topics with no biomedical continuity

Topics centered mainly on optimization theory, abstract RL, embedded systems, or non-health distributed systems would weaken the narrative of continuity.

## 2. Research Evolution

The progression visible from the master's is:

1. Clinical problem recognition: manual hematology review is subjective, slow, and variable.
2. Literature consolidation: systematic review of leukocyte computer vision.
3. Method development: comparison of YOLOv11 and ViT.
4. Data realism: inclusion of immature cells, artifacts, and staining variability.
5. Robustness awareness: HistAuGAN and cross-dataset evaluation.
6. Translational awareness: discussion of workflow integration and prospective validation.

The next doctoral step should therefore be:

`classification` -> `robust multimodal inference` -> `interpretable decision support in clinical laboratory medicine`

That is a natural scientific expansion.

## 3. Natural Long-Term Research Identity

### The researcher profile you are naturally building

You are not naturally moving toward being a generic computer scientist, nor only a laboratory specialist. The most coherent identity is:

**a researcher in trustworthy clinical-laboratory intelligence, especially computational hematology and multimodal diagnostic support**

### Scientific niche you could realistically own long-term

The niche with the best long-term ownership potential is:

**AI for clinical laboratory reasoning that bridges microscopic morphology, structured laboratory data, and interpretable decision support**

This niche is stronger than simply "medical image AI" because it:

- leverages your laboratory background directly
- remains clinically grounded
- supports both imaging and non-imaging publications
- can expand from hematology to broader laboratory medicine
- is less crowded than generic LLM-in-healthcare work

## 4. Strategic Doctoral Themes

## Theme 1. Multimodal Clinical-Laboratory Intelligence for Hematology

### Core idea

Develop multimodal AI systems that combine peripheral smear morphology with structured laboratory data such as CBC parameters, analyzer flags, metadata, and possibly expert textual interpretation to improve diagnostic support.

### Why this is the strongest path

- strongest continuity with your master's
- clinically meaningful expansion rather than topic replacement
- keeps image expertise while widening the computational scope
- supports method papers, dataset papers, and translational papers
- still aligned with current AI trends without becoming trend-dependent

### Why it fits your profile

This theme preserves your strongest prior asset: morphology. But instead of staying at isolated cell classification, it moves toward clinically realistic inference.

### Publication potential

High. It can generate:

- multimodal method paper
- dataset/infrastructure paper
- domain generalization or calibration paper
- interpretable clinical decision support paper

### Main risk

Requires access to structured laboratory data and careful data governance. Still, this is manageable if scoped around existing institutional or partner workflows.

## Theme 2. Trustworthy AI for Interlaboratory Generalization and Diagnostic Robustness

### Core idea

Study how hematology AI systems fail across institutions and develop strategies for domain adaptation, uncertainty estimation, calibration, explainability, and out-of-distribution detection in clinical-laboratory settings.

### Why this is strategically strong

- almost perfect continuity with the dissertation's limitations section
- scientifically serious and less hype-driven
- highly realistic for a full-time working researcher
- easier to scope than a broad agentic AI thesis

### Publication potential

High to very high, especially if framed as robustness for real-world deployment rather than only model tuning.

### Main risk

The theme is rigorous but less flashy than agentic AI. Its strength is solidity, not trend appeal.

## Theme 3. Evidence-Grounded Laboratory Reasoning Systems Using Knowledge Structures and Agentic AI

### Core idea

Build clinically grounded reasoning systems for laboratory interpretation using combinations of structured lab data, morphology outputs, knowledge graphs, retrieval, and limited agentic workflows.

### Why this should be a secondary, not primary, identity

This is promising, but only if it grows out of laboratory intelligence rather than replacing it. The most credible version is not "an AI agent for healthcare" in general. It is:

`laboratory-grounded reasoning and decision support`

### Publication potential

Potentially very high, but more variable. This path is more vulnerable to hype cycles and saturation if not tied to a concrete laboratory use case.

### Main risk

If this becomes too generic, it can look disconnected from your master's and less defensible in selection and later publication.

## 5. State-of-the-Art Positioning

Recent literature signals confirm that several adjacent areas are growing quickly, but not all are equally strategic for you.

### Multimodal biomedical AI

This is a strong growth area. Recent papers show rapid movement toward multimodal foundation models and multimodal reasoning in healthcare, but clinical deployment remains limited. That means the area is promising, but there is still room for domain-specific, clinically grounded work rather than only large-scale general models.

Examples:

- MetaGP: multimodal EHR + imaging foundation model, Cell Reports Medicine, 2025  
  https://pubmed.ncbi.nlm.nih.gov/40187356/
- Multimodal medical reasoning with proactive agent collaboration, 2025  
  https://pubmed.ncbi.nlm.nih.gov/40852092/

Strategic implication: good area to enter, but through a narrow laboratory niche rather than generic foundation-model competition.

### Interpretable hematologic AI

This looks especially promising for you. Recent work is moving toward interpretable hematologic diagnosis from peripheral blood smears, which validates your instinct that morphology plus interpretability is not exhausted.

Example:

- Interpretable Multiple Instance Learning for Hematologic Diagnosis from Peripheral Blood Smears, 2025  
  https://pubmed.ncbi.nlm.nih.gov/41282106/

Strategic implication: your master's already sits close to this frontier, and you can extend into slide-level or case-level reasoning.

### Agentic AI in healthcare

This area is expanding quickly, but it is at higher risk of oversaturation and weak evaluation. It is attractive for visibility, but dangerous as a primary PhD identity unless grounded in a real laboratory problem.

Example:

- MedARC: adaptive multi-agent refinement for medical reasoning, 2026  
  https://pubmed.ncbi.nlm.nih.gov/41109093/

Strategic implication: use agentic AI as an enabling layer, not as your core identity.

### Knowledge graph plus LLM clinical reasoning

This is growing and remains scientifically useful when tied to factuality, traceability, and structured healthcare data. It becomes weak only when implemented as generic RAG/chatbot work.

Examples:

- Review on knowledge graphs for healthcare, 2025  
  https://pubmed.ncbi.nlm.nih.gov/40712809/
- Structured reflective reasoning for medical KG retrieval-augmented generation, 2025  
  https://pubmed.ncbi.nlm.nih.gov/41250680/

Strategic implication: good fit if centered on laboratory interpretation, not on general-purpose medical assistants.

## 6. Feasibility for a Full-Time Working Researcher

Your doctorate must reward focused, reusable assets. The best kinds of projects for your situation are:

- projects built around one or two reusable datasets
- pipelines that support multiple papers from the same infrastructure
- questions that do not depend on massive prospective data collection from scratch
- studies that combine retrospective data, benchmarking, and domain knowledge
- work that can produce incremental publications without requiring a single huge final experiment

### Best-feasibility profile

The most feasible doctoral profile for you is:

**dataset-centered, multimodal, translational, and publication-modular**

That means:

- avoid a thesis that depends entirely on building a giant new clinical deployment from zero
- avoid overcommitting to massive LLM experimentation without grounded data assets
- prefer a staged program where each year can yield a paper

## 7. Final Recommendations

### Top 3 doctoral themes

#### 1. Multimodal clinical-laboratory intelligence for hematology

Best balance of continuity, originality, advisor fit, and long-term identity.

#### 2. Trustworthy AI for interlaboratory robustness and deployment in hematology

Safest and most defensible continuation of the dissertation.

#### 3. Evidence-grounded laboratory reasoning systems using knowledge structures and selective agentic AI

Highest future-facing upside, but should be anchored to themes 1 or 2.

### Strongest strategic path

Theme 1 with a thesis framed around:

**from leukocyte morphology classification to multimodal, interpretable, and robust hematology decision support**

This is the most coherent path overall.

### Safest path

Theme 2:

**robustness, domain adaptation, uncertainty, and interlaboratory validation for hematology AI**

This has the lowest risk of looking artificial and the best methodological continuity.

### Highest-upside path

Theme 3, but only if anchored to laboratory data:

**knowledge-grounded and agentic laboratory reasoning systems**

High upside, higher saturation risk, and greater dependency on careful problem framing.

### Most publication-efficient path

Theme 1. It can produce multiple paper types from one coherent infrastructure.

## 8. Suggested First Doctoral Paper Ideas

### Paper 1

**Multimodal Hematology Intelligence: Fusing Peripheral Smear Morphology and Structured Laboratory Data for Interpretable Diagnostic Support**

Why first:

- strongest continuity
- broad enough for good impact
- practical enough to build the thesis infrastructure

### Paper 2

**Interlaboratory Robustness in Hematology AI: Domain Shift, Uncertainty, and Calibration in Peripheral Blood Smear Analysis**

Why second:

- directly extends the dissertation limits
- methodologically strong
- defensible for PPGCC selection and later publication

### Paper 3

**Knowledge-Grounded Laboratory Reasoning for Hemogram Interpretation Using Morphology-Aware AI Outputs**

Why third:

- introduces reasoning/agentic layer only after the morphology and data layer is established

## 9. Suggested First-Year Roadmap

### Months 1-3

- define one core doctoral question, not three
- align with the advisor around one reusable data/programmatic asset
- map available data sources beyond images: CBC values, analyzer flags, textual comments, workflow metadata
- design a thesis architecture with modular paper outputs

### Months 4-6

- build or structure the multimodal dataset
- define baseline tasks and clinically meaningful endpoints
- prepare Paper 1 or a strong workshop/journal submission from the dataset plus baseline model

### Months 7-9

- run robustness/domain generalization experiments
- incorporate calibration, uncertainty, or OOD detection
- prepare Paper 2

### Months 10-12

- prototype the reasoning layer only after the multimodal base is stable
- explore knowledge graph, retrieval, or limited agentic workflow tied to laboratory interpretation
- define the second-year thesis consolidation plan

## 10. Final Strategic Conclusion

Your best doctoral positioning is not to leave your master's theme behind. It is to elevate it.

The most strategic identity for PPGCC/UFSC is:

**a researcher in trustworthy multimodal clinical-laboratory AI, with hematology as the anchor domain and interpretable decision support as the translational goal**

This gives you:

- continuity with the master's
- room for scientific expansion
- compatibility with current AI trends
- realistic feasibility for a full-time professional
- a stronger long-term niche than generic medical AI or generic agentic AI

If you preserve morphology as your anchor and expand toward multimodal laboratory reasoning, the transition will look natural, mature, and strategically defensible.
