# Citation
- title: Reducing Patient Waiting Time at Public Hospitals Through Predictive Modeling
- authors: Tsitsi Mandizvida; Sibonile Moyo; Mary Dzinomwa et al.
- year: 2024
- country: Zimbabwe
- journal: 3rd Zimbabwe Conference on Information Communication & Technology (ZCICT), IEEE
- source file: /Users/joaokasprowicz/Documents/Projects/research-agent/projects/phd-positioning/literature/pdfs/tier2/Reducing_Patient_Waiting_Time_at_Public_Hospitals_Through_Predictive_Modeling.pdf

# Study Characteristics
- study objective: Use predictive modeling to classify public-hospital queue records as delayed or not delayed.
- healthcare setting: Five public health centers in Harare, Bulawayo and Gweru, Zimbabwe.
- patient population: Patients attending selected public health centers between Oct 1 and Dec 31, 2023.
- sample size: Exact sample size not clearly extracted; paper states the sample was adequate for analysis.
- study design: Predictive modeling study using electronic records.

# Data
- data source: Electronic records from five public health centers.
- variables used: Waiting time, appointment scheduling, triage process, referral pathway, administrative factors and demographics.
- outcomes measured: Binary delayed/not-delayed queue classification.

# Methods
- statistical methods: Stratified K-fold cross-validation and model-performance metrics including ROC AUC.
- machine learning methods: Logistic Regression, Decision Tree, Random Forest and XGBoost.
- simulation methods: No simulation component.
- queueing methods: Queue data are classified but not analytically modeled.
- optimization methods: No direct optimization; prediction intended to guide operational decisions.

# Results
- main findings: XGBoost was the best-performing model, but overall discrimination was modest.
- quantitative outcomes: XGBoost ROC AUC 0.63; other models ranged from 0.56 to 0.60.

# Limitations
- stated limitations: Not clearly captured in extracted text.
- implicit limitations: Modest performance, short data window and limited validation reduce evidentiary strength; good cautionary example against overclaiming ML.

# Relevance for SUS Waiting Lists
- relevance score (1-5): 3
- justification: Useful as a low-resource public-hospital ML example, but not as strong as SUS-specific regulation studies.
