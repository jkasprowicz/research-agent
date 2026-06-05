# 1. Linha de pesquisa, tema e orientador

**Linha de pesquisa:** Inteligência Computacional.  
**Tema pretendido:** aplicação e desenvolvimento de métodos de inteligência artificial explicável para apoio à decisão em sistemas de regulação em saúde.  
**Orientador indicado:** Jônata Tyska Carvalho.

# 2. Título

**Apoio à Decisão Baseado em Inteligência Artificial Explicável para Gestão de Filas de Espera em Sistemas de Regulação do SUS**

# 3. Introdução, motivação e problema de pesquisa

Os sistemas de regulação do Sistema Único de Saúde (SUS) coordenam o acesso de usuários a consultas especializadas, exames, procedimentos e serviços de maior complexidade. Nesse contexto, listas de espera não são apenas registros administrativos: constituem sistemas dinâmicos, nos quais solicitações entram, mudam de estado, recebem prioridades, retornam para ajustes, são autorizadas, agendadas, canceladas, executadas ou removidas por diferentes motivos. A gestão dessas filas afeta o tempo de acesso, a alocação de recursos, a transparência do sistema e a capacidade de resposta dos gestores.

A literatura nacional recente evidencia a relevância do tema para o SUS. Estudos sobre listas cirúrgicas, atenção ambulatorial especializada, regulação de encaminhamentos e atualização de listas mostram que centralização, organização do fluxo, telessaúde e revisão ativa da demanda podem reduzir tempos de espera, custos e acúmulos de solicitações (Gadenz et al., 2021; Pachito et al., 2022; Pazin-Filho et al., 2024; Giannotti et al., 2025; Salles et al., 2026). Ao mesmo tempo, esses estudos indicam que a qualidade dos dados, a heterogeneidade entre especialidades, a ausência de registros completos de saída e a dificuldade de interpretar gargalos permanecem desafios relevantes.

Do ponto de vista da Computação, esse cenário pode ser tratado como um problema de modelagem de eventos, predição temporal, explicabilidade e apoio à decisão. Métodos de aprendizado de máquina já foram aplicados à previsão de tempos de espera e de padrões de atendimento em saúde (Shin et al., 2024; Gloyn et al., 2026), enquanto modelos de filas, simulação e otimização têm sido usados para avaliar capacidade, atrasos e cenários operacionais (Thompson et al., 2024; Wartelle et al., 2026). Entretanto, ainda é pouco explorada a integração desses métodos em sistemas reais de regulação do SUS, com foco em explicações acionáveis para gestores e sem substituir a decisão humana.

O problema de pesquisa consiste em investigar como dados históricos de sistemas de regulação podem ser modelados para identificar, prever e explicar comportamentos problemáticos em filas de espera, produzindo evidências acionáveis para apoio à decisão gerencial sem automatizar decisões de acesso. A hipótese central é que uma representação baseada em eventos, combinada a modelos preditivos explicáveis e validação temporal, pode revelar riscos de estagnação, espera excessiva, inconsistência cadastral, cancelamento, no-show, retorno ou gargalo de capacidade de modo mais útil do que indicadores agregados tradicionais.

# 4. Estado da arte e lacuna científica

As listas de espera em saúde têm sido estudadas sob diferentes perspectivas. No contexto brasileiro, há evidências de que a gestão centralizada de filas cirúrgicas pode reduzir backlog e tempo mediano de espera (Pazin-Filho et al., 2024), e que programas de gestão de acesso podem diminuir o tempo para cirurgia cardíaca no SUS (Antunes et al., 2025). Estudos em atenção especializada discutem as listas como conceito crítico para a organização do SUS e para a equidade no acesso (Giannotti et al., 2025). Em serviços específicos, como fonoaudiologia e saúde bucal especializada, observa-se que a atualização de dados, a relação entre atenção primária e especializada e a estrutura dos serviços influenciam diretamente o tempo de acesso (Cavalcanti et al., 2022; De-Carli et al., 2023; Salles et al., 2026).

Outra linha de evidência envolve o gerenciamento de encaminhamentos. Estratégias de telessaúde e regulação remota demonstraram impacto na redução de listas de espera e de custos em sistemas públicos brasileiros (Gadenz et al., 2021; Pachito et al., 2022; Pfeil et al., 2025). Esses estudos reforçam que parte da demanda especializada pode ser organizada, redirecionada ou resolvida por processos regulatórios mais qualificados. Contudo, a maior parte dessa literatura avalia intervenções organizacionais retrospectivamente, sem propor modelos preditivos explicáveis que apoiem a identificação antecipada de comportamentos problemáticos da fila.

Na literatura computacional, métodos de inteligência artificial têm sido aplicados à previsão de espera em departamentos de emergência, ambulatórios e sistemas de agendamento. Revisões recentes indicam que modelos de aprendizado de máquina podem superar estimativas simples baseadas em médias móveis (Gloyn et al., 2026). Abordagens explicáveis, como SHAP, já foram usadas para interpretar fatores associados ao tempo de espera ambulatorial, incluindo tamanho da fila, características do atendimento e variáveis temporais (Shin et al., 2024). Também há estudos sobre previsão de no-show e tempo de serviço em agendamento ambulatorial (Fall et al., 2025). Ainda assim, muitas abordagens concentram-se em desempenho preditivo, sem avaliar suficientemente utilidade operacional, calibração temporal, equidade ou integração com fluxos reais de decisão.

Modelos de teoria das filas, simulação e apoio à decisão complementam essa discussão ao representar relações entre chegada, capacidade, serviço e atraso. Trabalhos recentes avaliam impacto de algoritmos de triagem sobre tempo de espera, modelagem de crowding em emergência e alocação de recursos em redes públicas de saúde (Thompson et al., 2024; Wang et al., 2024; Wartelle et al., 2026). Porém, essas abordagens ainda são pouco adaptadas aos dados, estados e decisões típicos de sistemas de regulação do SUS. A lacuna científica, portanto, não está em demonstrar que filas existem ou que modelos preditivos são possíveis, mas em construir uma abordagem computacional explicável, validada temporalmente e orientada a eventos para apoiar a gestão de filas de espera em regulação pública.

# 5. Objetivos

O objetivo geral é desenvolver e avaliar métodos de inteligência artificial explicável para modelar comportamentos problemáticos em filas de espera de sistemas de regulação do SUS, produzindo indicadores e explicações que apoiem a tomada de decisão gerencial.

Os objetivos específicos são:

1. Modelar dados históricos de regulação como eventos, estados e transições de filas de espera, definindo uma representação computacional adequada para solicitações, prioridades, especialidades, unidades, datas, status e desfechos.
2. Definir e caracterizar desfechos operacionais de comportamento problemático, como espera excessiva, estagnação, inconsistência cadastral, cancelamento, no-show, retorno, exclusão ou risco de gargalo.
3. Desenvolver e validar modelos preditivos explicáveis para identificar esses comportamentos, comparando-os com baselines simples e modelos estatísticos ou temporais.
4. Avaliar desempenho, calibração, robustez, explicabilidade e, quando os dados permitirem, diferenças entre subgrupos e cenários operacionais relevantes para apoio à decisão.

# 6. Encaminhamento metodológico

A pesquisa será conduzida como estudo computacional retrospectivo, quantitativo e aplicado, baseado em registros históricos pseudonimizados de sistemas de regulação. O domínio inicial será a regulação de acesso a serviços especializados, com escopo delimitado a um ou mais conjuntos de dados retrospectivos que contenham solicitações, especialidades ou procedimentos, datas, status e desfechos. A proposta não pressupõe implantação em produção nem tomada autônoma de decisões; os modelos serão concebidos como instrumentos de análise, explicação e apoio humano à decisão.

A primeira etapa consistirá na construção de um modelo de dados baseado em eventos. Cada solicitação será representada por identificador pseudonimizado, data de entrada, tipo de serviço, especialidade ou procedimento, prioridade ou risco quando disponível, unidade solicitante, unidade executante, município ou região, histórico de status e desfecho final. Sempre que existirem registros longitudinais, serão modeladas transições como entrada na fila, autorização, devolução, agendamento, cancelamento, não comparecimento, execução, exclusão ou retorno para complementação. Essa etapa permitirá transformar registros administrativos heterogêneos em uma estrutura analítica adequada a tarefas preditivas e explicáveis.

Na segunda etapa, serão definidos desfechos operacionais de interesse. Exemplos incluem espera superior a limiares definidos por especialidade, estagnação por ausência de mudança de status, alto risco de no-show ou cancelamento, indicação de demanda obsoleta, retorno recorrente, ausência de desfecho documentado e concentração de solicitações em filas com baixa vazão. A definição desses desfechos considerará tanto a literatura quanto a disponibilidade real dos campos. Quando não houver variáveis suficientes para determinado desfecho, a análise será restringida aos comportamentos observáveis de modo reprodutível.

Na etapa de modelagem, serão avaliados baselines simples, como regras baseadas em tempo de espera, prioridade e histórico da especialidade, além de modelos estatísticos e de aprendizado supervisionado. Conforme a estrutura dos dados, poderão ser utilizados regressão logística, modelos de sobrevivência, árvores de decisão, florestas aleatórias, gradient boosting e modelos calibrados para risco temporal. A escolha final dos modelos será guiada por desempenho, interpretabilidade, robustez e adequação ao uso em apoio à decisão. O objetivo não será maximizar complexidade algorítmica, mas produzir modelos confiáveis, auditáveis e compreensíveis para o domínio.

A validação será preferencialmente temporal, separando períodos de treinamento, validação e teste para reduzir vazamento de informação e aproximar o uso prospectivo. Serão comparados modelos com baselines administrativos, como FIFO, prioridade registrada, tempo acumulado na fila e médias históricas por especialidade. As métricas incluirão, conforme o tipo de tarefa, AUC, sensibilidade, especificidade, F1, Brier score, calibração, erro absoluto médio, medidas de ranking e análise de desempenho por especialidade ou serviço. Será dada atenção a casos de erro operacionalmente relevantes, como falsos negativos em situações de risco de espera excessiva.

A explicabilidade será tratada como componente central. Serão investigadas explicações globais e locais para identificar fatores associados a comportamentos problemáticos, tais como tempo acumulado, especialidade, status, histórico de devoluções, prioridade, origem da solicitação, sazonalidade e vazão da fila. Métodos como SHAP ou alternativas interpretáveis serão usados quando compatíveis com o modelo adotado. As explicações serão organizadas em formato voltado a gestores, indicando fatores acionáveis, incerteza e limitações. O sistema proposto será concebido como apoio à decisão e análise retrospectiva ou prospectiva de risco, não como mecanismo autônomo de priorização ou autorização de acesso.

Como avaliação complementar, serão analisadas diferenças de desempenho e de espera entre subgrupos quando existirem variáveis adequadas e eticamente utilizáveis, como região, unidade solicitante, especialidade, idade ou prioridade. Caso estejam disponíveis dados de capacidade, agenda ou volume de atendimento, serão avaliados cenários retrospectivos simples, como aumento de capacidade, revisão ativa de listas, priorização de atualização cadastral ou redirecionamento regulatório. Essa etapa será condicionada à disponibilidade dos dados e terá caráter de simulação de apoio à decisão, sem promessa de implantação operacional.

# 7. Contribuições científicas esperadas para a Computação

As contribuições esperadas concentram-se em Computação, tendo a saúde como domínio de aplicação. A primeira contribuição é uma representação baseada em eventos para filas de espera em sistemas de regulação, capaz de organizar estados, transições, desfechos e atributos operacionais de modo adequado à análise temporal. A segunda é uma taxonomia computacional de comportamentos problemáticos em filas, diferenciando espera excessiva, estagnação, inconsistência, cancelamento, no-show, retorno, demanda obsoleta e gargalos de vazão.

A terceira contribuição é o desenvolvimento e a validação de modelos preditivos explicáveis para dados operacionais de regulação, com comparação a baselines administrativos e validação temporal. A quarta contribuição é uma estratégia de explicabilidade voltada a gestores, conectando fatores preditivos a possíveis ações humanas, sem automatizar decisões de acesso. A quinta contribuição é um conjunto de critérios de avaliação para apoio à decisão em filas de saúde pública, combinando desempenho preditivo, calibração, robustez, interpretabilidade, análise de subgrupos e utilidade operacional.

Com isso, a proposta busca avançar a área de Inteligência Computacional aplicada à saúde ao integrar modelagem de eventos, aprendizado de máquina explicável, validação temporal e apoio à decisão em um domínio público real, complexo e socialmente relevante.

# 8. Viabilidade, delimitação de escopo e cronograma sintético

O projeto é delimitado à análise computacional de dados retrospectivos de sistemas de regulação e atenção especializada. Não se pretende desenvolver uma plataforma nacional, substituir protocolos existentes, automatizar priorização de pacientes ou implantar um sistema em produção. O foco é construir e avaliar métodos generalizáveis de modelagem, predição explicável e apoio à decisão, aplicados a conjuntos de dados disponíveis mediante aprovação ética e governança adequada.

O conjunto mínimo viável inclui registros de solicitações, datas, status, especialidade ou procedimento e desfecho. Com esse núcleo, já é possível caracterizar a dinâmica das filas, definir desfechos, construir baselines e avaliar modelos preditivos. Campos adicionais, como prioridade, município, unidade solicitante, motivo de cancelamento, agenda, capacidade ou variáveis demográficas, permitirão análises mais refinadas, mas não serão pressupostos obrigatórios para a execução inicial. Essa estratégia modular reduz o risco do projeto e permite produção científica mesmo diante de limitações de dados.

O cronograma sintético prevê: no primeiro ano, revisão dirigida, submissão ética, definição do modelo de dados e caracterização inicial; no segundo ano, construção dos desfechos, baselines, modelos preditivos e validação temporal; no terceiro ano, aprofundamento da explicabilidade, análise de subgrupos e simulação retrospectiva condicional à disponibilidade de dados; no quarto ano, consolidação dos resultados, redação de artigos e finalização da tese. A modularidade permite ajustar o escopo conforme a qualidade e granularidade dos dados, preservando a coerência entre objetivos, metodologia e contribuições esperadas.

# 9. Referências

ANTUNES, S. T.; LIMA, V. A.; SANTOS, I. L.; MIGUEL, R. A.; RIBEIRO, G. C. A.; MENDES, E. T. Impact of management of access to cardiac surgery in the Brazilian Unified Health System at a university hospital in Campinas: pre-post analysis, 2013-2019. *Epidemiologia e Serviços de Saúde*, 2025.

CARDOSO, P. H. et al. Technological architecture for a multi-region solution within the regulation of Brazil's Unified Health System. *Frontiers in Digital Health*, 2026.

CAVALCANTI, R. P. et al. Factors associated with the waiting time for access to specialized oral healthcare services in Brazil. *Community Dentistry and Oral Epidemiology*, 2022.

DE-CARLI, A. D. et al. Factors related to the waiting time for scheduling an oral biopsy in Brazil: a multilevel analysis. *BMC Health Services Research*, 2023.

FALL, M.; SLAMA, I.; OUAZENE, Y.; TELMOUDI, A. J. Data-driven models for predicting no-show rates and service times in outpatient appointment scheduling. *Proceedings of CoDIT*, 2025.

GADENZ, S. D. et al. Telehealth to support referral management in a universal health system: a before-and-after study. *BMC Health Services Research*, 2021.

GIANNOTTI, E. M.; LOUVISON, M.; CHIORO, A. Listas de espera na atenção ambulatorial especializada: reflexões sobre um conceito crítico para o Sistema Único de Saúde. *Cadernos de Saúde Pública*, 2025.

GLOYN, T. et al. Using artificial intelligence to predict patient wait times in the emergency department: a scoping review. *Artificial Intelligence in Medicine*, 2026.

HROUB, S.; AYOB, M.; ABDULLAH, N. Patient waiting list management: a systematic analysis of current approaches and evidence gaps. *Proceedings of ICEEI*, 2025.

PACHITO, D. V. et al. Micro-costing of a remotely operated referral management system to secondary care in the Unified Health System in Brazil. *Ciência & Saúde Coletiva*, 2022.

PAZIN-FILHO, A. et al. Surgical waiting lists and queue management in a Brazilian tertiary public hospital. *BMC Health Services Research*, 2024.

PFEIL, J. N. et al. Telemedicine gatekeeping over 15,000 patients from specialist consultation waiting lists: a cost-minimization study. *Telemedicine Reports*, 2025.

SALLES, T. M. A. et al. Action on waiting list for Speech Therapy in the Unified Health System (SUS) in a medium-sized Brazilian municipality. *CoDAS*, 2026.

SHIN, J.; LEE, D. A.; KIM, J.; LIM, C.; CHOI, B.-K. Dissatisfaction-considered waiting time prediction for outpatients with interpretable machine learning. *Health Care Management Science*, 2024.

THOMPSON, Y. L. E. et al. Applying queueing theory to evaluate wait-time-savings of triage algorithms. *Queueing Systems*, 2024.

WANG, Y. et al. Using queueing models as a decision support tool in allocating point-of-care HIV viral load testing machines in Kisumu County, Kenya. *Health Policy and Planning*, 2024.

WARTELLE, A. et al. Data-driven queueing modelling: a simulation case study of emergency department crowding. *BMJ Health Care Informatics*, 2026.
