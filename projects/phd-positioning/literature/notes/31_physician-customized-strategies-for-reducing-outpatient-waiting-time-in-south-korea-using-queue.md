# Citation
- title: Physician-Customized Strategies for Reducing Outpatient Waiting Time in South Korea Using Queueing Theory and Probabilistic Metamodels
- authors: Hanbit Lee; Eun Kyoung Choi; Kyung A. Min; Eunji Bae; Hyun Lee; Jihyun Lee
- year: 2022
- country: South Korea
- journal: International Journal of Environmental Research and Public Health
- source file: /Users/joaokasprowicz/Documents/Projects/research-agent/projects/phd-positioning/literature/pdfs/tier2/ijerph-19-02073.pdf

# Study Characteristics
- study objective: Optimize outpatient waiting-time reduction strategies for individual physicians using queueing theory and probabilistic metamodels.
- healthcare setting: Outpatient department of a tertiary hospital in South Korea.
- patient population: Outpatient consultation sessions, customized at physician level.
- sample size: 542 consultation sessions reported in limitations.
- study design: Operational modeling/optimization study using real longitudinal outpatient data.

# Data
- data source: Outpatient waiting-time/consultation-session data from a tertiary hospital.
- variables used: Physician/session-level parameters, consultation times, arrival/session patterns and probability of waiting >30 minutes.
- outcomes measured: Probability of patients waiting more than 30 minutes and optimized physician-specific strategies.

# Methods
- statistical methods: Initial statistical analysis and probabilistic metamodeling.
- machine learning methods: No conventional ML model emphasized; metamodeling used for optimization.
- simulation methods: Metamodel-based scenario/optimization; not full DES in extracted abstract.
- queueing methods: Queueing theory calculates probability of waits over 30 minutes.
- optimization methods: NSGA-II multi-objective optimization for physician-specific strategy selection.

# Results
- main findings: Physician-customized strategies reduced the probability of long waits; department-level aggregate factors were not sufficient.
- quantitative outcomes: Average 30% decrease in probability of long waiting; dataset of 542 sessions noted as relatively small.

# Limitations
- stated limitations: Actual improvements may be lower than model estimates; small data volume per physician; field application needed.
- implicit limitations: Strong operations-research example but hospital outpatient setting differs from public waiting-list regulation.

# Relevance for SUS Waiting Lists
- relevance score (1-5): 4
- justification: Useful for showing that local heterogeneity matters and that explainable/customized operational strategies can beat generic rules.
