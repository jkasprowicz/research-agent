# Edital Requirements for the SUS Waiting-List Research Plan

Source used: `/Users/joaokasprowicz/Documents/Projects/research-agent/projects/phd-positioning/edital/ppgcc_2026_2.pdf`

## Strategic Interpretation

The research plan is the first eliminatory stage of the PPGCC/UFSC selection process. For admission purposes, the plan must optimize three dimensions simultaneously:

- **Adherence to the advisor's research theme**
- **Methodological clarity and state-of-the-art grounding**
- **Relevance, originality, feasibility, and Computer Science contribution**

For the SUS waiting-list direction, the safest admission framing is:

**Explainable predictive and simulation-based decision support for dynamic waiting-list management in SUS regulation workflows.**

This should be positioned as a Computer Science project in `Inteligência Computacional`, not as a health-policy essay.

## Required Sections from the Edital

The work plan must contain the following items:

| Requirement | Exact implication for the SUS plan |
|---|---|
| Linha de pesquisa e tema pretendidos | Use `Inteligência Computacional`; theme should explicitly match Jônata Tyska Carvalho's item on application/development of AI methods for health. |
| Orientador indicado | Indicate `Jônata Tyska Carvalho`, matching the form. Only include a second option if strategically confirmed. |
| Título | Use a computational title, not only a public-health title. |
| Introdução | Present waiting lists as dynamic, data-driven, computationally modellable systems. |
| Motivação e problema de pesquisa | Emphasize access, queue dynamics, bottlenecks, prediction, interpretability, decision support, and SUS management. |
| Objetivos | Include one general objective and focused specific objectives. |
| Discussão do estado da arte | Cover healthcare queues, patient flow ML, prioritization, discrete-event simulation, explainable AI, and SUS regulation. |
| Possíveis contribuições científicas para Computação | Must be explicit: event modeling, predictive modeling, simulation, explainability, temporal validation, operational utility. |
| Encaminhamento metodológico alinhado ao tema | Must show data, methods, baselines, validation, explainability, simulation, and feasibility. |
| Referências bibliográficas | References are excluded from the page limit; use focused, high-signal references. |

## Page Limit and Formatting Rules

| Rule | Requirement |
|---|---|
| Page limit | Up to **4 pages for doctorate**, excluding references. |
| Language | Portuguese or English. Portuguese is recommended for this application because the topic is SUS/regulação and the call is in Portuguese. |
| Font | Times New Roman, 12 pt. |
| Spacing | Single spacing. |
| Paper | A4. |
| Columns | Single column. |
| Margins | 2 cm. |
| Identity | The plan **must not contain any information that permits candidate identification**. Violation causes elimination. |

## Evaluation Criteria for the Plan

The plan score is:

`NPlano = (MediaAderenciaTemas + MediaMetodologiaFundamentacao + MediaRelevanciaViabilidade) / 3`

The plan is evaluated by at least two PPGCC/UFSC professors using:

| Criterion | What reviewers evaluate | Optimization for the SUS plan |
|---|---|---|
| Aderência aos Temas de Pesquisa | Alignment with selected line and advisor themes in Anexo I | Explicitly connect to `Inteligência Computacional` and AI methods for health. |
| Metodologia e Fundamentação | Clarity of objectives; adequacy of methodology; quality of state-of-the-art discussion; appropriate references | Avoid generic AI. Specify event logs, temporal validation, baselines, explainability, simulation, and metrics. |
| Relevância e Viabilidade | Scientific contribution; originality; clear problem delimitation; feasibility in course duration; coherence between objectives, methods, and expected contributions; writing quality | Frame as decision-support research, not national deployment. Use a staged plan that can work with minimum event-level data and expand if capacity data are available. |

## Selection Relevance

| Item | Effect |
|---|---|
| First stage | The plan is eliminatory. Candidates below the threshold do not proceed to remaining evaluations unless POSCOMP condition applies. |
| Minimum plan threshold | `NPlano >= 6.00`, or POSCOMP above or equal to the national mean for the year taken. |
| Final doctorate formula | `NF = 0.1*NAPos + 0.3*NPlano + 0.1*NCartas + 0.3*NNCV + 0.2*NArg` |
| Doctoral vacancies | 7 total doctorate vacancies; `Inteligência Computacional` has 2 doctorate vacancies. |
| Arguição | Doctoral candidates have a maximum 20-minute online arguição. The project, methodology, advisor compatibility, candidate background, publications, professional/research experience, availability, and English are evaluated. |

## Advisor Alignment

Relevant Anexo I theme:

**Jônata Tyska Carvalho - Inteligência Computacional**

Available themes include:

- Machine learning, Agentic AI, in-context learning, and post-training LLMs for specific domains.
- Application and development of AI methods for health and other domains.

The SUS plan should emphasize:

- machine learning for health-system operations;
- explainable AI;
- decision support;
- domain-specific AI;
- dynamic queue/event modeling;
- optional simulation/optimization as methodological extension.

Avoid overemphasizing pure operations research if it weakens the match with Jônata. Simulation should support the AI decision-support framing, not replace it.

## Admission-Optimized Framing Decision

Four candidate framings were compared:

| Option | Strength | Admission risk | Decision |
|---|---|---|---|
| A. Explainable prediction of problematic waiting-list behavior | Highly feasible with event-level data; strong ML/XAI fit | May appear too narrow or close to applied prediction | Use as the first methodological core |
| B. Hybrid ML + simulation for waiting-list decision support | Strongest doctoral scope; combines ML, explainability, simulation, and managerial utility | Requires capacity/slot data for full simulation; risk of overreach if promised too strongly | **Select as main admission framing** |
| C. Bottleneck/anomaly detection in regulation workflows | Feasible and useful; good first paper | Can become descriptive if not linked to models and decision support | Use as supporting analysis |
| D. Fairness-aware prioritization and transparency | High social relevance and originality | Politically/ethically sensitive; may look like automated prioritization | Use as evaluation layer, not thesis core |

Selected framing:

**Hybrid explainable ML + simulation for waiting-list decision support**, with an incremental design:

- Stage 1: event-log construction and queue-behavior characterization.
- Stage 2: explainable prediction of problematic queue behavior.
- Stage 3: bottleneck/anomaly detection and service-level explanations.
- Stage 4: simulation of managerial scenarios, if capacity data are available.

## Main Rejection Risks

| Risk | Why it matters | Mitigation |
|---|---|---|
| Candidate identification | The edital states that identifying information in the plan causes elimination. | Do not mention name, master's work, specific employer, publications, advisor meeting, or local privileged access. |
| Weak adherence to advisor theme | The plan must be in a theme offered by the indicated advisor. | Explicitly cite `Inteligência Computacional` and AI methods for health. |
| Health-management framing without CS contribution | Reviewers may see the topic as public health administration rather than Computer Science. | Center event modeling, ML, XAI, temporal validation, simulation, and decision support. |
| Generic waiting-time prediction | Too incremental and common. | Focus on problematic queue behavior, status transitions, operational explanations, and scenario analysis. |
| Overambitious national-scale system | Sounds infeasible for a PhD and dependent on political integration. | Limit to retrospective datasets from partner regulation systems; generalize methods, not deployment. |
| Data access uncertainty | Event-level data are essential. | State expected data clearly and design a staged plan: predictive/event-log studies can proceed before full capacity simulation. |
| Automated prioritization concern | Could raise ethical and political objections. | Frame as managerial decision support, monitoring, explanation, and scenario analysis, not autonomous patient ranking. |
| Weak references | Generic AI citations will not convince reviewers. | Use healthcare queues, patient flow ML, discrete-event simulation, prioritization, explainable decision support, and SUS regulation references. |
| Excessive literature review | Four pages are scarce. | Keep state of the art compact and move operational details to methodology. |
| Poor feasibility for working candidate | The plan may look too large. | Use retrospective data, staged objectives, reusable pipeline, and no prospective deployment requirement. |

