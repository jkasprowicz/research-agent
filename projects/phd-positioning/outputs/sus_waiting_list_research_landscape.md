# SUS Waiting-List Research Landscape

## Executive Verdict

The SUS waiting-list direction is a serious doctoral alternative. It may have **stronger admission and practical potential** than the current laboratory-medicine proposal if the potential advisor can provide or broker access to real event-level regulation data. Its strongest form is not a generic project on "predicting waiting time"; it is a Computer Science project on **explainable, predictive, and decision-oriented modeling of waiting-list dynamics in a universal public health system**.

The direction is strategically attractive because waiting lists are a visible, high-priority SUS problem; they involve dynamic queues, constrained capacity, prioritization, equity, no-shows, cancellations, service heterogeneity, and managerial decision-making. These are naturally computational problems involving machine learning, operations research, simulation, optimization, explainability, and decision support.

However, this direction only becomes stronger than the hematology-oriented plan under one condition: **access to real, longitudinal, event-level waiting-list data must be realistic**. Without that data, the project becomes either descriptive health-management research or a generic ML proof of concept. With that data, it can become a stronger PPGCC/UFSC admission topic than hematology because it aligns broadly with Computational Intelligence, AI for health, decision support, and public-sector impact while avoiding the unverified multimodal-image linkage risk identified in the LEAC feasibility assessment.

## Bottom-Line Comparison

| Dimension | SUS waiting-list direction | Hematology laboratory-medicine direction | Strategic judgment |
|---|---|---|---|
| Scientific novelty | High if framed as dynamic, explainable, workflow-aware queue intelligence for SUS regulation; moderate if reduced to wait-time prediction | Moderate-high after repositioning toward workflow-aware laboratory decision support; low if perceived as image classification extension | SUS has broader novelty if data access is real |
| Publication potential | High across health informatics, healthcare operations, OR, DSS, public health informatics, applied ML | High but narrower; stronger in laboratory AI and digital hematology | SUS offers more venue diversity |
| Practical impact | Very high: access to care, equity, resource allocation, management transparency | High but narrower: laboratory workflow, hematology triage, diagnostic support | SUS likely has larger public-system impact |
| Feasibility | Strong only with event-level regulation data; weak without it | Structured lab data already documented; multimodal morphology linkage not verified | Both depend on data, but SUS feasibility is binary |
| Continuity with candidate trajectory | Weaker thematic continuity; stronger continuity with health informatics, data science, healthcare management | Stronger continuity with master's, publication, biomedical-lab identity | Hematology preserves identity better |
| Alignment with Computer Science | Very strong if using ML + OR + simulation + XAI + DSS | Strong if framed around robust/interpretable ML and workflow decision support | SUS may look more classically computational if positioned well |
| Advisor alignment | Potentially very strong if the advisor suggested it; likely aligns with AI for health, domain-specific ML, decision support | Strong with Jônata; alternative with Renato | SUS may improve advisor buy-in |
| Admission probability | Potentially higher if the advisor is enthusiastic and data access is plausible | Strong but may appear niche and dependent on local lab data | SUS could be the safer admission bet if data path is credible |

**Decision:** do not abandon hematology yet, but treat SUS waiting lists as a top-tier competing direction. It should move ahead only if, before proposal rewriting, there is a concrete data-access path involving event-level records from a regulation system, municipal/state queue platform, SISREG/e-SUS Regulação, or a partner health department.

## 1. Scientific Landscape

### 1.1 SUS waiting lists as a health-system problem

In the SUS context, waiting lists are not simple FIFO queues. Official regulation guidance describes the waiting list as a dynamic management object: requests enter the queue, receive risk classification and prioritization, may be reclassified, may be returned to the requesting unit, may be scheduled, missed, cancelled, denied, fulfilled, or transferred. The Brazilian Ministry of Health's e-SUS Regulação model includes event-relevant fields such as request status, procedure code, request date, authorization date, execution date, patient identifier, requesting establishment, regulating establishment, executing establishment, modality, urgency/elective character, and clinical reason.

This makes the computational object richer than a "line": it is a **state-transition system under capacity constraints**. The real problem is not only estimating how long a patient will wait. It is understanding which queues are becoming problematic, which service characteristics explain bottlenecks, which requests are likely to stagnate or be returned, which priorities are not being served in time, and which managerial interventions may reduce delay or inequity.

Recent Brazilian discussion in *Cadernos de Saúde Pública* frames specialized outpatient waiting lists as a critical SUS concept and emphasizes monitoring, transparency, coordination, and the need to know who is waiting, why they are waiting, how long they have waited, and what care can be offered while they wait. This is important because it suggests a clear gap between policy/management needs and computational tooling.

### 1.2 Queue modeling and operations research

The mature international literature includes queueing theory, discrete-event simulation, appointment scheduling, capacity planning, elective-surgery prioritization, resource allocation, and operations management. This area is not new. What is scientifically alive is the move from static queue models toward **data-driven, adaptive, explainable, and policy-aware systems**.

Discrete-event simulation is widely used in healthcare because patient flow is dynamic, stochastic, and constrained by multiple resources. Reviews of healthcare DES show frequent use in emergency departments, outpatient clinics, staffing, scheduling, and patient-flow redesign. The open problem for SUS is not whether simulation works in abstract healthcare settings; it is how to use real regulation data to create models that reflect local service networks, heterogeneous procedures, municipal/state governance, and equity requirements.

### 1.3 Machine learning and predictive analytics

Machine learning in patient flow commonly targets admissions, emergency-department demand, length of stay, bottlenecks, wait times, no-shows, and resource needs. In waiting-list management, ML can predict:

- waiting time or probability of excessive wait;
- probability of no-show, cancellation, return, or loss to follow-up;
- probability of clinical worsening or high-risk pathway, when outcomes exist;
- queue stagnation, bottleneck formation, or service saturation;
- mismatch between requested procedure, specialty, priority, and available capacity.

The risk is that many ML papers stop at predictive performance. For a PhD, the stronger contribution would be to connect prediction to **managerial action**: which queue should be inspected, which procedure group needs capacity adjustment, which requests should be requalified, and what trade-offs occur under different prioritization policies.

### 1.4 Explainable AI and decision support

Waiting-list decisions affect access, equity, and public trust. Therefore, black-box prediction alone is strategically weak. Explainability matters at three levels:

- **Case-level explanation:** why a request is predicted to wait too long, be returned, or miss the target time.
- **Queue-level explanation:** which service characteristics, regions, specialties, or capacity patterns explain bottlenecks.
- **Policy-level explanation:** what would likely happen if slots, prioritization rules, quotas, or referral protocols changed.

The best Computer Science framing is therefore not "XAI for healthcare" generically. It is **explainable healthcare operations intelligence**: models that make queue dynamics understandable to managers and regulators while preserving auditable decision logic.

### 1.5 Brazilian evidence base

The Brazilian literature appears more concentrated in health policy, regulation, referral management, telehealth-mediated referral support, transparency, access, and descriptive queue studies than in advanced ML/OR decision-support systems for waiting-list dynamics.

Gadenz et al. (2021) provide a strong Brazilian anchor: a before-and-after study of telehealth-supported referral management in SUS specialized care, using 17 waiting lists and 124,869 cases. Waiting-list size decreased across localities after the intervention, with baseline median waiting times in the range of 159 to 241 days and reductions in some settings after six months. This shows that real waiting-list datasets exist, that queue interventions can be evaluated, and that referral management is measurable.

The Ministry of Health's current policy context also supports relevance. The Programa Nacional de Redução das Filas was created to expand access to elective surgeries, complementary exams, and specialized consultations, and from 2025 it is incorporated into PMAE's surgery component. The Ministry also emphasizes interoperability, RNDS sharing, e-SUS Captação de Filas, and decision support for reducing waiting times. This creates a favorable policy moment for computational research.

## 2. Main Research Areas Involved

| Area | Role in the topic | Mature parts | Open parts |
|---|---|---|---|
| Queue modeling | Formalizes demand, service rates, waiting times, prioritization, backlog, capacity | Classical queueing and DES are mature | SUS-specific dynamic queues with priority, return, reclassification, regional capacity, and equity are underdeveloped |
| Operations research | Supports capacity planning, appointment allocation, surgical prioritization, what-if simulation | Scheduling and elective surgery OR are established | Integration with real public regulation data and interpretable ML remains open |
| Healthcare management | Defines governance, regulation workflows, access, equity, transparency | Strong policy/management literature in SUS | Limited computational translation into actionable DSS |
| Machine learning | Predicts wait, no-show, cancellation, excessive wait, queue risk, service demand | ML patient-flow literature is active | Often disconnected from managerial action and external validation |
| Predictive analytics | Converts historical queue behavior into risk forecasts | Common in ED and hospital flow | Less mature for SUS outpatient/specialized-care regulation |
| Explainable AI | Makes predictions auditable and acceptable | General XAI literature is mature | Manager-facing explanations for queue operations are less developed |
| Decision support systems | Turns models into dashboards, alerts, prioritization support, and policy simulation | HIS and referral systems exist | Few rigorous AI/OR decision-support frameworks for SUS waiting-list governance |
| Fairness and access analytics | Evaluates whether allocation rules preserve equity | Fair ML is a mature research area | Operational fairness for public waiting lists remains sensitive and underexplored |

## 3. Current State of the Art

### 3.1 What is already solved

The following should not be claimed as novel:

- Describing that SUS waiting lists are long and fragmented.
- Showing that waiting time is a relevant access indicator.
- Building a simple dashboard of queue counts.
- Applying a generic regression/classification model to predict wait time.
- Using standard SHAP plots without operational interpretation.
- Proposing "AI for queue management" without a concrete decision point.
- Showing that capacity affects waiting time.
- Using simulation to show that increasing capacity reduces waiting.

### 3.2 Active international directions

The strongest international directions are:

- dynamic priority scoring for elective surgery;
- patient prioritization tools for non-emergency care;
- ML-assisted patient flow prediction;
- discrete-event simulation for healthcare operations;
- hybrid ML + simulation approaches;
- appointment scheduling and no-show-aware capacity planning;
- fairness-aware prioritization;
- transparent decision support for operations managers.

Powers et al. (2023), for example, propose dynamic priority scoring for elective surgery patients using waiting time and clinical factors, with simulation suggesting improved equity, transparency, and consistency. This is directly relevant because it shows a mature OR-style model of waiting-list management, but not in the SUS context.

Rathnayake et al. (2021) systematically reviewed patient-prioritization methods for elective surgery and highlight the broad range and inconsistency of prioritization methods. This supports a PhD gap around transparent, evidence-based, data-driven prioritization and monitoring.

### 3.3 Active Brazilian directions

Brazilian work is strong in:

- conceptual and policy analysis of waiting lists;
- referral regulation and specialized outpatient access;
- telehealth-supported referral management;
- transparency and monitoring;
- descriptive studies of waiting times and returned requests;
- official standardization efforts around e-SUS Regulação and MIRA.

Brazilian work appears weaker in:

- predictive modeling of queue behavior using individual request-level data;
- dynamic state-transition modeling of waiting-list records;
- explainable ML for managers;
- simulation of interventions using real regulation data;
- comparison of prioritization policies under fairness and efficiency metrics;
- integration of service capacity, request characteristics, and patient-flow outcomes.

This asymmetry is the opportunity.

## 4. Open Problems

### 4.1 Waiting lists are dynamic event processes, not static tables

Many analyses treat waiting lists as snapshots: number waiting, median wait, or average delay. The stronger computational formulation is longitudinal: requests move through statuses such as pending, authorized, scheduled, attended, no-show, cancelled, denied, excluded, returned, or transferred. Modeling these transitions can reveal behavior that static summaries hide.

### 4.2 Prioritization is not the same as prediction

Predicting who will wait longer is useful, but the managerial question is what action should be taken. A PhD contribution could distinguish prediction from prioritization, triage, capacity reallocation, and intervention planning.

### 4.3 Explainability must be operational

A queue manager does not need a generic feature-importance plot. They need explanations such as: which procedures are generating avoidable returns, which requesting units have high rework, which specialties are violating target times for priority groups, and which service-capacity patterns explain backlog accumulation.

### 4.4 Fairness and transparency are central, not optional

The SUS context requires equity. A model that optimizes average waiting time may worsen access for vulnerable groups or low-priority-but-long-waiting patients. A strong proposal should evaluate both efficiency and equity.

### 4.5 Data quality and interoperability are scientific problems

Official sources acknowledge the importance of interoperable regulation systems, RNDS sharing, and e-SUS Captação de Filas. For research, this means missingness, inconsistent procedure naming, local workflow variation, status semantics, duplicated requests, and policy changes are not just nuisances. They are part of the computational problem.

### 4.6 Intervention evaluation is hard

Waiting-list policies change over time, and external events can alter demand or supply. The Gadenz et al. study noted limitations related to lack of multiple pre-intervention time points and concurrent policy changes. This supports methodological contributions around temporal validation, interrupted time series when possible, counterfactual simulation, and careful avoidance of causal overclaiming.

## 5. Possible PhD Directions

### Direction 1: Explainable predictive modeling of problematic waiting-list behavior

**Core idea:** predict and explain requests, queues, or services at risk of problematic behavior, such as excessive waiting, repeated return, cancellation, no-show, stagnation, or priority-time violation.

**Computational kernel:** supervised learning, survival analysis, sequence modeling, temporal validation, calibration, explainable ML, subgroup analysis.

**Data required:** request-level records with timestamps, statuses, procedure/specialty, priority, requesting unit, executing unit, patient demographics, and final outcome.

**Publication potential:** high. Could yield papers on feature engineering for queue events, interpretable prediction of excessive wait, and operational explanation.

**Risk:** if framed only as wait-time prediction, it becomes incremental. The endpoint must be managerial risk and queue behavior.

### Direction 2: Hybrid ML + simulation decision support for SUS queue management

**Core idea:** combine predictive models with discrete-event simulation or queue simulation to test what-if scenarios for capacity allocation, priority rules, scheduling policies, and referral requalification.

**Computational kernel:** ML demand/wait/no-show models, DES, policy simulation, sensitivity analysis, optimization, decision support.

**Data required:** event-level queue records plus capacity or slot information by procedure/service/time period.

**Publication potential:** very high if real data are available. This is likely the strongest Computer Science direction.

**Risk:** requires capacity data, which may be harder to obtain than request records.

### Direction 3: Fairness-aware prioritization and transparency for public waiting lists

**Core idea:** evaluate and design prioritization models that balance clinical priority, waiting time, vulnerability, geography, service capacity, and transparency.

**Computational kernel:** ranking models, fairness metrics, multi-objective optimization, interpretable scoring, policy simulation.

**Data required:** priority/risk fields, demographic or territorial variables, waiting outcomes, procedure groups, and ideally protocol information.

**Publication potential:** high and socially relevant.

**Risk:** ethically and politically sensitive. Must avoid appearing to automate clinical priority decisions without governance.

### Direction 4: Detection of bottlenecks and anomalous queue dynamics

**Core idea:** identify services, regions, procedure groups, or request pathways with abnormal accumulation, return, rework, no-show, or delay patterns.

**Computational kernel:** time-series anomaly detection, process mining, clustering, graph/network analysis, interpretable dashboards.

**Data required:** timestamps, statuses, locations/units, procedure groups, flow transitions.

**Publication potential:** moderate-high. Strong as a first study because it can be done with less labeling.

**Risk:** could become descriptive unless linked to methodological novelty and decision support.

### Direction 5: Knowledge-grounded decision support for regulation workflows

**Core idea:** combine structured queue data with regulation protocols, procedure taxonomies, service capacity, and explanatory rules to support managers in understanding queue states and possible actions.

**Computational kernel:** knowledge graphs, rule-based constraints, retrieval over protocols, interpretable ML, decision-support interfaces.

**Data required:** queue records plus protocols, procedure mappings, and service metadata.

**Publication potential:** high if paired with Renato Fileto-style data integration/semantic enrichment; moderate if only conceptual.

**Risk:** may drift into generic knowledge-graph/LLM hype. Should remain grounded in queue decisions.

## 6. Strongest PhD Positioning If This Direction Advances

The strongest positioning is:

**Explainable and data-driven decision support for dynamic waiting-list management in the SUS.**

A sharper version:

**Explainable predictive and simulation-based models for detecting problematic queue behavior and supporting waiting-list management in the SUS.**

What this should mean:

- The unit of analysis is the regulation request, queue, service, or specialty over time.
- The task is not simply predicting a number of waiting days.
- The contribution is modeling queue dynamics, risk, prioritization, and management-relevant explanations.
- The output supports managers, not autonomous clinical decisions.
- The evaluation includes predictive performance, calibration, temporal robustness, interpretability, and operational utility.

## 7. Minimum Viable Doctoral Program

This should remain a research direction, not yet a proposal. But if it becomes the chosen path, a coherent PhD could contain:

### Study 1: Landscape and data model

Map waiting-list workflows and define a computational event model for SUS regulation records.

**Output:** taxonomy of queue events, status transitions, endpoints, data-quality issues, and candidate prediction/decision tasks.

### Study 2: Predictive modeling of problematic queue behavior

Develop temporally validated models for excessive waiting, return, cancellation/no-show, or priority-time violation.

**Output:** interpretable predictive models and calibrated risk estimates.

### Study 3: Queue-level explanation and bottleneck detection

Identify service characteristics and queue dynamics associated with backlog, rework, inequity, or unstable demand.

**Output:** queue phenotypes, bottleneck profiles, and manager-facing explanations.

### Study 4: Decision-support simulation

Use ML-informed simulation to compare capacity, prioritization, or referral-management scenarios.

**Output:** what-if analysis framework with efficiency and equity metrics.

This sequence is more coherent than jumping directly to an "AI platform."

## 8. Data Requirements

### Minimum dataset

- unique request identifier;
- patient pseudonymized identifier;
- request date and time;
- authorization date and time;
- scheduling date and time;
- execution/attendance date and time;
- request status history;
- status transition timestamps;
- procedure code, preferably SIGTAP;
- specialty or service;
- clinical priority or risk category;
- elective/urgent character;
- requesting establishment;
- regulating establishment;
- executing establishment;
- municipality/region;
- patient age and sex;
- no-show, cancellation, denial, return, exclusion, attended outcome.

### Strong dataset

- full event log, not only current status;
- capacity/slot availability by procedure/service/time;
- referral text or structured clinical reason;
- protocol/rule applied;
- reason for return or denial;
- rescheduling history;
- patient territorial vulnerability variables;
- outcomes after waiting, when available;
- policy/intervention timestamps.

### Critical feasibility question

Before rewriting the doctoral proposal, one must answer:

**Can the advisor or partner institution provide event-level records with timestamps and status transitions, not just aggregated queue counts?**

If yes, the direction is strong. If no, it is too risky for admission unless reformulated as a methodological project using public/aggregated data plus a simulated case study, which would be much weaker.

## 9. Ethics and Governance

Ethics complexity is moderate to high. The study can likely be retrospective and observational, but it involves sensitive health-access records and potentially identifiable patient trajectories. It will require:

- CEP/CONEP evaluation depending on data source and scope;
- LGPD-compliant anonymization or pseudonymization;
- data-use agreement with the health department, municipality, state, or partner institution;
- clear separation between research modeling and operational decision authority;
- explicit governance language preventing automated denial or deprioritization of care;
- fairness monitoring to avoid reinforcing existing inequities.

Ethically, this direction is defensible if framed as **managerial support and transparency**, not replacement of clinical/regulatory judgment.

## 10. Fit With PPGCC/UFSC

### Alignment with Computational Intelligence

Strong, if framed around:

- machine learning for dynamic healthcare operations;
- temporal prediction;
- explainable AI;
- robust evaluation under temporal drift;
- decision-support systems;
- simulation and optimization;
- domain-specific AI for health.

This likely fits the Jônata Tyska Carvalho axis well, especially if the meeting itself generated the direction.

### Alignment with Database / Renato Fileto alternative

Also strong if framed around:

- integration and semantic enrichment of complex health data;
- event logs and process-aware analytics;
- knowledge graphs for regulation protocols and procedure taxonomies;
- classification/prediction over complex data;
- LLMs only as auxiliary retrieval/explanation tools, not as the thesis core.

### Risk of seeming outside Computer Science

The main risk is that the topic sounds like health policy or public administration. The proposal must explicitly center the computational object:

- queue event modeling;
- predictive models;
- simulation;
- decision-support logic;
- explainability;
- fairness metrics;
- temporal validation.

## 11. Comparison Against the Hematology Proposal

### Where SUS is stronger

SUS waiting lists are stronger if:

- advisor enthusiasm is real;
- data access is plausible;
- the project uses queue dynamics and decision support, not descriptive statistics;
- the proposal targets a public-system problem with clear computational methods;
- the admission committee values broad impact and fit with the advisor's current interest.

Compared with hematology, SUS has:

- broader societal impact;
- clearer public-policy urgency;
- wider publication venue options;
- stronger natural connection to operations research and DSS;
- less dependence on image datasets and domain-specific morphology linkage;
- stronger potential for manager-facing explainable AI.

### Where hematology is stronger

Hematology remains stronger if:

- personal scientific continuity is weighted heavily;
- the committee values the candidate's existing publication trajectory;
- data access for SUS is uncertain;
- the advisor does not already have a partner/data channel;
- the candidate wants to build a long-term niche in laboratory AI.

Compared with SUS, hematology has:

- stronger continuity from the master's;
- stronger candidate-specific differentiation;
- existing technical infrastructure;
- a clearer biomedical-laboratory identity;
- lower risk of becoming generic health-services analytics.

### Critical distinction

The hematology proposal is **identity-strong but data-fragile in its multimodal layer**.

The SUS proposal is **impact-strong and advisor-promising but data-binary**.

If SUS event-level data are secured, SUS likely becomes the stronger admission strategy. If not, hematology remains safer because there is already documented structured laboratory data and a coherent prior trajectory.

## 12. Topics to Avoid

Do not frame the SUS direction as:

- "an AI system to solve SUS waiting lists";
- a generic waiting-time prediction model;
- a dashboard-only project;
- an LLM/agent project for healthcare management;
- a policy essay with light computation;
- an optimization model disconnected from real data;
- a fairness project without concrete queue decisions;
- a national-scale system unless national data are actually available.

Also avoid promising automated prioritization of patients. The safer language is:

**support for monitoring, explanation, risk identification, scenario analysis, and managerial decision-making.**

## 13. Strategic Recommendation

### Recommended next step

Before rewriting the doctoral proposal, conduct a **data-access feasibility check** with the advisor:

1. What system or institution could provide waiting-list data?
2. Are records event-level or aggregated?
3. Are historical status transitions available?
4. Are procedure codes, priorities, requesting/executing units, timestamps, and outcomes available?
5. Is capacity/slot data available?
6. Is the advisor expecting prediction, simulation, decision support, or all three?
7. Is there institutional support for ethics approval and data-use agreement?

### Decision rule

Move to SUS waiting lists if at least the following are plausible:

- event-level data;
- timestamps for entry and exit/status transitions;
- procedure/specialty/service fields;
- priority/risk field or proxy;
- final status/outcome;
- advisor support;
- realistic ethics route.

Stay with hematology if the SUS data path is vague, aggregate-only, politically blocked, or dependent on uncertain future negotiations.

## 14. Provisional Ranking of Possible Directions

| Rank | Direction | Novelty | Feasibility | Publication potential | Admission strength | Overall |
|---:|---|---|---|---|---|---|
| 1 | Hybrid explainable ML + simulation for SUS waiting-list decision support | Very high | Medium, data-dependent | Very high | Very high | Strongest if data access exists |
| 2 | Explainable prediction of problematic queue behavior | High | High if event data exist | High | High | Best minimum viable SUS topic |
| 3 | Bottleneck/anomaly detection in regulation workflows | Medium-high | High | Medium-high | High | Safest first study |
| 4 | Fairness-aware prioritization and transparency | High | Medium | High | Medium-high | Strong but politically sensitive |
| 5 | Knowledge-grounded regulation decision support | Medium-high | Medium | Medium-high | Medium | Good only if grounded in real protocols/data |

## 15. Final Judgment

The SUS waiting-list direction **can be stronger** than the hematology proposal, but not automatically.

It is stronger for:

- public impact;
- advisor alignment, if this came from the advisor's current interests;
- Computer Science breadth;
- decision-support framing;
- publication venue diversity;
- relevance to current Brazilian health-system priorities.

It is weaker for:

- continuity with the master's;
- candidate-specific scientific identity;
- guaranteed data access;
- avoiding a generic health-management appearance.

The best strategic interpretation is:

**If the advisor can anchor the project in real regulation data, the SUS waiting-list direction should be seriously considered as the new admission-optimized path. If data access remains speculative, the hematology proposal remains the safer path.**

The strongest possible title family would not mention "waiting lists" alone. It should emphasize the computational contribution:

- **Explainable Predictive Models for Waiting-List Dynamics in Public Healthcare Regulation**
- **Data-Driven Decision Support for Dynamic Waiting-List Management in the Brazilian Unified Health System**
- **Explainable Machine Learning and Simulation for Queue Intelligence in Public Healthcare Access**
- **Modeling Problematic Queue Behavior for Decision Support in SUS Regulation Workflows**

## Sources Consulted

- Ministério da Saúde. Programa Nacional de Redução das Filas. https://www.gov.br/saude/pt-br/composicao/saes/agora-tem-especialistas/pnrf/pnrf/
- Ministério da Saúde. Sistemas de Informação na Regulação do Acesso. https://www.gov.br/saude/pt-br/composicao/saes/drac/regulacao/regulacao-do-acesso/sistemas-de-informacao
- Ministério da Saúde. Modelo de Informação - e-SUS Regulação. https://wiki.saude.gov.br/e-SUSREGULACAO/index.php/Modelo_de_Informa%C3%A7%C3%A3o
- Ministério da Saúde. Orientações para Gestão da Fila de Espera. https://wiki.saude.gov.br/regulacao/index.php/Orienta%C3%A7%C3%B5es_para_Gest%C3%A3o_da_Fila_de_Espera
- Gadenz, S. D. et al. Telehealth to support referral management in a universal health system: a before-and-after study. *BMC Health Services Research*, 2021. https://link.springer.com/article/10.1186/s12913-021-07028-5
- Giannotti, E. M., Louvison, M., Chioro, A. Listas de espera na atenção ambulatorial especializada: reflexões sobre um conceito crítico para o Sistema Único de Saúde. *Cadernos de Saúde Pública*, 2025. https://www.scielo.br/j/csp/a/bk43VtWGF5HVrR8h9tMxwwk/
- Rathnayake, D., Clarke, M., Jayasinghe, V. Patient prioritisation methods to shorten waiting times for elective surgery: a systematic review of how to improve access to surgery. *PLOS ONE*, 2021. https://doi.org/10.1371/journal.pone.0256578
- Powers, J. et al. Managing surgical waiting lists through dynamic priority scoring. *Health Care Management Science*, 2023. https://link.springer.com/article/10.1007/s10729-023-09648-1
- El-Bouri, R. et al. Machine learning in patient flow: a review. *Machine Learning: Science and Technology*, 2021. https://doi.org/10.1088/2632-2153/abddc5
- Zhang, X. Discrete-event simulation modeling in healthcare: a comprehensive review. *IEEE Access*, 2021. https://doi.org/10.1109/ACCESS.2021.3123588
- Abuhay, T. M. et al. Machine learning integrated patient flow simulation: why and how? *Journal of Simulation*, 2023. https://doi.org/10.1080/17477778.2023.2217334
