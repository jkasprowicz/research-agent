# Oral Defense Cheat Sheet

## Perguntas prováveis da banca

### 1. Por que isso é doutorado em Ciência da Computação?

**Resposta curta:**  
Porque o núcleo do projeto é computacional: integração de modalidades heterogêneas, comparação de estratégias de fusão, robustez sob variabilidade de domínio, calibração, incerteza e interpretabilidade em nível de caso. A hematologia é o domínio translacional; a contribuição central é em IA multimodal confiável.

### 2. Isso não é apenas continuação do mestrado?

**Resposta curta:**  
Não no sentido incremental. O mestrado tratou da camada de inteligência morfológica em nível celular. O doutorado propõe um salto de nível inferencial: de classificação isolada para integração multimodal em nível de caso, com robustez e apoio à decisão laboratorial.

### 3. Por que multimodalidade é necessária?

**Resposta curta:**  
Porque a decisão hematológica real não depende apenas da imagem de uma célula. Ela depende da articulação entre morfologia, hemograma, flags do analisador e contexto do caso. Portanto, multimodalidade não é ornamentação; é a formulação computacional correta do problema.

### 4. Por que isso é viável?

**Resposta curta:**  
Porque o projeto é retrospectivo, modular e orientado à publicação. Ele começa com um conjunto mínimo de modalidades já bem definido, compara baselines unimodais e multimodais e não depende de um único estudo prospectivo massivo.

### 5. Qual é a contribuição científica real?

**Resposta curta:**  
A contribuição central é mostrar como integrar morfologia, hemograma e flags do analisador em inferência hematológica em nível de caso, e avaliar quando essa integração agrega valor em relação a modelos unimodais, sob critérios de robustez, calibração, incerteza e interpretabilidade.

## Como defender a continuidade com o mestrado

Use esta formulação:

> O mestrado estabeleceu minha base em morfologia hematológica assistida por IA, com dataset próprio, comparação de arquiteturas, variabilidade de coloração e generalização externa. O doutorado preserva esse núcleo, mas amplia o nível inferencial: em vez de reconhecer células isoladas, passa a integrar morfologia com hemograma, flags e contexto laboratorial para apoiar inferências em nível de caso.

Pontos a enfatizar:

- mesma âncora temática: hematologia;
- mesma modalidade central: morfologia;
- mesmo compromisso metodológico: robustez e aplicabilidade real;
- novo salto: fusão multimodal e decisão em nível de caso.

## Como defender a multimodalidade

Use esta formulação:

> O espaço image-only já é tecnicamente maduro, mas não representa adequadamente a lógica da prática laboratorial. Um achado morfológico ganha significado quando relacionado ao hemograma, às flags do analisador e ao contexto do caso. Por isso, a multimodalidade é necessária para aproximar a IA da inferência hematológica real.

Se a banca pressionar, cite tarefas concretas:

- priorização de revisão manual;
- identificação de casos suspeitos;
- análise de concordância ou discordância entre morfologia e analisador.

## Como defender a viabilidade

Use esta formulação:

> O projeto foi desenhado para ser executável por pesquisador em tempo integral porque é retrospectivo, modular e publication-friendly. Primeiro estrutura-se a base multimodal; depois comparam-se modelos unimodais e multimodais; em seguida avaliam-se robustez e interpretabilidade. Cada etapa pode gerar um produto científico independente.

Pontos de reforço:

- escopo mínimo de dados bem definido;
- sem dependência de coleta prospectiva ampla no início;
- sem promessas de plataforma universal;
- continuidade com infraestrutura e experiência do mestrado.

## Como defender a contribuição para Ciência da Computação

Use esta formulação:

> A contribuição não está apenas na aplicação em hematologia, mas na formalização de um problema de inferência multimodal em nível de caso, na comparação de estratégias de fusão, e na avaliação de robustez, calibração, incerteza e interpretabilidade sob variabilidade laboratorial real. Isso dialoga diretamente com Inteligência Computacional.

Evite respostas vagas como:

- “é IA aplicada à saúde”;
- “é importante para medicina”.

Prefira:

- fusão multimodal;
- confiabilidade;
- generalização;
- interpretabilidade.

## Como responder crítica de escopo

**Pergunta provável:** “Isso não está amplo demais?”

**Resposta recomendada:**  
O núcleo da tese é restrito: morfologia de esfregaço periférico, hemograma, flags do analisador e inferência em nível de caso. Robustez, interpretabilidade e apoio à decisão são desdobramentos desse núcleo. Estão fora do escopo integrações amplas com genômica, mielograma, citometria e sistemas genéricos baseados em LLM.

## Como responder crítica de incrementalismo

**Pergunta provável:** “Isso é só adicionar CBC ao que você já fazia?”

**Resposta recomendada:**  
Não. O ponto principal não é adicionar uma variável, mas mudar o problema computacional. O mestrado tratava de reconhecimento morfológico; o doutorado trata de integração multimodal, inferência em nível de caso e confiabilidade sob variabilidade de domínio.

## Como defender o diferencial do acesso laboratorial real

Use esta formulação:

> O acesso a dados laboratoriais retrospectivos reais é um diferencial porque permite estudar o problema como ele ocorre no laboratório, e não apenas em benchmarks imagéticos. Isso viabiliza investigar concordância entre morfologia, hemograma e flags, formular tarefas em nível de caso e produzir resultados com maior valor translacional.

## Resposta de um minuto

> Meu doutorado propõe uma expansão natural do meu mestrado em morfologia hematológica assistida por IA. Em vez de permanecer na classificação isolada de leucócitos, quero desenvolver métodos multimodais robustos e interpretáveis que integrem morfologia do esfregaço periférico com hemograma, flags do analisador e contexto laboratorial estruturado. A principal lacuna da literatura hoje não é a ausência de classificadores, mas a escassez de sistemas em nível de caso, mais próximos da lógica real do laboratório. O projeto é viável porque é retrospectivo, modular e orientado à publicação, e é relevante para a Ciência da Computação porque investiga fusão multimodal, robustez, calibração, incerteza e interpretabilidade em um domínio real e especializado.
