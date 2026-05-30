# Plano de Trabalho de Doutorado

## 1. Título

**Expansão da inteligência morfológica hematológica para inteligência clínico-laboratorial multimodal robusta e interpretável**

## 2. Introdução e contextualização

A análise morfológica do esfregaço sanguíneo periférico permanece central na hematologia laboratorial, mesmo em ambientes amplamente automatizados. Embora analisadores hematológicos forneçam parâmetros quantitativos, contagens diferenciais e flags instrumentais, a interpretação de alterações celulares imaturas, atípicas ou displásicas ainda depende da articulação entre morfologia, hemograma e contexto do exame (Zini, 2024). Em paralelo, a microscopia digital e os sistemas assistidos por inteligência artificial mostram que a morfologia hematológica já pode ser incorporada a fluxos computacionais com relevância prática, aproximando a área de ambientes digitais mais escaláveis e reprodutíveis (Katz et al., 2021).

A literatura recente em IA aplicada à hematologia, porém, é assimétrica. O espaço mais povoado permanece sendo a classificação morfológica baseada apenas em imagem, sobretudo para leucócitos em imagens isoladas de esfregaço periférico (Asghar et al., 2024). Essa linha foi também o ponto de partida da trajetória do candidato, com dissertação e publicação voltadas à classificação automática de leucócitos, com atenção à variabilidade de coloração, aumento de dados orientado ao domínio e generalização externa (Kasprowicz & Silva, 2026). Ao mesmo tempo, a revisão sistemática conduzida pelo candidato mostrou que, embora esse campo seja tecnicamente maduro em cenários controlados, permanecem lacunas relevantes em classes imaturas e atípicas, comparabilidade metodológica e aderência ao uso laboratorial real (Kasprowicz, Bacca, & Silva, 2026).

O doutorado proposto parte exatamente desse limite. Em vez de permanecer no eixo saturado de classificação image-only, propõe avançar para um problema computacional mais aderente à prática: integrar morfologia de esfregaço periférico, hemograma, flags do analisador e contexto laboratorial estruturado para inferência em nível de caso.

## 3. Justificativa

Esta proposta é justificada por três razões principais. A primeira é de continuidade científica. O mestrado já estabeleceu uma base metodológica sólida em morfologia hematológica assistida por IA, incluindo curadoria de dados, anotação orientada por especialistas, comparação de arquiteturas e preocupação explícita com robustez e generalização (Kasprowicz & Silva, 2026). O doutorado, portanto, não representa mudança temática, mas a progressão natural de `classificação celular` para `inferência multimodal em nível de caso`.

A segunda razão é a existência de uma lacuna científica clara. O mapeamento da literatura mostra que a integração entre morfologia, hemograma, flags do analisador e apoio à decisão em nível de caso ainda é pouco consolidada. Estudos recentes indicam a viabilidade dessa direção, seja pela agregação de citomorfologia com contagens sanguíneas em inferências associadas à doença (de Almeida et al., 2023), seja pela combinação entre análise de imagem e exames básicos de sangue para assistência diagnóstica (Horiuchi et al., 2026). Ainda assim, esse espaço permanece muito menos maduro do que a classificação puramente imagética.

A terceira razão é a relevância para a Ciência da Computação. O problema central não é apenas aplicar IA à saúde, mas investigar como integrar modalidades heterogêneas, comparar estratégias de fusão, avaliar robustez sob variabilidade laboratorial e produzir inferências interpretáveis em nível de caso. Isso o alinha diretamente à linha de Inteligência Computacional do PPGCC/UFSC. Além disso, o uso de dados retrospectivos reais aumenta a originalidade e a viabilidade da proposta, pois permite formular tarefas mais próximas do fluxo laboratorial do que benchmarks públicos puramente imagéticos.

## 4. Problema de pesquisa

Apesar dos avanços em visão computacional aplicada à hematologia, ainda são escassos sistemas robustos e interpretáveis capazes de integrar morfologia de esfregaço sanguíneo periférico, parâmetros do hemograma, flags do analisador hematológico e contexto laboratorial estruturado para apoiar inferências hematológicas em nível de caso.

## 5. Objetivos

### Objetivo geral

Desenvolver e avaliar uma abordagem de inteligência artificial multimodal para hematologia, capaz de integrar morfologia de esfregaço periférico, hemograma, flags do analisador e contexto laboratorial estruturado, com foco em robustez, interpretabilidade e apoio à decisão em nível de caso.

### Objetivos específicos

1. Construir uma base multimodal retrospectiva em hematologia, integrando imagens de esfregaço periférico, parâmetros do hemograma, contagens diferenciais, flags do analisador e metadados laboratoriais essenciais.
2. Desenvolver e comparar estratégias de fusão multimodal, contrastando modelos baseados apenas em imagem, apenas em dados estruturados e modelos integrados.
3. Investigar robustez, generalização, calibração e incerteza diante de variabilidade laboratorial real.
4. Avaliar mecanismos de interpretabilidade multimodal e sua utilidade em tarefas de triagem, priorização de revisão manual e identificação de padrões suspeitos.

## 6. Fundamentação teórica / estado da arte

A fundamentação teórica do projeto parte de dois diagnósticos convergentes. O primeiro é que a morfologia hematológica continua clinicamente relevante. Revisões recentes mostram que a citomorfologia permanece decisiva na avaliação de alterações hematológicas, mesmo com a incorporação de recursos digitais e inteligência artificial (Zini, 2024). Além disso, plataformas digitais de morfologia já demonstram viabilidade operacional e reprodutibilidade em ambiente real, o que reforça a maturidade translacional do domínio (Katz et al., 2021).

O segundo diagnóstico é que a maior parte da literatura em IA hematológica permanece concentrada em tarefas de classificação image-only. A revisão de Asghar et al. (2024) mostra forte predominância de pipelines baseados em CNNs e deep learning para classificação de leucócitos, com bom desempenho em classes maduras, mas com limitações de comparabilidade, generalização e aderência à lógica laboratorial. Em consonância com isso, a revisão sistemática do candidato destacou que o espaço image-only já é tecnicamente maduro, mas ainda insuficiente para cenários com maior ambiguidade morfológica e relevância clínica (Kasprowicz et al., 2026).

Essa limitação é estrutural. Na prática hematológica, a interpretação de um achado morfológico depende de sua articulação com o hemograma, com as flags do analisador e com o contexto do caso. A decisão laboratorial, portanto, é construída em nível de caso. Nesse ponto, a literatura ainda apresenta poucos estudos diretamente competitivos. De Almeida et al. (2023) mostraram que a análise computacional de esfregaços periféricos pode identificar citomorfologias associadas à doença e ganhar valor quando relacionada a blood counts. Horiuchi et al. (2026) mostraram a viabilidade de combinar análise de imagem de células periféricas com exames básicos de sangue para assistência diagnóstica. No eixo de apoio à decisão, PROSER demonstra que dados estruturados podem ser integrados à interpretação do esfregaço, ainda que sem constituir um framework multimodal profundo completo (Iscoe et al., 2023).

Assim, a principal lacuna do estado da arte não é a ausência de classificadores morfológicos, mas a escassez de sistemas multimodais, robustos e interpretáveis que integrem morfologia, hemograma, flags e contexto laboratorial estruturado para inferência hematológica em nível de caso.

## 7. Metodologia

A metodologia será retrospectiva, modular e orientada à publicação, de modo a compatibilizar rigor científico com viabilidade para pesquisador que trabalha em tempo integral.

Na primeira etapa, será realizada a curadoria da base multimodal, com definição dos critérios de inclusão dos casos e identificação das fontes de dados disponíveis. A base deverá integrar imagens de esfregaço periférico, parâmetros do hemograma, contagens diferenciais, flags do analisador hematológico e metadados laboratoriais essenciais. Nessa fase, serão tratados consistência temporal entre modalidades, qualidade dos registros e dados faltantes. O foco será a construção de uma base retrospectiva em nível de caso, e não de uma plataforma universal de hematologia.

Na segunda etapa, serão definidas as tarefas computacionais centrais, priorizando usos alinhados à rotina laboratorial, como priorização de revisão manual, identificação de casos suspeitos e análise de concordância ou discordância entre morfologia e sinais estruturados. Essa escolha é importante para justificar por que a multimodalidade é necessária e para evitar que o projeto se reduza a outro benchmark de classificação celular.

Na terceira etapa, serão implementados os baselines e os modelos multimodais. O desenho comparativo será obrigatório: modelos apenas com imagem, apenas com dados estruturados e modelos integrados. A contribuição computacional central estará na comparação entre estratégias de fusão e na análise de quando a multimodalidade realmente agrega valor em relação a abordagens unimodais.

Na quarta etapa, será conduzida a avaliação de robustez, generalização, calibração, incerteza e interpretabilidade. Essa etapa dialoga diretamente com a trajetória do candidato, que já investigou variabilidade de coloração e generalização externa em morfologia hematológica (Kasprowicz & Silva, 2026). No doutorado, essa lógica será expandida para sistemas multimodais em contexto laboratorial real.

O escopo permanece estritamente delimitado: pertencem ao núcleo da tese a morfologia de esfregaço periférico, o hemograma, as flags do analisador, a inferência em nível de caso, a robustez e a interpretabilidade. Estão fora do escopo central integrações amplas com genômica, mielograma, citometria de fluxo ou sistemas genéricos baseados em LLM.

## 8. Resultados esperados

Espera-se produzir uma base multimodal retrospectiva em hematologia adequada para experimentos reprodutíveis em nível de caso, além de métodos de fusão capazes de superar limitações de abordagens image-only em tarefas mais próximas da prática laboratorial. Também se espera gerar evidências sobre robustez, calibração, incerteza e interpretabilidade em IA multimodal aplicada à hematologia, contribuindo para sistemas mais confiáveis em ambiente real.

Do ponto de vista científico, o projeto deverá explicitar quando e por que a integração entre morfologia, hemograma e flags produz ganho inferencial em comparação com modelos unimodais. Do ponto de vista translacional, espera-se produzir saídas úteis para triagem e priorização de revisão manual, sem pretensão de substituir o especialista.

Em termos de publicação, o projeto foi desenhado para gerar, de forma realista, três ou quatro frentes principais: base multimodal e formulação do problema; comparação entre abordagens unimodais e multimodais; robustez e confiabilidade; e interpretabilidade aplicada ao apoio à decisão laboratorial.

## 9. Cronograma resumido

**Ano 1:** revisão dirigida da literatura, delimitação final do escopo, curadoria inicial da base retrospectiva e definição das tarefas centrais.  
**Ano 2:** implementação dos baselines unimodais, desenvolvimento inicial dos modelos multimodais e submissão do primeiro artigo.  
**Ano 3:** aprofundamento dos experimentos multimodais, avaliação de robustez, calibração, incerteza e interpretabilidade, com submissão dos artigos metodológicos principais.  
**Ano 4:** consolidação dos resultados, integração final da camada de apoio à decisão, redação e defesa da tese.

## 10. Referências

Asghar, R., Kumar, S., Shaukat, A., & Hynds, P. (2024). Classification of white blood cells (leucocytes) from blood smear imagery using machine and deep learning models: A global scoping review. *PLOS ONE*. https://doi.org/10.1371/journal.pone.0292026

de Almeida, J. G., Gudgin, E., Besser, M., Dunn, W. G., Cooper, J., Haferlach, T., Vassiliou, G. S., & Gerstung, M. (2023). Computational analysis of peripheral blood smears detects disease-associated cytomorphologies. *Nature Communications*. https://doi.org/10.1038/s41467-023-39676-y

Horiuchi, Y., Ravzanaadii, M., Bai, J., Matsuzaki, A., Kaniyu, K., Ando, J., Ando, M., Nojiri, S., Iwasaki, Y., Konishi, A., & Tabe, Y. (2026). Application of convolutional neural network image analysis and machine learning to basic blood tests for intelligent diagnostic assistance. *International Journal of Laboratory Hematology, 48*, 26-38. https://doi.org/10.1111/ijlh.14550

Iscoe, M. S., Loza, A. J., Turbiville, D., Campbell, S. M., Peaper, D. R., Balbuena-Merle, R. I., & Hauser, R. G. (2023). PROSER: A web-based peripheral blood smear interpretation support tool utilizing electronic health record data. *American Journal of Clinical Pathology, 160*, 98-105. https://doi.org/10.1093/ajcp/aqad024

Kasprowicz, J., Bacca, H. G., & Silva, A. G. (2026). Revisão sistemática sobre técnicas de visão computacional aplicadas à classificação de leucócitos. *Journal of Health Informatics, 18*. https://doi.org/10.59681/2175-4411.v18.2026.1519

Kasprowicz, J., & Silva, A. G. (2026). Comparative analysis of convolutional and vision transformer models for automated leukocyte classification enhanced by generative color augmentation. *Signal, Image and Video Processing*. https://doi.org/10.1007/s11760-026-05309-2

Katz, B.-Z., Feldman, M. D., Tessema, M., Benisty, D., Stewart Toles, G., Andre, A., Shtreker, B., Paz, F. M., Edwards, J., Jengehino, D., Bagg, A., Avivi, I., & Pozdnyakova, O. (2021). Evaluation of Scopio Labs X100 Full Field PBS: The first high-resolution full field viewing of peripheral blood specimens combined with artificial intelligence-based morphological analysis. *International Journal of Laboratory Hematology, 43*, 1408-1416. https://doi.org/10.1111/ijlh.13681

Zini, G. (2024). Hematological cytomorphology: Where we are. *International Journal of Laboratory Hematology, 46*, 789-794. https://doi.org/10.1111/ijlh.14330
