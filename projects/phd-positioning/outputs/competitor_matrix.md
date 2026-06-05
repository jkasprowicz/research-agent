# Competitor Matrix for `plano_doutorado_v2.md`

Legend: `High` = central component; `Partial` = present but not central or not fully evaluated; `Low/No` = absent or weak in article notes.

## Matrix

| Study | Waiting time prediction | Queue modelling | Event modelling | Explainability | Decision support | Temporal validation | SUS context | Operational evaluation |
|---|---|---|---|---|---|---|---|---|
| **Proposed V2** | Partial; not central | Partial; secondary | High | High | High | High intent | High | High intent, retrospective |
| Gloyn et al. 2026, AI for ED wait-time prediction | High | Partial queue features | Partial | Partial | Partial | Partial/unclear | No | Low/partial |
| Shin et al. 2024, interpretable outpatient wait prediction | High | Partial queue features | Partial hospital event logs | High | Partial | Partial/unclear | No | Partial |
| Fall et al. 2025, no-show/service-time prediction | Partial | Low | Partial scheduling data | Low/unclear | Partial scheduling support | Partial/unclear | No | Partial |
| Mandizvida et al. 2024, public-hospital delay classification | High delay classification | Low | Partial | Low | Partial | Partial/unclear | No | Low/modest |
| Gagliotti & Gutierrez 2025, cardiac-surgery ML prioritization | Partial | Low | Low/partial | Low/unclear | Partial prioritization support | Partial/unclear | Brazil, SUS-like cardiac context | Low/unclear |
| Pazin-Filho et al. 2024, Brazilian surgical queue management | High descriptive waiting time | Partial empirical queue management | Partial inflow/outflow/status | No | High managerial queue system | Retrospective time-series | High | High |
| Antunes et al. 2025, cardiac-surgery access management | High descriptive wait reduction | Low | Low | No | Partial management program | Pre-post | High | High |
| Salles et al. 2026, speech-therapy waiting-list update | Partial descriptive | Low | Partial status/update data | No | Partial list-cleaning support | No | High | Partial |
| Giannotti et al. 2025, SUS specialized waiting-list concept | No | Conceptual | Conceptual | No | Conceptual governance | No | High | No |
| Gadenz et al. 2021, telehealth referral management | High aggregate wait/list reduction | Partial referral queue context | Low/partial aggregate | No | High operational referral management | Before-after monthly | High | High |
| Pachito et al. 2022, referral management micro-costing | No/low | Low | Low | No | Partial cost decision support | No | High | Cost evaluation |
| Pfeil et al. 2025, telemedicine gatekeeping | Partial wait-list/cost outcomes | Partial gatekeeping context | Low/partial | No | High operational gatekeeping | Retrospective | High | High cost/throughput |
| Cardoso et al. 2026, SUS regulation architecture | Low | Partial queue-management functionality | Partial architecture entities/events | No/low | High information-system architecture | No/unclear | High | Partial architecture evaluation |
| Hroub et al. 2025, waiting-list management review | Partial review | Partial review | Low | Partial review | High review of tools | No | No/low | Review-level implementation gap |
| Wartelle et al. 2026, data-driven queueing simulation | Partial | High | High patient-flow states | Low | High scenario support | Partial validation | No | High in ED |
| Thompson et al. 2024, AI triage queueing | Partial wait-time savings | High | Low/abstract | No | High deployment-evaluation logic | Simulation/analytical | No | High analytical/simulation |
| Wang et al. 2024, queueing DSS for HIV VL machines | Turnaround-time focus | High | Low/partial network events | No | High resource-allocation DSS | Scenario/model-based | No | High public-health operations |
| Lee et al. 2022, physician-customized queueing optimization | High outpatient wait | High | Partial session data | Low | High strategy optimization | Partial/unclear | No | Partial, modeled not field-validated |
| Kruik-Kolloffel et al. 2024, medication reconciliation queueing | Partial workflow delay | High | Partial workflow events | No | High intervention comparison | Scenario/computer experiment | No | High workflow experiment |
| Lim et al. 2023, obstetric OR queueing | Partial probability of wait | High | Low | No | Staffing/capacity support | Retrospective parameters | No | High operational modelling |
| Wood et al. 2022, delayed transfers queueing | Delay/capacity focus | High | Low | No | Policy/economic support | Model-based | No | High economic scenario |
| Cavalcanti et al. 2022, specialized oral access | Descriptive waiting time | Low | Low | No | Low/partial management insight | Cross-sectional | High | Partial association |
| De-Carli et al. 2023, oral biopsy waiting | Descriptive scheduling delay | Low | Low | No | Low/partial management insight | Cross-sectional | High | Partial association |
| Lisboa et al. 2022, regulatory nurse workflow | Descriptive wait improvement | Low | Partial workflow states | No | High human workflow | No | High | Low/experience report |

## Where the Proposal Overlaps

| Overlap area | Main overlapping studies | Risk |
|---|---|---|
| Waiting-time and delay prediction | Gloyn et al. 2026; Shin et al. 2024; Mandizvida et al. 2024 | High if proposal drifts back to prediction as the headline. |
| ML prioritization in Brazilian waiting lists | Gagliotti & Gutierrez 2025 | High; direct competitor. Must differentiate from procedure-specific clinical prioritization. |
| SUS queue management | Pazin-Filho et al. 2024; Antunes et al. 2025; Salles et al. 2026 | Medium; proposal must not claim to invent queue management. |
| Referral management and gatekeeping | Gadenz et al. 2021; Pachito et al. 2022; Pfeil et al. 2025 | Medium; proposal should model workflows, not re-evaluate telehealth. |
| Regulation architecture | Cardoso et al. 2026 | Medium-high; proposal must be analytic/evaluative layer, not architecture. |
| Queueing/simulation/operations | Wartelle et al. 2026; Thompson et al. 2024; Wang et al. 2024; Lee et al. 2022 | High if proposal suggests novelty in queueing/simulation itself. |
| XAI for waiting | Shin et al. 2024 | High if proposal claims SHAP/explainability alone is novel. |

## Where the Proposal Differs

| Difference | Why it matters |
|---|---|
| It treats regulation as event-state-transition workflow, not only waiting-time outcome. | This is the clearest CS artifact if supported with enough methodological references. |
| It defines problematic waiting-list behaviors beyond raw waiting time. | This separates it from generic wait prediction and broadens scientific contribution. |
| It explicitly avoids autonomous prioritization. | This reduces ethical and admission risk. |
| It centers temporal validation and administrative baselines. | This makes it more rigorous than one-off model application. |
| It targets manager/regulator explanation, not only model interpretability. | This distinguishes from SHAP-only outpatient wait prediction. |
| It positions itself as an analytical layer over regulation systems. | This avoids conflict with Cardoso et al.'s architecture work. |
| It aims for transferable components: event schema, tasks, baselines, metrics and explanation templates. | This is the key defense against "local applied study" criticism. |

## Where Novelty Exists

| Novelty claim | Strength | Caveat |
|---|---|---|
| Event-based computational representation for SUS regulation waiting-list dynamics | Moderate-high | Needs process-mining/event-log citations or explicit methodological grounding in V3. |
| Taxonomy of problematic waiting-list behavior | Moderate-high | Must not become an arbitrary list; needs operational definitions. |
| Temporal validation protocol for regulation-event models | Moderate | Strong idea, but current cited corpus weakly supports temporal validation. |
| Manager-oriented XAI for regulation workflows | Moderate-high | Needs stronger XAI/DSS literature beyond Shin et al. |
| Retrospective operational utility evaluation without deployment | Moderate | Needs clear metrics; risk of being seen as weak utility without stakeholder evaluation. |
| Transferable framework rather than local model | Moderate | Valid only if the thesis produces reusable schema/tasks/metrics and not just site-specific results. |

## Most Dangerous Competitors

1. **Gagliotti & Gutierrez 2025**: directly threatens any claim that ML for Brazilian waiting-list prioritization is novel.
2. **Shin et al. 2024**: directly threatens any claim that interpretable waiting-time prediction is novel.
3. **Cardoso et al. 2026**: threatens any claim that regulation architecture or queue-management infrastructure is absent in SUS.
4. **Pazin-Filho et al. 2024**: threatens any claim that event-like queue management in Brazilian public hospitals is unexplored.
5. **Wartelle et al. 2026 / Thompson et al. 2024 / Wang et al. 2024**: threaten generic claims about queueing, simulation or operational DSS novelty.

## Brutal Takeaway

The V2 novelty survives only if the proposal is defended as:

> A reproducible event-based computational and evaluation framework for explainable, human-in-the-loop decision support in SUS regulation workflows.

It does not survive if reduced to:

> Applying machine learning or SHAP to predict waiting time in SUS queues.
