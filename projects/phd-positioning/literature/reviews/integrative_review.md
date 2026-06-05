# Integrative Review: Waiting Lists, Referral Management, Queueing, Machine Learning and Decision Support in Healthcare

## Scope and Evidence Base

This integrative review synthesizes the 33 structured article notes generated from the PDF corpus in `literature/pdfs/tier1/` and `literature/pdfs/tier2/`. The goal is not to replace a formal systematic review, but to identify the evidence structure most relevant to a PhD project on SUS waiting-list dynamics, explainable predictive modeling and decision support for healthcare managers.

The corpus contains three complementary evidence layers:

1. Direct SUS waiting-list and regulation evidence: empirical studies, conceptual papers, telehealth studies, cost analyses, regulation architecture and professional workflow reports.
2. Transferable computational methods: queueing theory, simulation, machine learning, optimization and explainable AI applied to healthcare operations.
3. Implementation and governance evidence: training, regulatory roles, task forces, interoperability and the gap between proposed prioritization tools and real-world adoption.

The strongest conclusion is that the most defensible PhD direction is not "predict waiting time" in isolation. The literature supports a broader, workflow-aware decision-support problem: how to use real operational data to detect, explain and support management of problematic waiting-list behavior in SUS-like regulation environments.

## Evidence Base Map

| Evidence family | Representative papers | Main study types | Core contribution | Direct applicability to SUS |
|---|---|---|---|---|
| SUS waiting-list management | Pazin-Filho et al. 2024; Antunes et al. 2025; Salles et al. 2026; Lisboa et al. 2022; Fujita et al. 2025 | Retrospective observational, pre-post, descriptive, experience report, editorial | Shows that list centralization, list updating, access management and targeted interventions can reduce waiting times or backlog | High |
| SUS specialized access and conceptual framing | Giannotti et al. 2025; Cavalcanti et al. 2022; De-Carli et al. 2023; Lemos et al. 2025 | Conceptual reflection, cross-sectional analyses, multicenter observational study | Frames waiting lists as access, equity, regulation and governance problems rather than merely scheduling problems | High |
| Referral management and telehealth | Gadenz et al. 2021; Pachito et al. 2022; Pfeil et al. 2025 | Before-after intervention, micro-costing, cost-minimization | Shows that telehealth/gatekeeping can reduce waiting-list size, waiting time and costs in Brazilian public healthcare | Very high |
| Queueing theory and operations research | Thompson et al. 2024; Lim et al. 2023; Wood et al. 2022; Lee et al. 2022; Kruik-Kolloffel et al. 2024; Kara and Sahin 2025; Wang et al. 2024 | Analytical queueing, computer experiment, capacity modeling, optimization | Provides formal tools for capacity, delay, prioritization and workflow trade-offs | Moderate to high, depending on availability of event-level SUS data |
| Simulation and hybrid operational modeling | Wartelle et al. 2026; Gabriel et al. 2020; Rifi et al. 2022; Alvarez-Vazquez et al. 2025 | Data-driven queueing simulation, DES, systematic review | Supports scenario testing before real-world interventions | Moderate |
| Machine learning for wait prediction and prioritization | Gloyn et al. 2026; Shin et al. 2024; Fall et al. 2025; Gagliotti and Gutierrez 2025; Mandizvida et al. 2024 | Scoping review, predictive modeling, conference studies | Predicts waiting time, no-show/service time, delay classification or urgent intervention | Moderate; strongest when paired with management action |
| Explainable AI | Shin et al. 2024; Gagliotti and Gutierrez 2025; Gloyn et al. 2026 | Interpretable ML, SHAP, review evidence | Shows need for interpretable predictions in operational contexts | High as a design principle; direct SUS evidence still limited |
| Decision-support systems and architecture | Cardoso et al. 2026; Wang et al. 2024; Thompson et al. 2024; Pazin-Filho et al. 2024 | Software architecture, queueing DSS, queue evaluation, hospital queue system | Moves from prediction to decision-support infrastructure | Very high for PhD positioning in Computer Science |
| Generic/background smart healthcare | Mahmudov and Mahmudova 2022; Sasikala et al. 2025 | Conceptual or weakly validated method papers | Broad AI/IoT/ML/queueing framing | Low to moderate; should not anchor the proposal |

## Main Themes

### Theme 1: Waiting lists are management systems, not just queues

The SUS-oriented articles show that waiting lists are not passive lists of patients. They are socio-technical systems shaped by regulation rules, data quality, professional roles, transparency, specialty-specific capacity, referral quality, patient updating, prioritization, cancellations and governance. Pazin-Filho et al. show the operational value of a centralized surgical indication system. Salles et al. show that list updating can remove obsolete demand and change scheduling capacity. Lisboa et al. and Fujita et al. emphasize human workflow, task-force models and professional coordination.

| Aspect | Synthesis |
|---|---|
| Strengths | Strong direct SUS evidence; concrete operational outcomes; highlights data quality, centralization and workflow realism. |
| Weaknesses | Often descriptive, retrospective or pre-post; limited predictive modeling; limited causal identification. |
| Evidence level | Moderate to high for operational relevance; lower for computational generalization. |
| Reproducibility | Moderate. Methods are understandable, but data are institutional and not openly reproducible. |
| Applicability to SUS | Very high. This is the problem layer a PhD proposal must preserve. |

### Theme 2: Referral management is a high-value intervention point

The strongest direct Brazilian evidence concerns referral management and telehealth-supported gatekeeping. Gadenz et al. found large reductions in waiting-list size after telehealth-supported referral management. Pachito et al. and Pfeil et al. add economic evidence, showing low per-case costs and cost reductions from remote regulation/gatekeeping.

| Aspect | Synthesis |
|---|---|
| Strengths | Direct SUS context; measurable waiting-list and cost outcomes; strong managerial relevance. |
| Weaknesses | Mostly evaluates interventions retrospectively; does not predict patient/list behavior prospectively. |
| Evidence level | High for practical relevance; moderate for causal inference. |
| Reproducibility | Moderate. Designs are transparent but depend on local systems such as RegulaSUS/Gercon. |
| Applicability to SUS | Very high, especially for specialized-care regulation and access management. |

### Theme 3: Advanced computational methods are promising but mostly external to SUS

Queueing theory, simulation, machine learning and optimization papers offer robust computational tools, but most are from emergency departments, outpatient clinics, operating rooms, radiology triage, pharmacy workflow or laboratory networks outside SUS. Their value is methodological transfer, not direct contextual evidence.

| Aspect | Synthesis |
|---|---|
| Strengths | Provides rigorous mathematical and computational vocabulary; supports prediction, scenario testing and capacity trade-off analysis. |
| Weaknesses | Often not validated in public regulation workflows; may optimize local processes rather than system-wide access. |
| Evidence level | High methodologically in selected papers; variable in conference/prototype studies. |
| Reproducibility | Moderate to high for analytical models; lower for proprietary hospital datasets. |
| Applicability to SUS | Moderate unless adapted to real regulation data, queue rules and managerial actions. |

### Theme 4: Prediction alone is insufficient

The ML literature predicts waiting time, no-show, service time, delay status or urgency. However, the prioritization review shows that many proposed tools do not reach implementation. The risk is a technically competent model with no managerial action, no workflow fit and no measurable queue impact.

| Aspect | Synthesis |
|---|---|
| Strengths | ML can model nonlinear patterns and patient/service heterogeneity; useful for early warning and triage. |
| Weaknesses | Many models focus on performance metrics rather than decisions; limited external validation and implementation evidence. |
| Evidence level | Moderate. Strong as proof of feasibility, weaker as implemented health-system evidence. |
| Reproducibility | Variable; usually limited by unavailable data and sparse code sharing. |
| Applicability to SUS | Moderate to high if tied to regulation actions and explainable outputs. |

### Theme 5: Decision support is the most mature PhD framing

The decision-support framing integrates the strongest strands: SUS governance, real regulation data, explainable prediction, queue dynamics and managerial action. Cardoso et al. support the architectural/interoperability layer. Wang et al. show queueing and optimization as a decision-support tool in a constrained public health network. Thompson et al. shows how classifier-based prioritization should be evaluated by wait-time impact, not just accuracy. Pazin-Filho et al. shows centralized queue infrastructure in a Brazilian public hospital.

| Aspect | Synthesis |
|---|---|
| Strengths | Computationally rigorous and managerially meaningful; avoids generic AI; aligns with Computer Science through models, systems and evaluation. |
| Weaknesses | Requires realistic access to event-level data and careful definition of actionable decisions. |
| Evidence level | Moderate to high as a synthesized direction, though direct SUS predictive DSS evidence remains limited. |
| Reproducibility | Potentially high if the PhD defines transparent data schemas, model protocols and evaluation metrics. |
| Applicability to SUS | Very high if built around regulation workflows, not abstract patient queues. |

## Waiting-List Management Approaches

| Approach | Key papers | What it does | Strengths | Weaknesses | Evidence level | SUS applicability |
|---|---|---|---|---|---|---|
| Centralized queue/list management | Pazin-Filho et al. 2024 | Consolidates fragmented surgical indications and monitors inflow, outflow, backlog and waiting time | Large real-world Brazilian dataset; strong operational realism | Single institution; not predictive | High operational evidence | Very high |
| Access-management program | Antunes et al. 2025 | Introduces management structure for cardiac surgery access | Demonstrates measurable wait reduction | Retrospective; severity not fully controlled | Moderate | High |
| Active list updating | Salles et al. 2026 | Contacts patients, removes obsolete demand and updates complaint/status | Shows data-quality problem in waiting lists | Single municipality; descriptive only | Moderate | Very high |
| Regulatory professional role | Lisboa et al. 2022 | Describes regulatory nurse actions in surgical waiting-list management | Captures human workflow and governance | Experience report; no statistical test | Low to moderate | High |
| Surgical task force | Fujita et al. 2025 | Weekend campaigns and multidisciplinary action to reduce pediatric ENT backlog | Pragmatic and scalable intervention idea | Editorial/local experience; no comparative design | Low | Moderate to high |
| Training for waiting-list management | Lisboa and Paz 2025 | Virtual training course for professionals | Addresses implementation capacity | Does not measure queue outcomes | Moderate educational evidence | Moderate |

### Synthesis

Waiting-list management evidence supports a PhD that treats the list as a dynamic operational object. The most relevant variables are not only patient attributes, but also entry date, priority, specialty, queue status, inflows/outflows, cancellations, reason for removal, service capacity, referral source, regulatory decisions and time-to-action. This is where the SUS corpus is strongest.

## Referral Management Approaches

| Approach | Key papers | Data/outcome focus | Strengths | Weaknesses | Evidence level | SUS applicability |
|---|---|---|---|---|---|---|
| Remote referral management | Gadenz et al. 2021 | Waiting-list size and waiting time before/after implementation | Large practical reductions; direct SUS context | Before-after design; aggregate measures | High practical, moderate causal | Very high |
| Micro-costing of referral management | Pachito et al. 2022 | Cost per referred case by locality/specialty | Adds economic feasibility evidence | Does not measure predictive performance | Moderate | Very high |
| Telemedicine gatekeeping | Pfeil et al. 2025 | Cost-minimization and specialist-demand reduction | Over 15,000 patients; strong cost argument | Assumptions where data unavailable | High practical | Very high |
| Regulation architecture | Cardoso et al. 2026 | Interoperability, queue management, auditability | Connects regulation to information systems | Limited quantitative patient outcomes | Moderate | Very high |
| Specialized oral access | Cavalcanti et al. 2022; De-Carli et al. 2023 | Waiting time and service characteristics in CEO | National SUS data; service variables | Cross-sectional associations | Moderate | High |

### Synthesis

Referral management is likely the best operational domain for an admission-oriented PhD because it is simultaneously computational, managerial and public-health relevant. The literature suggests a gap between systems that manage/refuse/redirect referrals and systems that learn from queue behavior to support managers with explainable, prospective evidence.

## Telehealth Approaches

| Paper | Telehealth role | Main outcome | Strengths | Weaknesses | Evidence level | SUS applicability |
|---|---|---|---|---|---|---|
| Gadenz et al. 2021 | Telehealth-supported referral management | Waiting-list reductions of 54.67% to 88.97%; waiting-time decreases in selected localities | Directly evaluates access effect | Pre-post and locality-dependent | High practical | Very high |
| Pachito et al. 2022 | Remote referral management costing | Cost per referral R$5.70-R$8.29 across localities | Feasibility and cost transparency | No full comparative effectiveness evaluation | Moderate | Very high |
| Pfeil et al. 2025 | RegulaSUS telemedicine gatekeeping | 60% cost reduction; R$7.83M societal savings over 36 months | Strong economic and operational case | Cost assumptions and limited documentation of removal reasons | High practical | Very high |

### Synthesis

Telehealth is not merely a digital-care intervention in this corpus; it is a regulation and demand-management mechanism. For the PhD, telehealth evidence supports the managerial importance of referral filtering, case review and demand redirection. However, the project should not become "telehealth evaluation"; its stronger computational contribution would be modeling the queue dynamics and decision points that such regulation systems generate.

## Queueing Theory Applications

| Application type | Key papers | Computational task | Strengths | Weaknesses | Evidence level | SUS applicability |
|---|---|---|---|---|---|---|
| Queue impact of AI triage | Thompson et al. 2024 | Estimate wait-time savings from classifier-based prioritization | Strong mathematical framing; moves beyond AUC | Radiology setting; simplified binary classifier | High methodological | Moderate to high |
| Data-driven queueing network | Wartelle et al. 2026 | Model ED crowding and simulate alternative pathways | Bridges statistical modeling and queueing simulation | ED-specific; complex adaptation | High methodological | Moderate |
| OR/staffing capacity | Lim et al. 2023 | Estimate staffing/OR capacity from arrivals and service rates | Clear queueing variables; real-world data | Birth-center-specific | Moderate | Moderate |
| Outpatient wait optimization | Lee et al. 2022 | Physician-customized queueing/metamodel optimization | Shows local heterogeneity matters | Small session-level data; field validation needed | Moderate | Moderate |
| Delayed transfers/capacity trade-off | Wood et al. 2022 | Estimate economically rational nonzero delay | Strong conceptual lesson on variability | NHS community-care context | Moderate to high | Moderate |
| Medication-reconciliation workflow | Kruik-Kolloffel et al. 2024 | Compare workflow interventions via queueing | Non-disruptive process evaluation | Pharmacy-specific assumptions | Moderate | Low to moderate |
| Disaster physician demand | Kara and Sahin 2025 | M/M/s demand-capacity estimation | Clear capacity modeling | Disaster context far from elective access | Moderate | Low |
| Public-health laboratory resource allocation | Wang et al. 2024 | Queueing + integer programming for machine allocation | Strong decision-support analogy in constrained public system | Laboratory network, not waiting list | High methodological | Moderate |

### Synthesis

Queueing theory is one of the strongest methodological pillars because waiting lists are fundamentally about arrivals, service capacity, prioritization, delays and variability. The literature also warns against naive targets such as eliminating all waiting: some waiting may reflect stochastic variability and limited capacity. For SUS, queueing models are most useful if combined with real event data and managerial scenarios.

## Machine Learning Applications

| ML application | Key papers | Inputs | Outputs | Strengths | Weaknesses | Evidence level | SUS applicability |
|---|---|---|---|---|---|---|---|
| ED waiting-time prediction | Gloyn et al. 2026 | Queue, staff/resource, patient and time features | Individualized ED wait estimates | Review-level evidence; ML outperforms rolling averages | ED-focused; sparse literature | Moderate | Moderate |
| Interpretable outpatient wait prediction | Shin et al. 2024 | Queue length, queue composition, appointment status, temporal and service variables | Waiting-time estimates and explanations | SHAP + asymmetric loss; operationally interpretable | Single hospital; outpatient context | High methodological | Moderate to high |
| No-show and service-time prediction | Fall et al. 2025 | Appointment, care type, provider, waiting time, ZIP/service features | No-show classification, service-time regression | Models uncertainty relevant to scheduling | Exact sample and generalization need verification | Moderate | Moderate |
| Cardiac surgical prioritization | Gagliotti and Gutierrez 2025 | 44 clinical/demographic variables | Urgent intervention prediction | Directly competitive Brazilian waiting-list ML | Narrow procedure; implementation not demonstrated | Moderate | High |
| Public-hospital delay classification | Mandizvida et al. 2024 | Waiting-time, scheduling, triage, referral/admin and demographic data | Delayed vs not delayed | Low-resource public-hospital example | Modest AUC; short data window | Low to moderate | Moderate |
| Hybrid ML + queueing resource allocation | Sasikala et al. 2025 | Workload/queue/resource states | Real-time resource allocation | Aligns with hybrid idea | Unclear data provenance/reproducibility | Low | Low to moderate |

### Synthesis

ML is promising but should be subordinated to a decision-support question. The most useful outputs for SUS would not be a single prediction, but explainable risk signals such as: probability of excessive wait, probability of no-show/dropout, probability of avoidable delay, likely bottleneck specialty/service, and expected effect of management actions. The literature suggests that raw predictive performance is insufficient unless linked to workflow, interpretability and evaluation of operational impact.

## Simulation Applications

| Simulation type | Key papers | Purpose | Strengths | Weaknesses | Evidence level | SUS applicability |
|---|---|---|---|---|---|---|
| Data-driven queueing simulation | Wartelle et al. 2026 | Evaluate ED crowding and alternative services | Combines real data with scenario evaluation | ED-specific and technically complex | High methodological | Moderate |
| DES + Lean + DOE | Gabriel et al. 2020 | Plan ED expansion and reduce LOS/waiting | Strong process-improvement example; quantitative scenarios | Simulated scenario effects may overstate real-world gains | Moderate | Low to moderate |
| OR uncertainty simulation | Rifi et al. 2022 | Assess impact of uncertainty on OR patient waiting time | Useful uncertainty framing | Case-inspired, limited validation | Moderate | Moderate |
| AI + simulation review | Alvarez-Vazquez et al. 2025 | Map AI/simulation integration in healthcare processes | Shows emerging hybrid field | Broad, not waiting-list specific | Moderate review evidence | Moderate |
| Queueing computer experiment | Kruik-Kolloffel et al. 2024 | Compare medication-reconciliation interventions | Non-disruptive evaluation before implementation | Workflow-specific | Moderate | Low to moderate |

### Synthesis

Simulation is most valuable for testing management scenarios before implementation. In a SUS waiting-list PhD, simulation should be used selectively: to evaluate action policies, capacity scenarios, referral filtering or prioritization strategies. It should not become a large universal digital twin unless the data infrastructure is unusually strong.

## Optimization Applications

| Optimization approach | Key papers | Decision optimized | Strengths | Weaknesses | Evidence level | SUS applicability |
|---|---|---|---|---|---|---|
| Integer programming + queueing | Wang et al. 2024 | Placement of HIV viral-load testing machines | Strong constrained-resource DSS | Different domain | High methodological | Moderate |
| NSGA-II outpatient strategy optimization | Lee et al. 2022 | Physician-specific waiting-time reduction strategies | Shows customized operational policies | Small session-level data; field validation needed | Moderate | Moderate |
| Centralized queue rationing | Pazin-Filho et al. 2024 | Surgical backlog and oncology/non-oncology rationing during COVID-19 | Real SUS-like hospital queue management | Not algorithmic optimization | High operational | Very high |
| Staffing/capacity queueing | Lim et al. 2023; Kara and Sahin 2025 | Number of staff/servers under demand | Clear capacity-planning logic | Different settings | Moderate | Moderate |
| AI triage queue evaluation | Thompson et al. 2024 | Prioritization impact from classifier deployment | Optimizes evaluation logic, not only accuracy | Radiology abstraction | High methodological | Moderate |

### Synthesis

Optimization should be framed conservatively. The PhD should not promise automatic allocation of care or replacement of regulation rules. A defensible contribution is decision-support optimization: compare transparent scenarios, estimate trade-offs and support managers in understanding consequences of interventions.

## Explainable AI Applications

| XAI application | Key papers | Explanation target | Strengths | Weaknesses | Evidence level | SUS applicability |
|---|---|---|---|---|---|---|
| SHAP for waiting-time prediction | Shin et al. 2024 | Why a patient or service context is expected to wait longer | Directly links interpretability to patient dissatisfaction and operations | Single-hospital outpatient case | High methodological | High as design principle |
| Explainability in ED wait prediction | Gloyn et al. 2026 | Model selection and communication of wait estimates | Review highlights feature categories and end-user needs | Review, not implemented SUS DSS | Moderate | Moderate |
| ML surgical prioritization | Gagliotti and Gutierrez 2025 | Risk-based priority for cardiac surgery | Directly competitive Brazilian use case | XAI details not clearly extracted; implementation uncertain | Moderate | High |

### Synthesis

Explainability is underrepresented but strategically important. The SUS problem requires explanations for managers, regulators and clinicians, not only feature importance for data scientists. The relevant question is: why is this queue, specialty, referral type or patient subgroup at risk of problematic delay, and what action could plausibly reduce it?

## Decision-Support Systems

| DSS type | Key papers | Decision supported | Evidence maturity | Strengths | Weaknesses | SUS applicability |
|---|---|---|---|---|---|---|
| Regulation architecture | Cardoso et al. 2026 | Multi-region SUS regulation, interoperability, auditability and queue monitoring | Moderate | Directly Computer Science and SUS-aligned | Limited quantitative patient impact | Very high |
| Centralized surgical list system | Pazin-Filho et al. 2024 | Queue visibility, backlog management, rationing | High operational | Large dataset and measurable outcomes | Single institution, not predictive | Very high |
| Telehealth referral/gatekeeping system | Gadenz et al. 2021; Pfeil et al. 2025; Pachito et al. 2022 | Referral review, specialist-demand reduction, cost management | High practical | Strong SUS and economic evidence | Not predictive/explainable DSS | Very high |
| Queueing/optimization DSS | Wang et al. 2024 | Resource allocation in constrained public-health network | High methodological | Strong OR/DSS template | Different domain | Moderate |
| AI triage evaluation DSS | Thompson et al. 2024 | Whether AI prioritization reduces wait for target cases | High methodological | Evaluates operational value of classifier | Radiology-specific abstraction | Moderate |
| Predictive wait-time support | Shin et al. 2024; Gloyn et al. 2026 | Wait prediction and explanation | Moderate to high methodological | Good ML/XAI basis | Limited implementation evidence | Moderate |

### Synthesis

The most mature decision-support direction combines: regulation architecture, central queue visibility, telehealth/referral-management evidence, predictive/explainable modeling and queueing/simulation evaluation. This moves the PhD from "AI for waiting lists" to "explainable, data-driven decision support for regulation and waiting-list management."

## Cross-Theme Comparison

| Theme | Strengths | Weaknesses | Evidence level | Reproducibility | Applicability to SUS |
|---|---|---|---|---|---|
| Waiting-list management | Directly addresses backlog, waiting time, centralization, list updating and human workflow | Often retrospective/descriptive; limited prediction | Moderate to high | Moderate | Very high |
| Referral management | Strong SUS operational and economic evidence | Limited prospective modeling and individualized prediction | High practical | Moderate | Very high |
| Telehealth | Demonstrated reductions/cost savings in Brazilian regulation contexts | May be intervention-specific; not inherently algorithmic | High practical | Moderate | Very high |
| Queueing theory | Formalizes arrivals, service rates, capacity, prioritization and delay | Requires assumptions and event-level data | High methodological | Moderate to high | Moderate to high |
| Machine learning | Captures nonlinear patterns, heterogeneity and risk signals | Risk of model-first framing; limited implementation evidence | Moderate | Variable | Moderate to high |
| Simulation | Allows safe scenario testing before operational changes | Data- and assumption-intensive; can overfit local workflows | Moderate | Moderate | Moderate |
| Optimization | Supports trade-off analysis and resource allocation | May be politically/ethically sensitive if framed as automatic rationing | Moderate to high methodological | Moderate | Moderate |
| Explainable AI | Essential for managerial trust and operational use | Sparse direct SUS examples | Moderate | Moderate | High as design principle |
| Decision support systems | Integrates models with workflows, architecture and action | Requires data access and careful scoping | Moderate to high | Potentially high if protocolized | Very high |

## Article Coverage Matrix

| # | Paper | Primary contribution to the integrative review | Relevance to SUS waiting lists |
|---|---|---|---|
| 1 | Gloyn et al., AI for ED wait-time prediction | ML review and feature categories for wait prediction | 4 |
| 2 | Shin et al., interpretable outpatient wait prediction | SHAP, asymmetric loss and dissatisfaction-aware wait prediction | 4 |
| 3 | Gadenz et al., telehealth referral management | Direct SUS before-after evidence of waiting-list reduction | 5 |
| 4 | Pazin-Filho et al., surgical queue management | Large Brazilian centralized surgical queue evidence | 5 |
| 5 | Giannotti et al., specialized outpatient waiting-list concept | SUS conceptual and policy framing | 5 |
| 6 | Antunes et al., cardiac surgery access management | Brazilian pre-post evidence of reduced cardiac surgery waiting time | 5 |
| 7 | Fall et al., no-show and service-time prediction | ML for appointment uncertainty | 4 |
| 8 | Hroub et al., waiting-list management review | Theory-practice gap in prioritization tools | 5 |
| 9 | Pachito et al., micro-costing referral management | Cost feasibility of remote referral management in SUS | 5 |
| 10 | Salles et al., speech-therapy waiting list | Data quality, list updating and demand characterization | 5 |
| 11 | Wartelle et al., data-driven queueing simulation | Hybrid data-driven queueing and simulation | 4 |
| 12 | Alvarez-Vazquez et al., AI + simulation review | Hybrid AI/simulation state of the art | 4 |
| 13 | Gabriel et al., DES + Lean ED expansion | DES and process-improvement example | 3 |
| 14 | Thompson et al., queueing evaluation of AI triage | Wait-time impact evaluation for classifier-based prioritization | 4 |
| 15 | Lim et al., obstetric OR queueing | Capacity/staffing queueing example | 3 |
| 16 | De-Carli et al., oral biopsy wait | National SUS access-delay analysis | 4 |
| 17 | Pfeil et al., telemedicine gatekeeping | Cost-minimization and specialist-demand reduction in Brazil | 5 |
| 18 | Wood et al., delayed transfers and queueing | Capacity-delay trade-off and stochastic variability | 3 |
| 19 | Rifi et al., OR uncertainty simulation | DES under uncertainty | 3 |
| 20 | Cavalcanti et al., specialized oral healthcare access | National SUS service-characteristic analysis | 4 |
| 21 | Sasikala et al., hybrid ML + queueing | Low-confidence hybrid resource-allocation prototype | 2 |
| 22 | Lemos et al., waiting time until surgery | Brazilian patient-level burden of surgical delay | 4 |
| 23 | Mahmudov and Mahmudova, smart health systems | Generic background on IoT/ML/queueing | 1 |
| 24 | Gagliotti and Gutierrez, cardiac surgery ML prioritization | Directly competitive Brazilian ML prioritization | 5 |
| 25 | Mandizvida et al., predictive delay classification | Low-resource public-hospital ML example | 3 |
| 26 | Wang et al., queueing DSS for HIV VL testing | Queueing + optimization decision-support template | 4 |
| 27 | Lisboa and Paz, training in waiting-list management | Implementation capacity and professional training | 3 |
| 28 | Lisboa et al., regulatory nurse actions | Human workflow and governance in surgical list management | 4 |
| 29 | Fujita et al., pediatric ENT surgical task force | Practical backlog intervention example | 3 |
| 30 | Cardoso et al., SUS regulation architecture | Information-systems architecture for regulation and queue management | 5 |
| 31 | Lee et al., physician-customized queueing optimization | Queueing/metamodel optimization for outpatient waits | 4 |
| 32 | Kruik-Kolloffel et al., medication reconciliation queueing | Queueing computer experiment for workflow intervention | 3 |
| 33 | Kara and Sahin, disaster demand-capacity queueing | Capacity estimation with M/M/s queueing | 2 |

## Integrated Findings

### What is well supported

The literature strongly supports that waiting lists in public healthcare are dynamic management systems affected by inflow, outflow, data quality, prioritization, capacity and professional workflow. In the SUS context, there is solid practical evidence that centralization, referral management, telehealth-supported gatekeeping and list updating can improve access indicators or reduce costs.

### What is methodologically promising

Queueing theory, simulation, ML, optimization and XAI are all relevant, but each solves a different computational problem. Queueing theory explains delays and capacity. ML predicts risk or time. Simulation tests scenarios. Optimization compares allocation strategies. XAI makes model outputs usable by managers and clinicians. Decision-support systems integrate these pieces into workflows.

### What remains weak

The weakest area is not the existence of algorithms, but implementation-grade, explainable, workflow-aware decision support for real public regulation systems. Many studies either describe management interventions without predictive modeling or develop predictive/optimization methods outside SUS without governance and implementation evidence.

### What should be avoided

A PhD proposal should avoid:

- A generic "AI for queues" framing.
- A narrow model that only predicts waiting time without decision consequences.
- Automatic prioritization language that appears to replace clinical/regulatory judgment.
- Overpromising digital twins or real-time optimization before data access is confirmed.
- Depending on weak/generic smart-health papers as central evidence.

## Implications for a SUS Waiting-List PhD

The most evidence-consistent PhD framing is:

> Explainable, data-driven decision support for detecting and managing problematic waiting-list behavior in SUS regulation workflows.

This framing is stronger than isolated waiting-time prediction because it is supported by all major evidence layers:

- SUS management studies define the problem and show practical impact.
- Referral/telehealth studies show an actionable intervention domain.
- Queueing theory formalizes delay, capacity and prioritization trade-offs.
- ML supports prediction of risk, waiting behavior and operational bottlenecks.
- Simulation and optimization support scenario evaluation rather than unsafe automatic decisions.
- XAI and DSS literature support explainability, workflow integration and Computer Science contribution.

## Proposed Synthesis Model

| Layer | Literature support | Possible PhD role |
|---|---|---|
| Data layer | Cardoso et al.; Pazin-Filho et al.; Salles et al. | Define regulation-event schema, data-quality indicators and waiting-list states |
| Descriptive analytics layer | Antunes et al.; Cavalcanti et al.; De-Carli et al.; Lemos et al. | Characterize waits, backlog, service heterogeneity and access inequalities |
| Predictive layer | Shin et al.; Gloyn et al.; Fall et al.; Gagliotti and Gutierrez | Predict problematic wait, no-show/dropout, delay risk or urgent deterioration |
| Queueing/simulation layer | Thompson et al.; Wartelle et al.; Lee et al.; Wang et al. | Evaluate whether predicted prioritization or management actions improve queue outcomes |
| Explainability layer | Shin et al.; Gloyn et al. | Explain drivers of problematic queue behavior to managers/regulators |
| Decision-support layer | Cardoso et al.; Wang et al.; Gadenz et al.; Pfeil et al. | Convert predictions and scenarios into transparent managerial evidence |

## Bottom-Line Conclusion

The corpus supports a strategically conservative but scientifically strong conclusion: SUS waiting-list research should not be positioned as a pure machine-learning prediction problem. The stronger contribution is a decision-support framework grounded in real regulation data, explainable prediction, queue dynamics and management actions. This direction is more aligned with Computer Science than a descriptive public-health study, more applicable to SUS than generic operations research, and more defensible than a broad AI/optimization platform.

