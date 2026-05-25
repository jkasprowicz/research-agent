# Plano de Trabalho de Doutorado com Referências

## Título provisório

**Inteligência clínico-laboratorial multimodal em hematologia: integração de morfologia de esfregaço periférico, parâmetros do hemograma e flags do analisador para apoio robusto e interpretável à decisão**

## 1. Introdução, motivação e relevância

A hematologia laboratorial contemporânea depende de uma articulação contínua entre automação analítica, revisão morfológica especializada e interpretação contextual dos resultados. Embora os analisadores hematológicos modernos forneçam parâmetros quantitativos amplos e flags de alerta, a análise citomorfológica do esfregaço periférico permanece central para o reconhecimento de alterações celulares imaturas, atípicas, reativas ou displásicas, e continua relevante mesmo na era da microscopia digital e da inteligência artificial (Zini, 2024). Ao mesmo tempo, sistemas digitais de morfologia com apoio algorítmico já demonstram utilidade operacional em fluxos reais, reforçando que a transformação computacional da hematologia não elimina a morfologia, mas a reinsere em novos arranjos de apoio à decisão (Katz et al., 2021).

A literatura recente em inteligência artificial aplicada à hematologia cresceu de forma expressiva, porém de maneira assimétrica. O eixo mais povoado é a classificação de leucócitos e outras células sanguíneas em imagens isoladas, com forte predominância de abordagens baseadas em deep learning e CNNs, o que caracteriza um campo tecnicamente ativo, mas já bastante denso em estudos de reconhecimento morfológico unimodal (Asghar et al., 2024). Em contraste, estudos que integrem de forma explícita morfologia de esfregaço, hemograma, sinais instrumentais e contexto laboratorial estruturado ainda são substancialmente menos numerosos. Essa assimetria sugere que o próximo avanço relevante não está em propor apenas mais um classificador celular, mas em deslocar o problema para a inferência clínico-laboratorial em nível de caso.

Essa mudança de foco é cientificamente justificável e computacionalmente fértil. Em prática real, a decisão hematológica raramente decorre apenas da aparência de uma célula isolada; ela emerge da combinação entre padrões morfológicos, contagens e índices hematológicos, flags do analisador, distribuição das alterações no esfregaço e coerência com o contexto do exame. Evidências recentes mostram que a integração entre citomorfologia e blood counts pode melhorar tarefas diagnósticas ou de estratificação, mas esse espaço ainda aparece de forma fragmentada e pouco consolidada como problema multimodal robusto em nível de caso (de Almeida et al., 2023; Horiuchi et al., 2026). Por isso, a proposta deste doutorado é centrada em **inteligência clínico-laboratorial multimodal em hematologia**, com a morfologia como âncora, mas indo além da classificação baseada apenas em imagem.

## 2. Problema de pesquisa e pergunta central

O problema central deste doutorado é a ausência de sistemas robustos e interpretáveis capazes de integrar, de forma coerente e útil ao fluxo laboratorial, a morfologia de esfregaços sanguíneos periféricos com dados laboratoriais estruturados para apoiar inferências hematológicas em nível de caso.

A pergunta central é:

**A integração multimodal entre morfologia de esfregaço periférico, parâmetros do hemograma, flags do analisador hematológico e contexto laboratorial estruturado permite construir sistemas de apoio à decisão hematológica mais robustos, interpretáveis e clinicamente úteis do que abordagens baseadas apenas em imagem?**

## 3. Lacuna científica e posicionamento no estado da arte

A lacuna científica identificada pode ser descrita em quatro níveis complementares.

Primeiro, existe uma **lacuna de integração**. A maior parte da literatura em IA hematológica se concentra em classificação ou detecção em imagens de células, enquanto a prática laboratorial opera a partir da convergência entre morfologia, CBC, differential, flags instrumentais e informações contextuais do caso. Revisões recentes deixam claro o volume e a maturidade relativa do campo de classificação morfológica, mas também ajudam a evidenciar que o problema de fusão entre modalidades permanece comparativamente menos desenvolvido (Asghar et al., 2024).

Segundo, existe uma **lacuna de nível inferencial**. Muitos trabalhos produzem saídas em nível de célula ou campo microscópico, enquanto a decisão laboratorial ocorre em nível de caso. Mesmo estudos mais sofisticados de análise computacional de esfregaços demonstram que o ganho translacional real aparece quando a morfologia é agregada e relacionada a desfechos, subtipos de doença ou sinais laboratoriais complementares, e não quando permanece restrita ao reconhecimento de células isoladas (de Almeida et al., 2023).

Terceiro, há uma **lacuna de robustez e generalização**. Em hematologia, variações de preparação do esfregaço, coloração, equipamento, scanner, protocolo institucional e composição do mix de casos afetam fortemente o desempenho dos modelos. Embora já existam estudos mostrando a importância de validação multicêntrica e generalização em análise morfológica digital, ainda é limitada a literatura que trata robustez, calibração e incerteza em sistemas genuinamente multimodais aplicados ao laboratório clínico (Katz et al., 2021; de Almeida et al., 2023).

Quarto, há uma **lacuna de apoio à decisão laboratorial**. Poucos trabalhos se aproximam da lógica real de triagem, revisão manual e interpretação integrada. Sistemas como o PROSER mostram que dados do prontuário e do laboratório podem ser organizados em ferramentas de suporte à interpretação do esfregaço, mas ainda há amplo espaço para métodos computacionais que incorporem a modalidade imagética e tratem a inferência de forma mais profunda e sistemática (Iscoe et al., 2023).

Em síntese, o estado da arte sugere que **imagem-only hematology** já é um campo maduro o suficiente para ser visto como espaço competitivo e parcialmente saturado, enquanto a **inferência multimodal clínico-laboratorial em nível de caso** permanece mais aberta, defensável e alinhada a uma tese de doutorado com identidade própria.

## 4. Continuidade com o mestrado

Esta proposta evolui diretamente da trajetória construída no mestrado. O eixo anterior foi a classificação automática de células hematológicas em imagens de esfregaço periférico, com desenvolvimento e comparação de modelos de visão computacional, construção de dataset próprio, análise de variabilidade de coloração, uso de augmentation e preocupação explícita com robustez e generalização.

O doutorado preserva esse núcleo, mas amplia o escopo inferencial:

`classificação celular` -> `representação morfológica` -> `integração multimodal` -> `apoio à decisão hematológica em nível de caso`

Não se trata, portanto, de uma mudança temática artificial. Trata-se de uma evolução metodológica natural: a morfologia permanece como âncora, enquanto o problema computacional passa a ser a integração entre sinais heterogêneos sob condições reais de laboratório. Essa transição é coerente com o estado da arte identificado no mapeamento e com a maturidade técnica já estabelecida na linha de pesquisa do candidato.

## 5. Objetivos

### Objetivo geral

Desenvolver e avaliar um sistema de inteligência artificial multimodal para hematologia capaz de integrar morfologia de esfregaço sanguíneo periférico, parâmetros do hemograma e sinais estruturados do laboratório, com foco em robustez, interpretabilidade e apoio à decisão em nível de caso.

### Objetivos específicos

1. Construir uma base multimodal clínico-laboratorial em hematologia, combinando imagens de esfregaço periférico com parâmetros do hemograma, flags do analisador e metadados laboratoriais relevantes.
2. Desenvolver e comparar estratégias de fusão multimodal para tarefas de inferência hematológica em nível de caso, contrastando abordagens unimodais e multimodais.
3. Investigar robustez, generalização, calibração, incerteza e interpretabilidade dos modelos sob variabilidade laboratorial real.
4. Propor e avaliar uma camada de apoio à decisão laboratorial baseada na contribuição conjunta das modalidades, priorizando transparência e utilidade prática.

## 6. Metodologia proposta

A metodologia será organizada em etapas modulares, compatíveis com execução gradual durante o doutorado por pesquisador que trabalha em tempo integral.

### Etapa 1. Curadoria e harmonização multimodal

Serão identificados casos com imagens morfológicas e dados estruturados associados. A base deverá integrar, no mínimo, imagens de esfregaço periférico, parâmetros do hemograma, contagens diferenciais, flags do analisador hematológico e metadados laboratoriais relevantes. O uso de dados laboratoriais reais constitui uma vantagem estratégica decisiva porque permite formular um problema mais original do que os benchmarks imagéticos tradicionais e aproxima a pesquisa das situações em que inconsistências, concordâncias ou discordâncias entre modalidades realmente importam para a interpretação do caso.

### Etapa 2. Formalização das tarefas em nível de caso

As tarefas serão definidas em nível de caso, com foco em aplicações como priorização de revisão manual, suporte à identificação de alterações morfológicas relevantes, triagem baseada em concordância entre morfologia e sinais estruturados e apoio à inferência diagnóstica assistida. Essa escolha responde diretamente à limitação dos estudos centrados em célula isolada e se aproxima mais da lógica decisória encontrada na rotina laboratorial (Iscoe et al., 2023; Horiuchi et al., 2026).

### Etapa 3. Modelagem computacional

Serão implementados baselines apenas com imagem, baselines apenas com dados tabulares e modelos multimodais com diferentes estratégias de fusão. O objetivo não será apenas maximizar desempenho preditivo, mas medir o ganho real da integração entre modalidades. A literatura mais próxima da proposta sugere que esse ganho é plausível e cientificamente promissor, sobretudo quando a morfologia é combinada com CBC ou outros sinais laboratoriais em tarefas orientadas ao caso (de Almeida et al., 2023; Horiuchi et al., 2026).

### Etapa 4. Robustez, generalização e interpretabilidade

Esta etapa avaliará generalização sob variação de domínio, calibração, incerteza, análise de erro e contribuição relativa de cada modalidade. A preocupação com robustez é central porque o ambiente laboratorial real está sujeito a heterogeneidade técnica e clínica. Assim, além de performance agregada, o projeto deverá investigar quando o modelo falha, qual modalidade sustenta a decisão e em quais cenários a multimodalidade de fato agrega valor (Katz et al., 2021; de Almeida et al., 2023).

### Etapa 5. Camada opcional de apoio interpretativo

Se a base multimodal principal estiver madura, poderá ser adicionada uma camada auxiliar de apoio interpretativo baseada em regras explícitas, recuperação estruturada ou mecanismos semelhantes. O uso de LLMs, se ocorrer, será subordinado ao problema laboratorial e não ao contrário. Essa delimitação é importante para evitar que a proposta se desloque para um uso genérico e pouco defensável de agentic AI, sem sustentação em dados reais ou em necessidade concreta do fluxo hematológico.

## 7. Viabilidade e relevância estratégica

A proposta foi desenhada para ser realista para quem trabalha em tempo integral. Sua viabilidade decorre de cinco características: aproveita experiência e infraestrutura já estabelecidas no mestrado; permite modularização em artigos independentes; depende mais de curadoria, integração e modelagem incremental do que de uma única coleta prospectiva massiva; pode começar com desenho retrospectivo; e concentra-se em um domínio bem delimitado.

Além disso, o acesso a dados laboratoriais reais representa vantagem competitiva relevante. Enquanto muitos estudos permanecem restritos a datasets públicos puramente imagéticos, a disponibilidade de CBC, flags, metadados laboratoriais e imagens associadas permite investigar um problema mais raro, mais translacional e mais difícil de replicar por grupos sem inserção no laboratório clínico. Essa condição fortalece a originalidade da tese e aumenta seu potencial de publicação.

## 8. Contribuições esperadas para Ciência da Computação

As contribuições esperadas não são apenas aplicadas à saúde. Em Ciência da Computação, o projeto pode contribuir para:

- formulação de um problema multimodal em ambiente laboratorial real;
- desenvolvimento e avaliação de estratégias de fusão entre imagem e dados estruturados;
- investigação de robustez, calibração e confiabilidade em IA multimodal;
- mecanismos de interpretabilidade para inferência heterogênea orientada à decisão;
- possível criação de um recurso multimodal reutilizável para pesquisa translacional.

Assim, o doutorado não deve ser apresentado como mera aplicação de IA a exames laboratoriais, mas como uma formulação computacional nova e metodologicamente relevante, motivada por um contexto hematológico concreto.

## 9. Produtos esperados e potencial de publicação

O projeto tem potencial para gerar pelo menos quatro frentes publicáveis:

1. caracterização e organização de base multimodal clínico-laboratorial em hematologia;
2. comparação entre baselines unimodais e modelos multimodais para inferência em nível de caso;
3. robustez, generalização, calibração e incerteza em hematologia multimodal;
4. apoio à decisão laboratorial com interpretabilidade orientada ao fluxo de trabalho.

Uma quinta frente, opcional, pode explorar suporte interpretativo estruturado, desde que fundamentado nos dados laboratoriais reais e não em promessas genéricas de automação cognitiva.

## 10. Enquadramento para orientação

O enquadramento principal recomendado é com **Jônata Tyska Carvalho**, apresentando a proposta como um problema de IA multimodal em saúde com ênfase em integração entre modalidades, robustez, interpretabilidade e inferência em nível de caso. Esse enquadramento mantém a proposta claramente computacional, evita reduzi-la a um problema apenas de visão computacional e preserva abertura para componentes de raciocínio estruturado sem depender de hype.

Como alternativa, **Renato Fileto** torna-se especialmente adequado se a proposta enfatizar mais fortemente a integração de dados complexos, a organização semântica do contexto laboratorial e a camada estrutural de apoio à decisão.

## 11. Delimitações e riscos de posicionamento

Para que a proposta permaneça competitiva, quatro riscos devem ser explicitamente evitados:

1. **Excesso de clinificação**: a tese deve sempre nomear o problema computacional de fusão, robustez e interpretabilidade.
2. **Incrementalismo**: não pode ser apresentada como apenas mais um modelo de classificação de leucócitos.
3. **Genericidade**: deve explicitar esfregaço periférico, hemograma, flags do analisador e inferência em nível de caso.
4. **Amplitude excessiva**: deve evitar prometer um sistema universal ou um “agente de hematologia” sem base metodológica e laboratorial correspondente.

## 12. Conclusão

O caminho mais forte para o doutorado é desenvolver uma proposta de **inteligência clínico-laboratorial multimodal em hematologia**, com a morfologia como âncora e com expansão para inferência em nível de caso, robustez e apoio à decisão. O estado da arte sugere que a limitação principal do campo não é a ausência de classificadores morfológicos, mas a ausência de sistemas que articulem, de forma confiável e interpretável, as diferentes modalidades que efetivamente sustentam a decisão hematológica. Essa formulação preserva continuidade com o mestrado, responde a uma lacuna real da literatura, demonstra maturidade científica e mantém alto potencial de publicação sem depender de buzzwords ou de uma transição temática artificial.

## Referências

Asghar, R., Kumar, S., Shaukat, A., & Hynds, P. (2024). Classification of white blood cells (leucocytes) from blood smear imagery using machine and deep learning models: A global scoping review. *PLOS ONE*. https://doi.org/10.1371/journal.pone.0292026

de Almeida, J. G., Gudgin, E., Besser, M., Dunn, W. G., Cooper, J., Haferlach, T., Vassiliou, G. S., & Gerstung, M. (2023). Computational analysis of peripheral blood smears detects disease-associated cytomorphologies. *Nature Communications*. https://doi.org/10.1038/s41467-023-39676-y

Horiuchi, Y., Ravzanaadii, M., Bai, J., Matsuzaki, A., Kaniyu, K., Ando, J., Ando, M., Nojiri, S., Iwasaki, Y., Konishi, A., & Tabe, Y. (2026). Application of convolutional neural network image analysis and machine learning to basic blood tests for intelligent diagnostic assistance. *International Journal of Laboratory Hematology, 48*, 26-38. https://doi.org/10.1111/ijlh.14550

Iscoe, M. S., Loza, A. J., Turbiville, D., Campbell, S. M., Peaper, D. R., Balbuena-Merle, R. I., & Hauser, R. G. (2023). PROSER: A web-based peripheral blood smear interpretation support tool utilizing electronic health record data. *American Journal of Clinical Pathology, 160*, 98-105. https://doi.org/10.1093/ajcp/aqad024

Katz, B.-Z., Feldman, M. D., Tessema, M., Benisty, D., Stewart Toles, G., Andre, A., Shtreker, B., Paz, F. M., Edwards, J., Jengehino, D., Bagg, A., Avivi, I., & Pozdnyakova, O. (2021). Evaluation of Scopio Labs X100 Full Field PBS: The first high-resolution full field viewing of peripheral blood specimens combined with artificial intelligence-based morphological analysis. *International Journal of Laboratory Hematology, 43*, 1408-1416. https://doi.org/10.1111/ijlh.13681

Zini, G. (2024). Hematological cytomorphology: Where we are. *International Journal of Laboratory Hematology, 46*, 789-794. https://doi.org/10.1111/ijlh.14330
