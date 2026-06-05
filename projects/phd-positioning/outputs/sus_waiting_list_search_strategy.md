# SUS Waiting-List Literature Search Strategy

## Objective

Build a focused, admission-oriented evidence base for a PhD plan on:

**Explainable predictive models and decision support for waiting-list dynamics in the Brazilian Unified Health System.**

The goal is not a systematic review yet. The goal is to identify enough high-quality literature to support:

- SUS waiting lists and regulation;
- healthcare queue dynamics;
- waiting-time prediction;
- patient prioritization;
- healthcare operations research;
- discrete-event simulation;
- explainable machine learning;
- decision support for healthcare managers.

## Core Concept Blocks

### Block A - SUS and Brazilian Regulation Context

English:

- "Brazilian Unified Health System"
- SUS
- "Sistema Único de Saúde"
- "healthcare regulation"
- "referral management"
- SISREG
- "e-SUS Regulação"
- "e-SUS Regulacao"
- "Regulação Assistencial"
- "Regulação do Acesso"
- "specialized care"
- "specialized outpatient care"
- "secondary care"

Portuguese:

- "Sistema Único de Saúde"
- SUS
- "lista de espera"
- "listas de espera"
- "fila de espera"
- "filas de espera"
- "regulação assistencial"
- "regulação do acesso"
- SISREG
- "e-SUS Regulação"
- "atenção especializada"
- "atenção ambulatorial especializada"
- "consultas especializadas"
- "cirurgias eletivas"

Spanish:

- "listas de espera"
- "sistema público de salud"
- "atención especializada"
- "gestión de listas de espera"

### Block B - Queues, Waiting Lists, and Patient Flow

- "waiting list*"
- "waiting time*"
- "healthcare queue*"
- "queue management"
- "queue dynamics"
- "patient flow"
- "access to care"
- "referral queue*"
- "elective surgery backlog"
- "appointment scheduling"
- "no-show"
- cancellation
- "excessive wait*"
- backlog

### Block C - Predictive Modeling and ML

- "machine learning"
- "artificial intelligence"
- "predictive model*"
- "predictive analytics"
- "risk prediction"
- "survival analysis"
- "time-to-event"
- "temporal validation"
- "calibration"
- "anomaly detection"
- "process mining"
- "sequence model*"

### Block D - Operations Research and Simulation

- "operations research"
- "operational research"
- "discrete-event simulation"
- "queueing theory"
- "queuing theory"
- "simulation model*"
- "capacity planning"
- optimization
- "resource allocation"
- "what-if analysis"
- "scenario analysis"
- "appointment scheduling"

### Block E - Explainability, Fairness, and Decision Support

- "explainable AI"
- "interpretable machine learning"
- XAI
- "decision support"
- "clinical decision support"
- "managerial decision support"
- "healthcare management"
- transparency
- fairness
- equity
- prioritization
- prioritisation
- "priority scoring"
- "triage"

## PubMed Search Strings

### Broad Search

```text
("Waiting Lists"[Mesh] OR "waiting list*"[tiab] OR "waiting time*"[tiab] OR "patient flow"[tiab] OR "healthcare queue*"[tiab] OR "queue management"[tiab] OR "referral management"[tiab])
AND
("Brazil"[Mesh] OR Brazil*[tiab] OR SUS[tiab] OR "Sistema Unico de Saude"[tiab] OR "Sistema Único de Saúde"[tiab] OR "Brazilian Unified Health System"[tiab] OR SISREG[tiab] OR "e-SUS"[tiab] OR "Regulacao Assistencial"[tiab] OR "Regulação Assistencial"[tiab])
```

Purpose: capture Brazilian/SUS waiting-list and regulation literature, including non-computational health-services papers.

### Focused Computational Search

```text
("Waiting Lists"[Mesh] OR "waiting list*"[tiab] OR "waiting time*"[tiab] OR "patient flow"[tiab] OR "referral management"[tiab] OR "queue management"[tiab])
AND
("Machine Learning"[Mesh] OR "Artificial Intelligence"[Mesh] OR "machine learning"[tiab] OR "artificial intelligence"[tiab] OR "predictive model*"[tiab] OR "predictive analytics"[tiab] OR "risk prediction"[tiab] OR "survival analysis"[tiab])
AND
("Decision Support Systems, Clinical"[Mesh] OR "decision support"[tiab] OR "healthcare management"[tiab] OR "patient prioritization"[tiab] OR prioritisation[tiab] OR prioritization[tiab])
```

Purpose: capture predictive and decision-support studies related to queues, patient flow, waiting times, and prioritization.

### Simulation / OR Search

```text
("waiting list*"[tiab] OR "waiting time*"[tiab] OR "patient flow"[tiab] OR "queue*"[tiab])
AND
("Models, Organizational"[Mesh] OR "Computer Simulation"[Mesh] OR "operations research"[tiab] OR "operational research"[tiab] OR "discrete-event simulation"[tiab] OR "queueing theory"[tiab] OR "queuing theory"[tiab] OR "capacity planning"[tiab] OR optimization[tiab])
AND
(healthcare[tiab] OR hospital*[tiab] OR outpatient[tiab] OR surgery[tiab] OR "specialized care"[tiab])
```

Purpose: identify OR, queueing, and simulation foundations.

## Scopus / Embase Search Strings

Use `TITLE-ABS-KEY` in Scopus. In Embase, adapt to title/abstract/keyword fields and add Emtree terms if available.

### Broad SUS / Regulation Search

```text
TITLE-ABS-KEY(
  ("waiting list*" OR "waiting time*" OR "fila de espera" OR "filas de espera" OR "lista de espera" OR "listas de espera" OR "patient flow" OR "referral management")
  AND
  (SUS OR "Sistema Único de Saúde" OR "Sistema Unico de Saude" OR "Brazilian Unified Health System" OR SISREG OR "e-SUS Regulação" OR "e-SUS Regulacao" OR "regulação assistencial" OR "regulacao assistencial" OR Brazil*)
)
```

### Focused ML / DSS Search

```text
TITLE-ABS-KEY(
  ("waiting list*" OR "waiting time*" OR "queue management" OR "queue dynamics" OR "patient flow" OR "referral management")
  AND
  ("machine learning" OR "artificial intelligence" OR "predictive analytics" OR "predictive model*" OR "risk prediction" OR "survival analysis" OR "anomaly detection" OR "process mining")
  AND
  ("decision support" OR "healthcare management" OR "patient prioritization" OR "patient prioritisation" OR "priority scoring" OR "explainable AI" OR "interpretable machine learning")
)
```

### Simulation / Operations Search

```text
TITLE-ABS-KEY(
  ("waiting list*" OR "waiting time*" OR "queue*" OR "patient flow" OR "elective surgery backlog")
  AND
  ("operations research" OR "operational research" OR "discrete-event simulation" OR "discrete event simulation" OR "queueing theory" OR "queuing theory" OR "capacity planning" OR optimization OR "resource allocation" OR "scenario analysis" OR "what-if analysis")
  AND
  (healthcare OR hospital* OR outpatient OR surgery OR "specialized care")
)
```

## IEEE Xplore / ACM Digital Library Search Strings

### Computational Queue Intelligence

```text
("healthcare" OR "health care" OR hospital OR outpatient)
AND
("waiting list" OR "waiting time" OR "queue management" OR "patient flow" OR "referral management")
AND
("machine learning" OR "predictive analytics" OR "decision support" OR "explainable AI" OR "interpretable machine learning")
```

### Simulation and Decision Support

```text
("healthcare" OR "health care" OR hospital OR outpatient)
AND
("discrete-event simulation" OR "queueing theory" OR "queuing theory" OR "operations research" OR optimization OR "capacity planning")
AND
("decision support" OR "scenario analysis" OR "what-if analysis" OR "resource allocation")
```

### Process and Anomaly Detection

```text
("healthcare" OR "health care")
AND
("patient flow" OR "queue" OR "waiting time" OR "referral")
AND
("process mining" OR "anomaly detection" OR "event log" OR "temporal modeling" OR "sequence modeling")
```

Purpose: find Computer Science and engineering papers likely absent from biomedical databases.

## SciELO Search Strings

### SUS Waiting Lists

```text
("listas de espera" OR "fila de espera" OR "filas de espera")
AND
("Sistema Único de Saúde" OR SUS OR "atenção especializada" OR "atenção ambulatorial especializada" OR "regulação assistencial" OR "regulação do acesso")
```

### Regulation and Specialized Care

```text
("regulação assistencial" OR "regulação do acesso" OR SISREG OR "e-SUS Regulação")
AND
("atenção especializada" OR "consultas especializadas" OR "cirurgias eletivas" OR "exames especializados" OR "lista de espera" OR "fila de espera")
```

### Portuguese Computational Search

```text
("aprendizado de máquina" OR "inteligência artificial" OR "modelo preditivo" OR "apoio à decisão" OR "simulação de eventos discretos" OR "pesquisa operacional")
AND
("fila de espera" OR "lista de espera" OR "tempo de espera" OR "fluxo de pacientes" OR "regulação assistencial")
```

Purpose: capture Brazilian public-health and management literature, including conceptual and policy sources that define the SUS problem.

## Google Scholar Search Strategy

Use staged searches rather than one large Boolean query.

### Stage 1 - Brazilian SUS Context

```text
"listas de espera" "atenção ambulatorial especializada" SUS
"fila de espera" "regulação assistencial" SUS
SISREG "lista de espera" "atenção especializada"
"e-SUS Regulação" "fila de espera"
"Sistema Único de Saúde" "tempo de espera" "consultas especializadas"
```

### Stage 2 - International Queue / OR Literature

```text
"healthcare waiting lists" "operations research"
"elective surgery waiting list" "dynamic priority scoring"
"patient prioritization" "waiting lists" "systematic review"
"discrete-event simulation" healthcare "waiting time"
"machine learning integrated patient flow simulation"
```

### Stage 3 - ML / XAI / DSS

```text
"machine learning" "waiting time prediction" healthcare
"patient flow" "machine learning" review
"explainable AI" "healthcare decision support" operations
"interpretable machine learning" "patient flow"
"decision support" "healthcare queue management"
```

### Stage 4 - Fairness and Transparency

```text
"fairness" "healthcare waiting lists"
"equity" "patient prioritization" "waiting lists"
"transparent prioritization" healthcare waiting list
"priority scoring" "waiting time" healthcare
```

## Priority Screening Labels

| Label | Definition |
|---|---|
| Core SUS context | Brazilian/SUS waiting-list, regulation, SISREG/e-SUS, specialized care, or referral-management paper. |
| Core computational | ML, OR, simulation, process mining, queue modeling, or DSS paper directly related to healthcare queues/waiting times. |
| Methodological foundation | General but strong paper on patient flow ML, DES, prioritization, XAI, fairness, or DSS. |
| Adjacent | Useful background but not directly about waiting lists or healthcare operations. |
| Exclude | Generic healthcare AI, clinical prediction unrelated to access/queues, policy-only without relevance, or non-health queueing with no transferable method. |

## Inclusion Criteria

- Last 5-7 years prioritized, with older foundational queueing/OR/DES papers allowed.
- Human healthcare settings.
- Waiting lists, patient flow, referral management, scheduling, prioritization, queue dynamics, or healthcare access.
- SUS/Brazilian public health system papers even if not computational, when they define the local problem.
- ML, prediction, XAI, operations research, simulation, optimization, process mining, or DSS methods.
- Reviews, original studies, methods papers, and official documentation relevant to regulation data.

## Exclusion Criteria

- Pure emergency triage papers without waiting-time, flow, queue, or management relevance.
- Generic medical AI without healthcare operations or access component.
- Queueing theory with no healthcare translation.
- Commercial queue-management material without scientific contribution.
- LLM/agent papers without concrete queue decision-support relevance.
- Pure policy commentary unless it defines SUS waiting-list concepts or data requirements.

## Recommended First Reading Set

- Ministério da Saúde documentation on PNRF, e-SUS Regulação, Sistemas de Informação na Regulação do Acesso, and Gestão da Fila de Espera.
- Giannotti et al. on specialized outpatient waiting lists in SUS.
- Gadenz et al. on telehealth-supported referral management in SUS.
- Rathnayake et al. on patient prioritization methods for elective surgery.
- Powers et al. on dynamic priority scoring for surgical waiting lists.
- El-Bouri et al. on machine learning in patient flow.
- Zhang on discrete-event simulation in healthcare.
- Abuhay et al. on ML-integrated patient-flow simulation.

