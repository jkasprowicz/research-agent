# 1. Linha de pesquisa, tema e orientador

**Linha de pesquisa:** Inteligência Computacional.  
**Tema pretendido:** modelagem baseada em eventos, inteligência artificial explicável e apoio à decisão em sistemas de regulação em saúde.  
**Orientador indicado:** Jônata Tyska Carvalho.

# 2. Título

**Arcabouço Computacional Baseado em Eventos para Apoio à Decisão Explicável em Sistemas de Regulação do SUS**

# 3. Introdução, motivação e problema de pesquisa

Sistemas de regulação do Sistema Único de Saúde (SUS) organizam o acesso a consultas especializadas, exames, procedimentos e serviços de maior complexidade. Embora frequentemente descritas como "filas de espera", essas estruturas não correspondem apenas a listas ordenadas por tempo. Elas constituem fluxos regulatórios dinâmicos nos quais solicitações são registradas, devolvidas, complementadas, priorizadas, autorizadas, agendadas, canceladas, executadas ou removidas por diferentes motivos. Cada mudança de estado produz informação relevante sobre o funcionamento do sistema, mas essa informação costuma permanecer dispersa em registros administrativos, relatórios agregados ou indicadores retrospectivos.

A literatura brasileira demonstra que a gestão de listas, a centralização de filas, a telessaúde aplicada à regulação, a atualização ativa de cadastros e a organização do acesso podem reduzir backlog, custos e tempos de espera em diferentes contextos do SUS (Gadenz et al., 2021; Pachito et al., 2022; Pazin-Filho et al., 2024; Antunes et al., 2025; Salles et al., 2026). Portanto, a contribuição pretendida não é demonstrar que filas existem, nem propor uma solução administrativa genérica para reduzi-las. O problema computacional é mais específico: transformar históricos de regulação em uma representação baseada em eventos, capaz de caracterizar comportamentos problemáticos da fila e produzir explicações úteis para apoio humano à decisão.

Do ponto de vista da Computação, o domínio de regulação em saúde pode ser tratado como um sistema temporal de eventos, estados, transições, desfechos e restrições operacionais. A proposta parte da premissa de que a ausência de uma representação computacional reprodutível limita a comparação entre modelos, a definição de desfechos, a validação temporal e a utilidade prática de métodos de inteligência artificial. Assim, o artefato central desta pesquisa será um arcabouço computacional para modelar fluxos de regulação, definir tarefas analíticas e avaliar modelos explicáveis orientados a decisão, e não apenas um classificador local de tempo de espera.

O problema de pesquisa consiste em investigar como dados históricos de sistemas de regulação do SUS podem ser representados como eventos, estados e transições para identificar, modelar e explicar comportamentos problemáticos em filas de espera, gerando evidências acionáveis para gestores e reguladores sem automatizar decisões de acesso. A pergunta central é: **como construir e avaliar um arcabouço computacional baseado em eventos que permita apoiar, de forma explicável e validada temporalmente, a análise de comportamentos problemáticos em fluxos de regulação do SUS?**

# 4. Estado da arte e lacuna científica

A literatura sobre listas de espera no SUS já estabeleceu a relevância do problema. Estudos nacionais descrevem listas como componentes críticos da atenção especializada e da equidade no acesso (Giannotti et al., 2025), mostram efeitos de centralização e gestão de filas cirúrgicas (Pazin-Filho et al., 2024), avaliam programas de gestão de acesso em cirurgia cardíaca (Antunes et al., 2025) e evidenciam que listas podem conter demandas obsoletas, inconsistentes ou modificadas ao longo do tempo (Salles et al., 2026). Esses trabalhos sustentam a importância do domínio, mas não resolvem o problema computacional de representar fluxos regulatórios como objetos analisáveis, comparáveis e explicáveis.

Outra linha consolidada envolve regulação remota e telessaúde. Estudos brasileiros sobre gerenciamento de encaminhamentos demonstram redução de filas e custos em sistemas públicos (Gadenz et al., 2021; Pachito et al., 2022; Pfeil et al., 2025). Além disso, arquiteturas tecnológicas recentes para regulação do SUS enfatizam interoperabilidade, monitoramento, transparência e gestão de filas (Cardoso et al., 2026). Esses resultados são fundamentais, mas indicam que a infraestrutura e a gestão de processos não eliminam a necessidade de camadas analíticas capazes de explicar padrões de estagnação, saídas não resolutivas, gargalos por especialidade, inconsistências de dados e riscos operacionais.

Na literatura computacional, previsão de espera, interpretação de modelos e teoria das filas já foram exploradas em saúde. Modelos de aprendizado de máquina podem estimar tempos de espera em emergências e ambulatórios, e abordagens interpretáveis como SHAP foram aplicadas à previsão de espera ambulatorial (Shin et al., 2024; Gloyn et al., 2026). Também há trabalhos de previsão de no-show e tempo de serviço em agendamento (Fall et al., 2025), priorização de cirurgia cardíaca com aprendizado de máquina no Brasil (Gagliotti; Gutierrez, 2025) e avaliação de triagem, simulação ou alocação de recursos por teoria das filas e otimização (Thompson et al., 2024; Wang et al., 2024; Wartelle et al., 2026). Assim, a novidade não está em aplicar aprendizado de máquina, SHAP, teoria das filas ou otimização a um novo conjunto de dados.

A lacuna científica está na integração ainda pouco desenvolvida entre sistemas reais de regulação do SUS e um arcabouço computacional que combine representação baseada em eventos, taxonomia de comportamentos problemáticos, validação temporal, explicabilidade orientada a gestores e avaliação de utilidade operacional. Em outras palavras, permanece em aberto como converter registros administrativos de regulação em tarefas computacionais reprodutíveis e transferíveis, mantendo apoio humano à decisão e evitando tanto a priorização autônoma de pacientes quanto a simples aplicação local de modelos preditivos conhecidos.

# 5. Objetivos

O objetivo geral é desenvolver e avaliar um arcabouço computacional baseado em eventos para representar, identificar e explicar comportamentos problemáticos em fluxos de regulação do SUS, produzindo apoio à decisão de caráter humano, auditável e validado temporalmente.

Os objetivos específicos são:

1. Formalizar um modelo de dados baseado em eventos para sistemas de regulação, incluindo solicitações, estados, transições, timestamps, especialidades, unidades, prioridades, desfechos e atributos operacionais disponíveis.
2. Definir uma taxonomia computacional de comportamentos problemáticos em filas de regulação, com foco inicial em espera excessiva contextualizada, estagnação, saída não resolutiva ou cancelamento/no-show e risco de gargalo por especialidade ou serviço.
3. Construir tarefas analíticas e modelos explicáveis para identificar esses comportamentos, comparando-os com baselines administrativos, estatísticos e temporais.
4. Avaliar o arcabouço por meio de validação temporal, calibração, análise de erro, robustez, explicabilidade, desempenho por subgrupos quando possível e utilidade operacional retrospectiva.

# 6. Encaminhamento metodológico

A pesquisa será conduzida como estudo computacional retrospectivo, quantitativo e aplicado, utilizando registros históricos pseudonimizados de sistemas de regulação, mediante aprovação ética e governança adequada. O escopo inicial será a regulação de acesso a serviços especializados. A unidade básica de análise será a solicitação regulatória e seu histórico de eventos, não apenas o paciente, o tempo de espera agregado ou a posição em uma fila. O conjunto mínimo viável inclui identificador pseudonimizado, datas, status, especialidade ou procedimento e desfecho. Campos adicionais, como prioridade, unidade solicitante, município, motivo de cancelamento, agenda, capacidade, atendimento realizado ou variáveis demográficas, serão incorporados quando disponíveis, sem constituírem pressuposto obrigatório para a primeira etapa.

A primeira etapa será a formalização do artefato computacional. Os registros administrativos serão mapeados para um modelo evento-estado-transição, no qual cada solicitação poderá ter eventos como entrada, devolução, complementação, autorização, agendamento, cancelamento, não comparecimento, execução, exclusão ou retorno. Essa representação permitirá derivar trajetórias, tempos entre estados, padrões de repetição, ausência de atualização, mudanças de prioridade e tipos de saída. O resultado esperado dessa etapa é um esquema analítico documentado, com regras de transformação, variáveis derivadas e critérios de qualidade dos dados.

A segunda etapa consistirá na definição da taxonomia de comportamentos problemáticos. Em vez de tratar tempo de espera como único desfecho, serão definidos desfechos operacionais observáveis e reproduzíveis. O núcleo inicial será composto por: espera excessiva contextualizada por especialidade ou regra local; estagnação por ausência de transição em intervalo relevante; saída não resolutiva, incluindo cancelamento, no-show, exclusão ou ausência de desfecho documentado; e risco de gargalo por concentração de entradas, baixa vazão ou acúmulo persistente em determinado serviço. Quando os dados não permitirem observar algum desfecho com confiabilidade, ele será excluído ou tratado como análise exploratória.

A terceira etapa desenvolverá modelos e baselines. Serão utilizados baselines administrativos, como FIFO, prioridade registrada, tempo acumulado, média histórica por especialidade e regras simples de status. Esses baselines são fundamentais porque a contribuição não será medida apenas por ganho preditivo abstrato, mas pela capacidade de superar critérios administrativos em tarefas operacionalmente relevantes. Modelos estatísticos, temporais e de aprendizado supervisionado serão avaliados conforme a estrutura dos dados, incluindo regressão logística, modelos de sobrevivência, árvores de decisão, florestas aleatórias, gradient boosting e modelos calibrados de risco. A escolha de modelos priorizará auditabilidade, estabilidade temporal e interpretabilidade, não complexidade algorítmica.

A validação será organizada como componente central do arcabouço. Sempre que a série histórica permitir, serão separados períodos de treinamento, validação e teste por janela temporal, reduzindo vazamento de informação e aproximando o cenário prospectivo. As métricas serão selecionadas por tarefa: discriminação, sensibilidade, especificidade, F1, Brier score, calibração, erro absoluto, métricas de ranking, análise de falsos negativos relevantes e desempenho por especialidade, unidade ou subgrupo disponível. A avaliação também examinará estabilidade entre períodos, degradação temporal e sensibilidade a registros ausentes ou inconsistentes.

A explicabilidade será desenhada para o fluxo de regulação. Métodos como SHAP, modelos inerentemente interpretáveis ou explicações baseadas em regras serão usados apenas quando contribuírem para compreender fatores acionáveis. As explicações serão organizadas em níveis complementares: solicitação individual, fila/especialidade, unidade ou serviço e visão temporal agregada. O objetivo é responder quais fatores contribuem para estagnação, saída não resolutiva ou gargalo, e não apenas ranquear variáveis para fins técnicos. As saídas serão concebidas como evidências para revisão humana, priorização de auditoria, atualização de lista, investigação de gargalos e planejamento gerencial, sem autorizar, negar ou reordenar automaticamente o acesso de pacientes.

A avaliação de utilidade operacional será retrospectiva. Serão comparados os sinais produzidos pelo arcabouço com baselines e trajetórias históricas, analisando se os modelos identificariam precocemente filas, serviços ou solicitações com comportamento problemático. Quando houver dados suficientes de capacidade, agenda ou ações gerenciais, poderão ser avaliados cenários retrospectivos simples. Essa etapa terá caráter analítico e experimental, não de implantação em produção nem de otimização automática da fila.

# 7. Contribuições científicas esperadas para a Computação

O artefato computacional central será um arcabouço baseado em eventos para análise de fluxos de regulação, composto por: modelo de dados evento-estado-transição, taxonomia de comportamentos problemáticos, tarefas analíticas, baselines administrativos, protocolo de validação temporal, estratégias de explicabilidade e critérios de avaliação de utilidade operacional.

A contribuição científica para a Computação está em formalizar um problema de decisão em saúde pública como um objeto computacional reprodutível. Diferentemente de uma aplicação local de aprendizado de máquina, o trabalho pretende produzir uma estrutura que permita comparar modelos, definir desfechos, avaliar robustez temporal e gerar explicações ligadas ao fluxo regulatório. A originalidade está na articulação entre modelagem de eventos, inteligência artificial explicável e avaliação de apoio à decisão em sistemas públicos de regulação.

A contribuição transferível será a definição de componentes adaptáveis a diferentes bases de regulação: mapeamento de eventos, família de desfechos, baselines, métricas e formatos de explicação. Mesmo que a validação empírica ocorra em conjuntos de dados específicos, o produto científico não dependerá de uma única instituição ou especialidade. A proposta busca gerar conhecimento reutilizável para sistemas que compartilham características de fluxos administrativos, múltiplos estados, restrições de capacidade, decisões humanas e necessidade de auditabilidade.

A contribuição não será a criação de um novo algoritmo universal, a implantação de uma plataforma nacional ou a substituição de protocolos de acesso. O avanço esperado é metodológico e avaliativo: mostrar como estruturar, validar e explicar modelos de apoio à decisão em regulação de forma temporalmente robusta, auditável e orientada ao uso humano.

# 8. Viabilidade, delimitação de escopo e cronograma sintético

O projeto é delimitado à análise retrospectiva de dados de regulação e ao desenvolvimento de um arcabouço computacional. Não se pretende automatizar priorização de pacientes, otimizar filas em produção, substituir reguladores, construir uma plataforma nacional ou prometer implantação operacional. Também não se assume que previsão de tempo de espera seja o objetivo central; ela poderá ser apenas um dos componentes derivados da análise de eventos.

A viabilidade decorre da modularidade. Com o conjunto mínimo de solicitação, datas, status, especialidade ou procedimento e desfecho, já é possível construir a representação de eventos, caracterizar trajetórias, definir desfechos observáveis, comparar baselines e avaliar modelos iniciais. Dados adicionais permitirão análises mais ricas, mas não serão necessários para sustentar o núcleo científico. A principal mitigação de risco será restringir os desfechos ao que puder ser observado de forma confiável e documentar explicitamente limitações de completude, granularidade e viés histórico.

O cronograma sintético prevê: no primeiro ano, revisão dirigida, submissão ética, análise de dicionários de dados e formalização do modelo evento-estado-transição; no segundo ano, construção da taxonomia, extração de variáveis, definição de baselines e primeiras tarefas analíticas; no terceiro ano, desenvolvimento e validação temporal dos modelos, calibração, explicabilidade e análise de robustez; no quarto ano, avaliação retrospectiva de utilidade operacional, consolidação do arcabouço, redação de artigos e finalização da tese. Essa organização permite publicações intermediárias e preserva coerência mesmo diante de limitações nos dados disponíveis.

# 9. Referências

ANTUNES, S. T.; LIMA, V. A.; SANTOS, I. L.; MIGUEL, R. A.; RIBEIRO, G. C. A.; MENDES, E. T. Impact of management of access to cardiac surgery in the Brazilian Unified Health System at a university hospital in Campinas: pre-post analysis, 2013-2019. *Epidemiologia e Serviços de Saúde*, 2025.

CARDOSO, P. H. et al. Technological architecture for a multi-region solution within the regulation of Brazil's Unified Health System. *Frontiers in Digital Health*, 2026.

FALL, M.; SLAMA, I.; OUAZENE, Y.; TELMOUDI, A. J. Data-driven models for predicting no-show rates and service times in outpatient appointment scheduling. *Proceedings of CoDIT*, 2025.

GADENZ, S. D. et al. Telehealth to support referral management in a universal health system: a before-and-after study. *BMC Health Services Research*, 2021.

GAGLIOTTI, K. Z. O.; GUTIERREZ, M. A. Optimizing Cardiac Surgery Waiting Lists with Machine Learning: a data-driven approach for clinical prioritization. *IEEE Conference Proceedings*, 2025.

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
