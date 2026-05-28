# Integrated Citation Version

## Citation-integrated positioning text

This version is designed as a literature-anchored companion to the final doctoral plan. It keeps the same scientific direction while making the evidentiary structure more explicit for future proposal editing, interview preparation, and article derivation.

### Core positioning sentence

The doctoral project advances **from morphology intelligence to multimodal clinical-laboratory intelligence in hematology** by integrating peripheral blood smear morphology with complete blood count parameters, analyzer flags, and structured laboratory context for robust, interpretable, case-level decision support (Zini, 2024; de Almeida et al., 2023; Horiuchi et al., 2026; Iscoe et al., 2023).

## 1. Continuity from the master's

The master's dissertation and the candidate's recent publication record establish a clear and defensible starting point for the doctorate. The prior work showed that automated leukocyte morphology analysis can be approached rigorously through curated datasets, specialist-informed labeling, architecture comparison, domain-specific stain augmentation, and external evaluation across datasets (Kasprowicz & Silva, 2026). The candidate's systematic review complements this empirical work by showing that the leukocyte-classification literature is already technically mature in many image-only settings, but still limited in immature-cell handling, methodological comparability, and translational realism (Kasprowicz et al., 2026).

These previous outputs justify the doctoral transition in two ways. First, they validate that AI-based hematological morphology is already a feasible and productive scientific line. Second, they reveal the boundary of image-only approaches and therefore motivate the next step: integrating morphology with other laboratory evidence instead of remaining at isolated-cell prediction (Kasprowicz et al., 2026; Kasprowicz & Silva, 2026).

## 2. Why image-only hematology is no longer enough

Image-only blood-smear AI remains important, but it no longer offers the strongest strategic niche for this doctoral trajectory. The current literature is densely populated with CNN-based and deep-learning-based leukocyte classification studies, especially for normal or relatively well-defined mature classes (Asghar et al., 2024). Even when performance is high, the literature still suffers from dataset heterogeneity, limited external comparability, and insufficient alignment with case-level laboratory reasoning (Asghar et al., 2024; Kasprowicz et al., 2026).

From a laboratory perspective, this limitation is structural rather than incidental. Peripheral smear interpretation is not performed at the level of a single cell detached from context. It depends on how morphological findings relate to CBC outputs, analyzer-generated alerts, lineage-wide patterns, and the broader review logic of the case (Zini, 2024). Therefore, scientific maturity in this field means moving from cell recognition alone to integrated inference.

## 3. Why multimodal case-level inference matters

The literature signals that the most meaningful advances arise when morphology is aggregated and interpreted beyond isolated cells. Computational morphology studies have already shown that disease-associated peripheral blood patterns can be detected at scale and that these patterns gain diagnostic value when interpreted together with blood counts (de Almeida et al., 2023). More directly, recent work in laboratory hematology has demonstrated that image-derived morphology and CBC data can be combined to support intelligent diagnostic assistance, which strongly supports the plausibility of this doctoral direction (Horiuchi et al., 2026).

This is precisely where the scientific gap becomes strongest. There are still relatively few studies that combine:

- peripheral blood smear morphology;
- complete blood count variables;
- analyzer flags;
- case-level interpretation logic;
- robustness and interpretability analysis in real laboratory conditions.

The project is therefore positioned in a space that is methodologically richer than image-only classification, but still substantially less saturated than generic multimodal healthcare AI.

## 4. Why real-world laboratory data matters

Access to real laboratory data is not only an operational convenience. It is a scientific differentiator. Public image datasets support benchmark development, but they rarely capture the heterogeneous and contextual signals that actually structure hematology workflows. Real data make it possible to study:

- morphology-CBC concordance and discordance;
- alert-driven review logic;
- variability in staining and acquisition;
- case-level prioritization tasks;
- practical interpretability demands.

This is why laboratory AI tools that use structured operational data are so relevant to the proposal. PROSER is especially useful as a translational reference because it demonstrates that peripheral smear interpretation can be computationally supported through structured integration of laboratory and clinical information, even though its method is not yet a full multimodal morphology-learning framework (Iscoe et al., 2023).

## 5. Why robustness must be central

Robustness is not an optional methodological add-on in this proposal. It is one of the thesis-defining scientific axes. The candidate's Springer paper already showed that stain-aware generative augmentation improved performance across architectures and that cross-dataset evaluation exposed meaningful generalization behavior beyond the training set (Kasprowicz & Silva, 2026). In broader hematology AI, digital morphology studies also indicate that external generalization and multicenter realism are necessary if a system is meant to support actual use rather than remain a benchmark exercise (Katz et al., 2021; de Almeida et al., 2023).

Accordingly, the doctoral contribution is not only to combine modalities, but to ask whether multimodal systems remain reliable under realistic laboratory variability. This includes calibration, uncertainty, domain shift, and interpretable failure analysis.

## 6. Citation-ready gap statement

The strongest citation-ready version of the scientific gap is:

> Current hematology AI literature is rich in image-only leukocyte and blood-smear classification, but still sparse in robust and interpretable systems that integrate peripheral blood smear morphology with CBC parameters, analyzer flags, and structured laboratory context for case-level decision support in real laboratory settings (Asghar et al., 2024; de Almeida et al., 2023; Horiuchi et al., 2026; Iscoe et al., 2023).

## 7. Citation-ready continuity statement

> The proposed doctorate extends the candidate's master's work on leukocyte morphology analysis by shifting from isolated-cell recognition toward multimodal clinical-laboratory inference, while preserving the same hematology domain, the same morphology anchor, and the same concern with robustness and translational realism (Kasprowicz et al., 2026; Kasprowicz & Silva, 2026).

## 8. Citation-ready relevance to Computer Science

> From a Computer Science perspective, the thesis addresses a challenging multimodal inference problem under heterogeneous, real-world constraints, requiring data fusion, robustness analysis, uncertainty handling, and interpretable decision support rather than only image classification performance optimization (de Almeida et al., 2023; Horiuchi et al., 2026; Katz et al., 2021).

## References

Asghar, R., Kumar, S., Shaukat, A., & Hynds, P. (2024). Classification of white blood cells (leucocytes) from blood smear imagery using machine and deep learning models: A global scoping review. *PLOS ONE*. https://doi.org/10.1371/journal.pone.0292026

de Almeida, J. G., Gudgin, E., Besser, M., Dunn, W. G., Cooper, J., Haferlach, T., Vassiliou, G. S., & Gerstung, M. (2023). Computational analysis of peripheral blood smears detects disease-associated cytomorphologies. *Nature Communications*. https://doi.org/10.1038/s41467-023-39676-y

Horiuchi, Y., Ravzanaadii, M., Bai, J., Matsuzaki, A., Kaniyu, K., Ando, J., Ando, M., Nojiri, S., Iwasaki, Y., Konishi, A., & Tabe, Y. (2026). Application of convolutional neural network image analysis and machine learning to basic blood tests for intelligent diagnostic assistance. *International Journal of Laboratory Hematology, 48*, 26-38. https://doi.org/10.1111/ijlh.14550

Iscoe, M. S., Loza, A. J., Turbiville, D., Campbell, S. M., Peaper, D. R., Balbuena-Merle, R. I., & Hauser, R. G. (2023). PROSER: A web-based peripheral blood smear interpretation support tool utilizing electronic health record data. *American Journal of Clinical Pathology, 160*, 98-105. https://doi.org/10.1093/ajcp/aqad024

Kasprowicz, J., Bacca, H. G., & Silva, A. G. (2026). Systematic review on computer vision techniques applied to leukocyte classification. *Journal of Health Informatics, 18*. https://doi.org/10.59681/2175-4411.v18.2026.1519

Kasprowicz, J., & Silva, A. G. (2026). Comparative analysis of convolutional and vision transformer models for automated leukocyte classification enhanced by generative color augmentation. *Signal, Image and Video Processing*. https://doi.org/10.1007/s11760-026-05309-2

Katz, B.-Z., Feldman, M. D., Tessema, M., Benisty, D., Stewart Toles, G., Andre, A., Shtreker, B., Paz, F. M., Edwards, J., Jengehino, D., Bagg, A., Avivi, I., & Pozdnyakova, O. (2021). Evaluation of Scopio Labs X100 Full Field PBS: The first high-resolution full field viewing of peripheral blood specimens combined with artificial intelligence-based morphological analysis. *International Journal of Laboratory Hematology, 43*, 1408-1416. https://doi.org/10.1111/ijlh.13681

Zini, G. (2024). Hematological cytomorphology: Where we are. *International Journal of Laboratory Hematology, 46*, 789-794. https://doi.org/10.1111/ijlh.14330
