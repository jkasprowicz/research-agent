# Reviewer Attack Simulation and Final Verdict for `plano_doutorado_v2.md`

Role simulated: hostile PPGCC reviewer, skeptical Computer Science professor, health informatics researcher, doctoral admission committee member.

## The 15 Strongest Criticisms That Could Reject the Proposal

| # | Criticism | Severity | Validity | Rebuttal possibility | Recommended fix |
|---:|---|---|---|---|---|
| 1 | The proposal may still be Health Management disguised as Computer Science. | High | Partially valid | Good. The title, objectives and methodology are computational, but the introduction is SUS-heavy. | Make the CS artifact visible in the first substantive paragraph; preserve event schema, validation and XAI vocabulary. |
| 2 | The central novelty, "event-based representation", may be only data modeling/ETL, not PhD-level research. | High | Valid risk | Moderate. It becomes PhD-level only if linked to task definitions, validation, baselines and transferability. | Add process-mining/event-log references and frame the artifact as a reproducible modeling/evaluation framework. |
| 3 | Waiting-time prediction, XAI and queueing are already solved in adjacent literature. | High | Valid | Strong if the proposal keeps saying novelty is not those methods. | Keep explicit contrast with Shin, Gloyn, Thompson, Wartelle and Wang. |
| 4 | There is already Brazilian ML for waiting-list prioritization in cardiac surgery. | High | Valid | Strong if differentiated by workflow scope, multiple events, multiple outcomes and human-in-the-loop DSS. | Mention that this is procedure-specific and does not provide a regulation-event framework. |
| 5 | SUS regulation architecture already exists; the proposed system may duplicate Cardoso et al. | High | Partially valid | Moderate. V2 positions itself as analytic layer, not architecture. | Add one clear phrase: "complementar a arquiteturas de regulação, não substituí-las". |
| 6 | The gap is an integration gap, not a fundamental CS research gap. | High | Partially valid | Moderate. Integration can be PhD-level if formalized as reusable framework/evaluation protocol. | Emphasize scientific artifacts: schema, taxonomy, benchmark tasks, validation protocol, explanation templates. |
| 7 | The proposal's transferability claim is weak because validation may occur in one local dataset. | High | Valid | Moderate. Transferability can be conceptual if components are defined generically, but empirical proof may be limited. | Use "potencialmente transferível" unless multiple datasets are guaranteed; define what transfers. |
| 8 | Data access and data completeness are major unresolved risks. | High | Valid | Moderate. The minimum viable dataset helps, but does not guarantee meaningful outcomes. | In V3, explicitly list core outcomes supported by minimum fields and optional outcomes requiring richer data. |
| 9 | "Problematic behavior" may remain too broad and subjective. | High | Partially valid | Good. V2 narrowed to four families, but definitions need thresholds and operational criteria. | Add concise operational definitions or examples for each family. |
| 10 | Retrospective utility evaluation may not prove usefulness for real managers. | Medium-high | Valid | Moderate. Retrospective evaluation is acceptable for admission, but weaker than stakeholder validation. | Add optional structured expert review if feasible, without promising deployment. |
| 11 | Temporal validation is asserted but not grounded in references or detail. | Medium-high | Valid | Good. Easy to fix with citations and one concise method phrase. | Add temporal split/leakage/covariate drift citations and clarify period-based split. |
| 12 | Explainability may collapse into SHAP plots, which is not novel. | Medium-high | Valid | Good. V2 says explanations must be workflow-oriented. | Add XAI/DSS references and define explanation outputs as case/queue/service-level summaries. |
| 13 | The proposal has too many methodological components for 4 years: schema, taxonomy, models, XAI, validation, subgroups, scenarios. | Medium | Partially valid | Good. V2 modularizes the work. | Mark scenario/subgroup analysis as conditional; keep core as schema + taxonomy + validation + XAI. |
| 14 | The health impact is plausible but not measurable without implementation. | Medium | Valid | Moderate. Admission plans do not need deployment, but impact claims must be modest. | Use "apoio retrospectivo/prospectivo à análise" rather than impact on waiting times. |
| 15 | The reference list is too domain-heavy and lacks seminal CS/method references. | Medium-high | Valid | Strong fix possible. | Add 2-4 CS-method references; remove weak/generic or less central domain references if page/list length matters. |

## Final Verdict

| Dimension | Assessment |
|---|---|
| Estimated admission score | **8.4-8.7/10** under a fair committee; **7.8-8.2/10** under a hostile CS-heavy reviewer. |
| Strongest aspect | The V2 successfully reframes the project around a computational artifact: event-based representation, taxonomy, temporal validation, explainable decision support and evaluation framework. |
| Weakest aspect | The methodological novelty still depends on claims that need stronger CS citations, especially event-log/process modeling, temporal validation, calibration and human-centered XAI/DSS evaluation. |
| Probability that the novelty claim survives scrutiny | **70%** as currently written; **82-85%** if V3 adds targeted CS-method citations and sharper operational definitions. |
| Probability that the proposal is perceived as Computer Science | **75%** as currently written; **85%+** if the first page foregrounds the computational artifact earlier and reduces management vocabulary. |
| Recommendation | **B) Minor revisions needed**, but they are strategically important. Do not create a new topic or rewrite from scratch; tighten citations, definitions and CS framing. |

## Hard-Line Admission Decision

If I were a strict admission reviewer, I would not reject V2 outright. I would score it as competitive but not yet maximally polished. It is stronger than V1 because it avoids weak novelty claims around waiting-time prediction and generic queue optimization. Its main remaining vulnerability is methodological anchoring: the proposal now claims a stronger CS artifact than its current citations fully support.

## Mandatory Fixes Before Final Submission

1. Add event-log/process-mining or workflow modeling citations.
2. Add temporal validation/leakage/covariate shift or clinical ML evaluation citations.
3. Add human-centered XAI or decision-support evaluation citations.
4. Define the four problematic behavior families more operationally.
5. Make explicit that the framework complements existing SUS regulation architectures.
6. Keep simulation and subgroup analysis conditional.
7. Preserve "human-in-the-loop" and "no autonomous prioritization" language.

## Bottom Line

The proposal is scientifically defensible but not invulnerable. The committee can attack it as a local applied health-management project unless V3 makes the computational contribution even more explicit and methodologically referenced. The right next step is **minor but surgical revision**, not another conceptual pivot.
