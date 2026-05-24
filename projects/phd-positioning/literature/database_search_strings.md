# Database-Specific Search Strings

## Use Notes

- Date drafted: `2026-05-24`
- Replace smart quotes if a database rejects them.
- Run each query exactly as written first, then adapt only if the interface requires syntax adjustments.
- If a controlled term is marked **to verify**, confirm it inside the database thesaurus before final execution.

## Controlled Vocabulary Table

### Verified MeSH anchors

| Concept | MeSH term | Status |
|---|---|---|
| Artificial intelligence | `"Artificial Intelligence"[Mesh]` | verified |
| Machine learning | `"Machine Learning"[Mesh]` | verified |
| Deep learning | `"Deep Learning"[Mesh]` | verified |
| Neural networks | `"Neural Networks, Computer"[Mesh]` | verified |
| Large language models | `"Large Language Models"[Mesh]` | verified |
| Hematology | `"Hematology"[Mesh]` | verified |
| Blood cell count | `"Blood Cell Count"[Mesh]` | verified |
| Leukocyte count | `"Leukocyte Count"[Mesh]` | verified |
| Leukocytes | `"Leukocytes"[Mesh]` | verified |
| Clinical laboratory techniques | `"Clinical Laboratory Techniques"[Mesh]` | verified |
| Decision support systems, clinical | `"Decision Support Systems, Clinical"[Mesh]` | verified |

### Verified DeCS anchors

| Concept | DeCS descriptor | Status |
|---|---|---|
| Inteligência Artificial / Artificial Intelligence | `Inteligência Artificial` / `Artificial Intelligence` | verified |
| Aprendizagem Profunda / Deep Learning | `Aprendizagem Profunda` / `Deep Learning` | verified |
| Hematologia / Hematology | `Hematologia` / `Hematology` | verified |
| Leucócitos / Leukocytes | `Leucócitos` / `Leukocytes` | verified |
| Contagem de Leucócitos / Leukocyte Count | `Contagem de Leucócitos` / `Leukocyte Count` | verified |
| Contagem de Células Sanguíneas / Blood Cell Count | `Contagem de Células Sanguíneas` / `Blood Cell Count` | verified |
| Sistemas de Apoio a Decisões Clínicas / Decision Support Systems, Clinical | `Sistemas de Apoio a Decisões Clínicas` | verified |
| Técnicas de Laboratório Clínico / Clinical Laboratory Techniques | `Técnicas de Laboratório Clínico` | verified |
| Modelos de Linguagem de Grande Escala / Large Language Models | `Modelos de Linguagem de Grande Escala` | verified |

### Provisional / to verify in Embase thesaurus

These are likely valid or closely mappable in Emtree, but should be checked in Embase before locked execution:

- `'artificial intelligence'/exp`
- `'machine learning'/exp`
- `'deep learning'/exp`
- `'neural network'/exp`
- `'large language model'/exp`
- `'hematology'/exp`
- `'blood cell count'/exp`
- `'leukocyte count'/exp`
- `'leukocyte'/exp`
- `'clinical laboratory technique'/exp`
- `'clinical decision support system'/exp`
- `'blood smear'/exp`
- `'peripheral blood smear'/exp`
- `'multimodal imaging'/exp` (note: may be too imaging-specific)
- `knowledge graph` as free text unless exact Emtree term is confirmed
- `foundation model` as free text unless exact Emtree term is confirmed
- `agentic ai` as free text unless exact Emtree term is confirmed

### Concepts to use mainly as free text

- peripheral blood smear
- peripheral blood film
- blood film
- hemogram / complete blood count / CBC / full blood count / FBC
- analyzer flag / instrument flag
- data fusion / multimodal learning
- foundation model
- knowledge graph
- reasoning-aware AI
- agentic AI
- domain shift / domain generalization / OOD

## Concept Blocks

### Block A. Hematology / laboratory domain

`hematolog* OR "laboratory medicine" OR "clinical laborator*" OR hemogram* OR haemogram* OR "complete blood count" OR CBC OR "full blood count" OR FBC OR "blood cell count" OR "leukocyte differential" OR "white blood cell differential" OR "hematologic test*" OR "haematologic test*"`

### Block B. Peripheral blood smear / morphology

`"blood smear*" OR "peripheral blood smear*" OR "peripheral smear*" OR "peripheral blood film*" OR "blood film*" OR "smear review" OR "cell morpholog*" OR "blood cell morpholog*" OR "leukocyte morpholog*" OR "white blood cell morpholog*" OR microscop*`

### Block C. Structured laboratory data / CBC / analyzer flags

`"complete blood count" OR CBC OR "full blood count" OR FBC OR hemogram* OR haemogram* OR "blood count parameter*" OR "laboratory parameter*" OR "structured laborator* data" OR "hematology analyzer*" OR "haematology analyzer*" OR "analyzer flag*" OR "analyser flag*" OR "instrument flag*" OR "differential count"`

### Block D. AI / ML / deep learning

`"artificial intelligence" OR "machine learning" OR "deep learning" OR "neural network*" OR "computer vision" OR transformer* OR "vision transformer*" OR YOLO OR "predictive model*" OR "computational model*"`

### Block E. Multimodal learning / data fusion

`multimodal OR "multimodal learning" OR "multimodal AI" OR "data fusion" OR "multimodal fusion" OR "multi-source data" OR "cross-modal" OR "image-tabular" OR "image and tabular" OR "image and laborator* data"`

### Block F. Reasoning systems / LLMs / knowledge-grounded AI

`reasoning OR "reasoning-aware" OR "clinical reasoning" OR "large language model*" OR LLM* OR "foundation model*" OR "knowledge graph*" OR "retrieval-augmented generation" OR RAG OR "agentic AI" OR "multi-agent" OR "decision support"`

### Block G. Robustness / domain shift / interpretability / uncertainty

`robust* OR "domain shift" OR "domain adaptation" OR "domain generalization" OR uncertainty OR calibration OR explainab* OR interpretab* OR "out-of-distribution" OR OOD`

## 1. PubMed / MEDLINE

### Broad / high sensitivity

```text
(
  "Hematology"[Mesh]
  OR "Blood Cell Count"[Mesh]
  OR "Leukocyte Count"[Mesh]
  OR "Leukocytes"[Mesh]
  OR "Clinical Laboratory Techniques"[Mesh]
  OR hematolog*[tiab]
  OR "laboratory medicine"[tiab]
  OR "clinical laborator*"[tiab]
  OR hemogram*[tiab]
  OR haemogram*[tiab]
  OR "complete blood count"[tiab]
  OR CBC[tiab]
  OR "full blood count"[tiab]
  OR FBC[tiab]
)
AND
(
  "blood smear*"[tiab]
  OR "peripheral blood smear*"[tiab]
  OR "peripheral smear*"[tiab]
  OR "peripheral blood film*"[tiab]
  OR "blood film*"[tiab]
  OR "cell morpholog*"[tiab]
  OR "leukocyte morpholog*"[tiab]
  OR microscop*[tiab]
  OR "smear review"[tiab]
  OR "Leukocytes"[Mesh]
)
AND
(
  "Artificial Intelligence"[Mesh]
  OR "Machine Learning"[Mesh]
  OR "Deep Learning"[Mesh]
  OR "Neural Networks, Computer"[Mesh]
  OR "Decision Support Systems, Clinical"[Mesh]
  OR "Large Language Models"[Mesh]
  OR "artificial intelligence"[tiab]
  OR "machine learning"[tiab]
  OR "deep learning"[tiab]
  OR "computer vision"[tiab]
  OR transformer*[tiab]
  OR "vision transformer*"[tiab]
  OR YOLO[tiab]
  OR multimodal[tiab]
  OR "data fusion"[tiab]
  OR "large language model*"[tiab]
  OR "knowledge graph*"[tiab]
  OR "decision support"[tiab]
)
```

**Captures:** the broadest set of hematology/laboratory AI studies touching smear morphology, multimodality, decision support, or LLM-style reasoning.

### Focused / high specificity

```text
(
  ("blood smear*"[tiab] OR "peripheral blood smear*"[tiab] OR "peripheral blood film*"[tiab] OR "blood film*"[tiab])
  AND
  ("complete blood count"[tiab] OR CBC[tiab] OR "full blood count"[tiab] OR FBC[tiab] OR hemogram*[tiab] OR "hematology analyzer*"[tiab] OR "analyzer flag*"[tiab] OR "instrument flag*"[tiab] OR "structured laborator* data"[tiab])
  AND
  (multimodal[tiab] OR "data fusion"[tiab] OR "multimodal learning"[tiab] OR "image and tabular"[tiab] OR "image and laborator* data"[tiab])
  AND
  ("artificial intelligence"[tiab] OR "machine learning"[tiab] OR "deep learning"[tiab] OR "computer vision"[tiab] OR transformer*[tiab] OR "clinical decision support"[tiab])
)
```

**Captures:** studies most directly aligned with the PhD direction: smear morphology + structured laboratory data + multimodal AI.

### Exploratory / cutting-edge

```text
(
  hematolog*[tiab]
  OR "clinical laborator*"[tiab]
  OR "blood smear*"[tiab]
  OR "complete blood count"[tiab]
  OR CBC[tiab]
)
AND
(
  "Large Language Models"[Mesh]
  OR "large language model*"[tiab]
  OR LLM*[tiab]
  OR "foundation model*"[tiab]
  OR "knowledge graph*"[tiab]
  OR "retrieval-augmented generation"[tiab]
  OR RAG[tiab]
  OR "agentic AI"[tiab]
  OR "multi-agent"[tiab]
  OR reasoning[tiab]
  OR "clinical reasoning"[tiab]
  OR "decision support"[tiab]
)
AND
(
  multimodal[tiab]
  OR "data fusion"[tiab]
  OR "structured laborator* data"[tiab]
  OR "analyzer flag*"[tiab]
  OR "domain shift"[tiab]
  OR robustness[tiab]
  OR interpretab*[tiab]
  OR uncertainty[tiab]
)
```

**Captures:** very recent reasoning-aware, knowledge-grounded, LLM, or agentic literature in hematology/laboratory contexts.

## 2. Scopus

Use `TITLE-ABS-KEY`.

### Broad / high sensitivity

```text
TITLE-ABS-KEY(
  (hematolog* OR "laboratory medicine" OR "clinical laborator*" OR hemogram* OR haemogram* OR "complete blood count" OR CBC OR "full blood count" OR FBC OR "blood cell count" OR "leukocyte differential")
  AND
  ("blood smear*" OR "peripheral blood smear*" OR "peripheral blood film*" OR "blood film*" OR "cell morpholog*" OR "leukocyte morpholog*" OR microscop*)
  AND
  ("artificial intelligence" OR "machine learning" OR "deep learning" OR "computer vision" OR "neural network*" OR transformer* OR "vision transformer*" OR YOLO OR multimodal OR "data fusion" OR "large language model*" OR "knowledge graph*" OR "decision support")
)
```

### Focused / high specificity

```text
TITLE-ABS-KEY(
  ("blood smear*" OR "peripheral blood smear*" OR "peripheral blood film*" OR "blood film*")
  AND
  ("complete blood count" OR CBC OR "full blood count" OR FBC OR hemogram* OR "hematology analyzer*" OR "analyzer flag*" OR "structured laborator* data")
  AND
  (multimodal OR "multimodal learning" OR "data fusion" OR "image and tabular" OR "image and laborator* data")
  AND
  ("artificial intelligence" OR "machine learning" OR "deep learning" OR "clinical decision support")
)
```

### Exploratory / cutting-edge

```text
TITLE-ABS-KEY(
  (hematolog* OR "clinical laborator*" OR "blood smear*" OR "complete blood count" OR CBC)
  AND
  ("large language model*" OR LLM* OR "foundation model*" OR "knowledge graph*" OR "retrieval-augmented generation" OR RAG OR "agentic AI" OR "multi-agent" OR reasoning OR "clinical reasoning")
  AND
  (multimodal OR "data fusion" OR "structured laborator* data" OR "domain shift" OR robustness OR uncertainty OR interpretab*)
)
```

**Scopus role:** broad interdisciplinary capture, including biomedical, informatics, and engineering papers.

## 3. Embase / Elsevier

Use Emtree plus title/abstract/keyword free text. Confirm provisional Emtree terms before locked execution.

### Broad / high sensitivity

```text
(
  'hematology'/exp OR 'blood cell count'/exp OR 'leukocyte count'/exp OR 'leukocyte'/exp OR 'clinical laboratory technique'/exp
  OR hematolog*:ti,ab,kw OR 'laboratory medicine':ti,ab,kw OR 'clinical laborator*':ti,ab,kw
  OR hemogram*:ti,ab,kw OR haemogram*:ti,ab,kw OR 'complete blood count':ti,ab,kw OR cbc:ti,ab,kw
)
AND
(
  'blood smear'/exp OR 'peripheral blood smear'/exp
  OR 'blood smear*':ti,ab,kw OR 'peripheral blood smear*':ti,ab,kw OR 'peripheral blood film*':ti,ab,kw OR 'blood film*':ti,ab,kw
  OR 'cell morpholog*':ti,ab,kw OR 'leukocyte morpholog*':ti,ab,kw OR microscop*:ti,ab,kw
)
AND
(
  'artificial intelligence'/exp OR 'machine learning'/exp OR 'deep learning'/exp OR 'neural network'/exp OR 'clinical decision support system'/exp
  OR 'large language model'/exp
  OR 'artificial intelligence':ti,ab,kw OR 'machine learning':ti,ab,kw OR 'deep learning':ti,ab,kw OR 'computer vision':ti,ab,kw
  OR transformer*:ti,ab,kw OR 'vision transformer*':ti,ab,kw OR yolo:ti,ab,kw OR multimodal:ti,ab,kw OR 'data fusion':ti,ab,kw
  OR 'large language model*':ti,ab,kw OR 'knowledge graph*':ti,ab,kw OR 'decision support':ti,ab,kw
)
```

### Focused / high specificity

```text
(
  ('blood smear*':ti,ab,kw OR 'peripheral blood smear*':ti,ab,kw OR 'peripheral blood film*':ti,ab,kw)
  AND
  ('complete blood count':ti,ab,kw OR cbc:ti,ab,kw OR 'full blood count':ti,ab,kw OR fbc:ti,ab,kw OR hemogram*:ti,ab,kw OR 'hematology analyzer*':ti,ab,kw OR 'analyzer flag*':ti,ab,kw OR 'structured laborator* data':ti,ab,kw)
  AND
  (multimodal:ti,ab,kw OR 'multimodal learning':ti,ab,kw OR 'data fusion':ti,ab,kw OR 'image and tabular':ti,ab,kw OR 'image and laborator* data':ti,ab,kw)
  AND
  ('artificial intelligence':ti,ab,kw OR 'machine learning':ti,ab,kw OR 'deep learning':ti,ab,kw OR 'clinical decision support':ti,ab,kw)
)
```

### Exploratory / cutting-edge

```text
(
  hematolog*:ti,ab,kw OR 'clinical laborator*':ti,ab,kw OR 'blood smear*':ti,ab,kw OR 'complete blood count':ti,ab,kw OR cbc:ti,ab,kw
)
AND
(
  'large language model*':ti,ab,kw OR llm*:ti,ab,kw OR 'foundation model*':ti,ab,kw OR 'knowledge graph*':ti,ab,kw
  OR 'retrieval-augmented generation':ti,ab,kw OR rag:ti,ab,kw OR 'agentic ai':ti,ab,kw OR 'multi-agent':ti,ab,kw
  OR reasoning:ti,ab,kw OR 'clinical reasoning':ti,ab,kw OR 'decision support':ti,ab,kw
)
AND
(
  multimodal:ti,ab,kw OR 'data fusion':ti,ab,kw OR 'structured laborator* data':ti,ab,kw
  OR 'domain shift':ti,ab,kw OR robustness:ti,ab,kw OR uncertainty:ti,ab,kw OR interpretab*:ti,ab,kw
)
```

**Embase role:** strong biomedical and conference coverage; especially useful for emerging clinical AI and conference abstracts.

## 4. SciELO / BVS

Use multilingual text words. Where the interface supports DeCS field selection, add descriptor filters separately.

### Broad / high sensitivity

```text
(
  hematologia OR hematology OR hematología OR
  "laboratório clínico" OR "laboratorio clínico" OR "clinical laboratory" OR
  hemograma OR hemogram OR haemogram OR
  "complete blood count" OR CBC OR "full blood count" OR FBC OR
  "contagem de leucócitos" OR "recuento de leucocitos" OR "leukocyte count"
)
AND
(
  "esfregaço sanguíneo" OR "esfregaço de sangue periférico" OR
  "frotis de sangre" OR "frotis de sangre periférica" OR
  "blood smear" OR "peripheral blood smear" OR "blood film" OR
  morfologia OR morphology OR morfología
)
AND
(
  "inteligência artificial" OR "inteligencia artificial" OR "artificial intelligence" OR
  "aprendizado de máquina" OR "aprendizaje automático" OR "machine learning" OR
  "aprendizagem profunda" OR "aprendizaje profundo" OR "deep learning" OR
  multimodal OR "dados multimodais" OR "datos multimodales" OR
  "fusão de dados" OR "fusión de datos" OR "data fusion" OR
  "apoio à decisão clínica" OR "apoyo a la decisión clínica" OR "clinical decision support"
)
```

### Focused / high specificity

```text
(
  ("esfregaço sanguíneo" OR "frotis de sangre" OR "blood smear" OR "peripheral blood smear")
  AND
  (hemograma OR "complete blood count" OR CBC OR "full blood count" OR "dados laboratoriais estruturados" OR "datos de laboratorio estructurados" OR "structured laboratory data" OR "analyzer flag" OR "hematology analyzer")
  AND
  (multimodal OR "dados multimodais" OR "datos multimodales" OR "fusão de dados" OR "fusión de datos" OR "data fusion")
  AND
  ("inteligência artificial" OR "inteligencia artificial" OR "artificial intelligence" OR "machine learning" OR "deep learning")
)
```

### Exploratory / cutting-edge

```text
(
  hematologia OR hematology OR hematología OR "laboratório clínico" OR "laboratorio clínico"
)
AND
(
  "modelos de linguagem de grande escala" OR "modelos de lenguaje de gran escala" OR "large language model" OR LLM OR
  "modelo fundacional" OR "foundation model" OR
  "grafo de conhecimento" OR "grafo de conocimiento" OR "knowledge graph" OR
  "IA agêntica" OR "IA agencial" OR "agentic AI" OR
  raciocínio OR razonamiento OR reasoning OR "clinical decision support"
)
AND
(
  multimodal OR "fusão de dados" OR "data fusion" OR robustez OR robustez OR robustness OR interpretabilidade OR interpretabilidad OR uncertainty
)
```

**SciELO role:** Latin American and Iberian visibility, especially for laboratory medicine and Portuguese/Spanish publications.

## 5. Web of Science

Use `TS=` for topic search.

### Broad / high sensitivity

```text
TS=(
  (hematolog* OR "laboratory medicine" OR "clinical laborator*" OR hemogram* OR haemogram* OR "complete blood count" OR CBC OR "full blood count" OR FBC OR "blood cell count" OR "leukocyte differential")
  AND
  ("blood smear*" OR "peripheral blood smear*" OR "peripheral blood film*" OR "blood film*" OR "cell morpholog*" OR "leukocyte morpholog*" OR microscop*)
  AND
  ("artificial intelligence" OR "machine learning" OR "deep learning" OR "computer vision" OR "neural network*" OR transformer* OR "vision transformer*" OR YOLO OR multimodal OR "data fusion" OR "large language model*" OR "knowledge graph*" OR "decision support")
)
```

### Focused / high specificity

```text
TS=(
  ("blood smear*" OR "peripheral blood smear*" OR "peripheral blood film*" OR "blood film*")
  AND
  ("complete blood count" OR CBC OR "full blood count" OR FBC OR hemogram* OR "hematology analyzer*" OR "analyzer flag*" OR "structured laborator* data")
  AND
  (multimodal OR "multimodal learning" OR "data fusion" OR "image and tabular" OR "image and laborator* data")
  AND
  ("artificial intelligence" OR "machine learning" OR "deep learning" OR "clinical decision support")
)
```

### Exploratory / cutting-edge

```text
TS=(
  (hematolog* OR "clinical laborator*" OR "blood smear*" OR "complete blood count" OR CBC)
  AND
  ("large language model*" OR LLM* OR "foundation model*" OR "knowledge graph*" OR "retrieval-augmented generation" OR RAG OR "agentic AI" OR "multi-agent" OR reasoning OR "clinical reasoning")
  AND
  (multimodal OR "data fusion" OR "structured laborator* data" OR "domain shift" OR robustness OR uncertainty OR interpretab*)
)
```

**Web of Science role:** citation-sensitive retrieval and cross-disciplinary coverage.

## 6. IEEE Xplore

Use Advanced Search. Prefer `Abstract` + `Author Keywords` + `Index Terms` when possible; otherwise use full metadata.

### Broad / high sensitivity

```text
("hematology" OR "clinical laboratory" OR "complete blood count" OR CBC OR "blood smear" OR "peripheral blood smear" OR "blood film")
AND
("artificial intelligence" OR "machine learning" OR "deep learning" OR "computer vision" OR transformer OR "vision transformer" OR YOLO OR multimodal OR "data fusion" OR "decision support")
```

### Focused / high specificity

```text
("blood smear" OR "peripheral blood smear" OR "blood film")
AND
("complete blood count" OR CBC OR "hematology analyzer" OR "analyzer flag" OR "structured laboratory data")
AND
(multimodal OR "data fusion" OR "image and tabular" OR "image and laboratory data")
AND
("machine learning" OR "deep learning" OR "clinical decision support")
```

### Exploratory / cutting-edge

```text
("hematology" OR "clinical laboratory" OR "blood smear" OR "complete blood count")
AND
("large language model" OR LLM OR "foundation model" OR "knowledge graph" OR "agentic AI" OR "multi-agent" OR reasoning)
AND
(multimodal OR "data fusion" OR robustness OR uncertainty OR interpretability)
```

**IEEE role:** computational methods, multimodal learning, fusion, and engineering-oriented decision support.

## 7. ACM Digital Library

Use Advanced Search. Interface field syntax varies by subscription layer, so if fielded syntax is rejected, run as plain boolean in `Anywhere`.

### Broad / high sensitivity

```text
("hematology" OR "clinical laboratory" OR "complete blood count" OR CBC OR "blood smear" OR "peripheral blood smear" OR "blood film")
AND
("artificial intelligence" OR "machine learning" OR "deep learning" OR "computer vision" OR transformer OR "vision transformer" OR YOLO OR multimodal OR "data fusion" OR "decision support")
```

### Focused / high specificity

```text
("blood smear" OR "peripheral blood smear" OR "blood film")
AND
("complete blood count" OR CBC OR "hematology analyzer" OR "analyzer flag" OR "structured laboratory data")
AND
(multimodal OR "data fusion" OR "image and tabular" OR "image and laboratory data")
AND
("machine learning" OR "deep learning" OR "clinical decision support")
```

### Exploratory / cutting-edge

```text
("hematology" OR "clinical laboratory" OR "blood smear" OR "complete blood count")
AND
("large language model" OR LLM OR "foundation model" OR "knowledge graph" OR "agentic AI" OR "multi-agent" OR reasoning)
AND
(multimodal OR "data fusion" OR robustness OR uncertainty OR interpretability)
```

**ACM role:** reasoning systems, knowledge-grounded AI, multimodal methods, and agentic systems that may not be fully represented in biomedical databases.

## Suggested Filters After Retrieval

Apply filters **after** running the raw queries:

- Years: `2021-2026`
- Humans when supported
- Article + conference paper
- Language: English, Portuguese, Spanish

## Important Cautions

1. `Multimodal Imaging` is a verified controlled term, but it is often too radiology/imaging-platform specific for this review.
2. `Blood Smear` may not behave as a stable controlled term across databases; always retain free-text smear terms.
3. `Foundation model`, `knowledge graph`, and `agentic AI` may be inconsistently indexed; free text is essential.
4. `Analyzer flags` are rarely captured by controlled vocab and should always remain free text.
