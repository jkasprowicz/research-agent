# Data Audit Round 1

## Scope

This review integrates the currently available evidence from:

- manuscript text and section files
- analysis notebooks
- rendered figures and tables committed in the repository
- the audit-script design in `notebooks/00_data_audit_summary.py`

Important limitation:

- The local processed CSVs and generated audit outputs were **not present in this worktree** at review time.
- Therefore, this is a **code-grounded and manuscript-grounded scientific/data audit**, not a full execution audit against live processed datasets.
- That absence is itself a reproducibility concern and is included below as a substantive finding.

## Executive Assessment

The project has a real publishable core. The strongest elements are:

- a large real-world cohort
- a biologically plausible three-cluster solution
- a concise multimarker laboratory panel
- clinically interpretable axes of variation
- clear descriptive differences by sex and age

The main vulnerabilities are also clear:

- the clustering solution may be partly driven by age structure and care-context mixing
- preprocessing choices are highly consequential and not yet stress-tested
- the current interpretation is stronger than the available robustness work
- repeated encounters are acknowledged upstream in the data pipeline but are not yet quantified in the manuscript results
- the final repository does not contain the processed datasets or audit outputs needed for full reproducibility

## What Strengthens the Paper

### 1. The clusters are clinically interpretable

The final analytic panel in [03_clustering_kmeans_final.py](/Users/joaokasprowicz/.codex/worktrees/9965/research-agent/projects/lab-phenotyping/notebooks/03_clustering_kmeans_final.py:10) uses eight variables that span meaningful physiological domains:

- inflammation: `PCR`
- hematologic response: `LEUCO`, `PLAQ`
- renal function: `CREATININA`, `UREIA`
- hepatocellular injury: `TGO`, `TGP`
- age: `idade`

That is a strength because the resulting phenotypes are not arbitrary latent vectors; they map to clinically legible axes.

### 2. The sex signal looks stronger than a purely incidental finding

The rendered Table 1 and the corresponding notebook [01d_tabela1_por_sexo.py](/Users/joaokasprowicz/.codex/worktrees/9965/research-agent/projects/lab-phenotyping/notebooks/01d_tabela1_por_sexo.py:114) show a meaningful redistribution of clusters by sex:

- inflammatory-renal phenotype enriched in men
- basal phenotype enriched in women

This is scientifically valuable because it suggests that cluster membership is not only a geometric artifact. Even if not the paper’s primary endpoint, this is a potentially important descriptive result and could strengthen the Discussion.

### 3. The age pattern is clinically coherent

The manuscript results describe the inflammatory-renal cluster as the oldest group, and the cluster-profiling notebook explicitly summarizes age by cluster in [04_cluster_profiles_final.py](/Users/joaokasprowicz/.codex/worktrees/9965/research-agent/projects/lab-phenotyping/notebooks/04_cluster_profiles_final.py:103). This supports the view that the clusters capture a biologically credible gradient rather than random partitioning.

### 4. The UMAP and heatmap support interpretability, not just separation

The UMAP figure and the standardized heatmap reinforce that:

- the clusters are only partially separable
- the phenotypes lie on a continuum
- the centroid profiles differ along recognizable laboratory axes

That is actually a scientific strength if framed correctly: the paper does not need “perfect separation”; it needs plausible latent structure in noisy real-world data.

### 5. The project already contains material for a stronger supplement

The repository includes multiple exploratory figures:

- heatmap of standardized cluster profiles
- cluster-specific boxplots
- care-setting stacked bars
- sex-distribution stacked bars
- biologically themed scatter plots

These are not all main-text figures, but they form a good supplementary backbone.

## What Weakens the Paper

### 1. The cohort definition is not fully stable across the pipeline

There is an unresolved tension between:

- the emergency-only filter in [02b_features_emergency_only.py](/Users/joaokasprowicz/.codex/worktrees/9965/research-agent/projects/lab-phenotyping/notebooks/02b_features_emergency_only.py:8)
- and the final care-setting mapping in [04_cluster_profiles_final.py](/Users/joaokasprowicz/.codex/worktrees/9965/research-agent/projects/lab-phenotyping/notebooks/04_cluster_profiles_final.py:23), which still includes `Outpatient`

This is more than a wording issue. It affects how reviewers will interpret:

- external validity
- the meaning of the care-setting association
- whether the clustering is driven partly by non-emergency care pathways

### 2. Age may be a major latent driver, possibly more than acknowledged

Age is used directly as a clustering variable in [03_clustering_kmeans_final.py](/Users/joaokasprowicz/.codex/worktrees/9965/research-agent/projects/lab-phenotyping/notebooks/03_clustering_kmeans_final.py:10), and the cohort clearly includes a pediatric segment in [01d_tabela1_por_sexo.py](/Users/joaokasprowicz/.codex/worktrees/9965/research-agent/projects/lab-phenotyping/notebooks/01d_tabela1_por_sexo.py:16).

This creates an important interpretive risk:

- part of the cluster structure may reflect life-stage composition rather than purely latent pathobiology

That does not invalidate the paper, but it means the Discussion should treat age not only as a descriptive covariate but as a possible structural driver of the clustering solution.

### 3. The density filter is clinically consequential and likely selective

The features pipeline excludes encounters with fewer than six non-missing analytes in the candidate panel in [02_build_features_24h_peak_final.py](/Users/joaokasprowicz/.codex/worktrees/9965/research-agent/projects/lab-phenotyping/notebooks/02_build_features_24h_peak_final.py:101).

This probably enriches the final cohort for:

- more extensively worked-up patients
- more complex or severe encounters
- adult patients over pediatric patients
- settings with denser test ordering patterns

This is one of the most important hidden selection mechanisms in the project. It may strengthen phenotype detectability but weaken representativeness.

### 4. Candidate-variable selection and final-variable selection are not fully reconciled

The upstream feature builder begins from a much broader candidate list in [02_build_features_24h_peak_final.py](/Users/joaokasprowicz/.codex/worktrees/9965/research-agent/projects/lab-phenotyping/notebooks/02_build_features_24h_peak_final.py:10), including:

- `FOSFATASE_ALCALINA`
- `BILIRRUBINA`
- `SODIO`
- `POTASSIO`
- `GLICOSE`
- `LDH`
- `CPK`
- `TAP`

But the final clustering uses only eight variables in [03_clustering_kmeans_final.py](/Users/joaokasprowicz/.codex/worktrees/9965/research-agent/projects/lab-phenotyping/notebooks/03_clustering_kmeans_final.py:10).

Reviewers may read this as:

- informal feature pruning
- post hoc optimization
- hidden dependence on data availability rather than a priori reasoning

### 5. The preprocessing chain is powerful enough to shape the phenotypes

The clustering pipeline performs:

- IQR clipping [03_clustering_kmeans_final.py](/Users/joaokasprowicz/.codex/worktrees/9965/research-agent/projects/lab-phenotyping/notebooks/03_clustering_kmeans_final.py:18)
- `log1p` transformation [03_clustering_kmeans_final.py](/Users/joaokasprowicz/.codex/worktrees/9965/research-agent/projects/lab-phenotyping/notebooks/03_clustering_kmeans_final.py:34)
- KNN imputation [03_clustering_kmeans_final.py](/Users/joaokasprowicz/.codex/worktrees/9965/research-agent/projects/lab-phenotyping/notebooks/03_clustering_kmeans_final.py:40)
- robust scaling [03_clustering_kmeans_final.py](/Users/joaokasprowicz/.codex/worktrees/9965/research-agent/projects/lab-phenotyping/notebooks/03_clustering_kmeans_final.py:46)

This is defensible, but it means the final solution is not a “raw data” phenotype. It is a phenotype under a specific preprocessing regime. Without sensitivity analyses, the robustness of interpretation remains uncertain.

### 6. Repeated encounters are identifiable upstream but not analytically resolved

The expanded dataset explicitly creates `patient_id` in [01_filtrar_exames_multimarcador.py](/Users/joaokasprowicz/.codex/worktrees/9965/research-agent/projects/lab-phenotyping/notebooks/01_filtrar_exames_multimarcador.py:18) and retains `numero_do_atendimento` [01_filtrar_exames_multimarcador.py](/Users/joaokasprowicz/.codex/worktrees/9965/research-agent/projects/lab-phenotyping/notebooks/01_filtrar_exames_multimarcador.py:146).

That is useful because it means the project could quantify:

- repeated encounters per patient
- whether high-frequency utilizers influence cluster balance
- whether phenotype assignment clusters by person rather than by episode

At present, that opportunity is not yet used.

### 7. Audit outputs are not yet present

The audit script is capable of generating:

- missingness tables
- range checks
- age summaries
- repeated-encounter summaries
- processed-dataset comparison reports

But none of those outputs are currently present in this worktree. That weakens the project’s immediate inspectability and means the manuscript claims about missingness and cohort composition are not independently auditable from committed outputs.

## Hidden Clinically Relevant Findings

### 1. Sex redistribution may be more publication-relevant than the current paper gives it credit for

The sex-by-cluster pattern is likely one of the clearest additional findings in the current package. It suggests the latent phenotypes are not evenly distributed across biological sex, which could be clinically meaningful and worth either:

- brief emphasis in the main Discussion
- or a dedicated supplementary table/figure

### 2. The pediatric signal may be a major source of heterogeneity

Because the cohort includes a non-trivial pediatric fraction and age is part of the clustering model, the pediatric/adult mix likely shapes cluster structure. This is clinically important, not merely technical.

This could mean:

- the basal cluster is enriched by pediatric or younger low-disruption encounters
- the inflammatory-renal phenotype may partly reflect adult/older-case concentration
- the care-setting association may be partly mediated by age structure

### 3. The weak care-setting association may actually strengthen the conceptual argument

If it holds after the age issue is explored, the small `V de Cramér` could be interpreted as evidence that routine laboratory phenotypes are not reducible to administrative care labels alone. That is a conceptually interesting result and could be framed as a strength, but only after acknowledging possible confounding by age and selection.

### 4. The project may contain a clinically meaningful “testing intensity phenotype”

Because inclusion requires at least six non-missing analytes from a broader candidate panel, the analytic cohort may already be enriched for a latent process of:

- higher clinician concern
- greater diagnostic workup
- more severe or complex presentations

This could itself be scientifically relevant, although it currently acts as a hidden inclusion mechanism rather than an explicit study question.

## Missingness Implications

Even without the missingness CSV outputs present, the code shows that missingness is central to the analytic design:

- the density filter removes sparse cases before clustering
- KNN then imputes the remaining missing values

This has three implications:

1. The manuscript should distinguish:
   - pre-filter missingness
   - post-filter missingness
   - post-imputation completeness

2. The observed phenotypes may represent the subset of encounters with sufficiently rich laboratory workup, not the full clinical population.

3. The effect of missingness may be partially structural:
   - pediatrics may have fewer tests
   - lower-acuity settings may order fewer analytes
   - some biochemical markers may encode practice patterns as much as biology

## Age and Pediatric/Adult Effects

This is one of the highest-priority scientific issues.

### Why it matters

- `idade` is directly included in clustering
- pediatric patients are present
- emergency pediatric and adult care are both represented in the final materials

### Likely consequences

- cluster separation may partly reflect age stratification
- care-setting differences may partly proxy age
- inflammatory-renal interpretation may be amplified by older-age concentration
- basal-cluster predominance may be inflated by younger or lower-complexity encounters

### Why this does not necessarily weaken the paper fatally

Age is clinically meaningful. If age helps define a biologically coherent phenotype, that can still be legitimate. The real issue is transparency:

- the paper should not imply that clusters are age-neutral
- age-stratified robustness should be discussed as a missing analysis

## Repeated Encounters

This is currently a latent but important issue.

### What is already available in the pipeline

- hashed `patient_id`
- encounter identifier

### Why it matters

Repeated encounters could:

- overweight frequent utilizers
- inflate cluster sizes for specific chronic-complex phenotypes
- make cluster distributions partly patient-driven rather than episode-driven

### What would strengthen the paper

At minimum, a supplementary analysis reporting:

- total encounters
- unique patients
- encounters per patient distribution
- whether cluster composition changes when keeping only first encounter

## Preprocessing Impact

The current preprocessing is thoughtful but high-impact.

### Potential positive effect

- reduces extreme skew
- reduces domination by outliers
- makes K-means more usable on real-world laboratory data

### Potential scientific downside

- may compress clinically relevant extremes
- may smooth biologically important tails
- may cause imputed values to reinforce central tendencies
- may help generate a cleaner geometry than the raw biological structure truly contains

This does not invalidate the analysis, but it means the clusters should be described as **preprocessing-dependent analytical phenotypes** rather than discovered “natural types.”

## Robustness of Cluster Interpretation

Current support for interpretation:

- clinically legible variables
- coherent heatmap pattern
- coherent UMAP partial structure
- meaningful sex redistribution
- strong age differences

Current gaps:

- no stability resampling
- no alternate algorithm comparison in final paper
- no adult-only or pediatric-only sensitivity
- no no-age clustering sensitivity
- no complete-case comparison

Interpretive bottom line:

The clusters are **plausible and useful as exploratory phenotypes**, but not yet fully robust enough for stronger translational claims.

## Possible Reviewer Criticisms

1. `Age is part of the clustering model, so how do we know the solution is not mainly age stratification plus correlated organ markers?`

2. `The final cohort may reflect testing intensity and missingness structure rather than underlying biology.`

3. `Why were these eight variables chosen from a larger candidate set, and how stable is the solution to alternate feature sets?`

4. `If the cohort was filtered to emergency-only, why does the final materials package still include outpatient care setting?`

5. `Without repeated-encounter sensitivity, how do we know cluster composition is not driven by recurring high-utilization patients?`

6. `A silhouette of 0.29 is acceptable for noisy clinical data, but what evidence shows the phenotypes are stable and not artifacts of preprocessing?`

7. `The hepatic phenotype may be under-characterized without bilirubin, coagulation variables, or broader liver function markers in the final model.`

## Additional Analyses That Could Strengthen the Paper

### Highest priority

1. Adult-only clustering sensitivity
2. Pediatric-only descriptive analysis, even if underpowered for clustering
3. Clustering sensitivity with age removed from the feature set
4. First-encounter-only sensitivity
5. Missingness table before and after density filtering

### Next priority

6. Complete-case vs KNN-imputed comparison
7. K-means vs one alternative method
8. Feature-set sensitivity:
   - with broader chemistry panel
   - without age
   - without platelet count or leukocytes

### Clinically valuable if linkable

9. Admission, ICU transfer, mortality, or length-of-stay association
10. Repeat clustering in temporally split cohorts

## What Should Become Supplementary Material

These items are strong candidates for supplement rather than main text:

- silhouette scores across `k=2..6`
- cluster-specific boxplots
- sex-by-cluster stacked bar
- care-setting stacked bar
- scatter plots of renal-inflammatory and hepatic spaces
- missingness summary tables
- repeated-encounter summary
- preprocessing sensitivity analyses

## What Could Become Future Work or a Second Paper

### Future work within the current paper’s trajectory

- validation against clinical outcomes
- adult-only vs pediatric-only phenotype comparison
- phenotype stability over time
- external validation in another institution

### Candidate second-paper directions

1. **Age-structured laboratory phenotyping in emergency care**
   - adult vs pediatric latent profiles
   - interaction between age and inflammatory/renal/hepatic patterns

2. **Repeated-encounter phenotype stability**
   - whether individuals recur in the same phenotype
   - whether phenotype transitions signal clinical worsening

3. **Phenotype-outcome linkage**
   - hospital admission
   - ICU use
   - mortality
   - revisits

4. **Testing-intensity and selection-bias analysis**
   - how laboratory ordering density shapes who enters the analytic cohort

## Bottom Line

### Most defensible strengthening points

- The clusters are clinically interpretable.
- Sex and age patterns appear meaningful.
- A weak care-setting association may support the conceptual value of multimarker phenotyping.
- The project has more scientific value than a simple visualization exercise.

### Most important weaknesses

- age/pediatric-adult confounding risk
- preprocessing dependence
- unresolved cohort-version inconsistency
- repeated-encounter uncertainty
- absent committed audit outputs and processed data

### Best next move before further manuscript revision

Run the audit script locally on the real processed files and use those outputs to answer four questions:

1. How much missingness remains after the density filter?
2. How many repeated encounters and repeated patients are present?
3. How strongly do pediatric/adult structure and age shape cluster membership?
4. Are the current clusters stable when age or preprocessing choices are varied?
