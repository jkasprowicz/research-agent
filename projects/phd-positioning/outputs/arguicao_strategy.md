# Estrategia de Arguicao - Doutorado PPGCC/UFSC

## Objetivo da arguicao

Pelo edital, a arguicao pesa **20% da nota final** e avalia:

- exposicao do projeto, justificativa, metodologia e compatibilidade com o orientador;
- formacao, atividades academicas, publicacoes e experiencia profissional/pesquisa;
- potencial como futuro pesquisador, razoes pela escolha do Programa, disponibilidade de tempo e projeto de vida;
- dominio da lingua inglesa.

Portanto, a meta nao e defender uma tese fechada. A meta e demonstrar maturidade cientifica, aderencia ao PPGCC, capacidade de execucao e abertura para refinamento com o orientador.

---

## Elevator pitch

Minha proposta parte da hematologia digital, mas nao se limita a classificacao de celulas. A ideia e investigar metodos de aprendizado de maquina para apoiar decisoes no fluxo de revisao hematologica, combinando dados estruturados de laboratorio, historico temporal e, quando disponivel, evidencia morfologica digital. O foco e computacional: modelagem robusta, interpretavel e avaliada em cenarios retrospectivos realistas, com hematologia como dominio de aplicacao.

---

## Resumo de 2 minutos

Minha formacao combina Ciencias Biomedicas, Informatica em Saude e Data Science, com experiencia profissional em laboratorio clinico e pesquisa em IA aplicada a hematologia. No mestrado, trabalhei com classificacao automatica de celulas hematologicas em imagens de esfregaco periferico, explorando arquiteturas de aprendizado profundo, Vision Transformers, YOLO, aumento de dados orientado a coloracao e construcao/curadoria de dataset. Esse trabalho tambem gerou publicacao em periodico da Springer, o que consolidou minha base tecnica em visao computacional aplicada a hematologia.

Para o doutorado, vejo uma oportunidade de evoluir naturalmente dessa etapa: sair da classificacao isolada de celulas e investigar suporte a decisao em nivel de caso. A literatura mostra que classificacao celular por imagem ja e um campo bastante explorado, enquanto ainda ha espaco para modelos que integrem informacoes laboratoriais estruturadas, historico temporal e evidencia morfologica para apoiar decisoes de revisao, priorizacao e alerta no fluxo hematologico.

O plano submetido esta estruturado de forma conservadora: primeiro trabalhar com dados laboratoriais retrospectivos estruturados, depois incorporar evidencias morfologicas digitais em subcoortes viaveis. Assim, o projeto preserva rigor computacional, evita prometer uma plataforma universal e se mantem executavel mesmo considerando que trabalho em tempo integral.

---

## Resumo de 5 minutos

Minha trajetoria cientifica comeca na interseccao entre laboratorio clinico e tecnologia. Venho da area biomedica, tenho experiencia em laboratorio e qualidade, e no mestrado em Informatica em Saude aprofundei a aplicacao de aprendizado profundo em hematologia digital. O foco inicial foi classificacao de celulas hematologicas em imagens de esfregaco periferico, incluindo classes mais desafiadoras, como celulas imaturas ou atipicas. Trabalhei com comparacao de arquiteturas, incluindo modelos convolucionais e Vision Transformers, e com estrategias de aumento de dados voltadas a variabilidade de coloracao.

Essa etapa foi importante porque criou uma base real de metodo, dados e dominio. Ao mesmo tempo, ela mostrou uma limitacao: classificacao celular isolada nao resolve sozinha o problema laboratorial em nivel de caso. Na rotina, uma decisao de revisao ou priorizacao combina hemograma, diferencial, parametros do analisador, flags, historico do paciente e achados morfologicos. Por isso, o doutorado que proponho nao e "mais um classificador de leucocitos". Ele busca subir o nivel da tarefa: de morfologia celular para suporte computacional a decisoes de revisao hematologica.

O estado da arte sustenta essa transicao. Existem revisoes mostrando maturidade em classificacao de leucocitos, estudos de morfologia digital e trabalhos que combinam morfologia e hemograma para tarefas especificas. Tambem ha sistemas de apoio a interpretacao de esfregaco e estudos de triagem por dados de analisador. A lacuna que me parece mais defensavel esta entre esses grupos: metodos robustos e interpretaveis para apoiar decisoes do fluxo real de laboratorio, especialmente quando as modalidades sao incompletas ou heterogeneas.

Metodologicamente, a proposta e faseada. Primeiro, definem-se coortes retrospectivas e tarefas computacionais de revisao, suspeicao ou gatilho futuro. Em seguida, desenvolvem-se modelos estruturados e longitudinais a partir de hemograma e dados laboratoriais. Depois, se houver vinculacao adequada e aprovacao etica, incorpora-se evidencia morfologica digital em subcoortes, sempre comparando modelos laboratoriais, morfologicos e multimodais. Por fim, avaliam-se calibracao, interpretabilidade, robustez temporal e utilidade operacional.

Para Ciencia da Computacao, a contribuicao esta na formulacao e avaliacao de modelos para decisao em fluxo real, nao apenas na aplicacao clinica. O projeto envolve aprendizado supervisionado, modelagem temporal, fusao multimodal, dados ausentes, calibracao, interpretabilidade e avaliacao por baselines e validacao temporal. O dominio e hematologia, mas o problema cientifico e de modelagem computacional confiavel em ambiente aplicado.

---

## Perguntas provaveis e respostas recomendadas

## 1. Por que este projeto e de Ciencia da Computacao?

Resposta:

Porque o nucleo nao e o diagnostico hematologico em si, mas a formulacao e avaliacao de metodos computacionais para suporte a decisao com dados heterogeneos, temporais e possivelmente multimodais. O projeto trabalha com aprendizado de maquina, fusao de dados, avaliacao de baselines, calibracao, interpretabilidade e validacao temporal. A hematologia e o dominio que torna o problema concreto.

## 2. Por que nao continuar apenas com classificacao de leucocitos?

Resposta:

A classificacao de leucocitos foi a base metodologica do mestrado, mas hoje esse campo ja esta relativamente maduro. Para o doutorado, a contribuicao mais forte e subir de nivel: usar a morfologia como uma fonte de evidencia dentro de decisoes em nivel de caso. Assim, ha continuidade, mas tambem evolucao cientifica real.

## 3. A proposta nao esta ampla demais?

Resposta:

Essa e uma preocupacao central. Por isso o plano foi estruturado de forma faseada. O nucleo minimo e modelagem retrospectiva de decisoes de revisao com dados laboratoriais estruturados. A camada morfologica entra como subcoorte quando houver disponibilidade e vinculacao adequada. A proposta nao depende de construir uma plataforma universal.

## 4. E se as imagens Cellavision, flags ou parametros de pesquisa nao forem acessiveis?

Resposta:

O projeto foi desenhado para sobreviver a esse risco. A primeira camada trabalha com dados laboratoriais estruturados e longitudinalidade, que ja permitem contribuicoes computacionais relevantes. A morfologia digital e um modulo incremental, nao uma condicao unica de viabilidade. Isso reduz o risco sem abandonar a direcao multimodal.

## 5. Qual e a principal novidade?

Resposta:

Nao e simplesmente combinar imagem e hemograma. A novidade esta em formular o problema como suporte robusto e interpretavel a decisoes do fluxo de revisao hematologica, comparando modalidades, avaliando temporalidade, tratando dados ausentes e medindo utilidade operacional, nao apenas acuracia diagnostica.

## 6. Como a proposta se alinha ao orientador indicado?

Resposta:

Ela se alinha a Inteligencia Computacional e ao desenvolvimento/aplicacao de metodos de IA em saude e dominios especificos. O projeto tem componente aplicado forte, mas tambem exige contribuicao em aprendizado de maquina, avaliacao de modelos e confiabilidade, que estao no centro do enquadramento computacional.

## 7. Como voce pretende conciliar doutorado e trabalho?

Resposta:

Com escopo incremental e publicavel. A proposta nao depende de coleta prospectiva extensa no primeiro momento. Ela comeca com coortes retrospectivas, tarefas bem definidas e modelos baselines. Isso permite produzir resultados parciais, ajustar o escopo com o orientador e evitar que o doutorado dependa de um unico experimento grande.

## 8. Por que PPGCC/UFSC?

Resposta:

Porque busco um doutorado em que o eixo principal seja a contribuicao computacional. Minha experiencia vem da saude, mas o objetivo agora e amadurecer como pesquisador em Ciencia da Computacao aplicada a problemas reais, com rigor metodologico em IA, modelagem e avaliacao.

## 9. Como voce avaliaria sucesso do projeto?

Resposta:

Por comparacao com baselines claros: modelos estruturados simples, modelos longitudinais, modelos com e sem morfologia e, quando possivel, regras tradicionais de revisao. As metricas incluiriam discriminacao, calibracao, sensibilidade em pontos operacionais relevantes, reducao potencial de carga de revisao e interpretabilidade.

## 10. Qual e a maior fraqueza da proposta?

Resposta:

A maior fraqueza potencial e a disponibilidade real de todas as modalidades. Por isso ela foi desenhada com um nucleo viavel e camadas incrementais. Vejo essa incerteza nao como algo a esconder, mas como algo a administrar metodologicamente desde o inicio.

## 11. Voce tem dominio da lingua inglesa?

Resposta:

Sim. A literatura principal da area e em ingles, minha publicacao internacional foi nesse idioma, e estou habituado a leitura, escrita e discussao tecnica em ingles. Se solicitado, posso apresentar ou discutir parte do projeto em ingles.

---

## Fragilidades que a banca pode atacar

| Fragilidade | Como responder |
|---|---|
| Projeto parece clinico demais | Reforcar tarefas computacionais, baselines, validacao, interpretabilidade e modelagem temporal |
| Dados multimodais nao estao garantidos | Explicar desenho faseado e nucleo estruturado retrospectivo |
| Tema parece continuacao do mestrado | Explicar mudanca de escala: de celula isolada para decisao em nivel de caso |
| Multimodalidade parece buzzword | Dizer que multimodalidade sera testada por ganho incremental, nao assumida como superior |
| Trabalha em tempo integral | Mostrar cronograma incremental, foco retrospectivo e publicacoes por etapas |
| Orientador pode nao ser especialista em hematologia | Explicar que hematologia e dominio; supervisao principal e em IA/metodos computacionais |
| Plano menciona segunda opcao em outra linha | Dizer que a prioridade e Inteligencia Computacional; segunda opcao existe apenas se o Programa entender que a parte de dados complexos e mais adequada |

---

## O que evitar na arguicao

1. Nao dizer que o projeto sera uma plataforma completa de hematologia.
2. Nao dizer que o modelo fara diagnostico autonomo.
3. Nao vender agentic AI ou LLM como eixo central.
4. Nao prometer acesso total a todos os dados antes da validacao etica.
5. Nao minimizar a dificuldade de vincular dados laboratoriais, imagens e historico.
6. Nao usar acuracia alta do mestrado como argumento unico.
7. Nao parecer fechado a ajustes do orientador.

---

## Como mostrar abertura sem parecer inseguro

Frases uteis:

- "Eu vejo o plano como uma proposta inicial, alinhada ao edital, mas refinavel com o orientador."
- "O eixo que considero mais forte e suporte computacional ao fluxo de revisao hematologica; a forma exata da tarefa pode ser ajustada conforme dados e orientacao."
- "A parte multimodal e importante, mas pretendo testa-la de modo incremental, comparando com baselines estruturados."
- "Prefiro um doutorado executavel e publicavel a uma promessa ampla demais."
- "A contribuicao que quero preservar e computacional: modelagem confiavel, interpretavel e validada em dados reais."

---

## Resposta curta para o trade-off ambicao vs aprovacao

Se a banca perguntar por que o plano nao promete uma solucao multimodal completa desde o inicio:

"A versao mais ambiciosa seria construir um sistema completo com imagens, hemograma, flags, parametros de pesquisa e historico clinico. Mas, para um doutorado bem executado, considero mais forte propor um nucleo metodologico viavel e expandi-lo conforme a disponibilidade real dos dados. Isso aumenta a chance de produzir ciencia consistente, em vez de depender de uma integracao total logo no primeiro ano."

---

## Postura final

A postura ideal e:

- tecnicamente confiante;
- epistemicamente conservadora;
- aberta a orientacao;
- clara sobre a contribuicao para Computacao;
- realista sobre dados e tempo;
- firme ao dizer que o projeto nao e apenas mais uma aplicacao clinica.

O tom deve ser: "eu tenho direcao, preparo e criterio; quero construir a tese certa com o Programa."
