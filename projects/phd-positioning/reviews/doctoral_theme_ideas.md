# Doctoral Theme Ideas for PPGCC/UFSC

## Strategic Framing

The goal is not to find the trendiest theme. The goal is to find doctoral themes that:

- grow naturally from the master's
- preserve your strongest scientific assets
- fit PPGCC/UFSC advisor availability
- remain realistic for a full-time working researcher
- generate multiple publication opportunities from one coherent program

The key principle is:

**keep morphology as the anchor, and expand toward multimodal, interpretable, and reasoning-aware laboratory intelligence**

## Theme 1. Multimodal Hematology Intelligence for Diagnostic Support

### Short thesis concept

Develop multimodal AI systems that integrate peripheral blood smear morphology with structured laboratory data, such as CBC parameters, analyzer flags, and contextual metadata, to produce more robust and clinically useful hematology decision support.

### Why this theme is strategically excellent

- strongest continuity with your dissertation
- expands scope without breaking identity
- protects your expertise in computer vision
- aligns with current multimodal AI trends
- remains clinically grounded and publication-friendly

### Why it looks natural from your master's

Your master's already established:

- morphology-based AI
- difficult cell classes
- domain shift awareness
- interpretability concerns
- translational motivation

The natural next question is not "which model is better?" but:

`how can morphology be combined with other laboratory evidence to support clinically realistic reasoning?`

### Candidate research questions

- Does combining smear morphology with CBC and analyzer flags improve differential diagnosis performance over image-only systems?
- Which multimodal fusion strategies are most robust in laboratory settings?
- Can multimodal models improve rare/immature cell recognition or uncertainty calibration?
- Which modalities contribute most to clinically meaningful decisions?

### Publication opportunities

- multimodal fusion method paper
- multimodal hematology dataset/resource paper
- explainability or calibration paper
- diagnostic support paper with ablation analysis

### Saturation assessment

Moderate.

General multimodal healthcare AI is becoming crowded, but multimodal laboratory intelligence for hematology is still much less saturated than generic radiology or foundation-model work.

### Current gaps

- weak availability of realistic multimodal laboratory datasets
- insufficient integration of morphology with structured lab signals
- limited focus on clinically difficult immature/atypical cells
- limited evidence on robustness across acquisition settings
- insufficient interpretability at case level rather than cell level

### Future potential

High. This theme can evolve toward:

- case-level decision support
- cross-institution validation
- morphology-aware report assistance
- broader laboratory medicine intelligence

### Saturation risk over time

Manageable if the work remains laboratory-specific and clinically grounded.

### Best advisor match

- Primary: Jônata Tyska Carvalho
- Secondary: Renato Fileto

### Why this theme is feasible

- can build incrementally from existing dataset assets
- supports modular papers
- does not require a huge immediate prospective trial
- compatible with retrospective and semi-structured data

## Theme 2. Trustworthy Hematology AI Under Domain Shift

### Short thesis concept

Develop and evaluate methods for interlaboratory robustness in hematology AI, focusing on domain adaptation, uncertainty estimation, calibration, out-of-distribution detection, and interpretability for peripheral blood smear analysis.

### Why this theme is strategically strong

This is the most direct continuation of the dissertation's actual scientific logic. Your master's already showed that performance changes under staining variability and external datasets. This theme turns that concern into the center of the doctorate.

### Why it looks natural from your master's

The dissertation already contains:

- HistAuGAN
- public external dataset evaluation
- explicit recognition of single-center limitations
- interest in real-world deployment constraints

So this is not a thematic transition. It is a deepening.

### Candidate research questions

- Which domain adaptation strategies best improve interlaboratory robustness?
- How should uncertainty be quantified in rare and morphologically ambiguous hematology classes?
- Can OOD detection identify when a model should defer to human review?
- Which explainability mechanisms are most clinically coherent for smear-based AI?

### Publication opportunities

- domain shift benchmark paper
- uncertainty/calibration paper
- interpretability or failure-mode analysis paper
- multi-center robustness paper

### Saturation assessment

Low to moderate.

There is broad activity in trustworthy medical AI, but hematology-specific robustness remains much less saturated than many other clinical imaging areas.

### Current gaps

- few hematology studies center external robustness as the main problem
- limited systematic work on uncertainty and deferral strategies
- limited integration between explainability and laboratory decision thresholds
- insufficient prospective thinking about deployment safety

### Future potential

Very high for a serious and durable scientific identity. This theme ages better than hype-driven topics.

### Saturation risk over time

Low. Robustness and validation remain essential even when specific model families change.

### Best advisor match

- Primary: Jônata Tyska Carvalho
- Secondary: Douglas Dyllon Jeronimo de Macedo

### Why this theme is feasible

- methodologically focused
- can leverage existing assets and public datasets
- suitable for staged publications
- realistic for someone working full-time

## Theme 3. Knowledge-Grounded Laboratory Reasoning and Selective Agentic AI

### Short thesis concept

Create reasoning systems for laboratory interpretation that combine morphology-derived AI outputs, structured laboratory data, biomedical knowledge structures, retrieval, and selective agentic workflows to support evidence-grounded interpretation.

### Why this theme is attractive

- aligns with your stated interest in agentic AI and health data reasoning
- fits current computational trends
- can become highly distinctive if tied to laboratory medicine
- allows expansion beyond image classification toward biomedical intelligence

### Why this theme is risky

Agentic AI in healthcare is currently expanding very quickly, which means:

- higher hype pressure
- weaker evaluation standards in many papers
- easier thematic drift
- greater risk of looking generic if not grounded in a specific laboratory problem

### Why it can still be strong for you

It becomes strong only when framed like this:

`reasoning over laboratory evidence`

not like this:

`building a healthcare agent`

That distinction matters.

### Candidate research questions

- Can morphology-aware structured outputs improve laboratory interpretation systems?
- Can knowledge graphs or retrieval improve factuality in hemogram reasoning?
- When should an agentic system defer to explicit laboratory rules or human validation?
- Can an evidence-grounded reasoning system reduce hallucinations in lab interpretation tasks?

### Publication opportunities

- knowledge-grounded reasoning architecture paper
- factuality/evaluation framework paper
- laboratory-domain RAG or KG paper
- human-AI workflow support paper

### Saturation assessment

Moderate to high at the generic healthcare level, but still moderate in the laboratory-specific niche.

### Current gaps

- most medical LLM/agentic work is not laboratory-specific
- factual grounding is often weak
- few systems combine morphology, structured lab data, and biomedical reasoning
- evaluation often ignores real workflow constraints

### Future potential

High upside if executed with discipline.

### Saturation risk over time

High if the work becomes generic or purely demo-like. Lower if it stays tied to laboratory intelligence.

### Best advisor match

- Primary: Renato Fileto
- Secondary: Jônata Tyska Carvalho

### Why this theme is feasible

Feasible only if staged after a solid data/morphology foundation. It should not be the first doctoral milestone.

## Themes That Look Tempting but Are Strategically Weak

## 1. Another pure leukocyte classifier benchmark

Weak because:

- too incremental
- easy to saturate
- does not meaningfully expand your identity

## 2. Generic healthcare chatbot or generic medical RAG

Weak because:

- poor continuity with the master's
- high saturation
- often methodologically shallow

## 3. Digital twins as the core thesis from day one

Weak because:

- broad and diffuse
- easy to become conceptual rather than publishable
- not the best immediate continuation of your current evidence base

## 4. Non-health AI topics just because they fit an advisor line

Weak because:

- damages continuity
- makes the transition look opportunistic
- underuses your biomedical differentiator

## Comparative Recommendation Matrix

| Theme | Continuity with Master's | Publication Potential | Advisor Fit | Feasibility | Long-Term Identity Value | Saturation Risk |
|---|---:|---:|---:|---:|---:|---:|
| Multimodal hematology intelligence | 5 | 5 | 5 | 4 | 5 | 3 |
| Trustworthy hematology AI under domain shift | 5 | 4 | 4 | 5 | 5 | 2 |
| Knowledge-grounded laboratory reasoning and selective agentic AI | 4 | 5 | 5 | 3 | 5 | 4 |

## Best Theme by Strategic Objective

### Best overall theme

Multimodal hematology intelligence.

Why:

- best overall balance
- preserves morphology continuity
- opens the door to reasoning and multimodality later
- strong advisor compatibility

### Safest theme

Trustworthy hematology AI under domain shift.

Why:

- strongest direct continuity
- lowest saturation risk
- highly realistic for a full-time researcher

### Highest-upside theme

Knowledge-grounded laboratory reasoning and selective agentic AI.

Why:

- strongest connection to future AI trends
- can be very distinctive if laboratory-specific
- but should be layered on top of the first two themes

## Suggested Thesis Framing Sentences

These framings are strategically stronger than generic AI wording.

### Strong framing 1

`This doctoral project investigates how multimodal artificial intelligence can support hematological interpretation by integrating peripheral blood smear morphology with structured laboratory data in robust and interpretable clinical-laboratory systems.`

### Strong framing 2

`The project advances from cell-level leukocyte classification toward trustworthy laboratory intelligence, emphasizing interlaboratory robustness, interpretability, and clinically grounded multimodal reasoning.`

### Strong framing 3

`The long-term goal is to develop evidence-grounded biomedical intelligence systems for laboratory medicine, using hematology as the initial translational domain.`

## Final Recommendation

If the objective is to maximize coherence, scientific maturity, and long-term positioning, the best order is:

1. Multimodal hematology intelligence
2. Trustworthy hematology AI under domain shift
3. Knowledge-grounded laboratory reasoning with selective agentic AI

This order is important. It keeps your doctorate anchored in the strongest part of your trajectory while still allowing expansion into higher-upside AI directions.
