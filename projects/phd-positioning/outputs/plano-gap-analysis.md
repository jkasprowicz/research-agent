# Gap Analysis do Plano Atual contra o Edital

## Premissa

Como a versao antiga do plano final de submissao nao esta presente no diretório atual de `outputs`, esta analise considera como "plano atual" o conjunto formado por:

- `phd_program_blueprint.md`
- `revised_positioning_report.md`
- `leac_feasibility_assessment.md`
- `literature_repositioning_review.md`

Ou seja, a analise avalia a direcao atual e seus argumentos, nao uma versao editavel especifica do texto final.

## Diagnostico geral

A direcao cientifica esta forte, mas ainda esta escrita como **programa de pesquisa** e nao como **plano de trabalho eliminatorio de edital**. Para admissao, o texto precisa ficar mais curto, mais anonimo, mais aderente ao Anexo I e menos dependente de ativos de dados ainda nao comprovados.

O principal conflito estrategico e este:

- a visao mais ambiciosa e um programa multimodal completo com imagens Cellavision, CBC, Sysmex, flags, discordancia e longitudinalidade;
- a proposta mais provavel de ser aprovada e um plano faseado, com nucleo viavel em dados laboratoriais retrospectivos e incorporacao morfologica como modulo condicionado a disponibilidade/validacao etica.

Para admissao, deve-se priorizar a segunda.

---

## 1. Forcas atuais

## Aderencia cientifica

O plano atual tem uma identidade clara:

- IA aplicada a saude
- hematologia digital
- dados laboratoriais reais
- apoio a decisao
- modelagem multimodal
- robustez e interpretabilidade

Isso conversa bem com `Inteligencia Computacional`, especialmente com o tema de Jônata Tyska Carvalho sobre aplicacao e desenvolvimento de metodos de IA para saude e dominios especificos.

## Maturidade da lacuna

As analises anteriores evitaram uma armadilha importante: nao tratar o projeto como "mais um classificador de leucocitos". O plano ja reconhece que:

- classificacao celular isolada esta saturada;
- sistemas imagem + CBC ja existem;
- o espaco mais forte esta em suporte a decisao orientado ao fluxo laboratorial.

Essa maturidade ajuda muito no criterio `Relevancia e Viabilidade`.

## Contribuicao computacional potencial

O blueprint tem bons eixos de Computacao:

- fusao multimodal
- modelagem temporal
- avaliacao por ablacao
- interpretabilidade
- calibracao
- robustez
- decisao sob dados incompletos

Isso permite defender que o projeto e de Ciencia da Computacao, nao apenas uma aplicacao clinica.

## Realismo pos-reavaliacao

A avaliacao de viabilidade do LEAC introduziu uma melhoria crucial: ela reconhece que a camada longitudinal estruturada esta mais documentada do que a camada completa imagem + flags + revisao. Esse reconhecimento deve entrar no plano como estrategia faseada.

---

## 2. Fraquezas atuais

## O plano ainda parece grande demais

O blueprint com quatro estudos, datasets A/B/C, discordancia, longitudinalidade e framework final e bom como arquitetura de doutorado, mas longo e ambicioso para um plano de 4 paginas. Em edital, isso pode soar como excesso de escopo.

## Dependencia excessiva de dados nao confirmados

Os estudos 1 e 2 assumem:

- imagens Cellavision linkadas por atendimento;
- labels de revisao;
- flags do analisador;
- parametros de pesquisa Sysmex;
- anotacao/adjudicacao de discordancia.

A avaliacao LEAC mostrou que isso ainda nao esta documentado. Se a banca perceber essa dependencia, pode atacar `exequibilidade`.

## Risco de identificacao do candidato

Versoes anteriores valorizavam continuidade com o mestrado, publicacao Springer, dataset proprio e contexto LEAC. Esses elementos sao fortes na arguição e no CV, mas perigosos no plano, porque o edital elimina plano com informacao que identifique o candidato.

## Aderencia ao Anexo I precisa estar mais visivel

O plano atual e bom cientificamente, mas precisa abrir com:

- linha de pesquisa;
- tema pretendido conforme Anexo I;
- orientador indicado;
- segunda opcao, se houver;
- enquadramento computacional.

Sem isso, o criterio `Aderencia aos Temas de Pesquisa` fica vulneravel.

## Metodologia precisa ser menos narrativa

O plano atual explica bem a historia, mas o edital avalia clareza de objetivos e adequacao metodologica. O texto novo deve mostrar:

- variaveis previstas;
- tarefas computacionais;
- baselines;
- comparadores;
- validacao temporal;
- metricas;
- criterios de sucesso.

## Estado da arte deve ser curto

As revisoes de literatura sao ricas, mas o plano nao pode virar mini-review. A banca precisa ver que a literatura foi compreendida, nao que tudo foi resumido.

---

## 3. Elementos faltantes para maximizar nota

## Para `Aderencia aos Temas`

Faltam no texto final:

- declaracao explicita da linha `Inteligencia Computacional`;
- tema do Anexo I em linguagem proxima ao edital;
- orientador indicado;
- relacao direta entre o metodo e IA aplicada a saude/domínios especificos.

## Para `Metodologia e Fundamentacao`

Faltam:

- formulacao clara do problema computacional;
- distincao entre coorte estruturada principal e subcoorte multimodal;
- estrategia para dados ausentes e modalidades incompletas;
- comparacao com modelos unimodais;
- definicao de metricas de desempenho e utilidade;
- validacao temporal ou por divisao retrospectiva.

## Para `Relevancia e Viabilidade`

Faltam:

- plano de contingencia caso imagens/flags nao estejam disponiveis;
- escopo minimo viavel;
- cronograma resumido de 4 anos;
- contribuicoes computacionais listadas sem exagero;
- argumento de exequibilidade para pesquisador que trabalha.

## Para a arguição

Faltam:

- pitch curto;
- resposta pronta para "por que isso e Computacao?";
- resposta pronta para "por que nao e clinico demais?";
- resposta pronta para "e se os dados multimodais nao existirem?";
- explicacao de disponibilidade de tempo.

---

## 4. Elementos desnecessarios ou perigosos no plano submetido

Devem sair do plano anonimo:

- nome do candidato;
- mencao direta a dissertacao;
- mencao direta a publicacao Springer;
- mencao a dataset proprio se puder identificar autoria;
- detalhes especificos do LEAC;
- numeros internos da base local se puderem identificar origem;
- narrativa autobiografica de continuidade;
- afirmacoes fortes de acesso a dados ainda nao comprovados;
- promessas de agentic AI ou foundation models;
- proposta de plataforma universal;
- optional fifth study;
- roteiro completo de quatro artigos se consumir pagina.

## 5. Secoes que consomem espaco sem melhorar score

## Longa historia da hematologia digital

Ajuda pouco. Deve virar 1 paragrafo de contextualizacao.

## Discussao extensa de classificacao de leucocitos

Importante para lacuna, mas nao deve ocupar muito. O ponto central e: image-only esta madura e limitada para decisao de caso.

## Detalhes operacionais de datasets A/B/C

Uteis internamente, mas longos para edital. Devem virar metodologia faseada.

## Eticas em camadas

Importante, mas pode ser resumido em "aprovacao etica, anonimizacao e uso retrospectivo".

## Lista de venues de publicacao

Boa para estrategia, desnecessaria no plano de trabalho do edital.

---

## 6. Recomendacao de reposicionamento para o plano v2

O plano v2 deve trocar a identidade ampla:

`inteligencia clinico-laboratorial multimodal em hematologia`

por uma identidade mais aprovada pelo edital:

`metodos de aprendizado de maquina para suporte robusto e interpretavel a decisao no fluxo de revisao hematologica`

Essa formulacao:

- soa mais computacional;
- e menos clinica;
- preserva hematologia;
- nao promete plataforma ampla;
- permite multimodalidade sem depender totalmente dela;
- protege a viabilidade.

## 7. Arquitetura recomendada do plano v2

1. Abrir com linha, tema, orientador e enquadramento.
2. Definir problema: decisoes de revisao hematologica dependem de sinais parciais e heterogeneos.
3. Lacuna: sistemas image-only, analyzer-only e imagem+CBC ainda nao resolvem suporte robusto ao fluxo real.
4. Objetivo geral: desenvolver e avaliar metodos computacionais para priorizacao/suporte a revisao.
5. Objetivos especificos: coorte, modelos estaticos/temporais, subcoorte multimodal, interpretabilidade/robustez.
6. Metodologia: retrospectiva, anonima, comparativa, faseada.
7. Contribuicoes: metodos, protocolo de avaliacao, evidencia de valor incremental multimodal, suporte interpretavel.
8. Cronograma: 4 anos, sem prometer tudo no primeiro ano.

## 8. Trade-off final

Para admissao, a proposta deve abrir mao de parte da ambicao original:

- Menos enfase em `agentic AI`, foundation models e tese multimodal completa.
- Mais enfase em problema computacional avaliavel, dados retrospectivos, validacao temporal e viabilidade.

Isso reduz brilho especulativo, mas aumenta muito a probabilidade de parecer executavel e aderente ao PPGCC.
