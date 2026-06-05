# Citation
- title: Dissatisfaction-considered waiting time prediction for outpatients with interpretable machine learning
- authors: Jongkyung Shin; Donggi Augustine Lee; Juram Kim; Chiehyeon Lim; Byung-Kwan Choi
- year: 2024
- country: South Korea
- journal: Health Care Management Science
- source file: /Users/joaokasprowicz/Documents/Projects/research-agent/projects/phd-positioning/literature/pdfs/tier1/10729_2024_Article_9676.pdf

# Study Characteristics
- study objective: Develop an interpretable outpatient waiting-time prediction framework that explicitly penalizes underestimation because underestimated waits can increase dissatisfaction.
- healthcare setting: Outpatient departments in a large South Korean hospital, including endocrinology/metabolism and neurosurgery case studies.
- patient population: Outpatients attending selected hospital departments.
- sample size: At least 7,709 outpatients reported for the endocrinology/metabolism dataset; full departmental sample details should be checked in tables before citation.
- study design: Retrospective predictive modeling case study using hospital information-system data.

# Data
- data source: Hospital information-system event logs and outpatient operational data.
- variables used: Queue length, queue composition, appointment status, patient/visit attributes, physician consultation time, temporal variables and operational process features.
- outcomes measured: Predicted waiting time; underestimation-aware model selection; explanations of predicted waiting time.

# Methods
- statistical methods: Model evaluation with accuracy/error metrics and the proposed dissatisfaction-aware asymmetric error score.
- machine learning methods: Machine-learning regression with asymmetric loss functions; SHAP for interpretability.
- simulation methods: No simulation component.
- queueing methods: Queue characteristics are central predictors and are interpreted using queueing intuition, but not as a full queueing-theory model.
- optimization methods: Model-selection framework balances accuracy against dissatisfaction risk from underestimation.

# Results
- main findings: Asymmetric loss reduced underestimation and SHAP highlighted operational drivers of waiting time, especially queue length and service-process variables.
- quantitative outcomes: The paper reports departmental model comparisons and examples of individual explanations; key numeric performance values should be extracted from the result tables before manuscript-level citation.

# Limitations
- stated limitations: Single-hospital case context and dependence on available HIS variables.
- implicit limitations: Strong for outpatient wait prediction but less directly connected to public-sector waiting-list governance, referral regulation or long-horizon queues.

# Relevance for SUS Waiting Lists
- relevance score (1-5): 4
- justification: Very relevant to explainable waiting-time prediction and reviewer-friendly Computer Science framing; less direct for SUS unless adapted to regulation workflow data.
