# Gap Validation Audit: SUS Waiting-List Doctoral Proposal

Audited proposal: `outputs/plano_doutorado_v1.md`  
Blueprint audited: `outputs/final_plan_blueprint.md`  
Evidence base audited: all review files in `literature/reviews/` and the 33 structured article notes generated from `literature/pdfs/tier1/` and `literature/pdfs/tier2/`.

## Executive Verdict

The proposed gap is scientifically defensible, but only under a precise framing.

The literature does **not** support a PhD novelty claim such as "using AI to predict waiting time" or "optimizing SUS queues with machine learning". Those components are already partially solved in adjacent healthcare operations literature and, in narrower forms, in Brazilian waiting-list contexts.

The literature **does** support a stronger, PhD-level gap:

> There is no clear evidence in the audited corpus of a reproducible, event-based, explainable and workflow-aware computational framework for modeling problematic waiting-list behavior in SUS regulation systems, validated temporally and designed as human-in-the-loop decision support for managers/regulators.

This is a composite gap. Its novelty is not one algorithm. Its novelty must be defended as the integration of: event-level representation, operational outcome taxonomy, temporal prediction, explainability for managerial action, validation against administrative baselines, and bounded decision-support evaluation in SUS regulation workflows.

## Direct Answers to the Validation Questions

| Question | Answer |
|---|---|
| Is the gap real? | Yes, as an integrated workflow-aware computational gap. The corpus contains strong SUS operational studies and strong computational methods, but little direct integration of SUS regulation event data, XAI, temporal validation and decision support. |
| Is the gap already solved? | No, not end-to-end in the audited corpus. However, several components are solved separately: queue management, telehealth referral management, waiting-time prediction, XAI for outpatient waits, queueing/simulation, regulation architecture and procedure-specific ML prioritization. |
| Is the gap only partially solved? | Yes. It is partially solved by Shin et al. for interpretable outpatient wait prediction, Gagliotti and Gutierrez for Brazilian cardiac-surgery ML prioritization, Cardoso et al. for SUS regulation architecture, Pazin-Filho et al. for queue management, and Thompson/Wartelle/Wang for queueing/simulation/DSS methods. |
| Is the gap merely an application of known methods? | It could become merely an application if framed as "apply ML/SHAP to waiting-list data". It becomes PhD-level if the contribution includes a defensible event schema, outcome taxonomy, temporal validation protocol, manager-oriented explanation layer and operational evaluation framework. |
| Is the contribution sufficiently novel for a PhD? | Yes, conditionally. The novelty is sufficient for a Computer Science PhD if the thesis contributes a generalizable computational framework and evaluation methodology, not only a local predictive model. |

## Central Claim Audit

| Central claim in the proposal | Supporting papers | Contradictory or limiting papers | Confidence | Risk |
|---|---|---|---|---|
| SUS waiting lists are dynamic operational systems, not merely administrative lists. | Giannotti et al. 2025; Pazin-Filho et al. 2024; Salles et al. 2026; Lisboa et al. 2022; Cardoso et al. 2026. | None directly contradict. The risk is that some papers are conceptual/descriptive rather than computational. | High | Low |
| Waiting-list management is practically relevant for SUS access, equity and resource planning. | Gadenz et al. 2021; Pazin-Filho et al. 2024; Antunes et al. 2025; Giannotti et al. 2025; Salles et al. 2026; Pfeil et al. 2025. | None directly contradict. The evidence is stronger for practical relevance than for causal generalization. | High | Low |
| Centralization, telehealth referral management and list updating can reduce waiting lists or waiting times. | Gadenz et al. 2021; Pachito et al. 2022; Pfeil et al. 2025; Pazin-Filho et al. 2024; Antunes et al. 2025; Salles et al. 2026. | These papers partially weaken novelty if the proposal claims to solve waiting lists through management alone. They also show that non-AI interventions may be sufficient in some settings. | High | Medium |
| Existing SUS studies rarely provide predictive, explainable, temporally validated decision support. | Pazin-Filho et al. 2024 has no ML/XAI; Gadenz et al. 2021 has no predictive model; Pachito et al. 2022 is costing; Salles et al. 2026 is descriptive; Antunes et al. 2025 is pre-post; Cardoso et al. 2026 is architecture. | Gagliotti and Gutierrez 2025 partially contradict by using ML for Brazilian cardiac-surgery waiting-list prioritization. Cardoso et al. 2026 partially contradict by providing regulation architecture and queue management. | High | Medium |
| ML for waiting-time prediction exists, but mostly outside SUS regulation and often without workflow-level decision evaluation. | Gloyn et al. 2026; Shin et al. 2024; Fall et al. 2025; Mandizvida et al. 2024. | Shin et al. 2024 is a strong interpretable wait-prediction paper. Mandizvida et al. 2024 applies predictive modeling in public hospitals. These narrow the novelty of pure prediction. | High | Medium |
| Interpretable waiting-time prediction is not novel by itself. | Shin et al. 2024 uses interpretable ML/SHAP for outpatient waiting-time prediction; Gloyn et al. 2026 maps AI wait-time prediction literature. | This contradicts any claim that XAI for waiting time is new. It supports only a domain/workflow-specific XAI gap. | High | High |
| Queueing, simulation and optimization are mature methods in healthcare operations. | Wartelle et al. 2026; Thompson et al. 2024; Wang et al. 2024; Lim et al. 2023; Wood et al. 2022; Lee et al. 2022; Kruik-Kolloffel et al. 2024; Alvarez-Vazquez et al. 2025. | These papers contradict novelty claims around generic queueing, DES, simulation or resource allocation. | High | High |
| Queueing/simulation methods are not yet strongly adapted to SUS regulation-event workflows in the audited corpus. | Wartelle et al. 2026 is ED-specific; Thompson et al. 2024 is radiology triage; Wang et al. 2024 is HIV laboratory allocation; Lee et al. 2022 is outpatient physician customization; Kruik-Kolloffel et al. 2024 is medication reconciliation. | Pazin-Filho et al. 2024 uses empirical queue-management principles in a Brazilian hospital; Cardoso et al. 2026 has queue-management architecture. These reduce but do not eliminate the gap. | Medium-High | Medium |
| A Brazilian ML waiting-list prioritization precedent exists, but it is narrow. | Gagliotti and Gutierrez 2025 directly applies ML to cardiac surgery waiting-list prioritization using clinical/demographic variables. | This is the strongest competitor. It weakens any broad "no AI in Brazilian waiting lists" claim. It can be rebutted because it is procedure-specific, not regulation-system-wide, and lacks demonstrated workflow/XAI/simulation impact in the notes. | High | High |
| SUS regulation architecture exists, but predictive/XAI decision-support layers are not shown as mature. | Cardoso et al. 2026 emphasizes multi-region regulation architecture, interoperability, transparency, real-time monitoring, queue management and auditability. | Cardoso et al. 2026 strongly competes with any claim of absent digital regulation infrastructure. The PhD must position itself as an analytic/predictive layer, not architecture. | High | Medium-High |
| Data quality and stale demand are real operational problems in waiting lists. | Salles et al. 2026 removed 147/393 records and found complaint discrepancies; Pfeil et al. 2025 notes limited documentation of removal reasons; Giannotti et al. 2025 discusses governance and conceptual ambiguity. | Evidence is descriptive and local; automated stale-demand detection is not proven by these papers. | Medium-High | Medium |
| Event-based modeling is a justified computational representation for regulation workflows. | Pazin-Filho et al. 2024 uses inflows/outflows/reasons; Shin et al. 2024 uses hospital event logs; Wartelle et al. 2026 models patient-flow states; Cardoso et al. 2026 concerns regulation events and interoperability. | No paper in the corpus proves that the proposed event schema will generalize across SUS systems. This remains a contribution but also a feasibility risk. | Medium | Medium |
| Human-in-the-loop decision support is necessary and safer than autonomous prioritization. | Hroub et al. 2025 identifies implementation gaps; Lisboa et al. 2022 shows human regulatory workflow; Giannotti et al. 2025 frames equity/governance; Cardoso et al. 2026 emphasizes transparency/auditability. | Hroub et al. 2025 reports many studies promoting automated systems, which means the field has competing automation-oriented framings. | High | Low |
| The proposal belongs to Computer Science, not only health management. | Computational pillars: event modeling, ML/XAI, temporal validation, queueing/simulation, calibration, explainability, DSS evaluation. Support from Shin et al. 2024; Thompson et al. 2024; Wartelle et al. 2026; Wang et al. 2024; Cardoso et al. 2026. | If implemented only as descriptive statistics over SUS queues, this claim fails. The plan must protect its CS center of gravity. | Medium-High | Medium |
| A minimum dataset can support a viable first phase. | Pazin-Filho et al. 2024 demonstrates value from inflow/outflow/reason/waiting-time data; Salles et al. 2026 uses status/update data; Shin et al. 2024 uses event logs for prediction. | More ambitious objectives need capacity, priority, exit reasons and scheduling data. Data availability is the largest feasibility uncertainty. | Medium | High |

## A. What Is Already Solved?

| Already solved area | Evidence | Implication for the proposal |
|---|---|---|
| Waiting lists are a major SUS access problem. | Giannotti et al. 2025; Pazin-Filho et al. 2024; Antunes et al. 2025; Salles et al. 2026; Lemos et al. 2025. | Do not claim novelty in identifying the problem. Use this only for motivation. |
| Centralized queue/list management can reduce backlog and waiting time. | Pazin-Filho et al. 2024; Antunes et al. 2025. | The proposal must not sound like a plan to merely centralize or monitor lists. |
| Telehealth/referral management can reduce specialist waiting lists and costs. | Gadenz et al. 2021; Pachito et al. 2022; Pfeil et al. 2025. | The proposal should not become a telehealth evaluation project. |
| Active list updating can reveal obsolete demand and improve scheduling. | Salles et al. 2026; Lisboa et al. 2022. | Stale-demand detection is promising, but manual cleanup is already known. |
| ML can predict waiting time, no-show, service time or delay in healthcare. | Gloyn et al. 2026; Shin et al. 2024; Fall et al. 2025; Mandizvida et al. 2024. | Prediction alone is not enough for PhD novelty. |
| XAI can support outpatient waiting-time prediction. | Shin et al. 2024. | SHAP-based feature explanation is not novel by itself. |
| Queueing, simulation and optimization can evaluate healthcare capacity and delay. | Wartelle et al. 2026; Thompson et al. 2024; Wang et al. 2024; Lim et al. 2023; Lee et al. 2022; Wood et al. 2022; Kruik-Kolloffel et al. 2024. | Generic queueing/simulation cannot be claimed as original. |
| SUS regulation architecture and queue-management infrastructure have been proposed/implemented. | Cardoso et al. 2026. | The PhD should not frame itself as building the first regulation architecture. |
| ML waiting-list prioritization exists in a Brazilian cardiac-surgery context. | Gagliotti and Gutierrez 2025. | This is the closest direct competitor; differentiation is mandatory. |

## B. What Is Partially Solved?

| Partially solved area | What exists | What remains open |
|---|---|---|
| Predictive modeling for operational waiting-list behavior | ML prediction exists in ED/outpatient/public-hospital contexts; cardiac-surgery prioritization exists in Brazil. | Generalized modeling of SUS regulation workflows, multiple queue states, stale demand, returns, no-show/cancellation and bottlenecks remains underdeveloped. |
| Explainable AI for waiting-related decisions | SHAP/interpretable ML exists for outpatient waiting time. | Manager/regulator-centered explanation for queue behavior and operational action is not established in SUS regulation. |
| Queueing/simulation for patient flow | Strong methods exist in ED, radiology, OR, medication reconciliation, laboratory networks and outpatient sessions. | Adaptation to SUS regulation event logs and referral-management policies remains open. |
| Decision support for health operations | Queueing DSS and regulation architectures exist. | Integrated predictive/XAI/temporal decision support for SUS waiting-list management is not shown as solved. |
| Stale-demand/list quality | Manual updating and descriptive evidence exist. | Automated detection, reproducible metrics and model-based prioritization of cleanup remain open. |
| Fairness/equity in waiting lists | Equity is conceptually central in SUS literature. | Computational fairness audits and subgroup performance evaluation for regulation models remain sparse in the audited corpus. |
| Workflow integration | Regulatory nurse actions, training and architecture papers emphasize human roles. | Evaluated human-in-the-loop AI outputs for managers/regulators remain open. |

## C. What Remains Unsolved?

The strongest unsolved problem is not a single missing algorithm. It is the lack of an end-to-end computational research object for SUS regulation waiting lists.

Specifically, the audited corpus does not show a mature answer to:

1. How should SUS regulation data be represented as events, states, transitions and outcomes so that waiting-list dynamics can be modeled reproducibly?
2. Which operational outcomes define "problematic waiting-list behavior" beyond raw waiting time?
3. Can historical regulation events predict excessive wait, stagnation, stale demand, no-show/cancellation, return/devolution or bottleneck risk better than administrative baselines?
4. Can explanations be designed for managerial action rather than only feature importance?
5. Can models be validated temporally and evaluated with calibration, robustness, subgroup performance and operational utility?
6. Can predictions be connected to queue-level consequences or retrospective scenarios without automating access decisions?

These remain unsolved enough to justify a PhD, provided the thesis is scoped as a computational framework and evaluation methodology.

## D. What Exactly Is the PhD Contribution?

The defensible PhD contribution should be stated narrowly:

| Contribution component | Why it is PhD-relevant | What it must not become |
|---|---|---|
| Event-based representation of SUS regulation workflows | Converts administrative records into a reproducible computational object with states, transitions, timestamps and outcomes. | A local data-cleaning script. |
| Taxonomy of problematic waiting-list behaviors | Defines computational targets beyond generic waiting-time prediction. | A vague list of management problems. |
| Temporally validated predictive models | Tests whether event histories improve detection of operational risk over baselines such as FIFO, priority and historical averages. | A leaderboard of generic classifiers. |
| Explainability layer for managers/regulators | Translates model drivers into actionable, auditable explanations for human-in-the-loop decision support. | SHAP plots without workflow interpretation. |
| Evaluation framework for waiting-list DSS | Combines predictive performance, calibration, temporal robustness, subgroup analysis and operational utility. | A single AUC/F1 result. |
| Conditional scenario analysis | If data permit, evaluates retrospective management scenarios without promising deployment or autonomous prioritization. | A universal digital twin or national optimization platform. |

The thesis should be defended as:

> A Computer Science contribution in event-based health-system modeling, explainable predictive analytics and decision-support evaluation for public regulation workflows.

## Strongest Competing Works

| Competing work | Why it threatens the proposal | How to differentiate |
|---|---|---|
| Gagliotti and Gutierrez 2025, ML for cardiac surgery waiting-list prioritization | Direct Brazilian ML waiting-list example. Weakens broad claims of novelty. | Emphasize multi-state regulation workflows, multiple operational outcomes, human-in-the-loop DSS, temporal validation and manager-oriented explanations rather than procedure-specific urgent surgery prediction. |
| Shin et al. 2024, interpretable outpatient waiting-time prediction | Strong XAI wait-time prediction paper. Weakens novelty of SHAP/wait prediction. | Position the PhD around SUS regulation, long-horizon queues, event states, problematic behavior and managerial action, not outpatient wait estimation. |
| Cardoso et al. 2026, SUS regulation architecture | Direct SUS regulation technology architecture. Weakens claims about absent digital systems. | Position the PhD as an analytics/XAI layer and evaluation framework that could operate over such architectures. |
| Pazin-Filho et al. 2024, centralized surgical queue management | Strong Brazilian event-like queue dataset and operational management results. | Emphasize predictive/explainable modeling and generalizable event schema; do not claim centralization as novelty. |
| Gadenz/Pachito/Pfeil, RegulaSUS referral management | Shows referral management already reduces queues and costs. | Treat as evidence that regulation workflows matter; the PhD models behavior and supports decisions rather than evaluating telehealth intervention itself. |
| Wartelle et al. 2026 and Thompson et al. 2024 | Strong queueing/simulation methods for healthcare operations. | Use as methodological support; do not claim novelty in queueing theory. Novelty is SUS regulation adaptation and integrated evaluation. |

## Attempt to Reject the Proposal: 10 Strongest Reviewer Criticisms

| # | Skeptical criticism | Is it valid? | Rebuttal or required mitigation |
|---:|---|---|---|
| 1 | "This is not a Computer Science PhD; it is health management with AI vocabulary." | Partially valid. | Rebut by foregrounding event modeling, temporal prediction, calibration, XAI, baselines, validation protocol and DSS evaluation. The proposal must not spend too much space on SUS policy narrative. |
| 2 | "The literature already has ML waiting-time prediction and interpretable outpatient prediction." | Valid. | Rebut by conceding this and narrowing novelty: not generic prediction, but SUS regulation event modeling and decision-support evaluation for problematic queue behavior. |
| 3 | "There is already Brazilian ML for cardiac surgery waiting-list prioritization." | Valid and serious. | Rebut by differentiating scope and task: procedure-specific urgent surgery prediction versus multi-state regulation workflow, multiple operational outcomes, temporal validation and human-in-the-loop explanations. |
| 4 | "Queueing theory, simulation and resource allocation are already mature." | Valid. | Rebut by not claiming methodological novelty in queueing itself. Position simulation as conditional evaluation, not thesis core. |
| 5 | "SUS regulation architecture has already been developed; what is new?" | Partially valid. | Rebut that architecture enables data flow and monitoring, while the PhD studies predictive/explainable analytics and evaluation over regulation events. |
| 6 | "The proposal may only apply known models to local administrative data." | Valid risk. | Mitigate by defining original research artifacts: event schema, outcome taxonomy, temporal validation protocol, explanation templates and evaluation metrics. |
| 7 | "Data availability may be insufficient for the proposed outcomes." | Valid and high risk. | Mitigate with a minimum viable dataset and modular outcomes. Core must work with request ID, dates, status, specialty/procedure and outcome; richer analyses become optional. |
| 8 | "Problematic behavior is too broad and underspecified." | Valid. | V2 should restrict core outcomes to 3-4: excessive wait, stagnation, non-resolutive exit/no-show/cancellation, and specialty/service bottleneck risk. |
| 9 | "Human-in-the-loop decision support without deployment may not prove practical utility." | Partially valid. | Rebut through retrospective temporal validation, case-based review, administrative baselines and optional structured expert evaluation. Do not promise deployment. |
| 10 | "The proposal might produce a useful applied study but not a generalizable scientific contribution." | Partially valid. | Mitigate by emphasizing reproducible representation, benchmark tasks, validation protocol and transferable evaluation framework for public regulation workflows. |

## Final Scientific Defensibility Assessment

| Dimension | Assessment |
|---|---|
| Reality of gap | Strong, if formulated as integrated event-based XAI/DSS for SUS regulation workflows. |
| Risk of already solved gap | Medium. Components are solved; end-to-end SUS regulation decision-support is not. |
| Risk of mere application | Medium-High unless the thesis clearly contributes representation, outcome taxonomy and evaluation protocol. |
| PhD novelty | Sufficient but conditional. Novelty is in formalization and evaluation, not in inventing a new ML algorithm. |
| Feasibility | Moderate. Feasible with minimum event/status data; higher-risk if capacity, priority, exit reasons or demographic variables are missing. |
| Best defense strategy | Admit existing components, then argue the unsolved integration: SUS regulation events + problematic behavior taxonomy + temporal XAI + human-in-the-loop decision-support evaluation. |

## Required Positioning Adjustment for Future Versions

The V1 proposal is broadly defensible, but V2 should make three points sharper:

1. The project is **not** about predicting waiting time alone.
2. The core scientific artifact is a **computational representation and evaluation framework** for regulation-event data.
3. The thesis contribution is **workflow-aware explainable decision support**, not autonomous prioritization, national implementation or generic queue optimization.

If these boundaries are maintained, the proposed gap is scientifically defensible for PPGCC/UFSC. If they are blurred, a skeptical reviewer could reasonably downgrade the proposal as a local application of known ML/XAI/queueing methods.
