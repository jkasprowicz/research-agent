# Admission Evaluation of the Top 5 SUS Waiting-List PhD Projects

## Basis for Evaluation

Sources used:

- `outputs/edital_sus_plan_requirements.md`
- `literature/reviews/phd_project_portfolio.md`
- `literature/reviews/phd_supervisor_gap_assessment.md`
- `literature/reviews/integrative_review.md`
- `outputs/jonatan_tyska_followup_brief.md`

The PPGCC/UFSC plan evaluation is interpreted through the three plan criteria:

| Edital criterion | Admission interpretation |
|---|---|
| Aderência aos temas de pesquisa | Must clearly fit `Inteligência Computacional` and Jônata Tyska Carvalho's theme of AI methods for health/specific domains. |
| Metodologia e fundamentação | Must show state-of-the-art grounding, clear objectives, realistic methods, validation, references and Computer Science rigor. |
| Relevância e viabilidade | Must be original, feasible in four years, scoped enough for a working professional and not dependent on uncertain national deployment. |

Important admission constraint: the plan should avoid candidate-identifying information, overpromising data access, autonomous prioritization language and an overly public-health-only framing.

## Summary Ranking for Admission

| Admission rank | Project | Expected proposal score | Main reason |
|---:|---|---:|---|
| 1 | Explainable Decision Support for Problematic Waiting-List Behavior in SUS Regulation Workflows | 9.0/10 | Best balance of AI, health informatics, decision support, feasibility and advisor fit. |
| 2 | Referral Adequacy and Demand-Redirection Prediction for Specialized Care | 8.4/10 | Strong SUS/referral-management relevance and AI fit, but more dependent on regulator decision labels. |
| 3 | Stale-Demand and Data-Quality Intelligence for SUS Waiting Lists | 8.2/10 | Very feasible and practical, but may look less ambitious as a full CS doctorate if isolated. |
| 4 | Hybrid Machine Learning and Queueing Simulation for Specialized-Care Regulation Policies | 8.1/10 | Strong CS/OR contribution, but higher data and overreach risk for admission. |
| 5 | Fairness-Aware Prioritization Support for SUS Waiting Lists | 7.9/10 | Highest scientific/social novelty, but highest defense risk due to ethics, prioritization and sensitive-data requirements. |

## 1. Explainable Decision Support for Problematic Waiting-List Behavior in SUS Regulation Workflows

| Dimension | Evaluation |
|---|---|
| Expected score during proposal evaluation | **9.0/10**. Aderência: 9.2; metodologia/fundamentação: 8.8; relevância/viabilidade: 9.0. |
| Alignment with PPGCC | Very strong. It is clearly a Computer Science project: event-log modeling, predictive modeling, explainable AI, decision support, temporal validation and healthcare AI. |
| Alignment with advisor interests | Very strong. It matches AI methods for health and domain-specific AI without forcing pure operations research. Simulation can be optional. |
| Scientific maturity | High. It synthesizes the literature without overclaiming novelty: waiting-list management exists, but explainable AI decision support for SUS regulation is not solved. |
| Feasibility | High if at least one event-level regulation dataset is available. It can be executed retrospectively and staged into publishable studies. |
| Defense risk during oral examination | Low to moderate. Main risks: data access, scope breadth and how "problematic behavior" is defined. These are manageable with a staged design. |

**Admission assessment:** This is the safest strong project. It is mature, computational, feasible and defensible.

## 2. Hybrid Machine Learning and Queueing Simulation for Specialized-Care Regulation Policies

| Dimension | Evaluation |
|---|---|
| Expected score during proposal evaluation | **8.1/10**. Aderência: 8.6; metodologia/fundamentação: 8.8; relevância/viabilidade: 6.9. |
| Alignment with PPGCC | Very strong from a CS/OR perspective. It has ML, queueing, simulation and decision support. |
| Alignment with advisor interests | Good, but slightly less direct if the advisor expects AI/health rather than operations-research-heavy simulation. |
| Scientific maturity | High, but only if the plan clearly states that simulation depends on capacity/slot data and will be introduced after event-log modeling. |
| Feasibility | Moderate. Requires richer data: capacity, slots, service rates, policy changes and historical queue trajectories. |
| Defense risk during oral examination | Moderate to high. Reviewers may ask whether capacity data exist and whether simulation is too ambitious for four years. |

**Admission assessment:** Excellent as a methodological layer, risky as the headline project. It should be included as an optional or third-stage component, not the central admission promise.

## 3. Fairness-Aware Prioritization Support for SUS Waiting Lists

| Dimension | Evaluation |
|---|---|
| Expected score during proposal evaluation | **7.9/10**. Aderência: 8.4; metodologia/fundamentação: 8.2; relevância/viabilidade: 7.0. |
| Alignment with PPGCC | Strong. Fairness-aware AI, responsible ML and health decision support are CS-relevant. |
| Alignment with advisor interests | Good to strong, assuming the advisor is comfortable with responsible AI/fairness as part of AI for health. |
| Scientific maturity | Very high conceptually. It addresses a real unsolved gap: equity is discussed in SUS literature but rarely operationalized computationally. |
| Feasibility | Moderate to low unless the dataset includes usable demographic, geographic, priority and vulnerability variables. |
| Defense risk during oral examination | High. Reviewers may worry about automated prioritization, protected attributes, political sensitivity, ethics approval and whether fairness metrics are valid in this context. |

**Admission assessment:** Best high-impact research direction, but not the safest admission core. It should be framed as an evaluation layer within a decision-support project, not as autonomous prioritization.

## 4. Stale-Demand and Data-Quality Intelligence for SUS Waiting Lists

| Dimension | Evaluation |
|---|---|
| Expected score during proposal evaluation | **8.2/10**. Aderência: 8.0; metodologia/fundamentação: 7.8; relevância/viabilidade: 8.8. |
| Alignment with PPGCC | Moderate to strong. It fits data mining, information systems, data quality and applied AI, but may appear less ambitious if not connected to broader decision support. |
| Alignment with advisor interests | Good, especially as AI/data methods for health operations. Less aligned if presented as mostly data cleaning. |
| Scientific maturity | Good. It is grounded in direct SUS evidence that waiting lists contain obsolete or changed demand. |
| Feasibility | Very high. It can be executed with fewer variables than simulation/fairness projects and is a strong first-paper candidate. |
| Defense risk during oral examination | Low to moderate. Main risk: reviewers may say it is too incremental or operational rather than a PhD-level CS problem. |

**Admission assessment:** Safest technically, but not the strongest standalone doctorate. It is best as Objective 1 or Paper 1 inside the broader decision-support thesis.

## 5. Referral Adequacy and Demand-Redirection Prediction for Specialized Care

| Dimension | Evaluation |
|---|---|
| Expected score during proposal evaluation | **8.4/10**. Aderência: 8.7; metodologia/fundamentação: 8.2; relevância/viabilidade: 8.4. |
| Alignment with PPGCC | Strong. It involves predictive modeling, XAI, health informatics, classification, possibly NLP and decision support. |
| Alignment with advisor interests | Strong. It fits AI methods for health and the advisor-suggested SUS access/regulation direction. |
| Scientific maturity | Good to high. It is grounded in telehealth/gatekeeping literature and addresses avoidable demand in specialized care. |
| Feasibility | Moderate to high if decision labels exist: accepted, returned, denied, redirected, resolved in primary care, scheduled or completed. Lower if only queue status is available. |
| Defense risk during oral examination | Moderate. Reviewers may ask whether predicting adequacy becomes clinical triage and how safety/false negatives will be handled. |

**Admission assessment:** Very competitive, especially if referral-management data are likely. It is slightly narrower and more label-dependent than Project 1.

## Comparative Risk Matrix

| Project | Admission strength | Main defense attack | Best mitigation |
|---|---|---|---|
| Explainable decision support | Highest | "What exactly is problematic behavior?" | Define outcomes: excessive wait, stagnation, stale demand, no-show/dropout, priority-time violation and bottleneck risk. |
| Hybrid ML + simulation | High but risky | "Do you have capacity/slot data for simulation?" | Make simulation conditional and staged after event-log modeling. |
| Fairness-aware prioritization | High-impact but risky | "Are you deciding who gets care?" | Frame as fairness audit and human-in-the-loop support, not automated prioritization. |
| Stale-demand intelligence | Very feasible | "Is this just data cleaning?" | Embed it as a data-quality layer for predictive decision support. |
| Referral adequacy prediction | Strong | "Could this deny access incorrectly?" | Emphasize regulator support, conservative thresholds, explainability and false-negative safety analysis. |

## Recommendations

### 1. Best project for admission probability

**Explainable Decision Support for Problematic Waiting-List Behavior in SUS Regulation Workflows**

This is the best admission project because it scores strongly on all three edital criteria. It is aligned with `Inteligência Computacional`, clearly connected to AI for health, feasible with retrospective data, and broad enough for a doctorate without sounding like a national platform.

### 2. Best project for scientific impact

**Fairness-Aware Prioritization Support for SUS Waiting Lists**

This has the highest originality and social/scientific impact because fairness in SUS waiting-list AI is underdeveloped. However, it carries the highest admission risk because it depends on sensitive variables, careful ethics, and a very precise explanation that the system does not automate access decisions.

### 3. Best project balancing admission and impact

**Explainable Decision Support for Problematic Waiting-List Behavior in SUS Regulation Workflows**, with **fairness and simulation as evaluation layers**.

This balance is stronger than choosing fairness or simulation as the headline. It lets the proposal appear mature, feasible and computational while preserving room for high-impact publications.

## Final Doctoral Theme Optimized for PPGCC/UFSC Approval

**Theme**

Explainable artificial intelligence and event-based modeling for decision support in SUS waiting-list regulation workflows.

**Optimized title**

**Modelagem Preditiva Explicável para Apoio à Decisão em Filas de Espera de Sistemas de Regulação do SUS**

**Slightly more CS-explicit title**

**Inteligência Artificial Explicável para Modelagem e Apoio à Decisão em Filas de Espera de Sistemas de Regulação do SUS**

**Most admission-safe title**

**Apoio à Decisão Baseado em Inteligência Artificial Explicável para Gestão de Filas de Espera em Sistemas de Regulação do SUS**

## Recommended Final Positioning

For the submission, use the admission-safe framing:

> The project aims to develop and evaluate explainable AI methods for modeling problematic waiting-list behavior in SUS regulation workflows, supporting managers through risk detection, bottleneck explanation and retrospective scenario analysis.

Avoid making simulation, fairness or prioritization the title-level promise. Include them as controlled methodological components:

- **Core:** event-level modeling and explainable prediction.
- **Feasibility layer:** stale-demand/data-quality analysis.
- **Decision-support layer:** manager-facing explanations and risk indicators.
- **Evaluation layer:** fairness audit and, if data permit, scenario simulation.

This positioning maximizes approval probability while keeping the project scientifically strong.

