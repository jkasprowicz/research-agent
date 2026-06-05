# Pitch de 10 Minutos

## Objetivo do Pitch

Apresentar a proposta com profundidade suficiente para antecipar críticas sobre novidade, escopo, viabilidade e aderência à Computação, sem transformar a fala em defesa de tese.

## 0:00-0:50 — Abertura

O projeto proposto tem como título **Arcabouço Computacional Baseado em Eventos para Apoio à Decisão Explicável em Sistemas de Regulação do SUS**. Ele está alinhado à linha de Inteligência Computacional e tem como domínio aplicado os fluxos de regulação em saúde pública.

A motivação parte de uma observação simples: muitas vezes chamamos esses sistemas de "filas de espera", mas computacionalmente eles são mais do que listas ordenadas por tempo. Eles são fluxos temporais de eventos, estados, transições, desfechos e restrições operacionais.

## 0:50-1:50 — Motivação e Problema

Em um sistema de regulação, uma solicitação pode ser registrada, devolvida para complementação, priorizada, autorizada, agendada, cancelada, executada ou removida. Cada transição carrega informação sobre o funcionamento do fluxo. Entretanto, essa informação frequentemente aparece de forma fragmentada em registros administrativos, relatórios agregados ou indicadores retrospectivos.

O problema de pesquisa é: **como construir e avaliar um arcabouço computacional baseado em eventos que permita apoiar, de forma explicável e validada temporalmente, a análise de comportamentos problemáticos em fluxos de regulação do SUS?**

Essa formulação é importante porque desloca o foco de "prever tempo de espera" para "representar e avaliar o comportamento do fluxo".

## 1:50-3:00 — Estado da Arte e O Que Já Está Resolvido

A literatura nacional já mostra que listas de espera são centrais para o acesso especializado no SUS. Também há evidências de que centralização de filas, telessaúde, atualização de cadastros e gestão ativa podem reduzir backlog e custos em determinados contextos.

Na literatura computacional, também há avanços relevantes: previsão de tempo de espera, modelos interpretáveis, teoria das filas, simulação e apoio à decisão em saúde. Portanto, a proposta não afirma que esses temas são inéditos.

O posicionamento é conservador: previsão de espera já existe; teoria das filas já é madura; SHAP não é novidade; arquiteturas de regulação já são discutidas; e há trabalhos brasileiros com aprendizado de máquina para priorização em listas específicas.

## 3:00-4:20 — Lacuna Científica

A lacuna está na integração desses componentes em um arcabouço computacional voltado aos fluxos reais de regulação do SUS. Em especial, ainda há espaço para:

- representar solicitações como eventos, estados e transições;
- definir comportamentos problemáticos além do tempo bruto de espera;
- comparar modelos com baselines administrativos;
- validar temporalmente para reduzir vazamento de informação;
- avaliar calibração e estabilidade;
- produzir explicações orientadas ao regulador, e não apenas rankings de variáveis;
- medir utilidade operacional de forma retrospectiva, sem prometer implantação.

A diferença para os competidores diretos é a seguinte. Shin et al. focam previsão interpretável de espera ambulatorial. Gagliotti e Gutierrez focam priorização por machine learning em cirurgia cardíaca. Cardoso et al. tratam arquitetura tecnológica para regulação. Wartelle et al. exploram modelagem de filas em emergência. Minha proposta se posiciona como uma camada analítica complementar: transforma registros regulatórios em tarefas computacionais reprodutíveis e explicáveis.

## 4:20-5:50 — Objetivos

O objetivo geral é desenvolver e avaliar um arcabouço computacional baseado em eventos para representar, identificar e explicar comportamentos problemáticos em fluxos de regulação do SUS, produzindo apoio à decisão humano, auditável e validado temporalmente.

Os objetivos específicos são quatro:

1. Formalizar um modelo de dados baseado em eventos para solicitações, estados, transições, timestamps, especialidades, unidades, prioridades, desfechos e atributos operacionais disponíveis.
2. Definir uma taxonomia computacional de comportamentos problemáticos, com foco em espera excessiva contextualizada, estagnação, saída não resolutiva e risco de gargalo.
3. Construir tarefas analíticas e modelos explicáveis, comparando-os com baselines administrativos, estatísticos e temporais.
4. Avaliar o arcabouço por validação temporal, calibração, análise de erro, robustez, explicabilidade e utilidade operacional retrospectiva.

## 5:50-7:15 — Metodologia

A metodologia será retrospectiva, quantitativa e aplicada. O conjunto mínimo viável é propositalmente enxuto: identificador pseudonimizado da solicitação, datas, status, especialidade ou procedimento e desfecho. Com isso, já é possível derivar trajetórias, tempos entre estados e algumas famílias de comportamento.

A primeira etapa será mapear os registros para um modelo evento-estado-transição, inspirado em logs de eventos e mineração de processos. A segunda será operacionalizar os comportamentos problemáticos:

- espera excessiva contextualizada: permanência acima de limiar por regra local, distribuição histórica ou meta administrativa;
- estagnação: ausência de transição relevante por intervalo definido;
- saída não resolutiva: cancelamento, no-show, exclusão, devolução persistente ou encerramento sem evidência de acesso;
- risco de gargalo: desequilíbrio persistente entre entrada e saída, acúmulo ou deterioração temporal.

Depois, modelos estatísticos e de aprendizado supervisionado serão comparados com baselines como FIFO, prioridade registrada, tempo acumulado, média histórica e regras simples de status.

## 7:15-8:25 — Validação, Explicabilidade e Utilidade

A validação será temporal sempre que possível: períodos de treino, validação e teste separados cronologicamente para reduzir vazamento de informação e aproximar uso prospectivo. A avaliação incluirá discriminação, sensibilidade, especificidade, F1, Brier score, calibração, erro absoluto, métricas de ranking e análise de falsos negativos relevantes.

A explicabilidade será desenhada para o fluxo de regulação. O projeto pode usar SHAP, modelos interpretáveis ou regras, mas o objetivo não é produzir gráficos genéricos. As explicações devem apoiar perguntas como: por que esta solicitação parece estagnada? Por que esta especialidade concentra saídas não resolutivas? Que fatores operacionais aparecem associados a gargalos?

A utilidade operacional será avaliada retrospectivamente: antecedência do sinal, concentração de casos problemáticos nos estratos de risco, estabilidade por período e especialidade, ganho em relação aos baselines e clareza das explicações.

## 8:25-9:20 — Escopo, Ética e Viabilidade

O projeto não promete implantação, não substitui sistemas de regulação, não substitui reguladores e não faz priorização autônoma de pacientes. Essa delimitação é intencional. O doutorado deve produzir um arcabouço cientificamente sólido; implantação exigiria outra etapa de validação, governança e pactuação.

A viabilidade vem da modularidade. Se houver dados mínimos, o núcleo da tese é possível. Se houver dados adicionais, como prioridade, unidade, agenda, capacidade ou variáveis demográficas, as análises podem ser ampliadas. Se algum desfecho não for observável com confiabilidade, ele será tratado como exploratório ou removido do núcleo.

## 9:20-10:00 — Contribuição e Fechamento

A contribuição para Computação é formalizar fluxos de regulação como objetos computacionais reprodutíveis e avaliáveis. O resultado esperado não é um algoritmo universal nem uma plataforma nacional, mas um arcabouço com esquema de eventos, desfechos computáveis, baselines, validação temporal, explicações orientadas ao uso e critérios de utilidade operacional.

Em síntese, a proposta busca transformar a regulação de uma visão de "fila como lista" para uma visão de "fluxo como objeto computacional", permitindo análise explicável, auditável e temporalmente robusta para apoio humano à decisão no SUS.

## Perguntas Que Devem Vir Depois

| Pergunta | Resposta curta |
|---|---|
| Isso é Computação? | Sim: representação por eventos, tarefas computacionais, validação temporal, calibração, XAI e avaliação de apoio à decisão. |
| Qual é a novidade? | A integração reprodutível desses componentes em fluxos reais de regulação do SUS. |
| Vai priorizar pacientes? | Não. O projeto apoia revisão humana e não automatiza acesso. |
| E se os dados forem incompletos? | O núcleo usa dados mínimos; desfechos não confiáveis saem do núcleo. |
| Qual é o maior risco? | Dados. A mitigação é modularidade, escopo mínimo e documentação explícita de qualidade. |
