# Gap Validation Matrix for `plano_doutorado_v2.md`

Purpose: evaluate whether the proposed gap is genuinely supported after reading the V2 proposal, prior gap audit, literature reviews, and Tier 1/Tier 2 article notes.

## Matrix

| Component | Existing literature | Evidence | Already solved? | Partially solved? | Open problem? | Confidence |
|---|---|---|---|---|---|---|
| Event-based representation | SUS studies contain inflow/outflow, statuses and regulation architecture; ED and outpatient papers use operational/event-like data. | Pazin-Filho et al. 2024 uses surgical indications, inflow/outflow and exit reasons; Cardoso et al. 2026 describes regulation architecture/interoperability; Shin et al. 2024 uses outpatient event logs; Wartelle et al. 2026 models patient-flow states. | No, not as a standardized SUS regulation framework. | Yes. Event-like data exist in individual systems, but not a reproducible event-state-transition artifact for regulation workflows. | Define event schema, states, transitions, timestamps, outcomes and derived variables for regulation data. | Medium-High |
| Waiting-list modelling | Waiting lists are studied descriptively, operationally and epidemiologically in SUS; ML waiting/delay models exist outside or adjacent to SUS. | Giannotti et al. 2025; Pazin-Filho et al. 2024; Antunes et al. 2025; Salles et al. 2026; Gloyn et al. 2026; Shin et al. 2024; Mandizvida et al. 2024. | Problem relevance and descriptive modeling are solved. | Yes. Prediction/delay modeling exists, but not broadly in SUS regulation workflows. | Model multi-state waiting-list behavior beyond single waiting-time outcome. | High |
| Queue dynamics | Queueing theory is mature in healthcare operations; SUS queue management exists empirically. | Thompson et al. 2024; Wartelle et al. 2026; Wang et al. 2024; Lim et al. 2023; Lee et al. 2022; Pazin-Filho et al. 2024. | Generic queueing and some queue management are solved. | Yes. Queue dynamics are modeled in ED/radiology/lab/OR settings and empirically in SUS surgical lists. | Adapt queue dynamics to regulation-event data and managerial actions without claiming new queueing theory. | High |
| Temporal validation | Some ML studies use retrospective data and model evaluation, but the corpus does not show mature temporal validation for SUS regulation models. | Gloyn et al. 2026 notes implementation/generalization gaps; Shin et al. 2024 uses retrospective outpatient data; Mandizvida et al. 2024 uses short-window public-hospital data. | No. | Partially in general health ML, weakly in this corpus for regulation. | Define temporal train/validation/test protocol, leakage prevention and stability analysis for regulation data. | Medium |
| Explainable AI | Interpretable ML has been applied to outpatient waiting-time prediction; XAI is underdeveloped for SUS regulation workflows. | Shin et al. 2024 uses SHAP; Gloyn et al. 2026 reviews wait-prediction models; Hroub et al. 2025 identifies implementation gaps. | XAI for waiting-time prediction is partly solved. | Yes. XAI exists technically, but mostly not designed for SUS managers/regulators or multi-level queue explanations. | Produce explanations at request, queue/specialty, service/unit and temporal levels tied to actionable workflow. | High |
| Decision support | Queueing/optimization DSS and SUS regulation architecture exist; many prioritization tools lack implementation. | Wang et al. 2024; Thompson et al. 2024; Cardoso et al. 2026; Hroub et al. 2025; Pazin-Filho et al. 2024. | Decision support exists in adjacent domains; regulation architecture exists. | Yes. Existing work supports monitoring, queueing decisions or architecture, but not integrated XAI/event-based DSS for SUS waiting lists. | Define decision-support outputs, baselines, explanation formats and retrospective utility evaluation. | High |
| Healthcare regulation workflows | Brazilian studies strongly describe regulation, referral management, telehealth, governance and professional workflow. | Gadenz et al. 2021; Pachito et al. 2022; Pfeil et al. 2025; Giannotti et al. 2025; Lisboa et al. 2022; Cardoso et al. 2026. | The workflow/problem context is well established. | Yes. Practical regulation interventions exist, but mostly without predictive/XAI modeling. | Convert regulation workflow into computational tasks and evaluation protocols. | High |
| Operational utility evaluation | Queueing papers evaluate wait-time savings/scenarios; SUS studies report operational outcomes; ML papers often stop at predictive performance. | Thompson et al. 2024; Wang et al. 2024; Wartelle et al. 2026; Pazin-Filho et al. 2024; Gadenz et al. 2021; Shin et al. 2024. | Operational outcomes are evaluated in some domains. | Yes. Utility evaluation exists but is fragmented: operational studies lack ML/XAI, ML studies lack workflow utility. | Link model outputs to retrospective operational value without deployment or autonomous prioritization. | Medium-High |
| Data quality / stale demand | Manual list updating and documentation gaps are documented. | Salles et al. 2026; Pfeil et al. 2025; Giannotti et al. 2025. | Manual updating relevance is solved. | Yes. Data-quality problems are known, but automated/computational metrics are not mature. | Define reproducible indicators for stale, missing, inconsistent or non-resolutive records. | Medium-High |
| Human-in-the-loop regulation | Human regulatory roles and implementation gaps are documented. | Lisboa et al. 2022; Hroub et al. 2025; Giannotti et al. 2025; Cardoso et al. 2026. | Human role relevance is established. | Yes. Systems may support or automate decisions, but safe human-in-the-loop XAI for regulation is not well evidenced. | Design explainable outputs for review, audit and managerial action without automated access decisions. | High |
| Transferability beyond local dataset | Multi-region architecture exists; queue methods are transferable; but empirical validation across regulation databases is not shown. | Cardoso et al. 2026; Thompson et al. 2024; Wartelle et al. 2026; Wang et al. 2024. | No. | Weakly. Some methods are transferable in principle; SUS regulation transferability remains unproven. | Define components that can transfer: event schema, task definitions, baselines, metrics, explanation templates. | Medium |

## What Exactly Remains Unsolved?

The exact unsolved problem is:

> How to transform historical records from SUS regulation workflows into a reproducible event-based computational object, define operationally meaningful problematic waiting-list behaviors, evaluate explainable models through temporal validation and administrative baselines, and translate the outputs into human-in-the-loop decision support without claiming autonomous prioritization or national deployment.

This unsolved problem has four layers:

1. **Representation gap:** there is no clearly validated event-state-transition schema for SUS regulation waiting-list dynamics in the audited corpus.
2. **Task-definition gap:** waiting time is overused as a simple outcome; problematic behaviors such as stagnation, non-resolutive exit, stale demand and bottleneck risk need reproducible definitions.
3. **Evaluation gap:** existing ML and queueing papers often evaluate accuracy, wait reduction or scenarios separately; the proposal needs combined evaluation across temporal validation, calibration, interpretability and operational utility.
4. **Workflow gap:** existing SUS regulation evidence is strong but mostly descriptive/managerial; existing computational evidence is strong but mostly outside SUS. The missing piece is workflow-aware, explainable decision support for regulation managers.

## Brutal Validity Check

| Question | Answer |
|---|---|
| Is the gap real? | Yes, but it is an integration/formalization gap, not an algorithmic gap. |
| Is it already solved? | No end-to-end. Many components are solved separately. |
| Is it merely local application? | It could become local application if V3 does not emphasize representation, task definitions and evaluation framework. |
| Is the proposed contribution novel enough? | Probably yes for an admission proposal, if it avoids claiming novelty in ML, SHAP, queueing or queue management. |
| Main residual weakness | Transferability and temporal validation are asserted more strongly than the current references support. |
