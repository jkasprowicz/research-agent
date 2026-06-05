# PhD Supervisor Gap Assessment: SUS Waiting Lists, Regulation Systems and Decision Support

## Supervisor Verdict

The literature does not support a PhD framed simply as "machine learning to predict waiting time" or "AI to optimize queues." Those problems are either already demonstrated in adjacent healthcare settings or too narrow to sustain a strong Computer Science doctorate.

The literature does support a stronger and more defensible PhD problem:

> Explainable, data-driven decision support for detecting, explaining and simulating problematic waiting-list behavior in SUS regulation workflows, with emphasis on specialized outpatient care, referral management, patient prioritization and resource-allocation scenarios.

The novelty is not the existence of waiting lists, telehealth, queueing theory, ML prediction or centralized management. The novelty is integrating these elements into a reproducible, workflow-aware computational framework for real SUS regulation data.

## Problems Already Solved

These areas should be treated as foundations, not as novelty claims.

| Research problem | Current state of evidence | Remaining gap | Novelty potential | Expected publication impact |
|---|---|---|---|---|
| Demonstrating that SUS waiting lists are a major access problem | Strong Brazilian conceptual and empirical evidence shows waiting lists are critical for specialized outpatient care, surgery and access equity. | Need better computational characterization, but the problem itself is established. | Low if framed only as problem description. | Low to moderate; useful background, not a main PhD contribution. |
| Showing that centralized waiting-list management can reduce backlog and waiting time | Brazilian surgical-list evidence shows centralized queue/list systems can reduce waiting time and backlog. | Need predictive, explainable and prospective decision support on top of centralization. | Low for simply proposing centralization. | Moderate in health-services journals; limited CS novelty. |
| Showing that telehealth/referral management can reduce waiting lists and costs | RegulaSUS and related studies show reductions in list size, waiting time and costs through telehealth-supported referral management/gatekeeping. | Need individualized and system-level analytics to explain which queues, referrals or specialties benefit most. | Low for re-evaluating telehealth alone. | Moderate to high in health policy if new data are strong; limited CS impact alone. |
| Showing that list updating/data cleaning matters | Speech-therapy waiting-list evidence shows obsolete demand and changed complaints affect the queue. | Need automated detection of stale, inconsistent or high-risk queue records. | Moderate if converted into computational data-quality methods. | Moderate; strong practical relevance. |
| Modeling healthcare waiting/capacity with queueing theory | Queueing applications exist in OR staffing, ED crowding, medication reconciliation, delayed transfers, disaster planning and AI triage evaluation. | Need adaptation to SUS regulation-event data and referral workflows. | Low for generic queueing model; moderate if SUS-specific and data-driven. | Moderate to high if methodologically rigorous. |
| Predicting waiting times or delays with ML | ED, outpatient and public-hospital studies show ML can predict waiting times, no-show/service time or delay classes. | Need external validation, decision impact, explainability and fit to regulation systems. | Low for another isolated predictor. | Moderate if only predictive; higher if integrated with DSS. |
| Using SHAP/interpretable ML for waiting-time explanation | Interpretable outpatient waiting-time prediction has been demonstrated using SHAP and asymmetric loss. | Need explanations designed for SUS managers/regulators, not just model developers. | Moderate if adapted to managerial reasoning and policy actions. | Moderate to high in applied AI/health informatics. |
| Simulating patient-flow scenarios | DES and hybrid AI/simulation are established in ED/OR/process optimization contexts. | Need bounded, realistic simulation of regulation actions in SUS waiting lists. | Low for generic simulation; moderate to high for action-linked SUS scenarios. | Moderate to high if simulation supports decisions and is validated. |

## Problems Partially Solved

These areas have evidence, but still leave space for a PhD-level contribution.

| Research problem | Current state of evidence | Remaining gap | Novelty potential | Expected publication impact |
|---|---|---|---|---|
| Predicting problematic waiting-list behavior in SUS regulation workflows | ML wait prediction exists outside SUS; SUS studies describe waits and interventions but rarely model future behavior. | Define and predict operationally meaningful outcomes: excessive wait, stagnation, avoidable delay, dropout/no-contact, reprioritization need, referral mismatch. | High. | High, especially for health informatics, AI in healthcare and CS applied to public systems. |
| Patient prioritization in Brazilian waiting lists | A cardiac-surgery ML prioritization study exists, but it is narrow and disease/procedure-specific. | Generalizable prioritization-support framework for specialized outpatient regulation remains open. | High if framed as support/explanation, not automatic rationing. | High if validated on real SUS data. |
| Integration of ML with queueing theory | Hybrid examples exist, but many are outside SUS or weakly validated. | Need a principled architecture connecting predictions to queue-level consequences. | High. | High for CS venues if evaluation goes beyond AUC. |
| Simulation of management actions before implementation | Simulation exists in ED/OR settings, but not strongly in SUS referral regulation. | Need realistic scenarios: increased capacity, tele-regulation, priority rule changes, stale-list cleanup, specialty redistribution. | High if scoped carefully. | Moderate to high. |
| Explainable decision support for regulators | XAI exists for outpatient waiting time; SUS regulation architecture exists, but not combined with XAI. | Need explanations at case, queue, specialty and system levels. | High. | High if explanations are evaluated with stakeholders or realistic use cases. |
| Detecting bottlenecks in specialized outpatient care | Cross-sectional SUS oral-health studies identify service factors associated with waits. | Need longitudinal bottleneck detection using event-level regulation data. | High. | Moderate to high. |
| Referral-management analytics | Telehealth/gatekeeping studies show intervention value, but not predictive triage of referral flows. | Need models explaining referral accumulation, rejected/redirected referrals and queue pressure. | High. | High for SUS-focused applied informatics. |
| Data-quality assessment in waiting lists | Descriptive evidence shows stale records and complaint changes. | Need systematic computational metrics for list validity, duplicate demand, inactive cases, missing priority and inconsistent status. | Moderate to high. | Moderate; strong practical utility. |
| Human workflow integration | Experience reports and training studies describe roles and capacity-building. | Need models that respect regulator workflow and produce actionable outputs. | Moderate to high. | Moderate; stronger if paired with DSS evaluation. |
| Resource-allocation support | Queueing/optimization literature is mature in other settings. | Need transparent scenario-based allocation support for SUS managers without overclaiming automatic optimization. | Moderate to high. | High if rigorous and ethically framed. |

## Problems Not Solved

These are the strongest candidates for a PhD contribution.

| Research problem | Current state of evidence | Remaining gap | Novelty potential | Expected publication impact |
|---|---|---|---|---|
| A reproducible computational representation of SUS waiting-list dynamics | SUS systems and queue concepts exist, but there is no widely validated event-level representation for regulation workflows. | Define states, transitions, timestamps, outcomes and queue events for specialized outpatient/referral management. | Very high. | High; foundational CS/health-informatics contribution. |
| Explainable prediction of problematic queue behavior in SUS regulation | Adjacent ML exists; direct SUS explainable models are sparse. | Build models that predict and explain queue stagnation, excessive wait, referral mismatch and access risk. | Very high. | High. |
| Linking individual predictions to queue-level consequences | Most ML studies stop at prediction; queueing papers often assume classifier behavior abstractly. | Evaluate whether model-based prioritization actually changes waiting-time distribution, equity and backlog dynamics. | Very high. | Very high if executed well. |
| Workflow-aware decision support for healthcare managers | DSS examples exist, but not integrated for SUS waiting-list regulation with explainability and simulation. | Create manager-facing outputs: bottleneck alerts, scenario comparisons, risk strata and explanation summaries. | Very high. | High to very high. |
| Fairness-aware waiting-list analytics in SUS | Access equity is discussed conceptually, but fairness metrics are mostly absent in the analyzed computational papers. | Measure whether delays or model recommendations differ by geography, socioeconomic proxy, age, sex, priority, specialty or referral origin. | Very high. | High, especially if handled carefully and transparently. |
| Stale-list and invalid-demand detection | Empirical evidence shows stale records; computational detection is not established. | Predict outdated/inactive demand and quantify its effect on backlog and waiting-time estimates. | High. | Moderate to high. |
| Multi-specialty specialized outpatient regulation modeling | Existing evidence is often single specialty, surgical, dental or ED-based. | Build models across specialties with shared schema but specialty-specific behavior. | High. | High if data access permits. |
| Actionable simulation of regulation policies | Simulation exists in hospitals, not as a mature SUS regulation policy sandbox. | Simulate impact of interventions: capacity changes, telehealth review, priority-rule changes, cleanup campaigns, no-show mitigation. | High. | High if model is validated and not overbuilt. |
| Transparent patient-prioritization support without replacing clinical judgment | Prioritization tools exist but implementation evidence is weak. | Design assistive prioritization with explanations, constraints and human override. | High. | High, but ethically sensitive. |
| Evaluation metrics for waiting-list DSS | Literature uses waiting time, backlog, AUC, costs or throughput separately. | Define combined metrics: predictive performance, wait-time impact, equity impact, resource use, manager interpretability and implementation burden. | Very high. | Very high for a CS PhD if formalized clearly. |

## Consolidated Research Problem Table

| Research problem | Current state of evidence | Remaining gap | Novelty potential | Expected publication impact |
|---|---|---|---|---|
| Waiting-list burden in SUS | Well established by conceptual, surgical, outpatient and specialized-care studies. | Computational modeling of dynamic behavior. | Low alone. | Low as main contribution. |
| Centralized queue management | Demonstrated in Brazilian hospital surgical lists. | Predictive and explainable support for ongoing management. | Moderate. | Moderate. |
| Referral management and telehealth | Strong Brazilian practical/economic evidence. | Predictive/explainable analytics for referral flows. | High. | High. |
| Queue data quality | Empirically visible in list-updating studies. | Automated stale/inconsistent record detection. | High. | Moderate to high. |
| Waiting-time prediction | Demonstrated in ED/outpatient contexts. | SUS regulation-specific, action-linked prediction. | Moderate if isolated; high if DSS-linked. | Moderate to high. |
| No-show/service-time prediction | Demonstrated in outpatient scheduling. | Adaptation to referrals, scheduling and regulation events. | Moderate. | Moderate. |
| Patient prioritization | Partially demonstrated in cardiac surgery and review literature. | Generalizable, explainable, fairness-aware prioritization support. | High. | High. |
| Queueing-based capacity modeling | Mature in multiple healthcare contexts. | Data-driven SUS regulation queueing models. | Moderate to high. | High if validated. |
| Simulation of patient flow | Mature in ED/OR, weaker in regulation. | Simulation of SUS referral/waiting-list policies. | High. | High. |
| Resource allocation | Mature methodologically outside SUS. | Transparent scenario-based support for SUS managers. | High. | High. |
| Explainable AI for managers | Demonstrated in outpatient waits, sparse in SUS. | Manager/regulator-centered explanation layer. | High. | High. |
| Fairness-aware access analytics | Conceptually important, computationally underdeveloped in corpus. | Equity metrics and bias analysis for waits and model outputs. | Very high. | High. |
| Decision-support architecture | SUS regulation architecture exists, but predictive/simulation layers are missing. | Integrated DSS pipeline with data, models, explanations and scenarios. | Very high. | Very high. |
| Implementation evidence for prioritization tools | Literature identifies a theory-practice gap. | Prospective or retrospective workflow evaluation of actionable DSS. | Very high. | Very high if feasible. |

## Methodological Gaps

| Gap | Why it matters | Evidence from corpus | PhD opportunity |
|---|---|---|---|
| Prediction and queueing are rarely integrated end-to-end | Predictive accuracy does not guarantee better waiting-list outcomes. | ML papers predict waits; queueing papers evaluate capacity separately. | Build a framework where predictions are evaluated by queue impact. |
| Evaluation often stops at AUC/error metrics | Managers need consequences, not just model scores. | ML studies emphasize performance; Thompson et al. shows the importance of wait-time savings. | Define evaluation metrics combining prediction, wait reduction, backlog, equity and interpretability. |
| Limited temporal/event-level modeling | Waiting lists evolve through states, not static rows. | SUS studies report before-after or cross-sectional outcomes. | Model queue states, transitions and time-to-event outcomes. |
| Limited causal or counterfactual reasoning | Managers ask what would happen under intervention. | Pre-post studies show changes but cannot fully isolate causes. | Use simulation and quasi-experimental evaluation where possible. |
| Weak multi-level modeling of case, specialty and system | Regulation operates across individual patients, specialties and services. | Evidence is often single-setting or aggregate. | Build hierarchical/multilevel models for patient, specialty and service effects. |

## Data Gaps

| Gap | Why it matters | Evidence from corpus | PhD opportunity |
|---|---|---|---|
| Lack of standardized event schema for regulation data | Without a schema, models are local and hard to reproduce. | Cardoso et al. emphasizes architecture/interoperability; Pazin-Filho et al. uses hospital queue data. | Define a reproducible data model for referrals, queue states and outcomes. |
| Missing reasons for queue exit/removal | Exit reason is essential for distinguishing solved cases, no-contact, cancellation and inappropriate referral. | Pfeil et al. notes limited documentation of removal reasons. | Develop outcome taxonomy and missingness-aware models. |
| Stale and outdated demand | Backlog may be inflated by invalid cases. | Salles et al. removed many users after list updating. | Create stale-record detection and list-validity indicators. |
| Limited patient-level socioeconomic/access variables | Fairness analysis depends on proxies for vulnerability and geography. | Conceptual/access papers highlight equity, but computational papers rarely operationalize it. | Incorporate geography, referral origin, priority, age, sex and deprivation proxies where ethical/legal. |
| Fragmented systems and interoperability | Regulation data may be split across local systems. | Cardoso et al. identifies multi-region architecture and interoperability needs. | Design methods tolerant to heterogeneous schemas and missing variables. |

## Operational Gaps

| Gap | Why it matters | Evidence from corpus | PhD opportunity |
|---|---|---|---|
| Models do not map cleanly to manager actions | A risk score is useless if no action follows. | Prioritization review shows poor implementation of tools. | Define action categories: review, update, redirect, prioritize, capacity request, telehealth gatekeeping. |
| Specialty heterogeneity is under-modeled | Queue behavior differs by specialty, procedure and resource type. | Oral-health, cardiac, speech-therapy and surgical papers show specialty-specific patterns. | Build specialty-aware models with shared structure and local calibration. |
| Queue cleanup is treated as manual activity | Manual updating works but is labor-intensive. | Salles et al. and Lisboa et al. show operational list maintenance. | Develop computational triage for list-cleaning campaigns. |
| Capacity and demand are not jointly modeled | Waiting time depends on inflow and service capacity. | Queueing papers formalize capacity; SUS papers often describe outcomes. | Combine demand forecasting with service-capacity and queue-state features. |
| Referral quality is insufficiently modeled | Poor referrals generate avoidable demand and delay. | Telehealth/gatekeeping studies show demand can be redirected. | Predict referral adequacy or mismatch risk using structured regulation data. |

## Implementation Gaps

| Gap | Why it matters | Evidence from corpus | PhD opportunity |
|---|---|---|---|
| Prioritization tools rarely reach real-world use | Implementation failure is a central weakness in the field. | Waiting-list management review reports low implementation rates. | Design for low-burden, human-in-the-loop use from the start. |
| Limited stakeholder-centered evaluation | Manager trust and usability are crucial. | Training/regulatory nurse papers show human roles are central. | Evaluate outputs with regulators/managers through case reviews or structured expert feedback. |
| Interoperability and auditability are underused in ML papers | Public systems need traceability. | Cardoso et al. frames auditability and multi-region regulation architecture. | Create auditable model outputs and documented decision logs. |
| Ethical/legal constraints are often implicit | Prioritization affects access rights. | SUS conceptual papers emphasize equity and governance. | Treat DSS as assistive, transparent and overrideable. |
| Cost and operational burden are rarely connected to AI models | Managers need feasibility, not only predictions. | Pachito et al. and Pfeil et al. show economic importance. | Include implementation burden and resource implications in model evaluation. |

## Explainability Gaps

| Gap | Why it matters | Evidence from corpus | PhD opportunity |
|---|---|---|---|
| Explanations are mostly feature importance, not managerial reasoning | Managers need to know what can be acted upon. | Shin et al. uses SHAP, but SUS-specific explanation needs are absent. | Produce explanations by actionable drivers: queue length, specialty capacity, referral source, stale risk, priority mismatch. |
| Case-level and queue-level explanations are not connected | A case explanation may not explain system bottlenecks. | ML papers focus on prediction; queueing papers focus on system behavior. | Build multi-level explanation: patient/referral, queue, specialty and municipality/service. |
| Explanations rarely include uncertainty | Overconfident explanations can mislead prioritization. | Most papers do not emphasize uncertainty communication. | Add calibrated risk intervals, confidence bands or uncertainty flags. |
| No clear explanation format for SUS regulators | Different users need different explanation granularity. | Human workflow papers show regulators and managers have distinct roles. | Design explanation templates for operational review. |

## Fairness Gaps

| Gap | Why it matters | Evidence from corpus | PhD opportunity |
|---|---|---|---|
| Equity is discussed more than measured | SUS access is equity-driven, but computational fairness metrics are scarce. | Giannotti et al. and access papers frame equity; ML papers rarely test it. | Evaluate delay and model performance by geography, referral origin, sex, age, priority and vulnerability proxies. |
| Prioritization may reinforce existing access bias | Historical data encode past inequities. | Cardiac prioritization and waiting-time models use retrospective data. | Use fairness audits and sensitivity analyses before recommending prioritization support. |
| Rural/remote access is under-modeled | Referral systems often serve heterogeneous territories. | Telehealth and SUS regulation papers imply geographic access variation. | Model spatial/municipal effects and access-distance proxies. |
| Fairness impact of queue interventions is not simulated | Reducing mean wait may worsen vulnerable subgroup access. | Queueing/simulation papers rarely address fairness. | Simulate distributional impacts, not only mean waiting time. |

## Simulation Gaps

| Gap | Why it matters | Evidence from corpus | PhD opportunity |
|---|---|---|---|
| Simulation is rarely applied to SUS regulation workflows | ED/OR simulations do not capture referral regulation dynamics. | Wartelle, Gabriel and Rifi are methodologically useful but contextually distant. | Build bounded simulations for referral queues and specialized outpatient access. |
| Simulations often lack validation against real queue trajectories | Unvalidated simulations can be persuasive but wrong. | Scenario studies depend heavily on assumptions. | Validate simulated backlog/wait distributions against historical data. |
| Intervention policies are not standardized | It is unclear which actions should be simulated. | SUS studies describe different interventions: centralization, telehealth, cleanup, task forces. | Simulate a small set of realistic policies, not a universal platform. |
| Uncertainty is under-communicated | Managers need plausible ranges, not point estimates. | Rifi et al. emphasizes uncertainty in OR waits. | Report scenario bands and sensitivity analyses. |

## Healthcare Management Gaps

| Gap | Why it matters | Evidence from corpus | PhD opportunity |
|---|---|---|---|
| Waiting-list governance lacks computational observability | Managers need visibility into inflow, outflow, stagnation and bottlenecks. | Pazin-Filho et al. shows central visibility matters. | Build dashboards/metrics conceptually, even if not full software deployment. |
| Regulations and protocols are not encoded as model constraints | Pure ML may violate management rules. | SUS regulation papers emphasize protocols and governance. | Represent priority rules and eligibility constraints explicitly. |
| Resource allocation lacks transparent trade-off support | Managers balance fairness, urgency, capacity and cost. | Queueing/optimization and telehealth cost papers show trade-offs. | Develop decision-support outputs comparing scenarios and trade-offs. |
| Human regulators remain central but under-modeled | Systems must assist, not replace regulation teams. | Regulatory nurse and training studies demonstrate human role. | Human-in-the-loop design should be part of the research contribution. |
| Success metrics are fragmented | Studies separately measure wait time, backlog, cost, accuracy or satisfaction. | Corpus uses inconsistent outcomes. | Propose a multidimensional evaluation framework for SUS waiting-list DSS. |

## Strongest PhD-Level Gap

The strongest gap is:

> A reproducible, explainable and workflow-aware computational framework for modeling SUS waiting-list dynamics and supporting regulation decisions, integrating prediction, queue-state analysis, scenario simulation and fairness-aware evaluation.

This gap is strong because it is:

- Grounded in direct SUS evidence.
- Clearly aligned with Computer Science.
- Not already solved by telehealth or centralized-list studies.
- Not reducible to another ML prediction task.
- Feasible if event-level regulation data are available.
- Publishable as a sequence of studies: data model, descriptive queue analytics, predictive/XAI model, simulation/evaluation framework and decision-support validation.

## What I Would Not Approve as a PhD Framing

| Weak framing | Why it is weak |
|---|---|
| "Using AI to predict SUS waiting time" | Too narrow; adjacent literature already predicts waits; weak decision contribution. |
| "Optimizing SUS queues with machine learning" | Too vague and potentially ethically risky; sounds like automatic rationing. |
| "Telehealth to reduce waiting lists" | Already well supported; more health-services evaluation than CS PhD unless computational layer is added. |
| "A digital twin of SUS waiting lists" | Too ambitious and likely infeasible for admission-stage work. |
| "A generic platform for queue management" | Overbroad and implementation-heavy; likely impossible within PhD scope. |

## Best PhD Framing After Gap Analysis

Recommended title direction:

> Explainable Decision Support for Problematic Waiting-List Behavior in SUS Regulation Workflows

Alternative title direction:

> Data-Driven Modeling and Simulation of Waiting-List Dynamics for Specialized Care Regulation in SUS

Core research question:

> How can event-level regulation data be modeled to detect, explain and simulate problematic waiting-list behavior in SUS specialized-care access, while preserving transparency, fairness and managerial actionability?

Most defensible contribution:

> Not an algorithm that decides who receives care, but a computational decision-support framework that helps managers understand where queues are failing, which cases or services are at risk, and what plausible management actions may improve access.

