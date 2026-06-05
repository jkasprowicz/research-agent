# Final Submission Readiness Report

## Scope

This report evaluates `plano_doutorado_v3.md` after the targeted fixes recommended in:

- `citation_audit_v2.md`
- `gap_validation_matrix.md`
- `competitor_matrix.md`
- `ppgcc_alignment_audit_v2.md`
- `reviewer_attack_simulation_v2.md`

The selected topic was preserved: **Apoio à decisão baseado em inteligência artificial explicável para gestão de filas de espera em sistemas de regulação do SUS**.

## Readiness Scores

| Dimension | Estimated score | Rationale |
|---|---:|---|
| Adherence to edital and PPGCC framing | 9.0/10 | The plan follows the expected structure, foregrounds the research line, title, problem, objectives, methodology, expected contributions, feasibility and references. The first page now signals the computational artifact immediately. |
| Methodology score | 8.8/10 | The methodology is coherent, modular and now better grounded in event-log modeling, process mining, temporal validation, calibration, human-centered XAI and decision-support evaluation. |
| Relevance score | 8.8/10 | The problem is practically relevant for SUS regulation and scientifically framed as a Computer Science contribution. The proposal avoids unsupported promises of deployment or autonomous prioritization. |
| Feasibility score | 8.7/10 | The minimum viable dataset reduces risk, and optional analyses are clearly conditional on data availability. The main risk remains access, completeness and granularity of regulation data. |
| Originality score | 8.5/10 | The novelty is defensible as an event-based computational and evaluation framework, not as a new ML algorithm. This is strong enough for admission, though not invulnerable to a reviewer seeking algorithmic novelty. |
| Overall expected NPlano | 8.8/10 | Competitive and substantially safer than V2 under a skeptical Computer Science reading. |

## Strongest Aspects of V3

1. **Computational artifact appears immediately.** The introduction no longer starts as a health-management discussion; it begins with the event-based framework.
2. **Methodological backbone is stronger.** Process mining, event logs, temporal validation, calibration, human-centered XAI and decision-support evaluation are now cited.
3. **Problematic behaviors are operational.** The four behavior families are defined using observable or derivable criteria.
4. **Competitor distinction is explicit.** Shin et al., Gagliotti and Gutierrez, Cardoso et al. and Wartelle et al. are no longer only cited; the proposal explains what it does differently.
5. **Ethical and scope boundaries are clear.** The framework complements regulation systems, does not replace them and does not autonomously prioritize patients.

## Remaining Weaknesses

| Weakness | Severity | Mitigation in V3 | Residual risk |
|---|---|---|---|
| Data access and completeness are uncertain | High | Minimum viable dataset is defined; richer variables are optional. | If only sparse status/date fields are available, model complexity and operational utility may be limited. |
| Transferability may be hard to prove empirically | Medium-high | V3 uses "potencialmente transferível" and defines transferable components. | A reviewer may ask whether one dataset is enough to support transferability. |
| Contribution is formalization/evaluation, not new algorithm | Medium | V3 frames novelty as event representation plus task, validation and explanation framework. | A strongly algorithm-oriented reviewer may score originality more conservatively. |
| Retrospective utility is weaker than real deployment evaluation | Medium | V3 explicitly avoids deployment and defines retrospective utility criteria. | A reviewer may still ask how usefulness to managers will be established. |
| Reference list is longer | Low | References are outside the body/page limit. | The final DOCX must keep references clearly separated. |

## Reviewer Attack Survival

| Attack point | V3 status |
|---|---|
| "This is Health Management, not Computer Science." | Mostly rebutted. The first sentence, objectives, methodology and contributions are computational. |
| "Event modeling is just ETL." | Rebuttable. V3 connects event modeling to task definition, baselines, validation, XAI and utility evaluation. |
| "Waiting-time prediction is already solved." | Rebutted. V3 explicitly states waiting-time prediction is not central. |
| "Gagliotti and Gutierrez already did ML prioritization in Brazilian waiting lists." | Rebutted. V3 does not propose autonomous/procedure-specific prioritization. |
| "Cardoso et al. already proposed the regulation architecture." | Rebutted. V3 is positioned as a complementary analytic layer. |
| "SHAP explanations are not novel." | Rebutted. V3 emphasizes workflow-oriented explanation and human-AI interaction. |
| "There is no proof of operational value." | Partially rebutted. V3 defines retrospective operational utility, but deployment-level proof remains outside scope. |

## Page-Limit Readiness

The markdown body before references contains approximately **2,182 words**. The DOCX was rendered and visually inspected using A4, Times New Roman 12, single spacing and compact section spacing. The proposal body occupies **pages 1-4**, and the references begin on **page 5**, preserving the four-page limit excluding references.

## Final Recommendation

**Ready for Submission.**

The proposal is not flawless, but it is now strategically optimized for admission. It is scientifically defensible, computationally framed, realistic, and cautious about scope. The remaining weaknesses are appropriate topics for oral defense rather than reasons to delay submission.
