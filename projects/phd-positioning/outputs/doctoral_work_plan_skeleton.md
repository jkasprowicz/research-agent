# Esqueleto do Plano de Trabalho de Doutorado

## Título provisório

**Inteligência clínico-laboratorial multimodal em hematologia: integração de morfologia de esfregaço periférico, hemograma e sinais estruturados para apoio robusto à decisão**

## 1. Linha de pesquisa e aderência ao PPGCC/UFSC

### Linha principal recomendada

`Inteligência Computacional`

### Enquadramento recomendado

Projeto de inteligência artificial aplicada à saúde voltado ao desenvolvimento de modelos multimodais para integração entre imagens citomorfológicas e dados laboratoriais estruturados, com ênfase em robustez, interpretabilidade e apoio à decisão em hematologia.

### Orientador principal

`Jônata Tyska Carvalho`

### Orientador alternativo

`Renato Fileto`

## 2. Introdução e motivação

A revisão morfológica em hematologia continua sendo essencial para a identificação de alterações celulares relevantes que muitas vezes não são plenamente capturadas por analisadores automatizados. Ao mesmo tempo, a literatura recente em IA aplicada à hematologia mostra forte concentração em classificação de leucócitos baseada apenas em imagem. Embora esse campo seja tecnicamente ativo, ele é insuficiente para representar a lógica real da prática laboratorial, que depende da integração entre morfologia, parâmetros do hemograma, flags instrumentais e contexto estruturado do exame.

Dessa forma, há uma lacuna entre a maturidade da visão computacional hematológica e a construção de sistemas de apoio à decisão em nível de caso, mais próximos do fluxo real do laboratório clínico.

## 3. Problema de pesquisa

Como integrar, de forma robusta e interpretável, a morfologia de esfregaço periférico com parâmetros do hemograma, flags do analisador hematológico e contexto laboratorial estruturado para produzir suporte computacional à decisão em hematologia em nível de caso?

## 4. Pergunta central

A integração multimodal entre morfologia de esfregaço periférico, hemograma e sinais estruturados do laboratório melhora o desempenho, a robustez e a utilidade prática de sistemas de apoio à decisão hematológica em comparação com abordagens baseadas apenas em imagem?

## 5. Hipótese de trabalho

Modelos multimodais que integrem sinais morfológicos e laboratoriais estruturados produzirão inferências mais robustas, mais interpretáveis e mais úteis em nível de caso do que modelos unimodais baseados apenas em imagem, especialmente em cenários com maior variabilidade e ambiguidade morfológica.

## 6. Objetivo geral

Desenvolver e avaliar um sistema de inteligência artificial multimodal para hematologia capaz de integrar morfologia de esfregaço sanguíneo periférico, parâmetros do hemograma e sinais estruturados do laboratório, com foco em robustez, interpretabilidade e apoio à decisão em nível de caso.

## 7. Objetivos específicos

1. Construir uma base multimodal em hematologia combinando imagens citomorfológicas, hemograma, flags do analisador e metadados laboratoriais relevantes.
2. Desenvolver e comparar estratégias de fusão multimodal para tarefas de inferência hematológica em nível de caso.
3. Avaliar robustez, generalização, calibração e incerteza dos modelos em cenários de variabilidade laboratorial.
4. Propor uma camada interpretável de apoio à decisão laboratorial baseada na contribuição conjunta das modalidades analisadas.

## 8. Lacuna científica

A literatura atual é abundante em classificação morfológica de células sanguíneas, porém ainda escassa em sistemas multimodais e robustos que integrem imagem e dados laboratoriais estruturados em tarefas de apoio à decisão hematológica em nível de caso.

## 9. Metodologia proposta

### Etapa 1. Curadoria e estruturação dos dados

- definição de critérios de inclusão de casos
- harmonização entre imagens, CBC/hemograma, flags e metadados
- análise de qualidade, missingness e consistência

### Etapa 2. Definição das tarefas

Possíveis tarefas centrais:

- priorização de revisão manual
- suporte à identificação de alterações relevantes
- inferência de risco ou categoria diagnóstica em nível de caso

### Etapa 3. Baselines computacionais

- modelo apenas com imagem
- modelo apenas com dados tabulares
- modelo multimodal com diferentes estratégias de fusão

### Etapa 4. Robustez e interpretabilidade

- avaliação sob variabilidade interlaboratorial
- calibração e incerteza
- explicabilidade por modalidade
- análise de falhas

### Etapa 5. Extensão opcional

- mecanismo de raciocínio estruturado
- camada de apoio interpretativo baseada em regras ou recuperação

## 10. Viabilidade

O projeto é viável para execução por pesquisador em tempo integral de trabalho porque:

- pode ser modularizado em artigos independentes
- reutiliza experiência, infraestrutura e competências já desenvolvidas no mestrado
- depende mais de curadoria e modelagem incremental do que de um único experimento massivo
- permite etapas retrospectivas antes de qualquer validação prospectiva

## 11. Contribuições esperadas para Ciência da Computação

- estratégias de fusão multimodal entre imagem e dados laboratoriais estruturados
- avaliação de robustez em IA multimodal para ambientes clínico-laboratoriais
- mecanismos de interpretabilidade em modelos heterogêneos
- formalização computacional de tarefas laboratoriais em nível de caso
- possível recurso multimodal reutilizável para pesquisa futura

## 12. Resultados e produtos esperados

- base multimodal estruturada
- pipeline computacional reprodutível
- artigos científicos em IA aplicada à saúde / hematologia computacional
- framework de apoio à decisão laboratorial assistido por IA

## 13. Possíveis artigos derivados

1. dataset e caracterização multimodal
2. comparação unimodal versus multimodal
3. robustez, generalização e incerteza
4. apoio à decisão e interpretabilidade em fluxo laboratorial

## 14. Delimitação do escopo

O projeto não pretende:

- substituir o hematologista ou analista clínico
- resolver toda a hematologia diagnóstica
- depender centralmente de LLMs ou agentes genéricos

O projeto pretende:

- integrar modalidades relevantes
- melhorar inferência em nível de caso
- aproximar IA hematológica do laboratório real
