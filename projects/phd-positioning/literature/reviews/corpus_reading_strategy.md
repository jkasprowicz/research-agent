# Corpus Reading Strategy - SUS Waiting-List PhD Proposal

## Objective

Build the minimum high-value reading corpus required before writing the final PPGCC/UFSC PhD proposal. The aim is not completeness; it is enough evidence to make the proposal specific, computationally credible, and feasible.

## Updated Screening Snapshot

| Metric | Count |
|---|---:|
| Raw records loaded | 702 |
| Unique records screened | 654 |
| Duplicates removed | 48 |
| A. Directly Competitive | 92 |
| B. Methodologically Relevant | 84 |
| C. Contextual Background | 149 |
| D. Exclude | 329 |

## Recommended Reading Order

1. Read Tier 1 first: these papers define the proposal backbone around SUS access, waiting-list management, queueing, waiting-time prediction, referral management, simulation and decision support.
2. Read Tier 2 next: these papers strengthen methods and adjacent operational evidence, especially queueing theory, demand-capacity modeling, appointment scheduling, no-show modeling and Brazilian access studies.
3. Read Tier 3 selectively: use these to fill methodological gaps in patient-flow prediction, delayed discharge, bed allocation, fairness and operational decision support.
4. Do not read the excluded set unless a title is manually rescued for a specific reason. Most excluded papers are generic healthcare AI, diagnostic imaging, disease-specific treatment-delay studies, transplant-only papers or non-health queueing.

## Estimated First Reading Load

| Phase | Papers | Purpose |
|---|---:|---|
| First pass | 15 | Establish the closest competitors and SUS/access backbone. |
| Second pass | 20 | Strengthen methods, validation, simulation and operational endpoints. |
| Selective pass | 15 | Add support for patient-flow prediction, no-show/scheduling, delayed discharge, bed allocation and explainability. |
| Total priority corpus | 50 | Enough to write a mature admission plan without drowning in low-signal literature. |

## Key Themes to Extract While Reading

- Unit of analysis: patient, request, appointment, queue, service, hospital, specialty, procedure or regulatory system.
- Computational task: waiting-time prediction, no-show prediction, service-time estimation, prioritization, patient flow, delayed discharge, demand-capacity estimation, queue simulation or decision support.
- Data requirements: timestamps, status transitions, specialty/procedure, priority, service capacity, appointment outcomes, no-show, cancellation, referral status and institutional unit.
- Evaluation design: temporal validation, external validation, simulation-only validation, retrospective validation, operational metrics, calibration and subgroup/equity checks.
- Decision target: manager-facing monitoring, risk identification, scenario analysis, prioritization support or workflow redesign.
- Limitations: single site, emergency-only focus, lack of SUS/regulation context, no external validation, no capacity data, weak explainability or no event-log modeling.

## Expected Gaps Before Writing the Final Proposal

- Few papers are likely to combine SUS regulation, event-level waiting-list data, explainable prediction and simulation in one study.
- Brazilian/SUS papers are expected to justify the access/regulation problem, but most will not provide advanced computational methods.
- Computational papers are expected to provide methods, but many are non-SUS, emergency-department-specific or generic hospital operations.
- Simulation papers may require capacity/slot/resource data that may not be available in the first project phase.
- Prioritization/fairness papers are useful, but the proposal should avoid promising autonomous patient ranking.

## Suggested Next Searches Only If Major Gaps Remain

Run additional searches only after reading Tier 1 and Tier 2:

- `SISREG` OR `e-SUS Regulação` AND `lista de espera` AND `dados` OR `regulação do acesso`
- `process mining` AND healthcare AND `referral` OR `waiting list`
- `event log` AND healthcare AND `waiting time` OR `patient flow`
- `explainable machine learning` AND `waiting time prediction` AND healthcare
- `discrete-event simulation` AND `referral management` AND healthcare
- `fairness` AND `healthcare waiting list` OR `patient prioritization`

## Practical Rule for Proposal Writing

Before drafting the final proposal, extract only what helps answer four admission questions:

- What is already known about waiting-list, queue and patient-flow modeling?
- What remains unsolved in SUS/regulation workflows?
- Why are explainable prediction and simulation a Computer Science contribution?
- What data are minimally required to make the project feasible?
