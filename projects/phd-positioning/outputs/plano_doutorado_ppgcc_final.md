# Plano de Doutorado PPGCC/UFSC

## 1. Título

**Expansão da inteligência morfológica hematológica para inteligência clínico-laboratorial multimodal robusta e interpretável**

## 2. Introdução e contextualização

A análise morfológica do esfregaço sanguíneo periférico permanece como componente central da hematologia laboratorial, mesmo em contextos altamente automatizados. Embora analisadores hematológicos modernos ofereçam parâmetros quantitativos amplos, contagens diferenciais e flags instrumentais, a interpretação de alterações celulares imaturas, atípicas, displásicas ou reativas continua dependendo, em grande medida, da articulação entre revisão morfológica, hemograma e contexto do exame (Zini, 2024). Em paralelo, o avanço da microscopia digital e de sistemas assistidos por inteligência artificial demonstra que a morfologia hematológica pode ser progressivamente incorporada a fluxos laboratoriais computacionalmente mediados, aproximando a prática diagnóstica de ambientes digitais mais escaláveis e auditáveis (Katz et al., 2021).

A literatura recente em inteligência artificial aplicada à hematologia, contudo, apresenta uma assimetria importante. O campo mais povoado continua sendo o da classificação morfológica baseada apenas em imagem, com forte predominância de arquiteturas convolucionais e de aprendizado profundo aplicadas à identificação de leucócitos em imagens isoladas de esfregaço periférico (Asghar et al., 2024). O próprio percurso de pesquisa do candidato se insere nesse espaço inicial, tendo desenvolvido e avaliado modelos para classificação automática de leucócitos, com ênfase em construção de dataset, variabilidade de coloração, aumento de dados orientado ao domínio e generalização externa (Kasprowicz & Silva, 2026). Além disso, a revisão sistemática conduzida pelo candidato mostrou que, embora esse campo seja tecnicamente maduro para classes normais e cenários controlados, ainda persistem desafios relevantes relacionados à heterogeneidade metodológica, às células imaturas e atípicas e à distância entre desempenho experimental e aplicabilidade laboratorial real (Kasprowicz, Bacca, & Silva, 2026).

Nesse contexto, o doutorado proposto não busca reproduzir o eixo já saturado de classificação image-only, mas sim avançar para um problema computacional mais aderente à lógica da prática laboratorial: a **integração entre morfologia de esfregaço periférico, parâmetros do hemograma, flags do analisador hematológico e contexto laboratorial estruturado para inferência em nível de caso**. Trata-se, portanto, de uma transição da **inteligência morfológica hematológica** para uma **inteligência clínico-laboratorial multimodal**, mantendo a hematologia como domínio âncora, mas ampliando o nível de abstração e a contribuição computacional esperada.

## 3. Justificativa

A justificativa científica desta proposta decorre de três argumentos complementares.

O primeiro é de **continuidade acadêmica e maturidade da trajetória**. O mestrado já estabeleceu uma base metodológica consistente para o estudo computacional da morfologia hematológica, incluindo curadoria de dados, anotação orientada por especialistas, comparação rigorosa entre arquiteturas, preocupação com robustez e análise de generalização (Kasprowicz & Silva, 2026). Assim, a transição para o doutorado não configura mudança temática artificial, mas a progressão natural de `classificação celular` para `inferência multimodal em nível de caso`.

O segundo argumento é de **lacuna científica real**. O mapeamento inicial da literatura mostrou que o espaço verdadeiramente competitivo para o doutorado não está mais em propor outro classificador de leucócitos, mas em investigar sistemas que combinem morfologia de esfregaço periférico com evidências laboratoriais estruturadas, como hemograma e flags instrumentais, em tarefas de apoio à decisão hematológica. Os estudos mais próximos dessa direção ainda são poucos, heterogêneos e pouco consolidados, especialmente quando se consideram robustez, interpretabilidade e uso em fluxo laboratorial real (de Almeida et al., 2023; Horiuchi et al., 2026; Iscoe et al., 2023).

O terceiro argumento é de **relevância para a Ciência da Computação**. A proposta não consiste apenas em aplicar IA a um problema médico, mas em formalizar e investigar um problema multimodal sob restrições reais: integração entre modalidades heterogêneas, inferência em nível de caso, calibração, incerteza, generalização sob variabilidade laboratorial e interpretabilidade orientada à decisão. Nesse sentido, o projeto se alinha diretamente à linha de Inteligência Computacional do PPGCC/UFSC, ao mesmo tempo em que preserva um domínio de aplicação altamente especializado e cientificamente fértil.

Do ponto de vista estratégico, também há uma justificativa de viabilidade. O acesso a dados laboratoriais retrospectivos reais representa vantagem competitiva importante, pois permite investigar tarefas mais próximas do mundo real do que aquelas encontradas em benchmarks públicos puramente imagéticos. Essa condição favorece tanto a originalidade quanto o potencial de publicação do projeto, sem exigir, como pré-condição, uma coleta prospectiva ampla desde o início do doutorado.

## 4. Problema de pesquisa

Apesar dos avanços recentes em visão computacional aplicada à hematologia, ainda são escassos sistemas robustos e interpretáveis capazes de integrar, de forma coerente, a morfologia de esfregaço sanguíneo periférico com parâmetros do hemograma, flags do analisador hematológico e contexto laboratorial estruturado para apoiar inferências hematológicas em nível de caso.

Dessa forma, o problema de pesquisa pode ser formulado da seguinte maneira:

**Como desenvolver sistemas de inteligência artificial capazes de integrar, de forma robusta, interpretável e viável em contexto retrospectivo, a morfologia de esfregaço periférico com hemograma, flags do analisador e dados laboratoriais estruturados, para apoiar a decisão hematológica em nível de caso?**

## 5. Objetivos

### Objetivo geral

Desenvolver e avaliar uma abordagem de inteligência artificial multimodal para hematologia capaz de integrar morfologia de esfregaço sanguíneo periférico, parâmetros do hemograma, flags do analisador hematológico e contexto laboratorial estruturado, com foco em robustez, interpretabilidade e apoio à decisão em nível de caso.

### Objetivos específicos

1. Construir uma base multimodal retrospectiva em hematologia, integrando imagens de esfregaço periférico, parâmetros do hemograma, contagens diferenciais, flags do analisador e metadados laboratoriais essenciais.
2. Desenvolver e comparar estratégias de fusão multimodal para tarefas de inferência hematológica em nível de caso, contrastando modelos baseados apenas em imagem, apenas em dados estruturados e modelos integrados.
3. Investigar robustez, generalização, calibração e incerteza dos modelos diante de variabilidade laboratorial real, incluindo cenários de heterogeneidade de coloração, composição dos casos e distribuição das classes.
4. Avaliar mecanismos de interpretabilidade multimodal e sua utilidade em tarefas de apoio à decisão laboratorial, como triagem, priorização de revisão manual e identificação de padrões suspeitos.

## 6. Fundamentação teórica / estado da arte

A fundamentação teórica do projeto parte do reconhecimento de que a morfologia hematológica continua sendo clinicamente relevante e computacionalmente promissora. Revisões recentes em hematologia laboratorial destacam que a citomorfologia mantém papel decisivo no diagnóstico e na avaliação de alterações hematológicas, mesmo diante da incorporação de tecnologias digitais e inteligência artificial (Zini, 2024). Estudos com sistemas de microscopia digital assistida por IA também mostram que a morfologia pode ser integrada a fluxos laboratoriais reais com reprodutibilidade e valor operacional, o que reforça a maturidade translacional do domínio (Katz et al., 2021).

Entretanto, a maior parte da literatura em IA hematológica ainda se concentra em tarefas de classificação de leucócitos ou células sanguíneas em imagens isoladas. A revisão de escopo de Asghar et al. (2024) mostra que esse campo é amplamente dominado por pipelines baseados em CNNs e deep learning, com bom desempenho em classes maduras e datasets relativamente controlados, mas com limitações de comparabilidade, generalização e aderência ao raciocínio laboratorial real. Em convergência com esse diagnóstico, a revisão sistemática conduzida pelo candidato demonstrou que a área já apresenta forte maturidade técnica para reconhecimento image-only, mas ainda carece de abordagens mais robustas para classes imaturas e contextos de maior relevância clínica (Kasprowicz et al., 2026).

Esse cenário evidencia uma limitação estrutural da abordagem image-only. Na prática hematológica, a interpretação de achados morfológicos depende de sua articulação com o hemograma, com as flags do analisador, com a distribuição das alterações no esfregaço e com o contexto do caso. A decisão laboratorial, portanto, é construída em nível de caso, e não apenas no nível de uma célula isolada. Nesse ponto, a literatura disponível aponta sinais importantes, porém ainda pouco consolidados. O trabalho de de Almeida et al. (2023) mostrou que a análise computacional de esfregaços periféricos pode identificar citomorfologias associadas a doença e ganhar valor quando relacionada a blood counts, com evidências de generalização externa. Horiuchi et al. (2026), por sua vez, apresentaram um dos exemplos mais diretamente alinhados a esta proposta ao combinar análise de imagem de células periféricas com exames básicos de sangue para assistência diagnóstica inteligente.

No eixo de apoio à decisão, ferramentas como o PROSER demonstram que dados laboratoriais estruturados e contexto clínico podem ser incorporados à interpretação de esfregaços, ainda que sem constituir, por si só, um framework multimodal completo de aprendizado profundo (Iscoe et al., 2023). Esse tipo de estudo é particularmente relevante porque aproxima a pesquisa da lógica real de triagem, revisão e interpretação laboratorial.

Outro componente central do estado da arte é a robustez. O artigo Springer do candidato mostrou que a classificação de leucócitos é sensível à variabilidade de coloração e que estratégias de aumento de dados orientadas ao domínio, como HistAuGAN, podem melhorar desempenho e generalização externa sem modificação arquitetural (Kasprowicz & Silva, 2026). Ainda assim, a maior parte dos estudos de robustez permanece concentrada em pipelines imagéticos. O mapeamento da literatura sugere que a robustez em sistemas genuinamente multimodais para hematologia permanece como espaço aberto, especialmente quando associada a calibração, incerteza e interpretabilidade.

Assim, a lacuna que fundamenta este doutorado pode ser sintetizada da seguinte forma: **a literatura em hematologia computacional é ampla em classificação morfológica baseada apenas em imagem, mas ainda escassa em sistemas multimodais, robustos e interpretáveis que integrem morfologia de esfregaço periférico, hemograma, flags do analisador e contexto laboratorial estruturado para inferência em nível de caso**. É nessa lacuna que o presente plano se posiciona.

## 7. Metodologia

A metodologia proposta será retrospectiva, modular e orientada à publicação, de modo a compatibilizar rigor científico com viabilidade de execução por pesquisador que trabalha em tempo integral.

Na primeira etapa, será realizada a **curadoria e harmonização da base multimodal**, com definição dos critérios de inclusão dos casos e identificação das fontes de dados relevantes. A base deverá integrar, no mínimo, imagens de esfregaço periférico, parâmetros do hemograma, contagens diferenciais, flags do analisador hematológico e metadados laboratoriais essenciais. Nessa fase, serão tratados aspectos de consistência temporal entre modalidades, qualidade dos registros, dados faltantes e critérios mínimos de representatividade. O foco será a construção de uma base retrospectiva em nível de caso, e não de um repositório universal de hematologia.

Na segunda etapa, serão formalizadas as **tarefas computacionais centrais**. A proposta prioriza tarefas alinhadas à prática laboratorial, como priorização de revisão manual, detecção de padrões suspeitos, suporte à interpretação integrada e análise de concordância ou discordância entre morfologia e sinais estruturados. Essa escolha evita reduzir o projeto a outro benchmark de classificação celular e preserva a aderência ao problema real de decisão laboratorial.

Na terceira etapa, serão implementados os **baselines e modelos multimodais**. Isso incluirá, inicialmente, modelos baseados apenas em imagem, modelos baseados apenas em dados estruturados e, em seguida, estratégias de fusão multimodal em diferentes níveis. O objetivo não será apenas maximizar acurácia, mas avaliar o ganho real da integração entre modalidades, identificando quando a morfologia agrega informação singular, quando os dados tabulares predominam e quando a combinação entre ambos é necessária para inferência mais confiável.

Na quarta etapa, será conduzida a **avaliação de robustez, generalização, calibração e incerteza**. Essa etapa será central para a contribuição em Ciência da Computação, uma vez que pretende investigar o comportamento dos modelos diante de variabilidade laboratorial real, incluindo efeitos de heterogeneidade de coloração, composição dos dados, distribuição das classes e possíveis diferenças temporais ou setoriais. Também serão realizados estudos de interpretabilidade multimodal, buscando explicitar a contribuição relativa de cada modalidade para as inferências produzidas.

Na quinta etapa, será desenvolvida uma **camada restrita de apoio à decisão laboratorial**, orientada por interpretabilidade e utilidade prática. Essa camada poderá incluir saídas explicáveis para triagem ou revisão manual e, apenas se o núcleo multimodal estiver suficientemente maduro, mecanismos complementares baseados em regras explícitas ou recuperação estruturada. O projeto não terá como eixo central LLMs, agentes genéricos ou promessas de automação universal.

Em termos de delimitação, pertencem ao núcleo da tese a morfologia de esfregaço periférico, o hemograma, as flags do analisador, a inferência em nível de caso, a robustez e a interpretabilidade. Domínios adicionais, como alterações eritrocitárias mais amplas ou morfologia plaquetária, poderão ser incorporados apenas se fortalecerem tarefas bem definidas e não comprometerem a viabilidade do plano. Estão explicitamente fora do escopo central integrações amplas com genômica, mielograma, citometria de fluxo, plataformas universais de hematologia ou teses genéricas sobre LLMs.

## 8. Resultados esperados

Espera-se que o projeto produza resultados em quatro níveis principais.

No nível de infraestrutura científica, espera-se a construção de uma base multimodal retrospectiva em hematologia, organizada em nível de caso e adequada para experimentos reprodutíveis de integração entre morfologia e dados estruturados. No nível metodológico, espera-se o desenvolvimento e a avaliação de estratégias de fusão multimodal capazes de superar as limitações de abordagens image-only em tarefas mais próximas do fluxo laboratorial real.

No nível de confiabilidade computacional, espera-se gerar evidências sobre robustez, generalização, calibração, incerteza e interpretabilidade em IA multimodal aplicada à hematologia, contribuindo para o avanço de sistemas mais confiáveis em ambientes laboratoriais reais. No nível translacional, espera-se produzir mecanismos de apoio à decisão laboratorial com utilidade potencial em triagem e priorização de revisão manual, sem pretender substituir o especialista humano.

Em termos de publicação, o projeto foi desenhado para gerar, de forma realista, ao menos quatro frentes publicáveis: um artigo sobre base multimodal e formulação do problema; um artigo sobre comparação entre abordagens unimodais e multimodais; um artigo centrado em robustez, calibração e incerteza; e um artigo sobre interpretabilidade e apoio à decisão em fluxo laboratorial. Essa estrutura reforça a viabilidade do plano para um pesquisador em regime de trabalho integral.

## 9. Cronograma resumido

**Ano 1**

- aprofundamento teórico e consolidação da revisão de literatura dirigida;
- definição fina do escopo da base retrospectiva;
- curadoria inicial e harmonização dos dados multimodais;
- especificação das tarefas computacionais centrais.

**Ano 2**

- implementação dos baselines unimodais;
- desenvolvimento inicial dos modelos multimodais;
- primeiros experimentos comparativos entre imagem, dados estruturados e fusão;
- submissão do primeiro artigo.

**Ano 3**

- aprofundamento dos experimentos multimodais;
- análise de robustez, generalização, calibração e incerteza;
- estudos de interpretabilidade multimodal;
- submissão de artigos metodológicos centrais.

**Ano 4**

- consolidação da camada de apoio à decisão laboratorial;
- integração final dos resultados;
- redação e defesa da tese;
- submissão dos artigos finais e preparação de produtos derivados.

## 10. Referências

Asghar, R., Kumar, S., Shaukat, A., & Hynds, P. (2024). Classification of white blood cells (leucocytes) from blood smear imagery using machine and deep learning models: A global scoping review. *PLOS ONE*. https://doi.org/10.1371/journal.pone.0292026

de Almeida, J. G., Gudgin, E., Besser, M., Dunn, W. G., Cooper, J., Haferlach, T., Vassiliou, G. S., & Gerstung, M. (2023). Computational analysis of peripheral blood smears detects disease-associated cytomorphologies. *Nature Communications*. https://doi.org/10.1038/s41467-023-39676-y

Horiuchi, Y., Ravzanaadii, M., Bai, J., Matsuzaki, A., Kaniyu, K., Ando, J., Ando, M., Nojiri, S., Iwasaki, Y., Konishi, A., & Tabe, Y. (2026). Application of convolutional neural network image analysis and machine learning to basic blood tests for intelligent diagnostic assistance. *International Journal of Laboratory Hematology, 48*, 26-38. https://doi.org/10.1111/ijlh.14550

Iscoe, M. S., Loza, A. J., Turbiville, D., Campbell, S. M., Peaper, D. R., Balbuena-Merle, R. I., & Hauser, R. G. (2023). PROSER: A web-based peripheral blood smear interpretation support tool utilizing electronic health record data. *American Journal of Clinical Pathology, 160*, 98-105. https://doi.org/10.1093/ajcp/aqad024

Kasprowicz, J., Bacca, H. G., & Silva, A. G. (2026). Revisão sistemática sobre técnicas de visão computacional aplicadas à classificação de leucócitos. *Journal of Health Informatics, 18*. https://doi.org/10.59681/2175-4411.v18.2026.1519

Kasprowicz, J., & Silva, A. G. (2026). Comparative analysis of convolutional and vision transformer models for automated leukocyte classification enhanced by generative color augmentation. *Signal, Image and Video Processing*. https://doi.org/10.1007/s11760-026-05309-2

Katz, B.-Z., Feldman, M. D., Tessema, M., Benisty, D., Stewart Toles, G., Andre, A., Shtreker, B., Paz, F. M., Edwards, J., Jengehino, D., Bagg, A., Avivi, I., & Pozdnyakova, O. (2021). Evaluation of Scopio Labs X100 Full Field PBS: The first high-resolution full field viewing of peripheral blood specimens combined with artificial intelligence-based morphological analysis. *International Journal of Laboratory Hematology, 43*, 1408-1416. https://doi.org/10.1111/ijlh.13681

Zini, G. (2024). Hematological cytomorphology: Where we are. *International Journal of Laboratory Hematology, 46*, 789-794. https://doi.org/10.1111/ijlh.14330
