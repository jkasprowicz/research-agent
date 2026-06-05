# Citation
- title: Data-driven Models for Predicting No-show Rates and Service Times in Outpatient Appointment Scheduling
- authors: Moustapha Fall; Ilhem Slama; Yassine Ouazene; Achraf Jabbeur Telmoudi
- year: 2025
- country: France/Tunisia-authored; dataset from U.S. veterans care
- journal: Proceedings of the 2025 International Conference on Control, Decision and Information Technologies (CoDIT), IEEE/IFAC
- source file: /Users/joaokasprowicz/Documents/Projects/research-agent/projects/phd-positioning/literature/pdfs/tier1/Data-driven_Models_for_Predicting_No-show_Rates_and_Service_Times_in_Outpatient_Appointment_Scheduling.pdf

# Study Characteristics
- study objective: Predict no-show probability and service-time variability to improve outpatient appointment scheduling.
- healthcare setting: Primary and specialized outpatient care for U.S. veterans.
- patient population: Veterans with outpatient appointments between 2016 and 2023.
- sample size: Eight-year dataset; exact number of appointments should be verified in the tables before citation.
- study design: Predictive modeling study using CRISP-DM workflow.

# Data
- data source: Historical appointment/scheduling dataset from primary and specialized care.
- variables used: Waiting time, type of care, care provider, ZIP code, appointment/service attributes and engineered features.
- outcomes measured: No-show classification and service-time regression.

# Methods
- statistical methods: Performance metrics for classification and regression; imbalance handling with sampling/class weighting.
- machine learning methods: Random Forest, XGBoost, AdaBoost and Artificial Neural Networks.
- simulation methods: No simulation component in the extracted text.
- queueing methods: Queue consequences are motivating factors but not formal queueing-theory model.
- optimization methods: Designed to inform scheduling and reduce physician idle time/patient waiting time, but optimization is indirect.

# Results
- main findings: ANN achieved superior performance in both no-show and service-time tasks; key predictors differed by task.
- quantitative outcomes: The abstract reports ANN as best-performing; exact scores should be extracted from the paper tables.

# Limitations
- stated limitations: Conference paper; generalization depends on the veteran dataset and operational context.
- implicit limitations: Focuses appointment-level uncertainty, not public waiting-list regulation or equity across queue prioritization.

# Relevance for SUS Waiting Lists
- relevance score (1-5): 4
- justification: Methodologically useful for predictive features and outpatient scheduling, especially if SUS data include no-show/cancellation/service-time patterns.
