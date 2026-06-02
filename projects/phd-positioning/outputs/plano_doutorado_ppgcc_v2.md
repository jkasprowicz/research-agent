# Plano de Trabalho - Doutorado

## Linha de pesquisa, tema e orientação

**Linha de pesquisa:** Inteligência Computacional.

**Tema pretendido:** aplicação e desenvolvimento de métodos de inteligência artificial para saúde, com ênfase em aprendizado de máquina para domínios específicos.

**Orientador indicado:** Jônata Tyska Carvalho.

**Segunda opção de orientação:** Renato Fileto, caso o Programa considere adequada a adaptação do plano para a linha de Banco de Dados, especialmente nos temas de integração, análise de dados complexos, classificação e predição.

## Título

**Modelos robustos e interpretáveis de aprendizado de máquina para suporte à decisão no fluxo de revisão hematológica**

## Introdução, motivação e problema de pesquisa

A revisão de esfregaços de sangue periférico permanece uma etapa relevante na rotina hematológica, especialmente quando resultados automatizados sugerem alterações celulares, suspeita de células imaturas, anormalidades morfológicas ou inconsistências entre parâmetros laboratoriais. Apesar do avanço de analisadores hematológicos e sistemas de morfologia digital, a decisão de revisar, priorizar ou interpretar um caso ainda depende da combinação de múltiplos sinais: contagem global e diferencial, parâmetros plaquetários e eritrocitários, flags do analisador, histórico laboratorial e, quando disponível, evidência morfológica digital.

Grande parte da literatura em inteligência artificial para hematologia concentra-se em classificação de células a partir de imagens, particularmente leucócitos em esfregaços periféricos. Esse campo é importante, mas encontra-se relativamente maduro e limitado para decisões laboratoriais em nível de caso. Estudos mais recentes avançam para morfometria digital, predição de doenças a partir de esfregaços e integração entre morfologia e hemograma; contudo, ainda há lacuna na formulação computacional de sistemas orientados ao fluxo real de revisão laboratorial, nos quais o objetivo não é substituir o especialista ou produzir diagnóstico autônomo, mas apoiar decisões como priorização de revisão, detecção de casos suspeitos e identificação de discordâncias entre modalidades.

O problema de pesquisa proposto é: **como desenvolver e avaliar métodos de aprendizado de máquina capazes de integrar dados laboratoriais estruturados, histórico temporal e evidências morfológicas disponíveis para apoiar, de forma robusta e interpretável, decisões de revisão hematológica em nível de caso?**

## Objetivos

**Objetivo geral:** desenvolver e avaliar métodos computacionais robustos e interpretáveis para suporte à decisão no fluxo de revisão hematológica, utilizando dados laboratoriais retrospectivos e, quando disponível, evidência morfológica digital de esfregaços periféricos.

**Objetivos específicos:**

1. Definir tarefas computacionais de apoio à revisão hematológica em nível de caso, com ênfase em priorização de revisão, detecção de casos suspeitos e predição de gatilhos de revisão a partir de dados retrospectivos.
2. Construir modelos de aprendizado de máquina a partir de dados estruturados de hemograma, parâmetros laboratoriais, flags e trajetórias laboratoriais, comparando abordagens estáticas e longitudinais.
3. Avaliar, em subcoortes com disponibilidade adequada, o valor incremental de evidências morfológicas digitais em relação a modelos baseados apenas em dados laboratoriais estruturados.
4. Investigar robustez, calibração, interpretabilidade e utilidade operacional dos modelos, considerando validação temporal, análise de subgrupos, dados ausentes e comparação com baselines simples.

## Fundamentação e estado da arte

A automação da morfologia hematológica evoluiu de sistemas de pré-classificação celular e microscopia digital para abordagens com aprendizado profundo. Revisões recentes indicam desempenho elevado em tarefas de classificação de leucócitos, mas também apontam heterogeneidade metodológica, dependência de bases restritas e limitações em células raras, imaturas ou atípicas (Asghar et al., 2024). Em paralelo, a literatura de morfologia digital destaca que a adoção laboratorial desses sistemas envolve não apenas acurácia de classificação, mas padronização, fluxo de trabalho, qualidade da lâmina e revisão especializada (Kratz et al., 2019; Katz et al., 2021; Zini, 2024).

Trabalhos mais próximos do problema proposto já demonstram que sinais morfológicos derivados de esfregaços podem ser associados a doenças hematológicas e que a integração com contagens sanguíneas pode melhorar tarefas de discriminação em contextos específicos (de Almeida et al., 2023; Horiuchi et al., 2026). Também existem estudos que utilizam parâmetros de analisadores ou hemograma para flagging precoce e otimização de revisão manual (Haider et al., 2019; Hayes et al., 2025). Por outro lado, ferramentas como PROSER mostram a relevância de incorporar contexto laboratorial à interpretação do esfregaço, embora ainda dependam fortemente de lógica estruturada e entrada humana de achados morfológicos (Iscoe et al., 2023).

A lacuna científica, portanto, não está em demonstrar que imagens de células podem ser classificadas, nem apenas em combinar imagem e hemograma para uma tarefa diagnóstica isolada. A lacuna está em formular e avaliar, de modo computacionalmente rigoroso, modelos de suporte à decisão orientados ao fluxo de revisão hematológica, capazes de lidar com múltiplas modalidades, dados incompletos, histórico temporal e necessidade de explicações compreensíveis ao usuário técnico.

## Encaminhamento metodológico

O estudo será conduzido com dados retrospectivos anonimizados de laboratório clínico, mediante aprovação ética e governança adequada. A unidade principal de análise será o atendimento ou episódio laboratorial. O plano será organizado em quatro etapas metodológicas.

**Etapa 1 - definição da coorte, tarefas e baselines.** Serão definidos critérios de inclusão, janelas temporais e variáveis elegíveis, priorizando hemograma, diferencial, parâmetros plaquetários e eritrocitários, flags disponíveis, variáveis laboratoriais complementares e informações temporais. As tarefas iniciais serão formuladas como problemas de classificação, ranqueamento ou predição temporal relacionados à necessidade de revisão, suspeição laboratorial ou ocorrência futura de gatilhos de revisão. Baselines incluirão regras simples, regressão logística, modelos baseados em árvores e modelos de gradiente.

**Etapa 2 - modelagem estruturada e longitudinal.** Serão desenvolvidos modelos com dados estruturados em dois cenários: avaliação estática de um episódio e avaliação longitudinal de trajetórias laboratoriais. Para o cenário longitudinal, serão considerados resumos temporais, variações relativas, tendências e modelos sequenciais quando a densidade temporal permitir. A avaliação usará divisões temporais retrospectivas, validação cruzada quando apropriado e métricas como AUROC, AUPRC, sensibilidade em pontos de operação definidos, calibração, valor preditivo e redução potencial de carga de revisão sob sensibilidade mínima.

**Etapa 3 - integração morfológica em subcoorte disponível.** Quando houver disponibilidade de imagens digitais ou saídas morfológicas estruturadas, será avaliado o valor incremental da morfologia em relação aos modelos estruturados. A comparação incluirá modelos apenas laboratoriais, modelos apenas morfológicos e modelos multimodais. Serão exploradas estratégias de fusão tardia, fusão intermediária e modelos robustos a modalidades ausentes. Essa etapa será tratada como subestudo controlado, evitando que a viabilidade do projeto dependa exclusivamente da disponibilidade integral de imagens.

**Etapa 4 - interpretabilidade, robustez e síntese do suporte decisório.** Serão investigadas explicações locais e globais, calibração, estabilidade temporal, desempenho por subgrupos e análise de casos discordantes entre sinais laboratoriais e morfológicos. O resultado esperado não será um sistema autônomo de diagnóstico, mas um arcabouço computacional para apoiar decisões de revisão, priorização e alerta em hematologia laboratorial.

## Possíveis contribuições científicas para Computação

A proposta pretende contribuir para a área de Computação em quatro frentes. Primeiro, pela formulação de tarefas de aprendizado de máquina orientadas ao fluxo laboratorial, nas quais o alvo é uma decisão operacional em nível de caso, e não apenas a classificação de uma célula ou doença. Segundo, pela avaliação de estratégias de integração multimodal em cenário retrospectivo realista, incluindo modalidades ausentes e comparação explícita com baselines unimodais. Terceiro, pela incorporação de modelagem temporal de trajetórias laboratoriais como fonte de evidência para decisões de revisão. Quarto, pela análise de robustez, calibração e interpretabilidade em um domínio sensível, no qual a utilidade do modelo depende tanto do desempenho preditivo quanto da confiabilidade operacional.

## Viabilidade e cronograma resumido

A proposta é planejada de forma incremental. No primeiro ano, serão definidos a coorte, as tarefas computacionais, a estratégia ética e os baselines estruturados. No segundo ano, serão desenvolvidos e avaliados modelos estáticos e longitudinais com dados laboratoriais estruturados. No terceiro ano, será incorporada a subcoorte morfológica disponível e avaliado o valor incremental da integração multimodal. No quarto ano, serão realizadas análises de robustez, interpretabilidade, síntese dos resultados e redação da tese.

Essa organização preserva viabilidade porque o núcleo do projeto pode avançar com dados laboratoriais retrospectivos estruturados, enquanto a camada morfológica digital é incorporada de forma controlada conforme disponibilidade, qualidade de vínculo e aprovação ética. Assim, a proposta mantém ambição científica compatível com doutorado sem depender de uma plataforma completa ou de integração total de dados desde o início.

## Referências

Asghar, M. Z. et al. Classification of white blood cells from blood smear imagery using machine and deep learning models: a global scoping review. *PLOS ONE*, 2024.

de Almeida, J. G. et al. Computational analysis of peripheral blood smears detects disease-associated cytomorphologies. *Nature Communications*, 2023.

Haider, R. Z.; Ujjan, I. U.; Shamsi, T. S. Cell population data-driven acute promyelocytic leukemia flagging through artificial neural network predictive modeling. *Translational Oncology*, 2019.

Hayes, J. M. et al. Development of criteria to optimize manual smear review of automated complete blood counts using a machine learning model. *Veterinary Clinical Pathology*, 2025.

Horiuchi, Y. et al. Application of convolutional neural network image analysis and machine learning to basic blood tests for intelligent diagnostic assistance. *International Journal of Laboratory Hematology*, 2026.

Iscoe, M. S. et al. PROSER: a web-based peripheral blood smear interpretation support tool utilizing electronic health record data. *American Journal of Clinical Pathology*, 2023.

Katz, B.-Z. et al. Evaluation of Scopio Labs X100 Full Field PBS: high-resolution full field viewing of peripheral blood specimens combined with AI-based morphological analysis. *International Journal of Laboratory Hematology*, 2021.

Kratz, A. et al. Digital morphology analyzers in hematology: ICSH review and recommendations. *International Journal of Laboratory Hematology*, 2019.

Zini, G. Hematological cytomorphology: where we are. *International Journal of Laboratory Hematology*, 2024.
