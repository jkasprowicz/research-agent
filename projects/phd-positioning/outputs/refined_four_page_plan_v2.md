# Refined Four-Page Doctoral Plan V2

## From Morphology Intelligence to Multimodal Clinical-Laboratory Intelligence in Hematology

### Proposed doctoral direction for PPGCC/UFSC

The proposed doctorate is centered on the transition **from morphology intelligence to multimodal clinical-laboratory intelligence in hematology**. Its core scientific objective is to develop robust and interpretable computational methods that integrate peripheral blood smear morphology with structured laboratory data, especially complete blood count parameters and hematology analyzer flags, in order to support case-level hematological inference in real laboratory settings.

This positioning preserves strong continuity with the candidate's master's dissertation and previous publications. The prior work did not merely test image classifiers. It established a clinically grounded research line in computational hematology through dataset construction, specialist-informed annotation, rigorous comparison of deep learning architectures, domain-aware augmentation for staining variability, and external evaluation across datasets (Kasprowicz & Silva, 2026). The candidate's systematic review also mapped the current field and showed that leukocyte classification from smear images is now technically mature for normal classes, while clinically relevant challenges remain concentrated in immature, atypical, and operationally realistic scenarios (Kasprowicz, Bacca, & Silva, 2026). The doctorate therefore does not represent a thematic jump. It represents the next inferential step in the same line of research.

## 1. Scientific context and motivation

Peripheral blood smear interpretation remains a fundamental component of laboratory hematology. Even with the widespread use of automated analyzers, relevant decisions still depend on the articulation between quantitative blood count outputs, analyzer alerts, and expert morphological review. Recent reviews in laboratory hematology reaffirm that cytomorphology continues to play an essential role in diagnostic interpretation, prognostic assessment, and hematology workflow, even as digital microscopy and AI become increasingly available (Zini, 2024). In parallel, digital systems such as full-field peripheral blood smear platforms have shown that AI-assisted morphology can be incorporated into real diagnostic environments, supporting the translational feasibility of computational hematology beyond proof-of-concept image benchmarks (Katz et al., 2021).

At the same time, the current AI literature in hematology is unevenly distributed. The most saturated area is image-only recognition of leukocytes and blood-cell morphologies. A recent scoping review demonstrated the predominance of CNN-based and deep learning pipelines for leukocyte classification, often with very high reported performance but under heterogeneous datasets, limited cross-setting comparability, and strong focus on mature normal classes (Asghar et al., 2024). The candidate's own systematic review reached a similar conclusion and highlighted the persistent gap in clinically relevant immature and atypical morphology (Kasprowicz et al., 2026). This means that another thesis centered on isolated-cell classification would have limited novelty and a weaker long-term scientific identity.

The evidence map developed for the doctoral positioning indicates a more promising and underexplored direction: **case-level multimodal hematology intelligence**. In real-world hematology, the meaning of morphology depends on its relationship with the broader case. A blast-like cell, a neutrophil dysplasia pattern, or an erythrocyte abnormality is not interpreted in isolation; it is interpreted in conjunction with the complete blood count, differential patterns, analyzer flags, and review context. Recent studies suggest the value of this broader integration. Computational morphology systems can extract disease-associated patterns with external generalization, especially when morphology is aggregated and interpreted alongside blood counts (de Almeida et al., 2023). More directly, recent work in laboratory hematology has shown the feasibility of combining image-derived morphology outputs with CBC data for intelligent diagnostic assistance (Horiuchi et al., 2026). In parallel, laboratory decision-support tools such as PROSER show that structured laboratory and record data can be operationally integrated into peripheral smear interpretation workflows (Iscoe et al., 2023).

These signals are strategically important. They show that image-only hematology is no longer the strongest frontier for this profile, while multimodal, robust, and case-level laboratory inference remains scientifically open, publication-friendly, and well aligned with the available advisors and the candidate's previous trajectory.

## 2. Central scientific gap

The strongest scientific gap is not the absence of accurate morphology classifiers. It is the absence of **robust, interpretable, case-level systems that integrate peripheral blood smear morphology with structured laboratory evidence**.

This gap has four dimensions. First, there is an **integration gap**: most studies remain restricted to image analysis and do not meaningfully combine morphology with CBC parameters, analyzer outputs, or laboratory metadata. Second, there is an **inferential gap**: much of the literature operates at the level of individual cells or fields, whereas real laboratory reasoning is case-based. Third, there is a **robustness gap**: staining variability, acquisition differences, scanner effects, and institutional workflow variation are acknowledged in image-only pipelines, but still insufficiently studied in multimodal hematology systems. Fourth, there is a **decision-support gap**: only a small subset of studies approach the logic of manual review prioritization, discordance analysis, or integrated smear interpretation that actually characterizes laboratory practice.

Accordingly, the doctoral problem can be formulated as follows:

**How can peripheral blood smear morphology be integrated with complete blood count parameters, analyzer flags, and structured laboratory context to produce robust, interpretable, and clinically useful case-level AI systems for hematology?**

## 3. Continuity from the master's dissertation

The master's dissertation established the **morphology intelligence layer** of this research trajectory. It showed that hematological morphology can be represented computationally with high-resolution learning signals, that modern computer vision architectures can discriminate clinically meaningful leukocyte classes, and that performance is sensitive to real-world staining variation and cross-dataset shift (Kasprowicz & Silva, 2026). This work also produced technical and scientific infrastructure that now enables multimodal expansion: curated morphology data, annotation logic, evaluation routines, and a clear understanding of where isolated-cell image analysis becomes insufficient.

The doctoral project extends this line naturally rather than replacing it. The progression is:

`isolated-cell leukocyte classification` -> `morphology-aware case representation` -> `multimodal clinical-laboratory inference`

This is an academically mature transition for three reasons. First, it preserves morphology as the anchor modality and therefore avoids an artificial thematic switch. Second, it expands from recognition to integration, which is a legitimate doctoral-level increase in methodological complexity. Third, it retains the candidate's strongest differentiators: peripheral blood expertise, laboratory realism, and explicit concern with robustness, generalization, and translational utility.

## 4. Research question and objectives

The central research question is:

**Does integrating peripheral blood smear morphology with CBC parameters, hematology analyzer flags, and structured laboratory context improve the robustness, interpretability, and practical usefulness of AI systems for hematological decision support when compared with image-only approaches?**

The general objective is to develop and evaluate a multimodal AI framework for hematology that operates at case level and supports laboratory decision making under realistic data variability.

The specific objectives are:

1. To build a multimodal hematology dataset that links smear morphology with CBC variables, differential counts, analyzer flags, and essential laboratory metadata.
2. To design and compare multimodal fusion strategies against image-only and tabular-only baselines for case-level hematological tasks.
3. To investigate robustness, calibration, uncertainty, and failure modes under real-world laboratory variability.
4. To produce interpretable decision-support outputs relevant to smear review, triage, or suspicious-pattern prioritization.

## 5. Methodological plan and scope boundaries

The thesis is intentionally bounded. Its core scope is **peripheral blood smear morphology plus structured hematology laboratory data**. It is not intended to become a universal hematology platform, a general medical foundation-model project, or a broad agentic AI system.

The methodological plan is modular and feasible for a full-time working researcher.

**Phase 1: multimodal data curation and harmonization.** The first phase will identify and structure case-level records linking smear images to CBC parameters, differential information, analyzer flags, and essential metadata. This phase is scientifically relevant in itself because multimodal hematology datasets are still rare, especially in clinically realistic settings.

**Phase 2: case-level task definition and baseline construction.** The project will define concrete case-level tasks such as abnormal-case prioritization, smear-review triage, suspicious-pattern detection, or morphology-versus-analyzer discordance analysis. Baselines will include image-only models, structured-data-only models, and multimodal fusion models.

**Phase 3: multimodal modeling.** Different fusion strategies will be implemented and compared, with emphasis on what multimodality actually adds relative to strong unimodal baselines. The aim is not simply to maximize accuracy, but to identify when morphology contributes unique information, when structured data dominates, and when the combination is necessary.

**Phase 4: robustness and interpretability.** Robustness is a central scientific axis of the thesis, not an afterthought. The prior Springer publication already showed that domain-aware augmentation and cross-dataset evaluation are critical for morphology pipelines (Kasprowicz & Silva, 2026). The doctorate will extend this logic to multimodal systems, investigating calibration, uncertainty, sensitivity to distributional shifts, and interpretable modality contributions.

**Phase 5: limited decision-support layer.** If the multimodal core is mature, the project may include a constrained layer of structured decision support, such as rule-grounded explanation or retrieval-supported interpretation. This is deliberately secondary. Generic LLM or agentic components are not the thesis identity and should only appear if they are clearly subordinate to the laboratory problem.

The scope is also explicitly controlled in terms of morphology domains. Immature cells, atypical leukocytes, and analyzer-alert-relevant patterns belong naturally to the core thesis because they connect directly to the master's work and to review prioritization. Broader erythrocyte and platelet morphology can be incorporated only if they strengthen a well-defined case-level task. Genomics, bone marrow, flow cytometry, and universal diagnostic claims are outside the doctoral core.

## 6. Expected contributions to Computer Science

Although translationally grounded in hematology, the thesis is fundamentally computational. Its contribution to Computer Science lies in the formalization and evaluation of a multimodal inference problem under real-world constraints.

The expected contributions are:

- a computational formulation of case-level multimodal hematology inference;
- data integration strategies linking image-derived morphology and structured laboratory variables;
- multimodal fusion methods evaluated under domain variability;
- robustness, calibration, and uncertainty analysis for laboratory AI;
- interpretable outputs suited to decision-support settings rather than only benchmark reporting.

This framing is important for PPGCC/UFSC. The proposal is not simply “AI applied to health.” It investigates how heterogeneous modalities can be combined in reliable and interpretable ways under real operational constraints, using hematology as a high-value translational domain.

## 7. Feasibility and publication strategy

The proposal is realistic because it builds on already established assets rather than starting from zero. The candidate enters the doctorate with a dissertation grounded in blood-smear morphology, a systematic review of the field, and a Springer publication demonstrating model comparison, generative stain augmentation, external evaluation, and morphology-centered interpretability (Kasprowicz et al., 2026; Kasprowicz & Silva, 2026). This prior work reduces startup risk and shortens the path to publishable doctoral outputs.

The project is also publication-oriented by design. A realistic publication sequence includes:

1. a multimodal dataset and problem-definition paper;
2. a core multimodal modeling paper with unimodal comparisons;
3. a robustness and reliability paper focused on calibration, uncertainty, or cross-setting behavior;
4. an interpretability or laboratory decision-support paper.

This sequence is coherent, incremental, and feasible within a doctoral timeline compatible with full-time work. It also avoids dependence on a single high-risk breakthrough.

## 8. Final positioning

The most defensible doctoral positioning for PPGCC/UFSC is therefore:

**from morphology intelligence to multimodal clinical-laboratory intelligence in hematology**

This formulation is strong because it preserves continuity with the master's dissertation, responds to a real and underconnected literature gap, foregrounds computational contribution, and remains realistic in scope. It avoids the two weakest alternatives for this profile: remaining in a saturated image-only benchmark space, or jumping prematurely to generic LLM-driven laboratory automation. Instead, it proposes a focused and mature doctorate in trustworthy laboratory AI, with peripheral blood morphology as the anchor and case-level multimodal inference as the scientific advance.

## References

Asghar, R., Kumar, S., Shaukat, A., & Hynds, P. (2024). Classification of white blood cells (leucocytes) from blood smear imagery using machine and deep learning models: A global scoping review. *PLOS ONE*. https://doi.org/10.1371/journal.pone.0292026

de Almeida, J. G., Gudgin, E., Besser, M., Dunn, W. G., Cooper, J., Haferlach, T., Vassiliou, G. S., & Gerstung, M. (2023). Computational analysis of peripheral blood smears detects disease-associated cytomorphologies. *Nature Communications*. https://doi.org/10.1038/s41467-023-39676-y

Horiuchi, Y., Ravzanaadii, M., Bai, J., Matsuzaki, A., Kaniyu, K., Ando, J., Ando, M., Nojiri, S., Iwasaki, Y., Konishi, A., & Tabe, Y. (2026). Application of convolutional neural network image analysis and machine learning to basic blood tests for intelligent diagnostic assistance. *International Journal of Laboratory Hematology, 48*, 26-38. https://doi.org/10.1111/ijlh.14550

Iscoe, M. S., Loza, A. J., Turbiville, D., Campbell, S. M., Peaper, D. R., Balbuena-Merle, R. I., & Hauser, R. G. (2023). PROSER: A web-based peripheral blood smear interpretation support tool utilizing electronic health record data. *American Journal of Clinical Pathology, 160*, 98-105. https://doi.org/10.1093/ajcp/aqad024

Kasprowicz, J., Bacca, H. G., & Silva, A. G. (2026). Systematic review on computer vision techniques applied to leukocyte classification. *Journal of Health Informatics, 18*. https://doi.org/10.59681/2175-4411.v18.2026.1519

Kasprowicz, J., & Silva, A. G. (2026). Comparative analysis of convolutional and vision transformer models for automated leukocyte classification enhanced by generative color augmentation. *Signal, Image and Video Processing*. https://doi.org/10.1007/s11760-026-05309-2

Katz, B.-Z., Feldman, M. D., Tessema, M., Benisty, D., Stewart Toles, G., Andre, A., Shtreker, B., Paz, F. M., Edwards, J., Jengehino, D., Bagg, A., Avivi, I., & Pozdnyakova, O. (2021). Evaluation of Scopio Labs X100 Full Field PBS: The first high-resolution full field viewing of peripheral blood specimens combined with artificial intelligence-based morphological analysis. *International Journal of Laboratory Hematology, 43*, 1408-1416. https://doi.org/10.1111/ijlh.13681

Zini, G. (2024). Hematological cytomorphology: Where we are. *International Journal of Laboratory Hematology, 46*, 789-794. https://doi.org/10.1111/ijlh.14330
