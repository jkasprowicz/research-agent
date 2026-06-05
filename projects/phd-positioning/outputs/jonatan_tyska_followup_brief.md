# Follow-Up Brief for Jônata Tyska Carvalho

## Goal of the Follow-Up Meeting

Clarify whether the SUS waiting-list direction can become a strong, feasible, admission-oriented PhD plan for PPGCC/UFSC.

The key decision is not whether the topic is relevant. It is. The key decision is whether there is a realistic data path and whether the advisor prefers the methodological core to be:

- explainable prediction;
- ML + simulation;
- bottleneck/anomaly detection;
- fairness-aware decision support;
- or a staged combination of these.

## 2-Minute Explanation of the New Idea

I would like to reshape the doctoral plan around waiting-list dynamics in the SUS, as we discussed. My understanding is that the strongest Computer Science framing is not simply to predict average waiting time, but to model waiting lists as dynamic event processes involving requests, status transitions, priorities, services, capacity constraints, cancellations, no-shows, returns and execution.

The proposed direction would be to develop explainable predictive models and, if data permit, simulation-based decision support for identifying problematic queue behavior. Examples include excessive waiting, stagnation, repeated returns to the requesting unit, priority-time violations, no-shows, cancellations and bottlenecks by specialty, procedure, service or region.

The practical output would not be an autonomous system deciding who receives care. It would be decision support for managers: monitoring, explanation, risk identification and scenario analysis. Scientifically, the contribution would sit in machine learning for healthcare operations, explainable AI, temporal validation, event-log modeling and possibly discrete-event simulation. I think this has strong alignment with Computational Intelligence and AI applied to health, but I want to confirm the expected scope, data availability and methodological emphasis before finalizing the submission plan.

## Candidate Background Points to Mention Naturally

- Biomedical Sciences background with strong health-domain literacy.
- MSc in Health Informatics.
- Professional experience in healthcare operations, quality, data and real-world constraints.
- Existing publication experience and ability to execute applied AI research.
- Current transition: from domain-specific healthcare AI toward broader health-system intelligence and decision support.
- Working professional, so the project must be retrospective, staged and publication-efficient.

Avoid making the meeting sound like a thesis defense. The posture should be:

**"I am shaping this into an admission plan and want to align it with your expectations, data possibilities and methodological priorities."**

## Questions About Data Access

1. Is there a concrete partner institution, municipality, state health department or research group that could provide waiting-list data?
2. Would the available data be event-level or only aggregated?
3. Are historical status transitions available, or only the current status of each request?
4. Which system would likely be involved: SISREG, e-SUS Regulação, e-SUS Captação de Filas, a municipal/state regulation platform, CROSS/SIRESP-like systems, or another local system?
5. Are dates available for request, authorization, scheduling, execution, cancellation, return, no-show and exclusion?
6. Are procedure codes available, preferably SIGTAP?
7. Are specialty/service, requesting unit, regulating unit, executing unit and municipality/region available?
8. Is there a priority/risk field? If yes, is it standardized or locally defined?
9. Are reasons for return, cancellation or denial available?
10. Are capacity/slot/agenda data available, or only demand-side request records?
11. Is there any linkage to outcomes, clinical deterioration, hospitalization or later use of emergency services, or should the first version avoid clinical outcomes?
12. What is the expected sample size and time span?
13. Would the dataset include multiple specialties/procedures or should the project focus on one service line first?
14. Are there known data quality problems: duplicated requests, inconsistent procedure naming, missing dates, local status semantics or policy changes?
15. Is there institutional support for CEP submission and a data-use agreement?

## Questions About Methodological Direction

1. Would you prefer the plan to emphasize explainable prediction, simulation/optimization, or a staged hybrid approach?
2. Should the admission plan mention Agentic AI/LLMs at all, or avoid them unless there is a clear protocol-retrieval/explanation use?
3. Is discrete-event simulation a good fit for your expectations, or should it be kept as an optional later stage?
4. Should the first study focus on excessive waiting, no-show/cancellation, returned requests, bottlenecks, or priority-time violation?
5. Would fairness/equity be central, or should it be treated as an evaluation layer?
6. What would count as a strong Computer Science contribution in your view?
7. Should the plan include a dashboard/interface prototype, or is methodological evaluation enough?
8. Which baseline comparisons would you expect: FIFO, current priority rules, logistic/GBM models, survival models, queueing baselines, simulation baselines?
9. Should the plan use process mining/event-log terminology?
10. Would a co-advisory conversation with an operations research or database professor be useful, or should the plan remain focused on Computational Intelligence?

## Possible Datasets

### Strongest Dataset

Event-level regulation records with:

- unique request ID;
- pseudonymized patient ID;
- request date/time;
- status history and transition timestamps;
- procedure code;
- specialty/service;
- priority/risk;
- requesting unit;
- regulating unit;
- executing unit;
- municipality/region;
- final status;
- no-show, cancellation, return, denial, execution;
- capacity/slots/agendas if available.

This supports prediction, bottleneck detection, explainability and simulation.

### Minimum Viable Dataset

Event-level records with:

- request ID;
- dates;
- status;
- procedure/specialty;
- priority or urgency proxy;
- requesting/executing units;
- final outcome.

This supports prediction and bottleneck detection, but may not support realistic simulation.

### Weak Dataset

Aggregated queue counts by service/month/municipality.

This supports descriptive monitoring and time-series analysis, but is weak for a PhD unless paired with a methodological simulation or a second data source.

### Public/Secondary Fallbacks

- Ministry of Health regulation documentation and MIRA/e-SUS models.
- Public transparency dashboards where available.
- Aggregated waiting-list panels from state/municipal systems.
- Published datasets from international waiting-list or patient-flow studies, only as methodological complements.

## Risks to Clarify Before Submission

| Risk | Question to resolve |
|---|---|
| No event-level data | Can the advisor identify a real data source before submission or early in the PhD? |
| No capacity data | Should simulation be optional rather than central? |
| Topic becomes health policy | What computational contribution should be foregrounded? |
| Overpromising decision support | Should the plan avoid interface/prototype language? |
| Automated prioritization concern | Should we explicitly state the project supports managers and does not automate access decisions? |
| Too broad across SUS | Should the first version focus on specialized outpatient care, elective surgery, or one service line? |
| Weak alignment with advisor theme | Which wording best matches the advisor's Anexo I theme? |
| Ethical/data governance complexity | Is there a likely CEP path and institutional data-use agreement? |
| Working-professional feasibility | Can the plan be staged around retrospective data, reusable pipelines and 3-4 publishable studies? |

## Recommended Position to Test With the Advisor

**Main proposal:** explainable predictive and simulation-based models for dynamic waiting-list decision support in SUS regulation.

**Staged scope:**

- First: event-log construction and descriptive queue-behavior map.
- Second: explainable prediction of problematic queue behavior.
- Third: bottleneck/anomaly detection with manager-facing explanations.
- Fourth: simulation of decision scenarios only if capacity/slot data are available.

**Non-goals:**

- no autonomous prioritization;
- no national deployment promise;
- no generic LLM/agent framing;
- no purely descriptive public-health study;
- no dependence on clinical outcomes unless available.

## Closing Ask for the Advisor

The most useful closing question:

**"For the admission plan, would you prefer that I frame the project primarily as explainable prediction of problematic queue behavior, or as a broader hybrid ML-plus-simulation decision-support framework with simulation treated as a later stage depending on data availability?"**

