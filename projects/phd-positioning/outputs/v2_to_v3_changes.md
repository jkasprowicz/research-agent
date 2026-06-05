# V2 to V3 Changes

## Summary

V3 preserves the selected doctoral topic and performs only surgical revisions. The proposal remains centered on an event-based computational framework for explainable, human-in-the-loop decision support in SUS regulation workflows. No new research direction was introduced.

## Mandatory Fixes Implemented

| Required fix | V3 implementation |
|---|---|
| Add methodological references for process mining and event-log modeling | Added van der Aalst (2016) and Rojas et al. (2016) in the introduction and methodology to support event-log/process-mining framing. |
| Add references for temporal validation and calibration | Added Steyerberg and Vergouwe (2014) and Van Calster et al. (2019) in the validation paragraph. |
| Add references for human-centered XAI | Added Amershi et al. (2019) and Tonekaboni et al. (2019) in the explainability paragraph. |
| Add references for decision-support evaluation | Added Friedman and Wyatt (2006) and Kawamoto et al. (2005) in the retrospective operational utility paragraph. |
| Define four problematic behavior families operationally | Expanded the methodology to define espera excessiva contextualizada, estagnação, saída não resolutiva and risco de gargalo using observable criteria. |
| State that the framework complements regulation architectures | Added explicit language in the introduction: the framework complements existing architectures and does not replace institutional systems. |
| State that it does not perform autonomous prioritization | Reinforced in the introduction, methodology, contributions and scope sections. |
| Move computational artifact earlier | The first sentence of the introduction now names the central computational artifact. |
| Strengthen distinction from Shin et al. | Clarified that V3 is not centered on individual waiting-time prediction. |
| Strengthen distinction from Gagliotti and Gutierrez | Clarified that V3 does not propose procedure-specific clinical prioritization or autonomous prioritization. |
| Strengthen distinction from Cardoso et al. | Clarified that V3 is an analytic/evaluative layer, not a regulation-system architecture. |
| Strengthen distinction from Wartelle et al. | Clarified that V3 does not claim a central contribution in queue simulation. |
| Preserve page limits | Body remains compact at approximately 2,182 words before references. References remain outside the body/page-limit assumption. |

## Main Scientific Repositioning Inside the Same Topic

V2 already avoided the weak framing of "waiting-time prediction". V3 makes that defense more explicit by positioning the thesis as a framework with six coupled components:

1. Event-state-transition representation.
2. Computable taxonomy of problematic behaviors.
3. Analytical tasks and administrative baselines.
4. Temporal validation and calibration protocol.
5. Workflow-oriented explainability.
6. Retrospective operational utility criteria.

This strengthens the argument that the project is a Computer Science contribution rather than a local health-management application.

## Citation Strategy Changes

The reference list was made more balanced. V2 was strong in SUS/domain references but relatively weak in methodological Computer Science references. V3 adds a targeted methodological backbone without excessive citation stacking.

New methodological references added:

- van der Aalst (2016) for process mining and event-log modeling.
- Rojas et al. (2016) for process mining in healthcare.
- Steyerberg and Vergouwe (2014) for model development and validation.
- Van Calster et al. (2019) for calibration.
- Amershi et al. (2019) for human-AI interaction.
- Tonekaboni et al. (2019) for clinical end-use XAI.
- Friedman and Wyatt (2006) for biomedical informatics evaluation.
- Kawamoto et al. (2005) for clinical decision-support evaluation.

## Risk Reduction

V3 directly reduces the main attack points identified in the audits:

- It reduces the risk of being perceived as Health Management by foregrounding the computational artifact in the first sentence.
- It reduces the risk of being perceived as ETL by linking event representation to task definition, baselines, validation and explanation.
- It reduces the risk of overclaiming novelty by explicitly distinguishing the proposal from direct competitors.
- It reduces ethical and feasibility risk by repeating that the framework supports human review and does not automate access decisions.
- It reduces data-risk exposure by keeping richer variables optional and retaining a minimum viable dataset.

## Remaining Trade-Offs

The proposal remains an integration/formalization contribution rather than a new-algorithm thesis. This is strategically appropriate for admission because it is more feasible and better aligned with the data-dependent nature of SUS regulation research. The main remaining weakness is that empirical transferability may depend on access to more than one regulation dataset; V3 therefore uses cautious language such as "potencialmente transferível".
