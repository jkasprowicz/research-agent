# Citation
- title: Applying queueing theory to evaluate wait-time-savings of triage algorithms
- authors: Yee Lam Elim Thompson et al.
- year: 2024
- country: United States
- journal: Queueing Systems
- source file: /Users/joaokasprowicz/Documents/Projects/research-agent/projects/phd-positioning/literature/pdfs/tier1/s11134-024-09927-w.pdf

# Study Characteristics
- study objective: Develop queueing-theory methods to quantify wait-time savings from AI-enabled triage algorithms.
- healthcare setting: Radiology image-interpretation workflow, used as a general model for classifier-based triage queues.
- patient population: Simulated/analytical patient-image arrivals, including diseased and non-diseased image classes.
- sample size: Analytical/simulation study over parameter ranges rather than a fixed empirical patient sample.
- study design: Queueing-theory modeling with simulation software for validation and confidence intervals.

# Data
- data source: Theoretical workflow models and parameterized diagnostic-performance/service-rate/arrival-rate scenarios.
- variables used: Classifier sensitivity/specificity, false positives/false negatives, arrival rates, radiologist service rates, number of servers and priority rules.
- outcomes measured: Mean waiting-time difference for prioritized/diseased cases with versus without AI triage.

# Methods
- statistical methods: Confidence intervals from simulation; analytical wait-time calculations.
- machine learning methods: No model is trained; AI classifier performance is parameterized as input.
- simulation methods: Workflow simulation tool used to verify queueing-theory results.
- queueing methods: Central method: single- and multi-server queueing models for prioritized triage.
- optimization methods: Not an optimization paper, but supports evaluation of triage deployment decisions.

# Results
- main findings: AI triage saves more time in busy, short-staffed settings; benefit depends on arrival rate, service rate and classifier error profile.
- quantitative outcomes: Quantitative outputs are scenario-dependent; the paper defines wait-time savings as mean waiting-time difference with versus without CADt.

# Limitations
- stated limitations: Abstracted workflow and assumptions; primarily radiology-focused; classifier outputs simplified to binary triage.
- implicit limitations: Not about SUS, but conceptually powerful for evaluating whether predictive prioritization actually improves queue outcomes.

# Relevance for SUS Waiting Lists
- relevance score (1-5): 4
- justification: Excellent methodological support for measuring operational value of AI triage beyond AUC, transferable to waiting-list decision support.
