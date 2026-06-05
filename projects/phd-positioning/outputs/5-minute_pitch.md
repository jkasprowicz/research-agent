# Pitch de 5 Minutos

## Objetivo do Pitch

Transmitir rapidamente que a proposta é:

- claramente de Computação;
- relevante para o SUS sem virar Saúde Pública;
- metodologicamente madura;
- realista;
- consciente das limitações e dos competidores.

## Roteiro Cronometrado

### 0:00-0:40 — Abertura

Minha proposta tem como tema um **arcabouço computacional baseado em eventos para apoio à decisão explicável em sistemas de regulação do SUS**. A ideia central é tratar filas de espera não como listas estáticas ordenadas por tempo, mas como fluxos regulatórios compostos por eventos, estados e transições.

Uma solicitação pode entrar na fila, ser devolvida, complementada, priorizada, autorizada, agendada, cancelada, executada ou removida. Cada mudança de estado contém informação sobre o funcionamento do sistema, mas essa informação costuma ficar dispersa em registros administrativos ou indicadores agregados.

### 0:40-1:30 — Problema Computacional

O problema computacional é transformar esses históricos de regulação em uma representação reprodutível baseada em eventos. A partir dela, o projeto busca definir tarefas analíticas para identificar comportamentos problemáticos como espera excessiva contextualizada, estagnação, saída não resolutiva e risco de gargalo por especialidade ou serviço.

Portanto, a proposta não é simplesmente prever tempo de espera. Também não é propor uma nova arquitetura de regulação, nem automatizar priorização de pacientes. O foco é construir uma camada analítica complementar aos sistemas existentes, capaz de produzir evidências explicáveis para revisão humana.

### 1:30-2:30 — Lacuna e Diferenciação

A literatura mostra que listas de espera e regulação são problemas relevantes no SUS, com estudos sobre centralização de filas, telessaúde, atualização de cadastros e arquiteturas tecnológicas. Na literatura computacional, já existem estudos de previsão de espera, modelos interpretáveis e teoria das filas.

Por isso, a novidade não está em aplicar aprendizado de máquina a mais uma fila. Em relação a Shin et al., a proposta não se limita à previsão interpretável de espera. Em relação a Gagliotti e Gutierrez, não propõe priorização clínica autônoma em uma fila específica. Em relação a Cardoso et al., não propõe uma arquitetura de sistema. Em relação a Wartelle et al., não reivindica contribuição central em simulação de filas.

A lacuna é a integração entre representação por eventos, taxonomia de comportamentos problemáticos, baselines administrativos, validação temporal, calibração, explicabilidade orientada ao usuário e avaliação retrospectiva de utilidade operacional em fluxos de regulação do SUS.

### 2:30-3:40 — Metodologia

A pesquisa será retrospectiva, quantitativa e aplicada, usando registros pseudonimizados de regulação. O conjunto mínimo viável inclui identificador da solicitação, datas, status, especialidade ou procedimento e desfecho. Campos adicionais, como prioridade, unidade solicitante, capacidade, agenda ou variáveis demográficas, serão incorporados quando disponíveis, mas não são condição para o núcleo da tese.

Metodologicamente, a primeira etapa é mapear registros administrativos para um modelo evento-estado-transição. A segunda é definir operacionalmente os quatro comportamentos problemáticos. A terceira é construir tarefas analíticas e comparar modelos com baselines administrativos, como FIFO, prioridade registrada, tempo acumulado e médias históricas. A quarta é validar temporalmente os modelos, avaliar calibração, erro, robustez e explicabilidade.

As explicações serão organizadas em níveis: solicitação individual, fila ou especialidade, unidade ou serviço e visão temporal agregada. A avaliação de utilidade será retrospectiva, considerando antecedência do sinal, ganho sobre baselines, estabilidade temporal e clareza das explicações.

### 3:40-4:30 — Contribuição para Computação

A contribuição para Computação está em formalizar um problema real de decisão como objeto computacional reprodutível. O produto científico esperado é um arcabouço composto por esquema de eventos, taxonomia de desfechos, tarefas analíticas, baselines, protocolo de validação temporal e formatos de explicação.

Isso diferencia o trabalho de uma aplicação local de machine learning. Mesmo que a validação empírica ocorra em bases específicas, os componentes do arcabouço podem ser adaptados a outros sistemas com fluxos administrativos, múltiplos estados, restrições de capacidade e decisões humanas.

### 4:30-5:00 — Fechamento

O projeto é deliberadamente conservador no escopo: não promete implantação, não substitui reguladores e não realiza priorização autônoma. Seu objetivo é criar base computacional robusta, explicável e auditável para compreender comportamentos problemáticos em fluxos de regulação. Essa combinação de modelagem baseada em eventos, inteligência artificial explicável, validação temporal e apoio humano à decisão é o núcleo da proposta para o PPGCC.

## Frase Final se Houver Tempo

Em resumo, a tese propõe sair de uma visão de "fila como lista" para uma visão de "regulação como fluxo computacional de eventos", tornando esse fluxo analisável, validável e explicável.

## Pergunta Mais Provável Após o Pitch

**"Mas onde está exatamente a contribuição de Computação?"**

Resposta curta: Está no arcabouço: representação evento-estado-transição, definição computável de desfechos, comparação com baselines, validação temporal, calibração, explicabilidade e avaliação retrospectiva de utilidade operacional.
