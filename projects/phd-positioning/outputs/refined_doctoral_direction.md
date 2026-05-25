# Direção Refinada de Doutorado

## Título-direção recomendado

**Inteligência clínico-laboratorial multimodal em hematologia: integração de morfologia de esfregaço periférico, parâmetros do hemograma e sinais estruturados de laboratório para apoio robusto e interpretável à decisão**

## Síntese estratégica

O mapeamento inicial da literatura mostra um cenário bastante claro:

1. A classificação baseada apenas em imagem para leucócitos e células sanguíneas é um campo já bastante povoado.
2. A integração entre morfologia, hemograma, flags do analisador e contexto laboratorial estruturado ainda é escassa.
3. Os trabalhos mais próximos da lacuna relevante são poucos, heterogêneos e ainda pouco consolidados em nível de caso.
4. LLMs e agentic AI em hematologia existem como sinal emergente, mas ainda aparecem mais como experimentação exploratória do que como eixo maduro e defensável de tese.

Portanto, a direção mais competitiva para o doutorado não é abandonar a morfologia, mas **elevá-la** de um problema de classificação celular para um problema de **inferência clínico-laboratorial multimodal em nível de caso**, com foco em:

- robustez interlaboratorial
- interpretabilidade
- apoio à decisão
- validação em dados laboratoriais reais

## 1. Melhor problema de pesquisa

O melhor problema de pesquisa para o doutorado é:

**Como desenvolver sistemas de inteligência artificial capazes de integrar, de forma robusta e interpretável, a morfologia de esfregaços sanguíneos periféricos com dados estruturados do laboratório clínico, como parâmetros do hemograma e flags do analisador hematológico, para produzir suporte diagnóstico e triagem em hematologia em nível de caso?**

Esse problema é superior a uma tese centrada apenas em classificação de leucócitos porque:

- dialoga diretamente com uma lacuna real da literatura
- tem valor computacional e translacional
- preserva continuidade com o mestrado
- abre espaço para contribuições metodológicas mais fortes em fusão multimodal, robustez e interpretabilidade

## 2. Pergunta central de pesquisa

**A integração multimodal entre morfologia de esfregaço periférico, parâmetros do hemograma, flags do analisador e contexto laboratorial estruturado melhora, de forma robusta e interpretável, o desempenho de sistemas de apoio à decisão hematológica em comparação com abordagens baseadas apenas em imagem?**

## 3. Objetivos específicos

### Objetivo específico 1

Construir e organizar uma base multimodal clínico-laboratorial em hematologia, integrando imagens de esfregaço periférico com parâmetros estruturados do hemograma, flags do analisador hematológico e metadados laboratoriais relevantes.

### Objetivo específico 2

Desenvolver e comparar arquiteturas computacionais de integração multimodal para inferência hematológica em nível de caso, avaliando diferentes estratégias de fusão entre sinais morfológicos e dados laboratoriais estruturados.

### Objetivo específico 3

Investigar robustez, generalização e confiabilidade desses sistemas diante de variabilidade interlaboratorial, com ênfase em calibração, incerteza, interpretabilidade e análise de falhas.

### Objetivo específico 4

Avaliar o potencial desses modelos como apoio à decisão em fluxos laboratoriais reais, especialmente em tarefas como triagem, priorização de revisão manual, suporte à identificação de alterações morfológicas relevantes e inferência diagnóstica assistida.

## 4. Lacuna científica central

A lacuna científica mais forte identificada pelo evidence map pode ser formulada da seguinte maneira:

**A literatura em hematologia computacional é abundante em estudos de classificação morfológica baseada em imagem, mas ainda é escassa em sistemas multimodais, robustos e interpretáveis que operem em nível de caso e integrem morfologia de esfregaço periférico com hemograma, flags do analisador e contexto laboratorial estruturado.**

Essa lacuna tem quatro componentes:

1. **Lacuna de integração**
   A maioria dos trabalhos permanece restrita à imagem, sem integração efetiva com sinais laboratoriais estruturados.

2. **Lacuna de nível de inferência**
   Grande parte da literatura opera em nível de célula, e não em nível de caso laboratorial.

3. **Lacuna de robustez**
   Robustez e generalização ainda são tratadas predominantemente em pipelines baseados apenas em imagem.

4. **Lacuna de apoio à decisão**
   Há poucos sistemas realmente voltados à lógica de revisão laboratorial, triagem ou suporte interpretativo integrado.

## 5. Evolução natural a partir da dissertação

Essa proposta evolui de forma orgânica da dissertação de mestrado.

No mestrado, o eixo central foi:

- classificação de células hematológicas em imagens de esfregaço periférico
- comparação rigorosa entre arquiteturas modernas
- construção de dataset próprio
- atenção a células imaturas e atípicas
- análise de robustez via aumento de dados e generalização externa

No doutorado, o salto não é temático, mas **de escopo inferencial**:

`classificação celular` -> `integração multimodal` -> `apoio à decisão hematológica em nível de caso`

Isso preserva:

- o domínio hematológico
- a morfologia como âncora
- a ênfase em robustez e aplicabilidade real

e adiciona:

- integração entre modalidades
- modelagem de contexto laboratorial
- interpretação orientada ao fluxo de trabalho

## 6. Vantagem competitiva do acesso a dados laboratoriais reais

O acesso a dados laboratoriais reais é uma vantagem competitiva decisiva por três razões.

### 1. Aumenta a originalidade

A maioria dos trabalhos mais saturados usa datasets públicos puramente imagéticos. O acesso a dados reais permite ir além do benchmark de imagem e avançar para um problema multimodal genuíno.

### 2. Aumenta o valor científico

Dados reais permitem estudar:

- relação entre morfologia e hemograma
- utilidade de flags do analisador
- regras de revisão manual
- variabilidade de aquisição e operação
- tarefas em nível de caso

Esse tipo de problema é metodologicamente mais rico do que apenas reconhecer tipos celulares.

### 3. Aumenta o valor translacional

Ter acesso a sinais laboratoriais reais aproxima a tese de uso concreto em:

- triagem
- priorização de revisão microscópica
- suporte à validação de resultados
- detecção de inconsistências entre morfologia e parâmetros automatizados

## 7. Metodologia viável para quem trabalha em tempo integral

O desenho metodológico precisa ser modular, reutilizável e publicável por etapas.

### Fase 1. Curadoria e harmonização de dados

- definir o escopo das variáveis laboratoriais
- harmonizar imagens, parâmetros do hemograma, flags e metadados
- construir um dataset multimodal em nível de caso
- documentar qualidade, missingness e regras de inclusão

### Fase 2. Baselines unimodais e multimodais

- baseline morfológico
- baseline tabular/laboratorial
- modelos multimodais com estratégias de fusão comparáveis
- definição de tarefas centrais: triagem, priorização, suporte a revisão, classificação de caso

### Fase 3. Robustez e confiabilidade

- avaliar generalização temporal ou intersetorial, quando possível
- estudar calibração, incerteza e análise de erro
- testar sensibilidade a variações de qualidade e composição dos dados

### Fase 4. Camada interpretável de apoio à decisão

- mecanismos de explicação de modalidade
- análise de contribuição relativa entre morfologia e hemograma
- saídas utilizáveis por especialistas, sem depender de LLMs genéricos

### Fase 5. Extensão opcional e bem controlada

Somente se a base principal estiver madura:

- camada de raciocínio apoiada por regras ou recuperação estruturada
- uso seletivo de LLM apenas como componente auxiliar, nunca como núcleo da proposta

### Por que isso é viável

- reutiliza infraestrutura do mestrado
- permite publicação incremental
- não depende de uma única coleta prospectiva massiva
- organiza a tese em blocos independentes, porém coerentes

## 8. Contribuições esperadas para Ciência da Computação

A proposta precisa ser claramente computacional. As contribuições esperadas para Ciência da Computação incluem:

### 1. Modelagem multimodal aplicada a dados heterogêneos

Desenvolvimento e avaliação de estratégias de fusão entre imagens citomorfológicas e dados laboratoriais estruturados.

### 2. Aprendizado robusto sob variabilidade de domínio

Estudo de generalização, calibração e incerteza em sistemas multimodais aplicados a ambientes laboratoriais reais.

### 3. Interpretabilidade multimodal orientada à decisão

Desenvolvimento de mecanismos que expliquem, em nível computacional, como diferentes modalidades contribuem para inferências em hematologia.

### 4. Infraestrutura de dados e benchmark translacional

Possível criação de um recurso multimodal reutilizável, com valor para pesquisa futura em IA biomédica.

### 5. Formulação computacional de um problema pouco explorado

Transformar a revisão hematológica multimodal em um problema formal de inteligência artificial, com tarefas, dados e critérios de avaliação mais próximos do mundo real.

## 9. Publicações potenciais

### Artigo 1

**Dataset e problema**

Construção e caracterização de uma base multimodal de hematologia integrando morfologia, hemograma e flags.

### Artigo 2

**Modelo multimodal**

Comparação entre abordagens unimodais e multimodais para inferência hematológica em nível de caso.

### Artigo 3

**Robustez e confiabilidade**

Generalização, calibração, incerteza e análise de falhas em hematologia multimodal.

### Artigo 4

**Apoio à decisão**

Modelo interpretável para triagem/revisão laboratorial assistida por IA.

### Artigo 5 opcional

**Raciocínio estruturado**

Camada de suporte interpretativo baseada em recuperação estruturada, regras ou conhecimento explícito.

## 10. Melhor enquadramento para orientação

## Orientador principal: Jônata Tyska Carvalho

O melhor enquadramento com Jônata é:

**IA multimodal e apoio à decisão em saúde, com ênfase em integração entre morfologia e dados laboratoriais estruturados**

Esse enquadramento funciona porque:

- mantém a proposta claramente em IA
- evita reduzi-la a um problema apenas de visão computacional
- abre espaço para raciocínio computacional, sem depender de hype

### Como apresentar para Jônata

Não enfatizar “LLM” como núcleo.

Enfatizar:

- integração multimodal
- inferência em nível de caso
- dados reais
- robustez
- suporte à decisão

## Alternativa: Renato Fileto

Com Renato, o melhor enquadramento é:

**integração semântica e análise multimodal de dados clínico-laboratoriais para apoio à decisão hematológica**

Esse enquadramento é forte quando a proposta destaca:

- integração de dados complexos
- estruturação e enriquecimento de dados laboratoriais
- raciocínio factual e apoio interpretativo

## 11. O que deve ser evitado

## Para não parecer excessivamente clínica

Evitar uma redação centrada em benefício assistencial genérico.

A proposta deve mostrar claramente:

- problema computacional
- desenho metodológico
- contribuição em fusão multimodal
- avaliação de robustez e interpretabilidade

## Para não parecer incremental demais

Evitar framing do tipo:

- “comparar novos modelos”
- “testar mais uma arquitetura”
- “melhorar acurácia da classificação”

O núcleo deve ser:

- integração multimodal em nível de caso
- não apenas refinamento de classificador

## Para não parecer genérica

Evitar expressões vagas como:

- “usar IA em hematologia”
- “aplicar LLMs em saúde”
- “criar sistema inteligente”

A proposta deve nomear explicitamente:

- esfregaço periférico
- hemograma
- flags do analisador
- apoio à decisão laboratorial

## Para não parecer ampla demais

Evitar prometer:

- diagnóstico universal em hematologia
- agente clínico geral
- integração com múltiplos domínios hospitalares

O escopo deve ser restrito a:

- hematologia laboratorial
- revisão morfológica periférica
- inferência assistida em nível de caso

## Formulação final recomendada

Se fosse necessário resumir toda a direção em uma única formulação estratégica, ela seria:

**Desenvolver e avaliar um sistema de inteligência artificial multimodal, robusto e interpretável, capaz de integrar morfologia de esfregaço sanguíneo periférico com parâmetros estruturados do hemograma e sinais do analisador hematológico, para apoio à decisão em hematologia em nível de caso.**

Essa formulação é:

- madura cientificamente
- coerente com o mestrado
- computacionalmente defensável
- publicável
- realista para execução com trabalho em tempo integral
