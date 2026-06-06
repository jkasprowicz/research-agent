# 1. Linha de pesquisa, tema e orientador

**Linha de pesquisa:** Inteligência Computacional.  
**Tema pretendido:** modelagem baseada em eventos, inteligência artificial explicável e apoio à decisão em sistemas de regulação em saúde.  
**Orientador indicado:** Jônata Tyska Carvalho.

# 2. Título

**Arcabouço Computacional Baseado em Eventos para Apoio à Decisão Explicável em Sistemas de Regulação do SUS**

# 3. Introdução, motivação e problema de pesquisa

Esta proposta tem como artefato central um arcabouço computacional baseado em eventos para representar fluxos de regulação do Sistema Único de Saúde (SUS), definir comportamentos problemáticos em filas de espera e avaliar modelos explicáveis de apoio humano à decisão. Sistemas de regulação organizam o acesso a consultas especializadas, exames, procedimentos e serviços de maior complexidade. Embora frequentemente descritas como "filas de espera", essas estruturas não correspondem apenas a listas ordenadas por tempo: são fluxos dinâmicos nos quais solicitações são registradas, devolvidas, complementadas, priorizadas, autorizadas, agendadas, canceladas, executadas ou removidas por diferentes motivos (Giannotti et al., 2025; Pazin-Filho et al., 2024; Cardoso et al., 2026).

A literatura brasileira demonstra que centralização de filas, telessaúde aplicada à regulação, atualização ativa de cadastros e gestão de acesso podem reduzir backlog, custos e tempos de espera em diferentes contextos do SUS (Gadenz et al., 2021; Pachito et al., 2022; Pazin-Filho et al., 2024; Antunes et al., 2025; Salles et al., 2026). Portanto, a contribuição pretendida não é demonstrar que filas existem, nem propor uma solução administrativa genérica para reduzi-las. O problema computacional é mais específico: transformar históricos de regulação em uma representação reprodutível baseada em eventos, capaz de caracterizar comportamentos problemáticos e produzir explicações úteis para reguladores e gestores.

Do ponto de vista da Computação, o domínio de regulação em saúde pode ser tratado como um sistema temporal de eventos, estados, transições, desfechos e restrições operacionais. A modelagem de logs de eventos é consolidada em mineração de processos e já possui aplicações relevantes em saúde (van der Aalst, 2016; Rojas et al., 2016), mas ainda é pouco explorada como base para avaliação explicável de fluxos de regulação do SUS. Assim, o arcabouço é concebido como camada analítica complementar e acoplável a arquiteturas de regulação existentes, mantendo regras de acesso e decisões regulatórias sob governança institucional e humana.

O problema de pesquisa consiste em investigar como dados históricos de sistemas de regulação do SUS podem ser representados como eventos, estados e transições para identificar, modelar e explicar comportamentos problemáticos em filas de espera, gerando evidências acionáveis para apoio humano à decisão. A pergunta central é: **como construir e avaliar um arcabouço computacional baseado em eventos que permita apoiar, de forma explicável e validada temporalmente, a análise de comportamentos problemáticos em fluxos de regulação do SUS?**

# 4. Estado da arte e lacuna científica

A literatura sobre listas de espera no SUS já estabeleceu a relevância do problema. Estudos nacionais descrevem listas como componentes críticos da atenção especializada e da equidade no acesso (Giannotti et al., 2025), mostram efeitos de centralização e gestão de filas cirúrgicas (Pazin-Filho et al., 2024), avaliam programas de gestão de acesso em cirurgia cardíaca (Antunes et al., 2025) e evidenciam que listas podem conter demandas obsoletas, inconsistentes ou modificadas ao longo do tempo (Salles et al., 2026). Esses trabalhos sustentam a importância do domínio, mas não resolvem o problema computacional de representar fluxos regulatórios como objetos analisáveis, comparáveis e explicáveis.

Outra linha consolidada envolve regulação remota, telessaúde e arquitetura de sistemas. Estudos brasileiros sobre gerenciamento de encaminhamentos demonstram redução de filas e custos em sistemas públicos (Gadenz et al., 2021; Pachito et al., 2022; Pfeil et al., 2025). Além disso, arquiteturas tecnológicas recentes para regulação do SUS enfatizam interoperabilidade, monitoramento, transparência, gestão de filas e acesso a informações por gestores e órgãos de controle (Cardoso et al., 2026). Esses resultados indicam uma oportunidade complementar: investigar a camada analítica que pode operar sobre registros produzidos por ecossistemas desse tipo, explicando estagnação, saídas não resolutivas, gargalos por especialidade, inconsistências de dados e riscos operacionais.

Na literatura computacional, previsão de espera, interpretação de modelos e teoria das filas já foram exploradas em saúde. Shin et al. (2024) tratam a previsão interpretável do tempo de espera ambulatorial; Gagliotti e Gutierrez (2025) investigam priorização por aprendizado de máquina em cirurgia cardíaca; Wartelle et al. (2026) aplicam modelagem de filas em emergência; e revisões recentes mostram o crescimento de modelos para espera e fluxo assistencial (Gloyn et al., 2026; Hroub et al., 2025). Portanto, a novidade desta proposta não está em aplicar aprendizado de máquina, SHAP, teoria das filas ou otimização a outro conjunto de dados.

A lacuna científica está na integração ainda pouco desenvolvida entre sistemas reais de regulação do SUS e um arcabouço computacional que combine representação baseada em eventos, taxonomia de comportamentos problemáticos, baselines administrativos, validação temporal, calibração, explicabilidade orientada ao usuário e avaliação retrospectiva de utilidade operacional. Em contraste com Shin et al. (2024), o foco não é apenas prever espera individual; em contraste com Gagliotti e Gutierrez (2025), não se propõe priorização clínica autônoma ou específica de um procedimento; em contraste com Cardoso et al. (2026), o foco não é a arquitetura transacional de regulação, mas a camada analítica e avaliativa que pode operar sobre seus registros; e, em contraste com Wartelle et al. (2026), não se reivindica contribuição central em simulação de filas. O núcleo científico é converter registros regulatórios em tarefas computacionais reprodutíveis e avaliáveis.

# 5. Objetivos

O objetivo geral é desenvolver e avaliar um arcabouço computacional baseado em eventos para representar, identificar e explicar comportamentos problemáticos em fluxos de regulação do SUS, produzindo apoio à decisão de caráter humano, auditável e validado temporalmente.

Os objetivos específicos são:

1. Formalizar um modelo de dados baseado em eventos para sistemas de regulação, incluindo solicitações, estados, transições, timestamps, especialidades, unidades, prioridades, desfechos e atributos operacionais disponíveis.
2. Definir uma taxonomia computacional de comportamentos problemáticos em filas de regulação, com foco inicial em espera excessiva contextualizada, estagnação, saída não resolutiva e risco de gargalo por especialidade ou serviço.
3. Construir tarefas analíticas e modelos explicáveis para identificar esses comportamentos, comparando-os com baselines administrativos, estatísticos e temporais.
4. Avaliar o arcabouço por validação temporal, calibração, análise de erro, robustez, explicabilidade, desempenho por subgrupos quando possível e utilidade operacional retrospectiva.

# 6. Encaminhamento metodológico

A pesquisa será conduzida como estudo computacional retrospectivo, quantitativo e aplicado, utilizando registros históricos pseudonimizados de sistemas de regulação, mediante aprovação ética e governança adequada. Quando houver acesso institucional e aprovação ética, a validação poderá envolver bases estaduais ou de múltiplas regiões, incluindo eventualmente Santa Catarina ou outros estados parceiros; essa possibilidade será tratada como ampliação de robustez e adaptabilidade, não como requisito para o núcleo da tese. A unidade básica de análise será a solicitação regulatória e seu histórico de eventos, não apenas o paciente, o tempo de espera agregado ou a posição em uma fila. O conjunto mínimo viável inclui identificador pseudonimizado, datas, status, especialidade ou procedimento e desfecho. Campos adicionais, como prioridade, unidade solicitante, município, motivo de cancelamento, agenda, capacidade, atendimento realizado ou variáveis demográficas, serão incorporados quando disponíveis.

A primeira etapa será a formalização do artefato computacional. Os registros administrativos serão mapeados para um modelo evento-estado-transição, compatível com princípios de logs de eventos e mineração de processos (van der Aalst, 2016; Rojas et al., 2016). Cada solicitação poderá ter eventos como entrada, devolução, complementação, autorização, agendamento, cancelamento, não comparecimento, execução, exclusão ou retorno. Essa representação permitirá derivar trajetórias, tempos entre estados, padrões de repetição, ausência de atualização, mudanças de prioridade e tipos de saída. O resultado esperado será um esquema analítico documentado, com regras de transformação, variáveis derivadas e critérios de qualidade dos dados.

A segunda etapa consistirá na definição operacional da taxonomia de comportamentos problemáticos. **Espera excessiva contextualizada** será definida como permanência acima de limiares derivados da regra local, da distribuição histórica por especialidade/procedimento ou de metas administrativas explícitas. **Estagnação** corresponderá à ausência de transição relevante por intervalo definido em solicitações ainda ativas. **Saída não resolutiva** incluirá cancelamento, não comparecimento, exclusão, devolução persistente ou encerramento sem evidência de acesso concluído. **Risco de gargalo por especialidade ou serviço** será caracterizado por desequilíbrio persistente entre entrada e saída, crescimento de acúmulo, concentração de solicitações estagnadas ou deterioração temporal dos indicadores. Quando os dados não permitirem observar algum desfecho com confiabilidade, ele será excluído do núcleo ou tratado como análise exploratória.

A terceira etapa desenvolverá modelos e baselines. Serão utilizados baselines administrativos, como FIFO, prioridade registrada, tempo acumulado, média histórica por especialidade e regras simples de status. Esses baselines são fundamentais porque a contribuição não será medida apenas por ganho preditivo abstrato, mas pela capacidade de superar critérios administrativos em tarefas operacionalmente relevantes. Modelos estatísticos, temporais e de aprendizado supervisionado serão avaliados conforme a estrutura dos dados, incluindo regressão logística, modelos de sobrevivência, árvores de decisão, florestas aleatórias, gradient boosting e modelos calibrados de risco. A escolha de modelos priorizará auditabilidade, estabilidade temporal e interpretabilidade, não complexidade algorítmica.

A validação será organizada como componente central do arcabouço. Sempre que a série histórica permitir, serão separados períodos de treinamento, validação e teste por janela temporal, reduzindo vazamento de informação e aproximando o cenário prospectivo. A avaliação seguirá princípios de desenvolvimento e validação de modelos preditivos, com atenção à calibração e à degradação temporal (Steyerberg e Vergouwe, 2014; Van Calster et al., 2019). As métricas serão selecionadas por tarefa: discriminação, sensibilidade, especificidade, F1, Brier score, calibração, erro absoluto, métricas de ranking, análise de falsos negativos relevantes e desempenho por especialidade, unidade, período, base ou subgrupo disponível.

A explicabilidade será desenhada para o fluxo de regulação, seguindo a premissa de que sistemas de IA devem apoiar a interação humano-computador e o contexto decisório, não apenas produzir importância de variáveis (Amershi et al., 2019; Tonekaboni et al., 2019). Métodos como SHAP, modelos inerentemente interpretáveis ou explicações baseadas em regras serão usados apenas quando contribuírem para compreender fatores acionáveis. As explicações serão organizadas em níveis complementares: solicitação individual, fila/especialidade, unidade ou serviço e visão temporal agregada. As saídas terão finalidade de revisão humana, auditoria, atualização de lista, investigação de gargalos e planejamento gerencial, sem efeito automático sobre autorização, negação ou reordenação do acesso.

A avaliação de utilidade operacional será retrospectiva e alinhada à literatura de avaliação de sistemas de apoio à decisão em saúde (Friedman e Wyatt, 2006; Kawamoto et al., 2005). Serão analisados critérios como antecedência do sinal, concentração de casos problemáticos nos estratos de maior risco, ganho em relação a baselines, estabilidade por período/especialidade e clareza das explicações. Como instrumentos experimentais de validação e comunicação científica, poderão ser construídos protótipos analíticos, painéis demonstradores ou ferramentas reprodutíveis, sem pressupor implantação em produção nem otimização automática da fila.

# 7. Contribuições científicas esperadas para a Computação

O artefato computacional central será um arcabouço baseado em eventos para análise de fluxos de regulação, composto por: modelo de dados evento-estado-transição, taxonomia de comportamentos problemáticos, tarefas analíticas, baselines administrativos, protocolo de validação temporal, estratégias de explicabilidade e critérios de avaliação de utilidade operacional.

A contribuição científica para a Computação está em formalizar um problema de decisão em saúde pública como um objeto computacional reprodutível. Diferentemente de uma aplicação local de aprendizado de máquina, o trabalho pretende produzir uma estrutura que permita comparar modelos, definir desfechos, avaliar robustez temporal e gerar explicações ligadas ao fluxo regulatório. A originalidade está na articulação entre modelagem de eventos, inteligência artificial explicável e avaliação de apoio à decisão em sistemas públicos de regulação.

A contribuição potencialmente transferível será a definição de componentes adaptáveis a diferentes bases de regulação: mapeamento de eventos, família de desfechos, baselines, métricas e formatos de explicação. Mesmo que a validação empírica ocorra em conjuntos de dados específicos, o produto científico não dependerá de uma única instituição ou especialidade. A possibilidade de bases estaduais ou de múltiplas regiões permitirá, quando viável, avaliar heterogeneidade entre contextos e estabilidade do arcabouço, preservando a proposta como pesquisa computacional e não como comparação administrativa de sistemas.

A contribuição não depende da criação de um novo algoritmo universal nem da implantação de uma plataforma nacional. O avanço esperado é metodológico, avaliativo e instrumental: mostrar como estruturar, validar e explicar modelos de apoio à decisão em regulação de forma temporalmente robusta, auditável e orientada ao uso humano. Protótipos analíticos, painéis demonstradores ou ferramentas experimentais poderão ser produzidos para validar e comunicar o arcabouço, mas não constituem promessa de produto operacional.

# 8. Viabilidade, delimitação de escopo e cronograma sintético

O projeto é delimitado à análise retrospectiva de dados de regulação e ao desenvolvimento de um arcabouço computacional avaliável. O escopo exclui efeitos automáticos sobre decisões de acesso, substituição de reguladores, implantação obrigatória em produção ou desenvolvimento de plataforma operacional. Ao mesmo tempo, admite a construção de artefatos demonstradores, scripts reprodutíveis ou painéis analíticos como meios de validação científica, documentação metodológica e eventual transferência tecnológica futura. Também não se assume que previsão de tempo de espera seja o objetivo central; ela poderá ser apenas um dos componentes derivados da análise de eventos.

A viabilidade decorre da modularidade. Com o conjunto mínimo de solicitação, datas, status, especialidade ou procedimento e desfecho, já é possível construir a representação de eventos, caracterizar trajetórias, definir desfechos observáveis, comparar baselines e avaliar modelos iniciais. Dados adicionais permitirão análises mais ricas, mas não serão necessários para sustentar o núcleo científico. A principal mitigação de risco será restringir os desfechos ao que puder ser observado de forma confiável e documentar explicitamente limitações de completude, granularidade, heterogeneidade entre bases e viés histórico.

O cronograma sintético prevê: no primeiro ano, revisão dirigida, submissão ética, análise de dicionários de dados e formalização do modelo evento-estado-transição; no segundo ano, construção da taxonomia, extração de variáveis, definição de baselines e primeiras tarefas analíticas; no terceiro ano, desenvolvimento e validação temporal dos modelos, calibração, explicabilidade, análise de robustez e protótipos analíticos de validação quando pertinentes; no quarto ano, avaliação retrospectiva de utilidade operacional, consolidação do arcabouço, redação de artigos e finalização da tese. Essa organização permite publicações intermediárias e preserva coerência mesmo diante de limitações nos dados disponíveis.

# 9. Referências

AMERSHI, S.; WELD, D.; VORVOREANU, M.; FOURNEY, A.; NAIR, S.; COLLOFELLO, J.; SUH, J.; IQBAL, S.; BENNETT, P. N.; INKPEN, K.; TEEVAN, J.; KIKIN-GIL, R.; HORVITZ, E. Guidelines for human-AI interaction. *Proceedings of the CHI Conference on Human Factors in Computing Systems*, 2019.

ANTUNES, S. T.; LIMA, V. A.; SANTOS, I. L.; MIGUEL, R. A.; RIBEIRO, G. C. A.; MENDES, E. T. Impact of management of access to cardiac surgery in the Brazilian Unified Health System at a university hospital in Campinas: pre-post analysis, 2013-2019. *Epidemiologia e Serviços de Saúde*, 2025.

CARDOSO, P. H. et al. Technological architecture for a multi-region solution within the regulation of Brazil's Unified Health System. *Frontiers in Digital Health*, 2026.

FRIEDMAN, C. P.; WYATT, J. C. *Evaluation Methods in Biomedical Informatics*. 2. ed. New York: Springer, 2006.

GADENZ, S. D. et al. Telehealth to support referral management in a universal health system: a before-and-after study. *BMC Health Services Research*, 2021.

GAGLIOTTI, K. Z. O.; GUTIERREZ, M. A. Optimizing Cardiac Surgery Waiting Lists with Machine Learning: a data-driven approach for clinical prioritization. *IEEE Conference Proceedings*, 2025.

GIANNOTTI, E. M.; LOUVISON, M.; CHIORO, A. Listas de espera na atenção ambulatorial especializada: reflexões sobre um conceito crítico para o Sistema Único de Saúde. *Cadernos de Saúde Pública*, 2025.

GLOYN, T. et al. Using artificial intelligence to predict patient wait times in the emergency department: a scoping review. *Artificial Intelligence in Medicine*, 2026.

HROUB, S.; AYOB, M.; ABDULLAH, N. Patient waiting list management: a systematic analysis of current approaches and evidence gaps. *Proceedings of ICEEI*, 2025.

KAWAMOTO, K.; HOULIHAN, C. A.; BALAS, E. A.; LOBACH, D. F. Improving clinical practice using clinical decision support systems: a systematic review of trials to identify features critical to success. *BMJ*, v. 330, p. 765, 2005.

PACHITO, D. V. et al. Micro-costing of a remotely operated referral management system to secondary care in the Unified Health System in Brazil. *Ciência & Saúde Coletiva*, 2022.

PAZIN-FILHO, A. et al. Surgical waiting lists and queue management in a Brazilian tertiary public hospital. *BMC Health Services Research*, 2024.

PFEIL, J. N. et al. Telemedicine gatekeeping over 15,000 patients from specialist consultation waiting lists: a cost-minimization study. *Telemedicine Reports*, 2025.

ROJAS, E.; MUNOZ-GAMA, J.; SEPÚLVEDA, M.; CAPURRO, D. Process mining in healthcare: a literature review. *Journal of Biomedical Informatics*, v. 61, p. 224-236, 2016.

SALLES, T. M. A. et al. Action on waiting list for Speech Therapy in the Unified Health System (SUS) in a medium-sized Brazilian municipality. *CoDAS*, 2026.

SHIN, J.; LEE, D. A.; KIM, J.; LIM, C.; CHOI, B.-K. Dissatisfaction-considered waiting time prediction for outpatients with interpretable machine learning. *Health Care Management Science*, 2024.

STEYERBERG, E. W.; VERGOUWE, Y. Towards better clinical prediction models: seven steps for development and an ABCD for validation. *European Heart Journal*, v. 35, n. 29, p. 1925-1931, 2014.

TONEKABONI, S.; JOSHI, S.; McCRADDEN, M. D.; GOLDENBERG, A. What clinicians want: contextualizing explainable machine learning for clinical end use. *Proceedings of Machine Learning for Healthcare*, 2019.

VAN CALSTER, B. et al. Calibration: the Achilles heel of predictive analytics. *BMC Medicine*, v. 17, 230, 2019.

VAN DER AALST, W. M. P. *Process Mining: Data Science in Action*. 2. ed. Berlin: Springer, 2016.

WARTELLE, A. et al. Data-driven queueing modelling: a simulation case study of emergency department crowding. *BMJ Health Care Informatics*, 2026.
