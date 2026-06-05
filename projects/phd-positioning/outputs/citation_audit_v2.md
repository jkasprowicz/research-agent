# Citation Audit of `plano_doutorado_v2.md`

Scope: paragraph-level audit of `outputs/plano_doutorado_v2.md` using `outputs/gap_validation_audit.md`, `outputs/v1_to_v2_changes.md`, all literature reviews, and all Tier 1/Tier 2 article notes.

Verdict: the proposal is scientifically coherent, but several high-value methodological claims need stronger citation support. The most exposed claims are not SUS/context claims; they are Computer Science claims about event-based representation, temporal validation, explainability for workflow action, and operational utility evaluation.

## Citation Audit Table

| Section | Paragraph | Claim | Citation needed? | Suggested references | Priority |
|---|---:|---|---|---|---|
| 1. Linha de pesquisa, tema e orientador | P1 | The project belongs to `Inteligência Computacional`. | No | Edital/Anexo theme, if allowed outside references. | Low |
| 1. Linha de pesquisa, tema e orientador | P2 | Event-based modeling, XAI and decision support fit regulation systems in health. | Yes | Cardoso et al. 2026; Shin et al. 2024; Wartelle et al. 2026; Thompson et al. 2024. | Medium |
| 1. Linha de pesquisa, tema e orientador | P3 | Advisor indication. | No | Not a scientific claim. | Low |
| 2. Título | P1 | The proposal is an event-based computational framework for explainable decision support. | No | Title claim; supported later. | Low |
| 3. Introdução | P1 | SUS regulation systems organize access to specialized care and requests move through multiple states. | Yes | Giannotti et al. 2025; Cardoso et al. 2026; Pazin-Filho et al. 2024; Lisboa et al. 2022. | High |
| 3. Introdução | P1 | Waiting lists are dynamic workflows rather than simple ordered lists. | Yes | Giannotti et al. 2025; Pazin-Filho et al. 2024; Salles et al. 2026; Cardoso et al. 2026. | High |
| 3. Introdução | P2 | Centralization, telehealth, active updating and access management can reduce backlog, costs or waits in SUS. | Yes | Gadenz et al. 2021; Pachito et al. 2022; Pfeil et al. 2025; Pazin-Filho et al. 2024; Antunes et al. 2025; Salles et al. 2026. | High |
| 3. Introdução | P2 | The contribution is not to demonstrate that queues exist, but to transform regulation histories into event representation. | Yes | Gap synthesis: Hroub et al. 2025; Cardoso et al. 2026; Pazin-Filho et al. 2024. Add process mining/event-log literature if available. | High |
| 3. Introdução | P3 | Regulation can be modeled as temporal events, states, transitions, outcomes and operational constraints. | Yes | Cardoso et al. 2026; Pazin-Filho et al. 2024; Wartelle et al. 2026; Shin et al. 2024. Missing seminal process-mining/event-log reference is a weakness. | High |
| 3. Introdução | P3 | Lack of reproducible representation limits model comparison, outcome definition, temporal validation and utility. | Yes | Hroub et al. 2025; Gloyn et al. 2026; Cardoso et al. 2026; phd_supervisor_gap_assessment. Add benchmarking/ML evaluation reference if V3 has space. | High |
| 3. Introdução | P3 | The artifact is a framework, not a local waiting-time classifier. | No | This is the proposal positioning, but it benefits indirectly from Shin et al. 2024 and Gagliotti & Gutierrez 2025 as contrast. | Medium |
| 3. Introdução | P4 | Historical SUS regulation data can be represented as events to identify problematic waiting-list behavior. | Yes | Pazin-Filho et al. 2024; Cardoso et al. 2026; Salles et al. 2026; Wartelle et al. 2026. | High |
| 3. Introdução | P4 | Human-in-the-loop support should avoid automating access decisions. | Yes | Hroub et al. 2025; Giannotti et al. 2025; Lisboa et al. 2022; Cardoso et al. 2026. | Medium |
| 4. Estado da arte | P1 | SUS waiting-list relevance is established. | Yes | Giannotti et al. 2025; Pazin-Filho et al. 2024; Antunes et al. 2025; Salles et al. 2026; Lemos et al. 2025 if retained. | High |
| 4. Estado da arte | P1 | Current SUS studies do not solve computational representation of regulatory flows. | Yes | Pazin-Filho et al. 2024; Antunes et al. 2025; Salles et al. 2026; Giannotti et al. 2025. Cite as contrast, but avoid overclaiming. | High |
| 4. Estado da arte | P2 | Remote regulation/telehealth reduces queues and costs. | Yes | Gadenz et al. 2021; Pachito et al. 2022; Pfeil et al. 2025. | High |
| 4. Estado da arte | P2 | SUS regulation architecture exists and addresses interoperability/monitoring/transparency. | Yes | Cardoso et al. 2026. | High |
| 4. Estado da arte | P2 | Infrastructure and process management do not eliminate need for analytical layers. | Yes | Cardoso et al. 2026; Hroub et al. 2025; Gloyn et al. 2026. This is inferential, so cite carefully. | Medium |
| 4. Estado da arte | P3 | Wait prediction, interpretability and queueing are already explored in healthcare. | Yes | Shin et al. 2024; Gloyn et al. 2026; Fall et al. 2025; Thompson et al. 2024; Wang et al. 2024; Wartelle et al. 2026. | High |
| 4. Estado da arte | P3 | Brazilian ML prioritization for cardiac surgery already exists. | Yes | Gagliotti & Gutierrez 2025. | High |
| 4. Estado da arte | P3 | Novelty is not applying ML/SHAP/queueing/optimization to another dataset. | Yes | Shin et al. 2024; Thompson et al. 2024; Wartelle et al. 2026; Wang et al. 2024; Gagliotti & Gutierrez 2025. | High |
| 4. Estado da arte | P4 | The scientific gap is integration of event representation, behavior taxonomy, temporal validation, XAI and operational evaluation in SUS regulation. | Yes | Strongly supported by synthesis, but each component needs literature contrast: Cardoso et al. 2026; Hroub et al. 2025; Shin et al. 2024; Wartelle et al. 2026; Thompson et al. 2024; Pazin-Filho et al. 2024. | High |
| 4. Estado da arte | P4 | Records can be converted into reproducible and transferable computational tasks. | Yes | Cardoso et al. 2026; Pazin-Filho et al. 2024. Missing event-log/process-mining references. | High |
| 5. Objetivos | P1 | Developing an event-based framework with auditability and temporal validation is the overall goal. | No | Objective statement; should be supported in previous sections. | Low |
| 5. Objetivos | P3 | Regulation systems can be formalized through events, states, transitions and timestamps. | Yes | Cardoso et al. 2026; Pazin-Filho et al. 2024; Wartelle et al. 2026. Missing formal event-log citation. | High |
| 5. Objetivos | P4 | Problematic behavior categories are scientifically justified. | Yes | Salles et al. 2026; Pazin-Filho et al. 2024; Gadenz et al. 2021; Fall et al. 2025; De-Carli et al. 2023; Cavalcanti et al. 2022. | High |
| 5. Objetivos | P5 | Baselines should be administrative, statistical and temporal. | Yes | Shin et al. 2024; Gloyn et al. 2026; Thompson et al. 2024. Add ML evaluation reference if possible. | Medium |
| 5. Objetivos | P6 | Temporal validation, calibration, subgroup performance and operational utility are appropriate evaluation axes. | Yes | Gloyn et al. 2026; Shin et al. 2024; Thompson et al. 2024; Hroub et al. 2025. Missing calibration/temporal validation seminal references. | High |
| 6. Metodologia | P1 | Retrospective pseudonymized regulation data are sufficient for initial study. | Yes | Pazin-Filho et al. 2024; Salles et al. 2026; Shin et al. 2024. | Medium |
| 6. Metodologia | P1 | Request/event history is a better unit than patient or aggregate waiting time. | Yes | Pazin-Filho et al. 2024; Wartelle et al. 2026; Cardoso et al. 2026. Missing process mining/event-log literature. | High |
| 6. Metodologia | P1 | Minimum viable fields are identifier, dates, status, specialty/procedure and outcome. | Yes | Pazin-Filho et al. 2024; Salles et al. 2026; Cardoso et al. 2026. | Medium |
| 6. Metodologia | P2 | Administrative records can be mapped into event-state-transition model. | Yes | Cardoso et al. 2026; Pazin-Filho et al. 2024; Wartelle et al. 2026. Missing BPM/process mining citations. | High |
| 6. Metodologia | P2 | Output of this phase is an analytic schema with derived variables and data-quality rules. | Yes | Salles et al. 2026; Cardoso et al. 2026. Add data-quality/information-systems reference if possible. | Medium |
| 6. Metodologia | P3 | Time waiting should not be the only outcome. | Yes | Gloyn et al. 2026; Hroub et al. 2025; Salles et al. 2026; Fall et al. 2025. | High |
| 6. Metodologia | P3 | Chosen behavior categories are observable and operationally relevant. | Yes | Salles et al. 2026; Pazin-Filho et al. 2024; Gadenz et al. 2021; Pfeil et al. 2025; Fall et al. 2025. | High |
| 6. Metodologia | P4 | Administrative baselines such as FIFO, priority and historical average are necessary comparators. | Yes | Thompson et al. 2024; Shin et al. 2024; Gloyn et al. 2026; Hroub et al. 2025. | High |
| 6. Metodologia | P4 | Models listed are reasonable for the data structure. | Yes | Shin et al. 2024; Gloyn et al. 2026; Fall et al. 2025; Mandizvida et al. 2024; Gagliotti & Gutierrez 2025. | Medium |
| 6. Metodologia | P4 | Auditability, stability and interpretability should dominate complexity. | Yes | Hroub et al. 2025; Shin et al. 2024; Cardoso et al. 2026. | Medium |
| 6. Metodologia | P5 | Temporal split reduces leakage and approximates prospective use. | Yes | Gloyn et al. 2026 notes implementation/generalization gaps, but a stronger ML validation reference is missing. | High |
| 6. Metodologia | P5 | Metrics listed are appropriate. | Yes | Shin et al. 2024; Gloyn et al. 2026; Fall et al. 2025; Thompson et al. 2024. Add calibration reference if possible. | Medium |
| 6. Metodologia | P6 | Explanations should be designed for regulation workflow, not only variable ranking. | Yes | Shin et al. 2024 as contrast; Hroub et al. 2025; Lisboa et al. 2022; Cardoso et al. 2026. | High |
| 6. Metodologia | P6 | Multi-level explanations by request, queue/specialty, unit/service and temporal aggregation are justified. | Yes | Cardoso et al. 2026; Pazin-Filho et al. 2024; Shin et al. 2024. Needs more direct DSS/XAI reference. | High |
| 6. Metodologia | P6 | Outputs should not authorize, deny or reorder access automatically. | Yes | Giannotti et al. 2025; Hroub et al. 2025; Lisboa et al. 2022. | Medium |
| 6. Metodologia | P7 | Retrospective operational utility evaluation is adequate without deployment. | Yes | Thompson et al. 2024; Wang et al. 2024; Kruik-Kolloffel et al. 2024; Wartelle et al. 2026. | High |
| 6. Metodologia | P7 | Simple retrospective scenarios depend on capacity/action data. | Yes | Wartelle et al. 2026; Wang et al. 2024; Lee et al. 2022; Kruik-Kolloffel et al. 2024. | Medium |
| 7. Contribuições | P1 | The artifact is composed of event model, taxonomy, tasks, baselines, temporal validation, XAI and operational criteria. | No | Proposal claim, but should be traceable to methods. | Medium |
| 7. Contribuições | P2 | Formalizing a health decision problem as a reproducible computational object is a CS contribution. | Yes | Cardoso et al. 2026; Wartelle et al. 2026; Thompson et al. 2024. Missing general CS/benchmarking reference. | High |
| 7. Contribuições | P2 | Novelty is articulation of event modeling, XAI and decision-support evaluation. | Yes | Gap matrix support: Cardoso et al. 2026; Shin et al. 2024; Hroub et al. 2025; Thompson et al. 2024; Wartelle et al. 2026. | High |
| 7. Contribuições | P3 | Components are transferable across regulation databases. | Yes | Cardoso et al. 2026 supports multi-region architecture, but transferability remains an assumption unless validated. | High |
| 7. Contribuições | P3 | Empirical validation in specific datasets can support broader scientific contribution. | Yes | Needs methodological/reference support. Current corpus supports indirectly only. | Medium |
| 7. Contribuições | P4 | The contribution is methodological/evaluative, not a new universal algorithm or deployment. | No | Positioning statement. | Low |
| 8. Viabilidade | P1 | Retrospective scope and no deployment/autonomous prioritization reduce risk. | Yes | Hroub et al. 2025; Giannotti et al. 2025; Lisboa et al. 2022. | Medium |
| 8. Viabilidade | P1 | Waiting-time prediction is not the central objective. | No | Scope statement; supported by previous contrast. | Low |
| 8. Viabilidade | P2 | Minimum dataset is enough for core event representation and initial modeling. | Yes | Pazin-Filho et al. 2024; Salles et al. 2026; Cardoso et al. 2026. This remains a feasibility assumption. | High |
| 8. Viabilidade | P2 | Restricting outcomes to observable fields mitigates data risk. | Yes | Salles et al. 2026; Pfeil et al. 2025; Cardoso et al. 2026. | Medium |
| 8. Viabilidade | P3 | Four-year schedule is feasible. | No/Weak | This is a planning claim; no paper citation needed, but it remains an admission risk if data access is uncertain. | Medium |

## Missing or Weak Reference Types

| Missing reference type | Why it matters | Priority |
|---|---|---|
| Process mining / event-log modeling in healthcare | The V2 central artifact is event-state-transition modeling, but current references only indirectly support it. | High |
| Temporal validation / leakage prevention in ML for health | Temporal validation is a core methodological claim; current corpus supports it only indirectly. | High |
| Calibration and clinical prediction model evaluation | Calibration is named, but not strongly grounded in cited references. | Medium |
| Human-centered explainable AI / decision-support evaluation | V2 claims manager-oriented explanations; current references are mostly SHAP/wait prediction or workflow context. | High |
| Data quality / missingness in health information systems | Data-quality claims are supported by Salles/Pfeil but would benefit from broader data-quality references. | Medium |
| Benchmark/task design or reproducibility frameworks | The "transferable computational artifact" claim needs general CS support beyond application papers. | Medium |

## Highest-Priority Citation Fixes Before Submission

1. Add one sentence with citations supporting regulation as event/state workflow, using Cardoso et al., Pazin-Filho et al., and ideally process-mining/event-log literature.
2. Add one citation set for temporal validation and leakage avoidance in health ML.
3. Add one citation set for XAI/decision support aimed at human workflow, not just SHAP.
4. Keep Gagliotti & Gutierrez in the references; it is dangerous but strategically necessary because it shows intellectual honesty about the direct competitor.
5. Avoid adding too many generic AI references; the proposal's weakness is not lack of AI citations but lack of event/DSS evaluation citations.
