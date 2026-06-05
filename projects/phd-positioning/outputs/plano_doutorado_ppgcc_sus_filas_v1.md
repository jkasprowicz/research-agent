# Plano de Trabalho - Doutorado

## Linha de pesquisa, tema e orientação

**Linha de pesquisa:** Inteligência Computacional.

**Tema pretendido:** aplicação e desenvolvimento de métodos de inteligência artificial para saúde, com ênfase em aprendizado de máquina, explicabilidade e suporte à decisão em sistemas públicos de saúde.

**Orientador indicado:** Jônata Tyska Carvalho.

## Título

**Modelos preditivos explicáveis e suporte à decisão para dinâmicas de listas de espera no Sistema Único de Saúde**

## Introdução, motivação e problema de pesquisa

Listas de espera para consultas especializadas, exames e procedimentos eletivos são um dos problemas mais visíveis de acesso no Sistema Único de Saúde (SUS). Apesar de frequentemente descritas como filas, essas listas não seguem necessariamente uma lógica simples de ordem de chegada. Solicitações podem ser classificadas por risco, devolvidas à unidade solicitante, autorizadas, agendadas, canceladas, não comparecidas, executadas ou reclassificadas conforme protocolos, disponibilidade assistencial e mudanças na capacidade dos serviços. Assim, uma lista de espera pode ser compreendida computacionalmente como um processo dinâmico de eventos, no qual solicitações transitam entre estados sob restrições de oferta, prioridade, território e capacidade.

O Ministério da Saúde tem enfatizado a necessidade de qualificar a regulação do acesso, ampliar a interoperabilidade dos registros de regulação assistencial e reduzir tempos de espera por consultas, exames e cirurgias. Ao mesmo tempo, a literatura sobre listas de espera no SUS aponta desafios de monitoramento, transparência, fragmentação de dados, heterogeneidade entre serviços e dificuldade de transformar registros administrativos em informação acionável para gestores. Experiências brasileiras de apoio à regulação por telessaúde mostram que intervenções organizacionais podem reduzir listas e tempos de espera, mas também evidenciam limitações metodológicas para analisar efeitos, heterogeneidade local e mudanças concorrentes nos fluxos assistenciais (Gadenz et al., 2021; Giannotti et al., 2025).

Na Ciência da Computação, há literatura consolidada sobre aprendizado de máquina para fluxo de pacientes, pesquisa operacional em saúde, simulação de eventos discretos, priorização de pacientes e sistemas de apoio à decisão. Entretanto, ainda há lacuna na formulação de métodos explicáveis, temporalmente validados e orientados a decisões gerenciais para modelar o comportamento de listas de espera em sistemas públicos de saúde com dados reais de regulação. O problema de pesquisa proposto é: **como desenvolver e avaliar modelos computacionais explicáveis capazes de caracterizar, prever e simular comportamentos problemáticos em listas de espera do SUS, de modo a apoiar gestores na identificação de gargalos, riscos operacionais e cenários de decisão?**

## Objetivos

**Objetivo geral:** desenvolver e avaliar métodos de aprendizado de máquina explicável e simulação para apoio à decisão na gestão de listas de espera do SUS, considerando registros retrospectivos de regulação assistencial e dinâmicas temporais de solicitações, prioridades, serviços e desfechos administrativos.

**Objetivos específicos:**

1. Formalizar um modelo computacional de eventos para registros de listas de espera, representando entradas, transições de status, tempos de permanência, prioridades, unidades solicitantes, unidades executantes, procedimentos e desfechos.
2. Desenvolver modelos preditivos para identificar comportamento problemático em filas, como espera excessiva, violação de tempo esperado, devoluções recorrentes, cancelamentos, faltas, estagnação e acúmulo anormal de solicitações.
3. Investigar métodos de explicabilidade em nível de solicitação, serviço e fila, produzindo evidências interpretáveis sobre fatores associados a gargalos, atrasos e instabilidade operacional.
4. Avaliar, quando houver dados de capacidade ou oferta assistencial, modelos de simulação de eventos discretos informados por aprendizado de máquina para comparar cenários de gestão, priorização, capacidade e encaminhamento.

## Estado da arte

No contexto brasileiro, listas de espera na atenção especializada têm sido discutidas como um problema crítico de acesso, coordenação do cuidado, transparência e gestão da oferta. Documentos oficiais de regulação descrevem a fila de espera como processo dinâmico, dependente de classificação de risco, priorização, capacidade dos serviços e monitoramento contínuo. O modelo de informação do e-SUS Regulação explicita variáveis compatíveis com uma modelagem orientada a eventos, incluindo status da solicitação, procedimento, datas de solicitação, autorização e execução, estabelecimentos envolvidos, modalidade assistencial e caráter da solicitação.

Estudos brasileiros sobre regulação e listas de espera mostram que a gestão do acesso não depende apenas de aumentar oferta, mas também de qualificar encaminhamentos, priorizar casos, reduzir devoluções, monitorar tempos e reorganizar fluxos. Gadenz et al. (2021), por exemplo, analisaram estratégias de telessaúde para apoio à regulação em múltiplas localidades do SUS e observaram reduções no tamanho das listas e nos tempos de espera em parte dos cenários avaliados. Ainda assim, a literatura nacional permanece predominantemente descritiva, normativa ou avaliativa, com menor presença de modelos computacionais preditivos, explicáveis e orientados à decisão.

Internacionalmente, métodos de priorização, pesquisa operacional e simulação têm sido aplicados à gestão de listas cirúrgicas, fluxo de pacientes, capacidade e agendamento. Revisões sobre priorização de pacientes mostram heterogeneidade de critérios e necessidade de métodos transparentes (Rathnayake et al., 2021). Sistemas de pontuação dinâmica de prioridade incorporam tempo de espera e fatores clínicos para tornar a ordenação mais objetiva e auditável (Powers et al., 2023). Em paralelo, aprendizado de máquina tem sido usado para prever demanda, fluxo, permanência, espera e sobrecarga operacional (El-Bouri et al., 2021), enquanto simulação de eventos discretos e abordagens híbridas ML-simulação são empregadas para análise de cenários e planejamento de recursos (Zhang, 2021; Abuhay et al., 2023).

A lacuna científica está na integração dessas frentes em um arcabouço computacional adequado ao contexto de regulação do SUS: modelagem longitudinal de eventos de fila, predição explicável de comportamento problemático, análise de gargalos e simulação de cenários gerenciais com validação temporal e métricas de utilidade operacional.

## Possíveis contribuições científicas para Computação

A proposta pretende contribuir para a Computação em cinco frentes. Primeiro, pela formalização de listas de espera como logs de eventos e transições de estado, permitindo transformar registros administrativos de regulação em objetos computacionais analisáveis. Segundo, pelo desenvolvimento e avaliação de modelos preditivos temporalmente validados para comportamento problemático de filas, indo além da simples estimação média de tempo de espera. Terceiro, pela investigação de explicabilidade orientada ao gestor, combinando explicações locais, globais e agregadas por serviço, procedimento ou território. Quarto, pela integração entre modelos preditivos e simulação de eventos discretos para análise de cenários, quando houver dados suficientes de capacidade. Quinto, pela avaliação de robustez, calibração, equidade e utilidade operacional em um domínio de alto impacto social.

## Encaminhamento metodológico

O estudo será retrospectivo, observacional e dependente de aprovação ética e acordo de uso de dados. A unidade principal de análise será a solicitação de regulação ou episódio de fila. O conjunto mínimo esperado inclui identificador pseudonimizado da solicitação, datas de entrada e movimentação, status da solicitação, procedimento, especialidade ou serviço, prioridade ou caráter da solicitação, unidade solicitante, unidade reguladora, unidade executante, município ou região, idade e sexo. Um conjunto ampliado poderá incluir histórico completo de transições, dados de capacidade, vagas ou agendas, motivo de devolução, motivo de cancelamento, protocolos aplicados, absenteísmo e marcadores territoriais.

A primeira etapa consistirá na construção do modelo de dados e do log de eventos. Serão definidos estados, transições, janelas temporais, critérios de inclusão, tratamento de duplicidades, inconsistências, dados ausentes e mudanças administrativas. Indicadores iniciais incluirão tempo até autorização, tempo até execução, tempo por status, volume de entrada, taxa de devolução, taxa de cancelamento, absenteísmo, acúmulo por serviço e distribuição por prioridade.

Na segunda etapa serão definidos alvos preditivos de utilidade gerencial, como espera excessiva, violação de prazo por prioridade, devolução recorrente, não comparecimento, cancelamento e estagnação. Serão comparados baselines simples, modelos estatísticos, análise de sobrevivência, árvores, modelos de gradiente e, quando apropriado, modelos sequenciais. A avaliação utilizará validação temporal, calibração, desempenho por subgrupos, análise de erro e comparação com regras simples de gestão.

Na terceira etapa serão investigadas explicações orientadas à decisão. A análise buscará responder não apenas quais solicitações têm maior risco, mas quais características de serviço, procedimento, unidade, prioridade, sazonalidade ou trajetória explicam gargalos e atrasos. Serão consideradas técnicas de interpretabilidade global e local, análise de importância de variáveis, explicações por subgrupos, detecção de anomalias e caracterização de perfis de filas.

Na quarta etapa, condicionada à disponibilidade de dados de oferta ou capacidade, será construído um modelo de simulação de eventos discretos para comparar cenários gerenciais, como redistribuição de capacidade, alteração de regras de priorização, qualificação de encaminhamentos, redução de faltas e mudanças no fluxo de devolução. A avaliação considerará métricas de eficiência e equidade, incluindo tempos de espera, proporção de solicitações acima de limiares, estabilidade da fila, impacto em grupos prioritários e sensibilidade a variações de demanda.

O projeto não propõe substituir decisões clínicas ou regulatórias por decisões automáticas. O foco é apoio à decisão, monitoramento, explicação e análise de cenários para gestores, preservando supervisão humana e governança institucional.

## Resultados esperados

Espera-se produzir um arcabouço computacional para modelar listas de espera como processos dinâmicos, identificar riscos operacionais, explicar gargalos e apoiar análise de cenários. Como resultados científicos, são esperados modelos e protocolos de avaliação reutilizáveis para dados de regulação, evidências sobre a utilidade de validação temporal e explicabilidade nesse domínio, e contribuições metodológicas para aprendizado de máquina aplicado a sistemas públicos de saúde. Como impacto aplicado, o projeto poderá apoiar gestores na leitura de filas, priorização de investigação operacional e planejamento de intervenções, sem automatizar decisões sensíveis de acesso.

## Cronograma resumido

No primeiro ano serão refinados problema, revisão bibliográfica, aprovação ética, modelo de dados e construção do log de eventos. No segundo ano serão desenvolvidos os modelos preditivos, baselines e validações temporais. No terceiro ano serão aprofundadas explicabilidade, análise de gargalos, subgrupos e robustez. No quarto ano serão conduzidas, se viáveis, simulações de cenários, síntese dos resultados, redação de artigos e conclusão da tese.

## Referências

Abuhay, T. M. et al. Machine learning integrated patient flow simulation: why and how? *Journal of Simulation*, 2023.

El-Bouri, R. et al. Machine learning in patient flow: a review. *Machine Learning: Science and Technology*, 2021.

Gadenz, S. D. et al. Telehealth to support referral management in a universal health system: a before-and-after study. *BMC Health Services Research*, 2021.

Giannotti, E. M.; Louvison, M.; Chioro, A. Listas de espera na atenção ambulatorial especializada: reflexões sobre um conceito crítico para o Sistema Único de Saúde. *Cadernos de Saúde Pública*, 2025.

Ministério da Saúde. Modelo de Informação - e-SUS Regulação. 2023.

Ministério da Saúde. Orientações para Gestão da Fila de Espera.

Powers, J. et al. Managing surgical waiting lists through dynamic priority scoring. *Health Care Management Science*, 2023.

Rathnayake, D.; Clarke, M.; Jayasinghe, V. Patient prioritisation methods to shorten waiting times for elective surgery: a systematic review of how to improve access to surgery. *PLOS ONE*, 2021.

Zhang, X. Discrete-event simulation modeling in healthcare: a comprehensive review. *IEEE Access*, 2021.

