# Search Landscape Report - SUS Waiting-List Direction

Generated on: 2026-06-02

Input directory:

`/Users/joaokasprowicz/Documents/Projects/research-agent/projects/phd-positioning/literature/raw_search_results/`

## 1. Scope and Method

This report analyzes all CSV exports currently available in `literature/raw_search_results/`.

Loaded files:

| Source folder | File | Raw records |
|---|---:|---:|
| `ieee` | `export2026.06.02-17.58.44.csv` | 167 |
| `pubmed` | `csv-WaitingLis-set.csv` | 172 |
| `pubmed` | `csv-WaitingLis-set (1).csv` | 50 |
| `scielo` | `export_20260602.csv` | 31 |
| **Total** |  | **420** |

Deduplication logic:

- Primary key: normalized DOI, when available.
- Secondary key: normalized title.
- PubMed-specific key: PMID, used for duplicate detection inside PubMed exports.
- SciELO-specific key: SciELO ID, used for duplicate detection inside SciELO exports.
- IEEE `Document Identifier` was **not** used as a deduplication key because it is not a unique article identifier in this export.

Important limitation:

- IEEE records include abstracts and explicit keyword fields.
- PubMed records in the current CSV export include title, journal, year, DOI and citation, but not abstracts or keywords.
- SciELO records include title, journal, year and URL, but not abstracts or keywords.
- Therefore, keyword analysis combines explicit IEEE keywords with extracted concepts from titles/abstracts/keywords. PubMed and SciELO concept detection is necessarily title-heavy.

## 2. Deduplication Summary

| Metric | Count |
|---|---:|
| Raw records loaded | 420 |
| Unique records after deduplication | 417 |
| Duplicate records removed | 3 |
| Duplicate groups detected | 3 |

Duplicate groups detected:

| Duplicate title | Sources/files |
|---|---|
| Temporal Data Mining in AI-based Patient Navigation Service | IEEE export, duplicate within same file |
| Impact of management of access to cardiac surgery in the Brazilian Unified Health System at a university hospital in Campinas: pre-post analysis, 2013-2019 | PubMed + SciELO |
| Organization of a Pediatric Scoliosis Surgery Task Force and Analysis of Clinical and Radiographic Outcomes | PubMed + SciELO |

Source presence after deduplication:

| Source | Unique-source presence |
|---|---:|
| PubMed | 222 |
| IEEE | 166 |
| SciELO | 31 |

Note: source presence sums to more than 417 because cross-database duplicate records retain both source labels.

## 3. Records by Year

The search corpus is strongly recent: 344 of 417 unique records are from 2021 onward.

| Year | Unique records | Visual |
|---:|---:|---|
| 2026 | 54 | ##################### |
| 2025 | 126 | ################################################## |
| 2024 | 79 | ############################### |
| 2023 | 46 | ################## |
| 2022 | 49 | ################### |
| 2021 | 35 | ############## |
| 2020 | 15 | ###### |
| 2019 | 1 | # |
| 2018 | 2 | # |
| 2017 | 2 | # |
| 2012 | 2 | # |
| 2011 | 2 | # |
| 2008 | 1 | # |
| 2007 | 2 | # |
| 2006 | 1 | # |

Interpretation:

- The search is dominated by 2024-2026 material, which is useful for admission positioning.
- Older records are sparse and likely represent Brazilian access/waiting-list background or specific clinical domains.
- The high 2025 count reflects both current AI/healthcare operations literature and broad search retrieval noise.

## 4. Records by Journal / Venue

Top journals and venues:

| Rank | Journal / venue | Records |
|---:|---|---:|
| 1 | Cien Saude Colet | 11 |
| 2 | IEEE Access | 10 |
| 3 | J Bras Nefrol | 9 |
| 4 | Cad Saude Publica | 9 |
| 5 | Transplant Proc | 6 |
| 6 | BMC Health Serv Res | 5 |
| 7 | PLoS One | 5 |
| 8 | Sci Rep | 4 |
| 9 | BMC Med Inform Decis Mak | 4 |
| 10 | Rev Gaucha Enferm | 4 |
| 11 | Epidemiol Serv Saude | 4 |
| 12 | Einstein (Sao Paulo) | 4 |
| 13 | Cadernos de Saúde Pública | 4 |
| 14 | 2025 Winter Simulation Conference (WSC) | 3 |
| 15 | Cureus | 3 |
| 16 | Int J Environ Res Public Health | 3 |
| 17 | Community Dent Oral Epidemiol | 3 |
| 18 | Arq Bras Cir Dig | 3 |
| 19 | Saúde em Debate | 3 |
| 20 | 2025 4th International Conference on Sentiment Analysis and Deep Learning (ICSADL) | 2 |

Interpretation:

- Brazilian public-health journals are well represented: `Cien Saude Colet`, `Cad Saude Publica`, `Saúde em Debate`, `Epidemiol Serv Saude`.
- IEEE and WSC entries indicate computational/operations-search coverage.
- Nephrology/transplant venues are overrepresented because waiting-list searches retrieve organ-allocation literature.

## 5. Records by Explicit Keyword

Explicit keyword fields are mostly from IEEE exports. PubMed and SciELO CSVs do not provide keyword fields in the current exports.

Top explicit keywords / indexed terms:

| Rank | Keyword / term | Records |
|---:|---|---:|
| 1 | machine learning | 82 |
| 2 | hospitals | 77 |
| 3 | real time systems | 49 |
| 4 | medical services | 47 |
| 5 | artificial intelligence | 44 |
| 6 | resource management | 39 |
| 7 | predictive models | 38 |
| 8 | optimization | 31 |
| 9 | accuracy | 27 |
| 10 | predictive analytics | 24 |
| 11 | data models | 23 |
| 12 | healthcare | 22 |
| 13 | machine learning algorithms | 20 |
| 14 | deep learning | 19 |
| 15 | internet of things | 16 |
| 16 | telemedicine | 15 |
| 17 | training | 15 |
| 18 | schedules | 15 |
| 19 | analytical models | 13 |
| 20 | protocols | 13 |
| 21 | technological innovation | 12 |
| 22 | decision making | 12 |
| 23 | scheduling | 12 |
| 24 | medical diagnostic imaging | 12 |
| 25 | reinforcement learning | 12 |

Interpretation:

- The IEEE portion is strongly computational, with emphasis on ML, predictive analytics, optimization, scheduling, resource management and decision making.
- Some terms are too generic for the PhD topic, especially `hospitals`, `real time systems`, `internet of things`, `medical diagnostic imaging`, and `smart healthcare`.
- The current search successfully captured the computational neighborhood, but not all computational records are waiting-list specific.

## 6. Extracted Concept Frequencies

Concepts were detected using normalized title/abstract/keyword text. Counts are overlapping; one record may belong to multiple concepts.

| Concept | Records |
|---|---:|
| ML / AI / predictive analytics | 167 |
| Decision support / explainability | 126 |
| Waiting lists / waiting time | 125 |
| Simulation / operations research / optimization | 108 |
| Brazil / SUS / regulation context | 99 |
| Patient flow / access / referrals | 98 |
| Prioritization / triage / equity | 88 |
| Emergency / pandemic / discharge | 88 |
| Surgery / elective procedures / transplant | 73 |
| Queue modeling / queue management | 26 |
| NLP / text mining / LLM | 22 |
| No-show / cancellation | 7 |

Visual summary:

```text
ML / AI / predictive analytics              | 167 | ##################################################
Decision support / explainability           | 126 | ######################################
Waiting lists / waiting time                | 125 | #####################################
Simulation / OR / optimization              | 108 | ################################
Brazil / SUS / regulation context           |  99 | ##############################
Patient flow / access / referrals           |  98 | #############################
Prioritization / triage / equity            |  88 | ##########################
Emergency / pandemic / discharge            |  88 | ##########################
Surgery / elective / transplant             |  73 | ######################
Queue modeling / management                 |  26 | ########
NLP / text mining / LLM                     |  22 | #######
No-show / cancellation                      |   7 | ##
```

Interpretation:

- The search has enough material to support a doctoral framing around explainable ML and decision support for waiting-list dynamics.
- The strongest computational neighborhoods are ML/prediction, decision support, simulation/optimization and patient-flow modeling.
- The narrowest but most directly relevant concepts are queue modeling, no-show/cancellation and SUS-specific waiting-list regulation.
- The small number of explicit no-show/cancellation records suggests this may be a focused subtopic rather than the central framing.

## 7. Major Thematic Clusters

Cluster counts are overlapping because records can belong to more than one thematic group.

| Cluster | Records | Strategic relevance |
|---|---:|---|
| Healthcare queues, wait-time and patient-flow methods | 131 | High. Core methodological neighborhood. |
| ML/AI prediction for healthcare operations | 143 | High, but needs filtering for operational relevance. |
| Simulation/optimization/OR decision support | 108 | High. Strong for Computer Science contribution. |
| Prioritization/triage/fairness | 82 | High but ethically sensitive; best as evaluation layer. |
| Generic hospital AI / smart healthcare | 51 | Mixed. Useful for methods, noisy for proposal. |
| Direct SUS/Brazil access and waiting-list evidence | 29 | Very high. Most important for contextual justification. |
| Condition-specific treatment delays | 14 | Adjacent; useful only when about access/waiting time. |
| Transplant/allocation waiting lists | 12 | Methodologically adjacent but potentially distracting. |
| No-show/cancellation/appointment adherence | 7 | Useful subproblem, not enough alone for thesis core. |
| Other / weak signal | 173 | Screening burden; many likely exclusions. |

### Cluster A - Direct SUS/Brazil Access and Waiting-List Evidence

Examples:

- Surgical waiting lists and queue management in a Brazilian tertiary public hospital
- Telehealth Strategies to Support Referral Management to Secondary Care in Brazil: A Cost-Effectiveness Analysis
- Poor access to health services for depression treatment in Brazil
- Waiting time for kidney transplantation based on calculated panel reactive antibodies: experience of a southern Brazilian center

Strategic value:

- This cluster anchors the project in the SUS context.
- It supports the claim that waiting lists, access, specialized care and regulation are real Brazilian health-system problems.
- It is probably smaller than expected, meaning the proposal should not claim a mature Brazilian AI-for-waiting-lists literature.

### Cluster B - Healthcare Queues, Wait-Time and Patient-Flow Methods

Examples:

- Reducing outpatient waiting time: a case study in Vietnamese private hospital
- Data-driven Models for Predicting No-show Rates and Service Times in Outpatient Appointment Scheduling
- Applying queueing theory to evaluate wait-time-savings of triage algorithms
- Patient Waiting List Management: A Systematic Analysis of Current Approaches and Evidence Gaps

Strategic value:

- This cluster supports the computational formulation of waiting lists as dynamic operations problems.
- It is the main bridge between SUS access problems and Computer Science methods.

### Cluster C - ML/AI Prediction for Healthcare Operations

Examples:

- Optimizing Patient Flow and Resource Allocation in Hospitals using AI
- Reducing Delayed Hospital Discharges Through AI-Driven Documentation and Machine Learning-Based Predictive Models
- A Machine Learning Pipeline Using KNIME to Predict Hospital Admission in the MIMIC-IV Database
- Predictive and Personalized Healthcare Scheduling by Integrating No Show Prediction with Artificial Intelligence

Strategic value:

- This cluster is highly relevant but noisy.
- It shows that ML for healthcare operations is active, but many papers are generic and not specific to waiting-list governance.
- For the PhD, the contribution must avoid becoming "generic AI for hospital operations."

### Cluster D - Simulation, Optimization and Operations Research

Examples:

- Integrating Lean Healthcare Practices with Discrete-Event Simulation to Reduce Patient Waiting Time in Outpatient Clinics at a Sri Lankan Public Hospital
- Combined Applications of Artificial Intelligence and Simulation for Healthcare Process Optimization: A Systematic Review
- Decision support model for the patient admission scheduling problem based on picture fuzzy aggregation information and TOPSIS methodology
- Bayesian Machine Learning for Decision Support in Healthcare Operations Management

Strategic value:

- This is one of the strongest clusters for PPGCC/Computer Science alignment.
- It supports the selected admission framing: hybrid explainable ML + simulation for decision support.
- It also introduces feasibility risk because simulation depends on capacity/slot/resource data.

### Cluster E - Prioritization, Triage and Fairness

Examples:

- Gender-Equity Model for Liver Allocation Using Artificial Intelligence (GEMA-AI) for Waiting List Liver Transplant Prioritization
- Artificial Intelligence-Driven Triage in Pediatric Emergency Departments
- An intelligent community-based system for healthcare prioritisation
- A Structure-Based Scoring Policy for Patient Stratification on the U.S. Heart Transplant National Waiting List

Strategic value:

- Relevant to prioritization and transparency.
- Politically and ethically sensitive in SUS if framed as automated patient ranking.
- Best used as an evaluation and governance concern, not as the central thesis promise.

### Cluster F - No-Show / Cancellation / Appointment Adherence

Examples:

- Predictive and Personalized Healthcare Scheduling by Integrating No Show Prediction with Artificial Intelligence
- Investigating Key Contributors to Hospital Appointment No-Shows Using Explainable AI
- Data-driven Models for Predicting No-show Rates and Service Times in Outpatient Appointment Scheduling

Strategic value:

- This is a concrete, feasible subproblem.
- It may become a first or second paper if the SUS dataset has appointment outcomes.
- It is too narrow as the full doctoral identity.

## 8. Most Frequent Concepts

The dominant concepts suggest that the current search landscape is organized around five axes:

| Axis | Evidence in corpus | Interpretation |
|---|---|---|
| AI/ML for healthcare operations | Very high | Good for PPGCC alignment, but broad/noisy. |
| Waiting time, queues and patient flow | High | Directly relevant to the new topic. |
| Decision support and explainability | High | Strong for admission framing and manager-facing contribution. |
| Simulation/optimization | High | Strong Computer Science contribution, especially if data access supports it. |
| Brazil/SUS/access context | Moderate | Enough for justification, but likely needs targeted expansion. |

Strategic implication:

The search supports the new PhD direction, but the strongest proposal should not be framed as generic healthcare AI. It should be framed as:

**event-based, explainable and simulation-aware decision support for waiting-list dynamics in SUS regulation workflows.**

## 9. Potentially Irrelevant or Low-Value Clusters

The search retrieved several clusters that may be useful only as background or should be excluded during screening.

| Potentially irrelevant cluster | Why it may be low value | Estimated signal |
|---|---|---|
| Generic hospital AI / smart healthcare | Often about IoT, smart hospitals, dashboards, sentiment analysis or broad AI transformation without queue-specific methods. | Mostly exclude or background only |
| Transplant/allocation waiting lists | Waiting-list terminology is relevant, but the allocation problem is highly domain-specific and may distract from SUS regulation workflows. | Adjacent, not central |
| Condition-specific treatment delays | Useful for access-to-care motivation, but many papers are disease-specific and not queue-modeling papers. | Background only unless methods transfer |
| Emergency/pandemic operations | Some methods transfer to patient flow, but many are emergency-department or COVID-specific. | Adjacent |
| NLP/patient feedback | Captures waiting time as satisfaction factor, not queue management. | Mostly exclude |
| Generic medical AI | Radiology, nuclear medicine, diagnostic support and clinical prediction papers without access/queue component. | Exclude |

Examples of likely low-relevance titles:

- AI in nuclear medicine
- Machine learning and deep learning for classifying the justification of brain CT referrals
- Intermittent fasting for adults with overweight or obesity
- Impact of a Digital Intelligence Platform on Radiology Workflow Efficiency and Patient Satisfaction
- Descriptor: Waiting in Line in Virtual Reality Dataset (WAIT)

## 10. Strategic Reading Priorities

### Highest priority

Prioritize records that combine at least two of the following:

- SUS/Brazil/regulation/access context;
- waiting list, waiting time or queue behavior;
- ML/prediction, decision support, simulation or optimization;
- patient-flow or referral-management endpoint.

High-priority examples from the current landscape:

- Surgical waiting lists and queue management in a Brazilian tertiary public hospital
- Patient Waiting List Management: A Systematic Analysis of Current Approaches and Evidence Gaps
- Telehealth Strategies to Support Referral Management to Secondary Care in Brazil: A Cost-Effectiveness Analysis
- Data-driven Models for Predicting No-show Rates and Service Times in Outpatient Appointment Scheduling
- Applying queueing theory to evaluate wait-time-savings of triage algorithms
- Combined Applications of Artificial Intelligence and Simulation for Healthcare Process Optimization: A Systematic Review

### Medium priority

Use selectively:

- transplant allocation and prioritization papers;
- emergency triage papers;
- generic patient-flow prediction papers;
- simulation/optimization papers from non-SUS contexts.

### Low priority / likely exclude

Exclude unless there is a specific methodological reason:

- generic diagnostic AI;
- patient sentiment/feedback papers;
- disease-treatment delay papers without queue modeling;
- smart hospital papers with no waiting-list or patient-flow task;
- broad AI transformation papers.

## 11. Initial Screening Recommendation

Suggested screening labels:

| Label | Use for |
|---|---|
| Directly relevant | SUS/Brazil waiting lists, regulation, queue management, referral management, or computational waiting-list decision support. |
| Methodologically relevant | Non-SUS ML/OR/simulation/XAI papers directly about queues, waiting time, appointment scheduling, patient flow or prioritization. |
| Adjacent background | Access-to-care, transplant allocation, emergency flow, no-show prediction, treatment delays, or health-system management papers with partial relevance. |
| Exclude | Generic medical AI, diagnostic imaging, sentiment analysis, non-queue patient satisfaction, disease-only treatment papers, generic smart hospital AI. |

## 12. Overall Assessment

The current search results are broad but useful. They support the SUS waiting-list PhD direction in three ways:

1. They show a strong computational literature around ML, decision support, simulation, optimization and patient-flow operations.
2. They identify a smaller but important Brazilian/SUS access and regulation literature that can justify the applied domain.
3. They reveal a gap between general healthcare operations AI and the specific need for explainable, event-based waiting-list decision support in SUS regulation.

The main problem is noise. A large fraction of the corpus is adjacent or weakly relevant. The next screening round should aggressively separate:

- **SUS waiting-list/regulation evidence**
- **transferable computational methods**
- **background health-access literature**
- **irrelevant generic healthcare AI**

Most important admission implication:

The evidence supports the selected framing:

**Explainable predictive models plus simulation-aware decision support for waiting-list dynamics in SUS.**

It does **not** support a generic "AI for SUS queues" proposal. The proposal should remain specific to event logs, queue behavior, temporal validation, explainability, and manager-facing decision support.

