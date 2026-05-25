# Rascunho de Plano de Trabalho de Doutorado

## Título provisório

**Inteligência clínico-laboratorial multimodal em hematologia: integração de morfologia de esfregaço periférico, parâmetros do hemograma e flags do analisador para apoio robusto e interpretável à decisão**

## 1. Introdução, motivação e relevância

A hematologia laboratorial depende de uma articulação contínua entre automação analítica e revisão morfológica especializada. Embora os analisadores hematológicos modernos forneçam parâmetros quantitativos amplos e flags de alerta, a análise citomorfológica de esfregaços periféricos permanece indispensável para o reconhecimento de alterações celulares relevantes, especialmente em casos com células imaturas, atípicas, reativas ou displásicas. Na prática, a decisão laboratorial não é baseada apenas na imagem de uma célula isolada, mas na combinação entre morfologia, hemograma, sinais instrumentais e contexto do exame.

A literatura recente em inteligência artificial aplicada à hematologia mostra crescimento importante, mas com forte concentração em tarefas de classificação baseada apenas em imagem. O mapeamento inicial realizado a partir de PubMed e Embase mostrou um campo muito ativo em classificação e detecção de leucócitos e células sanguíneas, incluindo arquiteturas convolucionais, transformadores visuais, técnicas de aumento de dados e abordagens de generalização. No entanto, o mesmo mapeamento mostrou que os trabalhos realmente voltados à integração entre morfologia de esfregaço periférico, parâmetros do hemograma, flags do analisador hematológico e contexto laboratorial estruturado ainda são poucos e fragmentados.

A principal oportunidade científica, portanto, não está em propor apenas mais um classificador celular, mas em avançar da inteligência morfológica para a **inteligência clínico-laboratorial multimodal em nível de caso**. Esse avanço é coerente com a realidade do laboratório clínico, com o histórico do candidato e com uma lacuna relevante para a Ciência da Computação aplicada à saúde: modelar, integrar e interpretar dados heterogêneos em ambientes com forte variabilidade e restrições reais de uso.

## 2. Problema de pesquisa e pergunta central

O problema central deste doutorado é a ausência de sistemas robustos e interpretáveis capazes de integrar, de forma coerente, a morfologia de esfregaços sanguíneos periféricos com dados laboratoriais estruturados para apoiar inferências hematológicas em nível de caso.

A pergunta central é:

**A integração multimodal entre morfologia de esfregaço periférico, parâmetros do hemograma, flags do analisador e contexto laboratorial estruturado permite construir sistemas de apoio à decisão hematológica mais robustos, interpretáveis e úteis do que abordagens baseadas apenas em imagem?**

## 3. Lacuna científica

A lacuna identificada pode ser descrita em quatro níveis.

Primeiro, existe uma **lacuna de integração**: a maior parte da literatura se concentra em imagens de células ou esfregaços, sem incorporar adequadamente hemograma, differential, flags ou metadados laboratoriais. Segundo, existe uma **lacuna de nível inferencial**: a maioria dos trabalhos produz saídas em nível de célula, enquanto a prática laboratorial opera em nível de caso. Terceiro, há uma **lacuna de robustez multimodal**: robustez, calibração, incerteza e generalização são estudadas principalmente em pipelines imagéticos, e muito menos em sistemas que combinem sinais heterogêneos. Quarto, existe uma **lacuna de apoio à decisão**: poucos estudos se aproximam da lógica real de triagem, revisão manual, interpretação integrada e fluxo laboratorial.

Essa lacuna é cientificamente relevante porque define um problema computacional ainda pouco explorado: a fusão de sinais laboratoriais heterogêneos em um sistema interpretável, confiável e útil para decisões assistidas em hematologia.

## 4. Continuidade com o mestrado

Esta proposta evolui diretamente da dissertação de mestrado do candidato. No mestrado, foram desenvolvidos e comparados modelos de aprendizado profundo para classificação automática de células hematológicas, com ênfase em classes morfologicamente relevantes, dataset próprio, variabilidade de coloração, robustez e generalização externa. O trabalho resultou não apenas em um problema de classificação, mas em uma base metodológica madura que inclui:

- formulação de problema clínico-laboratorial relevante
- construção e validação de dataset
- comparação rigorosa entre arquiteturas
- preocupação com classes difíceis
- análise de robustez e generalização
- preocupação com aplicabilidade real

O doutorado preserva a morfologia como âncora, mas amplia o nível de modelagem:

`classificação celular` -> `integração multimodal` -> `apoio à decisão hematológica em nível de caso`

Assim, não há ruptura temática. Há evolução metodológica e ampliação do escopo científico.

## 5. Objetivos

### Objetivo geral

Desenvolver e avaliar um sistema de inteligência artificial multimodal para hematologia capaz de integrar morfologia de esfregaço sanguíneo periférico, parâmetros do hemograma e sinais estruturados do laboratório, com foco em robustez, interpretabilidade e apoio à decisão em nível de caso.

### Objetivos específicos

1. Construir uma base multimodal clínico-laboratorial em hematologia combinando imagens de esfregaço periférico com parâmetros do hemograma, flags do analisador e metadados laboratoriais relevantes.
2. Desenvolver e comparar estratégias de fusão multimodal para tarefas de inferência hematológica em nível de caso, contrastando abordagens unimodais e multimodais.
3. Investigar robustez, generalização, calibração, incerteza e interpretabilidade dos modelos sob variabilidade laboratorial real.
4. Propor uma camada de apoio à decisão laboratorial baseada na contribuição conjunta das modalidades, priorizando transparência e utilidade prática.

## 6. Metodologia proposta

A metodologia será organizada em etapas modulares, compatíveis com execução ao longo do doutorado por pesquisador que trabalha em tempo integral.

### Etapa 1. Curadoria e harmonização multimodal

Serão identificados casos com imagens morfológicas e dados estruturados associados. A base deverá integrar, no mínimo:

- imagens de esfregaço periférico
- parâmetros do hemograma
- contagens diferenciais e variáveis relacionadas
- flags do analisador hematológico
- metadados laboratoriais relevantes

Nessa fase, serão definidos critérios de inclusão, qualidade, harmonização temporal e análise de dados faltantes.

### Etapa 2. Formalização das tarefas

As tarefas serão definidas em nível de caso, com foco em aplicações como:

- priorização de revisão manual
- suporte à identificação de alterações morfológicas relevantes
- apoio à inferência diagnóstica assistida
- triagem baseada em concordância ou discordância entre morfologia e sinais estruturados

### Etapa 3. Modelagem computacional

Serão implementados:

- baselines apenas com imagem
- baselines apenas com dados tabulares
- modelos multimodais com diferentes estratégias de fusão

O objetivo não será apenas maximizar acurácia, mas compreender o ganho real de integração entre modalidades.

### Etapa 4. Robustez e interpretabilidade

Esta etapa avaliará:

- generalização sob variação de domínio
- calibração e incerteza
- análise de erro
- contribuição relativa de cada modalidade
- interpretabilidade orientada ao laboratório

### Etapa 5. Camada opcional de raciocínio estruturado

Se a base multimodal principal estiver madura, poderá ser adicionada uma camada auxiliar de apoio interpretativo baseada em recuperação estruturada ou regras explícitas. O uso de LLMs, se ocorrer, será limitado e subordinado ao problema laboratorial, nunca como eixo central da tese.

## 7. Viabilidade

A proposta foi desenhada para ser realista para quem trabalha em tempo integral. Sua viabilidade se apoia em cinco pontos:

1. aproveita experiência e infraestrutura já estabelecidas no mestrado;
2. permite modularização em artigos independentes;
3. depende mais de curadoria e modelagem incremental do que de uma coleta prospectiva massiva única;
4. pode começar com desenho retrospectivo e evoluir para validações mais fortes;
5. concentra-se em um domínio estreito, evitando amplitude excessiva.

## 8. Contribuições esperadas para Ciência da Computação

As contribuições esperadas não são apenas aplicadas à saúde, mas computacionais:

- formulação de um problema multimodal em ambiente laboratorial real
- desenvolvimento de estratégias de fusão entre imagem e dados estruturados
- investigação de robustez e confiabilidade em IA multimodal
- mecanismos de interpretabilidade em inferência heterogênea
- possível benchmark ou recurso multimodal reutilizável

## 9. Produtos esperados e potencial de publicação

O projeto tem potencial para gerar pelo menos quatro frentes publicáveis:

1. caracterização e disponibilização de base multimodal;
2. comparação entre baselines unimodais e modelos multimodais;
3. robustez, calibração e incerteza em hematologia multimodal;
4. apoio à decisão e utilidade em fluxo laboratorial.

Opcionalmente, uma quinta frente pode explorar raciocínio estruturado ou suporte interpretativo, desde que fundamentado em dados laboratoriais reais.

## 10. Enquadramento para orientação

O enquadramento principal recomendado é com **Jônata Tyska Carvalho**, na linha de Inteligência Computacional, apresentando o projeto como problema de IA multimodal em saúde com ênfase em integração entre modalidades, robustez e inferência em nível de caso.

Como alternativa, **Renato Fileto** é especialmente adequado caso a proposta reforce mais fortemente a integração de dados complexos, o enriquecimento semântico e a organização da camada estrutural de apoio à decisão.

## 11. Delimitações e riscos de posicionamento

Para que a proposta permaneça competitiva, quatro riscos devem ser evitados:

1. **excesso de clinificação**: a proposta deve sempre explicitar o problema computacional;
2. **incrementalismo**: não pode ser apresentada como apenas mais um modelo de classificação;
3. **genericidade**: deve nomear explicitamente esfregaço periférico, hemograma e flags;
4. **amplitude excessiva**: deve evitar prometer um “agente de hematologia” ou solução universal.

## 12. Conclusão

O caminho mais forte para o doutorado é desenvolver uma proposta de **inteligência clínico-laboratorial multimodal em hematologia**, com a morfologia como âncora e com expansão para inferência em nível de caso, robustez e apoio à decisão. Essa formulação preserva a continuidade com o mestrado, responde a uma lacuna real da literatura, demonstra maturidade metodológica e mantém alto potencial de publicação, sem depender de buzzwords ou de um salto temático artificial.
