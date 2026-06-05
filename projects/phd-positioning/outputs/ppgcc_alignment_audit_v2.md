# PPGCC Alignment Audit for `plano_doutorado_v2.md`

Evaluator roles: senior PPGCC reviewer, skeptical Computer Science professor, health informatics researcher, doctoral admission committee member.

## Section-by-Section Discipline Balance

| Section | Computer Science content (%) | Health content (%) | Management content (%) | Risk interpretation |
|---|---:|---:|---:|---|
| 1. Linha de pesquisa, tema e orientador | 70 | 20 | 10 | Strong CS alignment through event modeling, XAI and decision support. |
| 2. Título | 75 | 15 | 10 | Strong CS signal; "arcabouço computacional" helps substantially. |
| 3. Introdução, motivação e problema de pesquisa | 50 | 35 | 15 | Balanced, but paragraph 1 can look health-regulation-heavy before the CS artifact appears. |
| 4. Estado da arte e lacuna científica | 48 | 32 | 20 | Improved from V1, but still uses many SUS/management studies. CS contrast is present in paragraph 3. |
| 5. Objetivos | 75 | 15 | 10 | Strong CS alignment: formalization, taxonomy, models, validation, calibration, explicability. |
| 6. Encaminhamento metodológico | 80 | 10 | 10 | Strongest CS section. Event schema, baselines, temporal validation, model evaluation and XAI are clearly computational. |
| 7. Contribuições científicas esperadas para a Computação | 85 | 5 | 10 | Strong CS section. Explicitly defines artifact and transferability. |
| 8. Viabilidade, delimitação de escopo e cronograma | 55 | 20 | 25 | Mixed. The anti-deployment and feasibility framing is necessary, but it can read like project management rather than scientific contribution. |
| 9. Referências | 45 | 35 | 20 | Reference list is still heavy in SUS/health-services studies. Needs 2-4 stronger CS-method citations if V3 permits. |

## Global Balance Estimate

| Category | Estimated share |
|---|---:|
| Computer Science | 65% |
| Health / SUS domain | 23% |
| Management / operations administration | 12% |

Verdict: the proposal is likely to be perceived as a Computer Science PhD if reviewers read past the introduction. The title, objectives, methodology and contribution sections are strong. The main risk is that a fast reviewer may anchor on SUS/filas/regulação and classify the problem as Health Management before reaching the computational artifact.

## Sections That May Look Like Public Health

| Section/paragraph | Why it may look like Public Health | Risk |
|---|---|---|
| Section 3, P1 | Discusses SUS access, consultations, exams, procedures and regulation workflows before naming the computational artifact. | Medium |
| Section 3, P2 | Cites many Brazilian intervention studies about backlog, costs and waiting time. | Medium |
| Section 4, P1 | Strongly grounded in SUS waiting-list relevance, equity and access. | Medium |
| Section 4, P2 | Discusses telessaúde, regulação remota and architecture; may sound like digital health policy. | Low-medium |

## Sections That May Look Like Health Management

| Section/paragraph | Why it may look like Health Management | Risk |
|---|---|---|
| Section 3, P2 | "centralização", "organização do fluxo", "reduzir backlog" are management terms. | Medium |
| Section 4, P2 | "infraestrutura", "gestão de processos", "camadas analíticas" could be interpreted as operational management if CS terms are not emphasized. | Medium |
| Section 6, P7 | Retrospective operational utility and scenario language can look like operations management rather than CS evaluation. | Low-medium |
| Section 8, P1-P3 | Feasibility, scope and schedule naturally read as project management. | Low |

## Sections That Clearly Support a Computer Science PhD

| Section/paragraph | Why it supports CS |
|---|---|
| Section 2, title | "Arcabouço Computacional Baseado em Eventos" immediately signals a CS artifact. |
| Section 3, P3 | Defines the system as temporal events, states, transitions, outcomes and constraints. |
| Section 3, P4 | Frames the research problem as event representation and explainable modeling. |
| Section 5, objectives | Formalization, taxonomy, analytical tasks, explainable models, baselines and validation are CS-aligned. |
| Section 6, P1-P6 | Strong method core: unit of analysis, event-state-transition model, tasks, models, baselines, temporal validation, calibration and XAI. |
| Section 7, P1-P4 | Explicitly names artifact, scientific contribution, transferability and non-algorithmic methodological contribution. |

## PPGCC Criteria Estimate

| Criterion | Estimated score | Rationale |
|---|---:|---|
| Aderência aos temas de pesquisa | 8.7/10 | Strong alignment with Inteligência Computacional, XAI and applied AI for health. Risk: health management theme could still dominate for a skeptical reviewer. |
| Metodologia e fundamentação | 8.4/10 | Methodology is coherent and rigorous. Weakness: central event-schema/temporal-validation claims need stronger CS citations. |
| Relevância e viabilidade | 8.6/10 | Relevant, scoped and modular. Weakness: data access and observable outcomes remain uncertain. |
| Estimated `NPlano` | 8.6/10 | Competitive, but not yet bulletproof. |

## Recommendations Before V3

| Recommendation | Reason | Priority |
|---|---|---|
| Add 2-4 methodological CS references on process mining/event logs, temporal validation, calibration and XAI/DSS evaluation. | Current references over-support the domain and under-support the core computational artifact. | High |
| Move a CS artifact sentence earlier in the introduction if page budget allows. | Prevents reviewer from anchoring on Health Management. | Medium |
| Use "fluxos de regulação" and "eventos" more than "filas" where possible. | Reduces public-health/queue-management framing. | Medium |
| Keep the direct competitor Gagliotti & Gutierrez, but explicitly contrast it in one phrase. | Demonstrates honesty and protects novelty. | High |
| Narrow "operational utility" metrics in V3. | Prevents the committee from asking what utility means without deployment. | High |
| Do not add a large section on SUS policy. | Would increase Public Health perception and consume page budget. | High |
| Do not make simulation or queue optimization central. | Mature adjacent literature makes that risky and data-heavy. | High |

## Final Alignment Verdict

The proposal is **more PPGCC-aligned than V1** because it now clearly defines a computational artifact. However, the proposal still needs a slightly stronger CS citation backbone. A skeptical Computer Science reviewer may accept the framing but ask whether the event-based framework is truly a scientific contribution or only a structured ETL/data-modeling exercise. V3 should preempt that by citing event-log/process-mining and validation literature and by sharpening the evaluation framework.
