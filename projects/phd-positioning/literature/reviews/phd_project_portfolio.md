# PhD Research Project Portfolio: SUS Waiting Lists and Regulation Systems

## Evaluation Logic

This portfolio translates the identified literature gaps into 15 possible PhD research projects. The scoring is intentionally conservative and oriented toward a 4-year Computer Science doctorate with practical dependence on SUS regulation data.

Scores use a 1-10 scale:

| Score | Meaning |
|---|---|
| Novelty | Scientific originality relative to the analyzed literature. |
| Feasibility | Probability of execution in 4 years with realistic SUS/regulation data access. |
| Impact on SUS | Expected practical value for SUS access, regulation, specialized outpatient care or waiting-list management. |
| UFSC CS fit | Alignment with Computer Science through AI, data modeling, operations research, simulation, decision support, explainability or information systems. |

Composite rank is the average of the four scores. Publication potential is described qualitatively inside each project.

## Ranked Project Overview

| Rank | Project | Novelty | Feasibility | SUS impact | UFSC CS fit | Composite |
|---:|---|---:|---:|---:|---:|---:|
| 1 | Explainable Decision Support for Problematic Waiting-List Behavior in SUS Regulation Workflows | 9 | 8 | 10 | 10 | 9.25 |
| 2 | Hybrid Machine Learning and Queueing Simulation for Specialized-Care Regulation Policies | 9 | 7 | 9 | 10 | 8.75 |
| 3 | Fairness-Aware Prioritization Support for SUS Waiting Lists | 10 | 6 | 10 | 9 | 8.75 |
| 4 | Stale-Demand and Data-Quality Intelligence for SUS Waiting Lists | 8 | 9 | 9 | 8 | 8.50 |
| 5 | Referral Adequacy and Demand-Redirection Prediction for Specialized Care | 8 | 7 | 10 | 9 | 8.50 |
| 6 | Event-Level Data Model and Benchmark for SUS Waiting-List Dynamics | 8 | 8 | 8 | 9 | 8.25 |
| 7 | Resource-Allocation Scenario Optimizer for Specialized Outpatient Capacity | 8 | 5 | 10 | 10 | 8.25 |
| 8 | Multi-Specialty Bottleneck Detection and Capacity Stress Forecasting | 7 | 8 | 9 | 8 | 8.00 |
| 9 | Human-in-the-Loop Regulation Decision Support with Auditability | 8 | 6 | 9 | 9 | 8.00 |
| 10 | Time-to-Care Survival Modeling for Specialized Outpatient Access | 7 | 9 | 8 | 8 | 8.00 |
| 11 | Offline Policy Evaluation for Waiting-List Prioritization Rules | 9 | 5 | 8 | 10 | 8.00 |
| 12 | Natural Language Processing of Referral Requests for Regulation Support | 8 | 6 | 8 | 9 | 7.75 |
| 13 | Telehealth Referral-Management Analytics for Queue Impact Assessment | 7 | 7 | 9 | 8 | 7.75 |
| 14 | No-Show, Dropout and Queue-Attrition Prediction in Specialized Care | 7 | 8 | 8 | 8 | 7.75 |
| 15 | Interoperability-Aware Regulation Data Pipeline for Cross-Region Waiting-List Analytics | 7 | 7 | 8 | 9 | 7.75 |

## 1. Explainable Decision Support for Problematic Waiting-List Behavior in SUS Regulation Workflows

| Field | Description |
|---|---|
| Title | Explainable Decision Support for Problematic Waiting-List Behavior in SUS Regulation Workflows |
| Research question | How can event-level regulation data be used to detect, predict and explain problematic waiting-list behavior in SUS specialized-care access? |
| Hypothesis | Event-level queue states, referral metadata, specialty context and historical regulation actions can predict problematic queue behavior more usefully than static waiting-time summaries, and explainable outputs can support managerial decisions without replacing regulation professionals. |
| Methodology | Define a regulation-event data model; construct retrospective cohorts; define outcomes such as excessive wait, stagnation, avoidable delay, stale demand, no-contact/dropout and reprioritization need; train interpretable ML/survival models; evaluate calibration, discrimination and subgroup performance; apply SHAP/counterfactual explanations; create manager-oriented explanation templates; validate retrospectively with case/queue examples. |
| Required data | Referral records, patient pseudonymous ID, specialty, requested procedure, priority/risk, municipality, referral origin, timestamps, queue status changes, scheduling, attendance, cancellation, rejection/redirection, exit reason and service capacity proxies. |
| Expected publications | Data model and outcome taxonomy for SUS regulation; predictive/XAI model for problematic waiting-list behavior; decision-support evaluation with retrospective queue cases. |
| Novelty score | 9 |
| Feasibility score | 8 |
| Impact on SUS | 10 |
| UFSC CS PhD fit | 10 |

## 2. Hybrid Machine Learning and Queueing Simulation for Specialized-Care Regulation Policies

| Field | Description |
|---|---|
| Title | Hybrid Machine Learning and Queueing Simulation for Specialized-Care Regulation Policies |
| Research question | Can ML predictions combined with queueing/simulation models estimate the impact of regulation policies on waiting time, backlog and access equity? |
| Hypothesis | Hybrid ML-queueing simulation can estimate policy consequences more realistically than aggregate historical averages, especially when queue behavior differs by specialty and referral source. |
| Methodology | Forecast arrivals, service rates and dropout/no-show risks; estimate specialty-specific queue parameters; build discrete-event or queueing simulation; test scenarios such as capacity increase, telehealth review, priority-rule changes, stale-list cleanup and referral redirection; validate against historical queue trajectories. |
| Required data | Longitudinal queue events, timestamps, specialty, capacity/scheduling data, attendance outcomes, referral status, priority and historical management interventions. |
| Expected publications | Queueing/simulation model of SUS regulation; hybrid ML-simulation policy evaluation; scenario-based decision-support paper. |
| Novelty score | 9 |
| Feasibility score | 7 |
| Impact on SUS | 9 |
| UFSC CS PhD fit | 10 |

## 3. Fairness-Aware Prioritization Support for SUS Waiting Lists

| Field | Description |
|---|---|
| Title | Fairness-Aware Prioritization Support for SUS Waiting Lists |
| Research question | How can prioritization-support models for SUS waiting lists be evaluated and constrained to avoid reinforcing access inequities? |
| Hypothesis | Historical waiting-list data contain systematic differences in delay, scheduling probability and model error across geography, referral origin, age, sex, priority and vulnerability proxies; fairness-aware evaluation can identify safer prioritization-support strategies. |
| Methodology | Define fairness metrics for waiting-list access; audit historical delays and model performance by subgroup; develop prioritization-support models with fairness constraints or post-processing; simulate queue impact on mean wait, tail wait and subgroup disparities; frame outputs as human-in-the-loop decision support. |
| Required data | Queue events, demographics, municipality/neighborhood, referral origin, priority, specialty, waiting time, outcome status, attendance and vulnerability proxies if ethically approved. |
| Expected publications | Fairness audit of SUS waiting-list access; fairness-aware prioritization-support model; simulation of equity impact under alternative prioritization rules. |
| Novelty score | 10 |
| Feasibility score | 6 |
| Impact on SUS | 10 |
| UFSC CS PhD fit | 9 |

## 4. Stale-Demand and Data-Quality Intelligence for SUS Waiting Lists

| Field | Description |
|---|---|
| Title | Stale-Demand and Data-Quality Intelligence for SUS Waiting Lists |
| Research question | Can computational methods identify obsolete, inconsistent or low-validity records that distort SUS waiting-list size and waiting-time estimates? |
| Hypothesis | A meaningful fraction of waiting-list backlog is explained by stale, duplicated, unreachable or clinically changed demand, and these cases can be detected from event history, contact patterns and referral metadata. |
| Methodology | Define data-quality indicators; classify exit reasons and stale-list outcomes; develop weakly supervised or supervised models for stale-demand risk; estimate how stale records distort backlog and waiting-time metrics; propose cleanup-prioritization rules for managers. |
| Required data | Waiting-list records, update/contact attempts, cancellation/removal reasons, duplicate identifiers, referral date, current status, scheduling/attendance outcomes and specialty. |
| Expected publications | Data-quality taxonomy for waiting lists; stale-demand prediction model; operational evaluation of list-cleanup prioritization. |
| Novelty score | 8 |
| Feasibility score | 9 |
| Impact on SUS | 9 |
| UFSC CS PhD fit | 8 |

## 5. Referral Adequacy and Demand-Redirection Prediction for Specialized Care

| Field | Description |
|---|---|
| Title | Referral Adequacy and Demand-Redirection Prediction for Specialized Care |
| Research question | Can regulation data predict which referrals are likely to be resolved, redirected, rejected or require specialized care? |
| Hypothesis | Structured referral characteristics and historical regulation decisions can predict referral adequacy and demand-redirection outcomes, supporting telehealth/gatekeeping and reducing avoidable specialty queue growth. |
| Methodology | Build referral-outcome taxonomy; model referral decision outcomes; compare structured-only and text-enhanced models if referral descriptions are available; explain drivers of redirection/rejection; evaluate specialty-specific performance and false-negative safety risks. |
| Required data | Referral request data, specialty/procedure, clinical priority, referral origin, regulator decision, rejection/redirection reason, telehealth opinion if available, scheduling and final outcome. |
| Expected publications | Referral-outcome taxonomy and descriptive analysis; ML/XAI model for referral adequacy; decision-support evaluation for gatekeeping workflows. |
| Novelty score | 8 |
| Feasibility score | 7 |
| Impact on SUS | 10 |
| UFSC CS PhD fit | 9 |

## 6. Event-Level Data Model and Benchmark for SUS Waiting-List Dynamics

| Field | Description |
|---|---|
| Title | Event-Level Data Model and Benchmark for SUS Waiting-List Dynamics |
| Research question | What event-level data representation is needed to reproducibly model waiting-list dynamics in SUS regulation systems? |
| Hypothesis | A standardized event schema with states, transitions, timestamps, outcomes and queue contexts will improve reproducibility and allow multiple predictive, queueing and fairness tasks to be benchmarked. |
| Methodology | Map real regulation workflows; define a state-transition model for referrals and waiting-list events; create derived features and outcomes; propose benchmark tasks such as excessive-wait prediction, stale-demand detection and bottleneck forecasting; evaluate baseline models. |
| Required data | Regulation system exports, event logs, timestamps, status codes, referral metadata, specialty, priority, scheduling and outcome fields. |
| Expected publications | Event schema and benchmark tasks; baseline predictive modeling paper; reproducibility/data-engineering paper for public-health regulation systems. |
| Novelty score | 8 |
| Feasibility score | 8 |
| Impact on SUS | 8 |
| UFSC CS PhD fit | 9 |

## 7. Resource-Allocation Scenario Optimizer for Specialized Outpatient Capacity

| Field | Description |
|---|---|
| Title | Resource-Allocation Scenario Optimizer for Specialized Outpatient Capacity |
| Research question | How can constrained optimization support transparent allocation of specialized outpatient capacity across services, specialties or municipalities? |
| Hypothesis | Scenario-based constrained optimization can reduce tail waiting times and backlog while preserving explicit fairness and priority constraints. |
| Methodology | Define decision variables such as appointment slots, specialty capacity, telehealth review capacity and cleanup campaigns; formulate constraints from capacity, priority and service rules; optimize objectives such as maximum wait, backlog, equity and resource use; compare scenarios retrospectively. |
| Required data | Queue size, demand arrivals, service capacity, appointment availability, specialty/procedure, priority, geography, attendance/no-show and historical allocation decisions. |
| Expected publications | Optimization formulation for SUS specialized access; scenario evaluation paper; fairness/constraint sensitivity analysis. |
| Novelty score | 8 |
| Feasibility score | 5 |
| Impact on SUS | 10 |
| UFSC CS PhD fit | 10 |

## 8. Multi-Specialty Bottleneck Detection and Capacity Stress Forecasting

| Field | Description |
|---|---|
| Title | Multi-Specialty Bottleneck Detection and Capacity Stress Forecasting in SUS Specialized Care |
| Research question | Can multi-specialty queue data forecast bottlenecks and capacity stress before waiting times become critical? |
| Hypothesis | Specialty-specific inflow, outflow, backlog, no-show and service-rate patterns can predict future queue stress and identify early-warning signals for managers. |
| Methodology | Build time-series and panel models by specialty/municipality; define bottleneck indicators; train forecasting models; compare statistical, ML and queueing-derived features; create explainable early-warning outputs. |
| Required data | Weekly/monthly inflows, outflows, queue size, appointment slots, specialty, procedure, priority, municipality, attendance and cancellation data. |
| Expected publications | Descriptive bottleneck taxonomy; forecasting model for specialty queue stress; early-warning decision-support paper. |
| Novelty score | 7 |
| Feasibility score | 8 |
| Impact on SUS | 9 |
| UFSC CS PhD fit | 8 |

## 9. Human-in-the-Loop Regulation Decision Support with Auditability

| Field | Description |
|---|---|
| Title | Human-in-the-Loop Regulation Decision Support with Auditability |
| Research question | How can AI-based waiting-list recommendations be designed to support, document and audit human regulation decisions? |
| Hypothesis | Human-in-the-loop decision support with explanations and audit trails can improve consistency and transparency of regulation decisions without automating access decisions. |
| Methodology | Design a DSS prototype or offline decision-support mockup; define recommendation types; implement explanation and audit logs; evaluate with retrospective cases and regulator/manager feedback; measure usability, perceived trust and decision consistency. |
| Required data | Retrospective regulation cases, decision outcomes, queue context, referral metadata and access to regulators/managers for structured evaluation. |
| Expected publications | Human-in-the-loop DSS design paper; evaluation with regulation professionals; auditability/explainability framework paper. |
| Novelty score | 8 |
| Feasibility score | 6 |
| Impact on SUS | 9 |
| UFSC CS PhD fit | 9 |

## 10. Time-to-Care Survival Modeling for Specialized Outpatient Access

| Field | Description |
|---|---|
| Title | Time-to-Care Survival Modeling for Specialized Outpatient Access |
| Research question | Can survival models better characterize time-to-scheduling and time-to-care in SUS waiting lists than average waiting-time metrics? |
| Hypothesis | Time-to-event modeling captures censoring, competing exits and specialty heterogeneity more appropriately than mean/median waiting-time summaries. |
| Methodology | Define time origins and event types; model scheduling, attendance, cancellation, rejection and no-contact as competing risks; evaluate Cox, random survival forests and gradient boosting survival models; produce interpretable risk profiles. |
| Required data | Referral date, status transitions, scheduling date, attendance date, cancellation/removal dates, exit reasons, specialty, priority and demographics/geography. |
| Expected publications | Survival analysis of SUS specialized access; competing-risk predictive model; methodological comparison of waiting-time metrics. |
| Novelty score | 7 |
| Feasibility score | 9 |
| Impact on SUS | 8 |
| UFSC CS PhD fit | 8 |

## 11. Offline Policy Evaluation for Waiting-List Prioritization Rules

| Field | Description |
|---|---|
| Title | Offline Policy Evaluation for Waiting-List Prioritization Rules |
| Research question | Can historical regulation data be used to safely compare alternative prioritization rules before implementation? |
| Hypothesis | Offline policy evaluation and counterfactual simulation can identify prioritization policies that reduce long waits or inequities without requiring risky prospective deployment. |
| Methodology | Reconstruct historical decision policies; define candidate policies; use causal inference, inverse propensity weighting, doubly robust estimation or simulation where assumptions permit; evaluate wait-time and fairness outcomes. |
| Required data | Detailed historical prioritization decisions, queue states at decision time, available capacity, outcomes, priority criteria and potential confounders. |
| Expected publications | Offline policy evaluation framework; counterfactual prioritization analysis; methodological paper on safe evaluation of public-health queue policies. |
| Novelty score | 9 |
| Feasibility score | 5 |
| Impact on SUS | 8 |
| UFSC CS PhD fit | 10 |

## 12. Natural Language Processing of Referral Requests for Regulation Support

| Field | Description |
|---|---|
| Title | Natural Language Processing of Referral Requests for Regulation Support |
| Research question | Can free-text referral descriptions improve prediction of priority, adequacy, specialty need and delay risk in SUS regulation? |
| Hypothesis | Referral text contains clinically and operationally useful signals not captured in structured fields, and NLP representations can improve regulation-support models if privacy and data quality are handled carefully. |
| Methodology | De-identify referral text; build text classification and representation models; compare structured-only, text-only and multimodal models; explain relevant terms/concepts; evaluate performance by specialty and subgroup. |
| Required data | Referral free text, structured referral fields, specialty, priority, regulator decisions, outcomes, timestamps and de-identification pipeline. |
| Expected publications | NLP dataset characterization; referral-text classification model; structured-plus-text decision-support paper. |
| Novelty score | 8 |
| Feasibility score | 6 |
| Impact on SUS | 8 |
| UFSC CS PhD fit | 9 |

## 13. Telehealth Referral-Management Analytics for Queue Impact Assessment

| Field | Description |
|---|---|
| Title | Telehealth Referral-Management Analytics for Queue Impact Assessment |
| Research question | How does telehealth-supported regulation change waiting-list dynamics across specialties, localities and priority groups? |
| Hypothesis | Telehealth/gatekeeping reduces avoidable demand and waiting-list growth unevenly across specialties, and queue analytics can identify where it creates the greatest system value. |
| Methodology | Conduct retrospective interrupted time-series or difference-in-differences where possible; model specialty-level changes in inflow, outflow, waiting time, backlog and redirection; estimate cost/access implications; add explainable subgroup analyses. |
| Required data | Telehealth review records, referral system data, waiting-list measures, specialty, locality, priority, costs if available and pre/post intervention periods. |
| Expected publications | Queue-impact evaluation of telehealth regulation; specialty heterogeneity analysis; cost/access decision-support paper. |
| Novelty score | 7 |
| Feasibility score | 7 |
| Impact on SUS | 9 |
| UFSC CS PhD fit | 8 |

## 14. No-Show, Dropout and Queue-Attrition Prediction in Specialized Care

| Field | Description |
|---|---|
| Title | No-Show, Dropout and Queue-Attrition Prediction in Specialized Care |
| Research question | Can waiting-list data predict which scheduled patients are likely to miss appointments, drop out or become unreachable? |
| Hypothesis | Appointment history, waiting time, referral source, geography and queue status can predict attrition risk and help reduce wasted capacity. |
| Methodology | Define no-show, dropout, unreachable and cancellation outcomes; train calibrated risk models; evaluate by specialty and subgroup; simulate targeted confirmation or overbooking strategies cautiously. |
| Required data | Appointments, attendance, cancellations, contact attempts, waiting time, patient geography, specialty, referral origin and prior no-show history if available. |
| Expected publications | Attrition/no-show prediction paper; intervention simulation paper; fairness audit of no-show risk models. |
| Novelty score | 7 |
| Feasibility score | 8 |
| Impact on SUS | 8 |
| UFSC CS PhD fit | 8 |

## 15. Interoperability-Aware Regulation Data Pipeline for Cross-Region Waiting-List Analytics

| Field | Description |
|---|---|
| Title | Interoperability-Aware Regulation Data Pipeline for Cross-Region Waiting-List Analytics |
| Research question | How can heterogeneous SUS regulation data be mapped into a common analytical layer for cross-region waiting-list modeling? |
| Hypothesis | A lightweight interoperability-aware pipeline can preserve local system differences while enabling comparable waiting-list indicators, models and fairness analyses. |
| Methodology | Map source systems and status codes; define common data model; implement ETL and validation rules; evaluate portability across specialties or regions; generate comparable indicators and baseline models. |
| Required data | Exports from one or more regulation systems, status dictionaries, procedure/specialty codes, timestamps, priority labels and local workflow documentation. |
| Expected publications | Common data model/pipeline paper; cross-region indicator comparison; reproducibility framework for regulation analytics. |
| Novelty score | 7 |
| Feasibility score | 7 |
| Impact on SUS | 8 |
| UFSC CS PhD fit | 9 |

## Top 5 Most Promising Projects

| Position | Project | Why it is in the Top 5 |
|---:|---|---|
| 1 | Explainable Decision Support for Problematic Waiting-List Behavior in SUS Regulation Workflows | Best balance of novelty, feasibility, SUS impact and Computer Science fit. It can absorb ML, XAI, survival analysis and DSS without overexpanding. |
| 2 | Hybrid Machine Learning and Queueing Simulation for Specialized-Care Regulation Policies | Strong CS/OR contribution and excellent publication potential, but requires richer capacity/event data and careful validation. |
| 3 | Fairness-Aware Prioritization Support for SUS Waiting Lists | Very high novelty and social relevance, but feasibility depends on having adequate demographic/geographic/vulnerability data and ethical framing. |
| 4 | Stale-Demand and Data-Quality Intelligence for SUS Waiting Lists | Highly feasible and practically valuable; excellent first-paper candidate. Slightly less ambitious as a full thesis unless integrated into a broader DSS. |
| 5 | Referral Adequacy and Demand-Redirection Prediction for Specialized Care | Very aligned with SUS referral management and telehealth evidence; strong if referral outcomes and regulator decisions are available. |

## Single Best Project

### Recommended project

**Explainable Decision Support for Problematic Waiting-List Behavior in SUS Regulation Workflows**

### Why this is the best single project

| Criterion | Assessment |
|---|---|
| Scientific novelty | High. The literature has waiting-list management, queueing, ML and telehealth separately, but not a mature explainable decision-support framework for SUS regulation workflows. |
| Publication potential | High. It can generate at least three papers: data model/outcome taxonomy, predictive/XAI modeling, and retrospective DSS/queue-impact evaluation. |
| Feasibility in 4 years | High if event-level regulation data are available from at least one system or municipality/region. It does not require prospective deployment to be publishable. |
| Availability of SUS data | Realistic. It can start with retrospective regulation exports and scale only if more data become available. |
| Alignment with AI | Strong through predictive modeling, explainability, calibration and uncertainty. |
| Alignment with Health Informatics | Strong through regulation data, access workflows, decision support and information-system relevance. |
| Alignment with Operations Research | Strong if queue-state features and scenario evaluation are included, without making the whole thesis depend on complex optimization. |
| Alignment with Computer Science | Very strong. It combines data modeling, ML, XAI, decision-support systems, evaluation metrics and possibly simulation. |

### Recommended thesis formulation

**Core thesis problem**

How can event-level SUS regulation data be transformed into explainable decision support for identifying and managing problematic waiting-list behavior in specialized outpatient care?

**Core contribution**

A reproducible computational framework that models waiting-list states, predicts problematic queue behavior, explains drivers of risk and supports managers with actionable, auditable evidence.

**Why it beats the alternatives**

It is broader and more publishable than stale-demand detection alone, more feasible than full optimization, safer than automatic prioritization, more Computer Science-oriented than telehealth evaluation, and more operationally relevant than isolated waiting-time prediction.

