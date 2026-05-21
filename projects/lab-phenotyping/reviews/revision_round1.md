# Revision Round 1

## Scope

This revision applied the previous scientific review as mandatory guidance and revised the manuscript text directly in `projects/lab-phenotyping/manuscript/paper.docx`.

`paper.md` was not available in the repository, so no Markdown manuscript file was updated.

## Major Modifications

1. Title rewritten conservatively.
   - Previous framing claimed that patterns were independent of care setting.
   - New title avoids causal or stronger-than-supported language.

2. Overstatements about care-setting independence removed.
   - The manuscript now states that the association with care setting was statistically significant but weak.
   - The Discussion explicitly says the findings do not demonstrate independence from care setting.

3. Manuscript values synchronized to the final versioned table/figure set where exact values were available.
   - Cohort size retained as `26,414`.
   - Cluster frequencies updated to:
     - inflammatory-renal: `5,837 (22.1%)`
     - hepatic: `5,029 (19.0%)`
     - basal: `15,548 (58.9%)`
   - Sex-distribution narrative revised to match the final Table 1 values rather than the earlier draft prose.

4. Discussion rewritten to separate:
   - observed findings
   - biologically plausible interpretations
   - methodological limitations
   - future applications

5. Placeholders and drafting notes removed from the manuscript body.
   - Removed or replaced:
     - `data-driven clinical phenotyping (diagnosis-agnostic)`
     - `latent biological phenotyping in undifferentiated emergency patients`
     - `perfil de atendimento, média, desvio padrão, por sexo…idade….`
     - `abstract`
     - `keywords`
     - `adicionar github?`
     - `COLOCAR NUMERO DE PARECER`
     - `INSERIR TABELA HERE`

6. Methods clarified to better reflect the implemented pipeline.
   - Added the final 8-variable analytical vector.
   - Added the minimum-density filter of at least 6 exams.
   - Added IQR clipping (`k=3`) before log transform.
   - Added KNN imputation and robust scaling details.
   - Added the rationale for selecting `k=3` based on silhouette plus interpretability.
   - Added UMAP parameters and clarified that UMAP was used only for visualization.

7. Table 1 rebuilt directly inside the `.docx`.
   - Inserted a full 5-column table aligned with the final rendered Table 1 figure values available in the repository.

8. Reference list expanded.
   - Added the key references cited in the rewritten Discussion that were missing from the earlier draft.

## Unresolved Issues

1. Care-setting version inconsistency remains unresolved at the project level.
   - The revised manuscript was reframed around clinical encounters rather than an emergency-only cohort because the final versioned care-setting figure includes:
     - `Emergency-Adult`
     - `Emergency-Pediatric`
     - `Outpatient`
   - This conflicts with parts of the earlier draft and some upstream notebook assumptions suggesting an emergency-only dataset.
   - I did not guess which version is the definitive analytical cohort.

2. Cluster characterization numbers were not fully reproducible from the versioned repository outputs.
   - Exact cluster medians/IQRs for all phenotype-specific variables were not available in versioned CSV outputs inside the repository.
   - To avoid inventing results, the revised Results section uses qualitative cluster characterization where exact synchronized numeric outputs were not accessible.

3. Ethics approval information is still incomplete.
   - The previous placeholder requesting the opinion number was removed from the manuscript body.
   - The final ethics/IRB approval identifier still needs to be inserted if applicable.

4. No versioned processed datasets are present in the repository.
   - Many notebooks depend on absolute local paths outside the repo.
   - This limits strict end-to-end reproducibility from the checked-in files alone.

## Remaining Methodological Concerns

1. Missingness is still not quantitatively reported in the manuscript.
   - The text now clarifies heterogeneous completeness and the use of KNN imputation.
   - A variable-level missingness table or heatmap is still needed for a stronger submission.

2. The rationale for the final 8-variable analytical vector is clearer but still could be strengthened.
   - Upstream feature-construction scripts begin from a broader candidate panel.
   - A short supplementary justification would improve transparency.

3. Sensitivity analyses remain absent from the manuscript package.
   - Recommended additions:
     - alternate `k`
     - complete-case vs imputed comparison
     - preprocessing sensitivity
     - alternate clustering method

4. Repeated encounters remain a limitation.
   - The manuscript now states that the unit of analysis was the encounter and that repeated encounters from the same patient may be represented more than once.
   - A quantified patient-level de-duplication sensitivity analysis would strengthen the study.

5. The care-setting analysis should still be interpreted cautiously.
   - The effect size is small.
   - The analytical version mismatch described above should be resolved before submission.

## Recommended Next Steps

1. Freeze one final analytical dataset version and regenerate all manuscript-linked outputs from it.
2. Add a supplementary missingness report.
3. Add at least one clustering sensitivity analysis.
4. Confirm the definitive cohort framing:
   - multi-setting
   - or emergency-only
5. Insert final ethics approval information if required.

## Scientific Strengthening Pass

### Major additions in this round

1. The Introduction was rewritten to improve scientific motivation and literature integration.
   - Added explicit framing around emergency-care heterogeneity and diagnostic uncertainty.
   - Added a clearer transition from classical biomarker interpretation to multimarker data-driven phenotyping.
   - Integrated literature on computational phenotyping, latent subphenotypes, and real-world laboratory data.

2. The Discussion was substantially deepened.
   - Added explicit comparison with:
     - Seymour et al. on sepsis phenotypes
     - Calfee et al. on ARDS subphenotypes
     - Becker et al. on unsupervised EHR phenotyping
     - real-world data quality literature
   - Separated:
     - directly observed results
     - biologically plausible interpretations
     - speculative future applications

3. In-text citations were inserted throughout the Introduction, Methods, and Discussion.

4. The UMAP figure was embedded directly into the manuscript with caption and linked references in Results and Discussion.

5. Section modularization files were created:
   - `manuscript/sections/introduction.md`
   - `manuscript/sections/methods.md`
   - `manuscript/sections/results.md`
   - `manuscript/sections/discussion.md`

6. A thematic literature file was created:
   - `references/core_literature.md`

## Unresolved Scientific Weaknesses

1. The manuscript is now scientifically stronger, but it still rests on an exploratory clustering analysis without external validation.

2. Cluster stability is still untested in the manuscript package.
   - There is no bootstrap stability analysis.
   - There is no comparison against alternative clustering algorithms in the main text.

3. Missingness is still described qualitatively rather than quantified in a formal table or figure.

4. The biological interpretation of the hepatic phenotype remains modestly supported.
   - The available variables support a transaminase-centered pattern.
   - They do not allow confident etiologic interpretation.

5. The inflammatory-renal phenotype is biologically plausible but not prognostically validated.
   - The manuscript now avoids overclaiming, but reviewers may still ask for outcome linkage.

6. Repeated encounters remain a methodological vulnerability.
   - The unit of analysis is the encounter, not the unique patient.
   - No sensitivity analysis currently quantifies the impact of repeated encounters.

## Remaining Missing Analyses

1. Variable-level missingness table or heatmap.
2. Sensitivity analysis for preprocessing choices.
3. Sensitivity analysis for alternate `k` values.
4. Alternate clustering method comparison.
5. If available in source data:
   - unique patient count
   - encounter-per-patient distribution
   - inclusion/exclusion flow diagram
6. If clinically available in source systems:
   - admission outcome
   - ICU transfer
   - mortality or short-term hard outcomes

## Possible Reviewer Criticisms

1. `Why should these clusters be believed if separation is modest and no stability analysis is shown?`

2. `How much of the cluster structure is driven by missingness, preprocessing, or measurement frequency rather than biology?`

3. `Why were these eight variables retained from a broader candidate panel?`

4. `How should readers interpret the care-setting analysis if the effect size is small and the analytic framing changed across project versions?`

5. `Without outcomes, how should clinical relevance be judged beyond face validity?`

6. `Does mixing emergency-adult, emergency-pediatric, and outpatient contexts introduce hidden structure that should have been analyzed separately?`

## Suggested Future Analyses

1. Add a supplementary clustering robustness section.
   - `k=2..6`
   - complete-case comparison
   - no clipping vs clipping
   - K-means vs one alternate method

2. Add variable-level missingness reporting.

3. Add a patient-level sensitivity analysis excluding repeated encounters or restricting to first encounter.

4. If downstream clinical data can be linked, test associations with:
   - admission
   - ICU use
   - short-term mortality
   - length of stay

5. If feasible, evaluate phenotype stability in a temporal split or an external cohort.
