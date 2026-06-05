# Evolução da Proposta: V1 para V2 após o Gap Validation Audit

Referências principais:

- `outputs/plano_doutorado_v1.md`
- `outputs/gap_validation_audit.md`
- `outputs/plano_doutorado_v2.md`

## Síntese da mudança estratégica

A V1 era defensável, mas ainda podia ser lida como uma proposta de "IA explicável para gestão de filas", com risco de parecer aplicação local de aprendizado de máquina, previsão de tempo de espera ou otimização de fila. O `gap_validation_audit.md` mostrou que esses componentes já estão parcialmente resolvidos na literatura.

A V2 reposiciona a proposta como um **arcabouço computacional baseado em eventos para apoio à decisão explicável em sistemas de regulação do SUS**. A contribuição passa a ser a formalização e avaliação de um objeto computacional transferível: modelo evento-estado-transição, taxonomia de comportamentos problemáticos, tarefas analíticas, baselines, validação temporal, explicabilidade e critérios de utilidade operacional.

## Mudanças principais

| Dimensão | V1 | V2 | Razão da mudança |
|---|---|---|---|
| Título | "Apoio à Decisão Baseado em Inteligência Artificial Explicável para Gestão de Filas de Espera..." | "Arcabouço Computacional Baseado em Eventos para Apoio à Decisão Explicável..." | A V1 podia soar como gestão de filas com IA. A V2 explicita o artefato computacional e a modelagem baseada em eventos. |
| Núcleo científico | Modelos de IA explicável para comportamentos problemáticos em filas. | Arcabouço computacional composto por representação de eventos, taxonomia, validação temporal e explicações orientadas a decisão. | O audit indicou que a novidade não pode estar apenas em aplicar ML/XAI. |
| Papel da previsão de tempo de espera | Aparecia como componente importante dentro da motivação e das métricas. | Deixa de ser eixo central e passa a ser possível componente derivado da análise de eventos. | O audit mostrou que previsão de espera já é parcialmente resolvida por Shin et al. e Gloyn et al. |
| Papel da otimização/teoria das filas | Presente como apoio metodológico e cenário complementar. | Tratada com mais cautela, sem reivindicar novidade em queueing, simulação ou otimização. | O audit mostrou que queueing, simulação e otimização já são métodos maduros. |
| Definição de lacuna | "Integração de métodos em sistemas reais de regulação do SUS." | "Ausência de arcabouço reprodutível baseado em eventos para converter registros de regulação em tarefas computacionais explicáveis e temporalmente validadas." | A lacuna ficou mais específica, menos genérica e menos vulnerável a concorrentes. |
| Artefato computacional | Implícito na metodologia. | Definido explicitamente como modelo evento-estado-transição, taxonomia, tarefas, baselines, validação, explicabilidade e avaliação operacional. | Responde à crítica de que poderia ser apenas aplicação local de modelos conhecidos. |
| Desfechos problemáticos | Lista ampla: espera excessiva, estagnação, inconsistência, cancelamento, no-show, retorno, exclusão, gargalo. | Núcleo priorizado: espera excessiva contextualizada, estagnação, saída não resolutiva/cancelamento/no-show e risco de gargalo por especialidade/serviço. | Responde à crítica de que "comportamento problemático" estava amplo demais. |
| Contribuição para Computação | Apresentada como modelagem, predição, explicabilidade e avaliação. | Apresentada como formalização computacional de fluxos de regulação, com componentes transferíveis e protocolo de avaliação. | Fortalece a defesa de que é PhD em Computação, não gestão em saúde. |
| Transferibilidade | Mencionada de forma genérica. | Explicada como adaptação de componentes a diferentes bases: mapeamento de eventos, família de desfechos, baselines, métricas e explicações. | Responde à crítica de que a tese poderia ser apenas estudo local. |
| Concorrentes diretos | Não diferenciava explicitamente Gagliotti/Gutierrez, Shin, Cardoso e trabalhos de queueing. | Cita e delimita esses trabalhos no estado da arte, deixando claro o que já está resolvido e o que permanece aberto. | Evita alegações frágeis de novidade. |
| Escopo | Já evitava implantação e priorização autônoma. | Reforça que não haverá plataforma nacional, otimização em produção, decisão autônoma ou substituição de reguladores. | Mantém segurança ética e viabilidade. |

## Como cada crítica do audit foi endereçada

| Crítica do audit | Validade | Alteração feita na V2 |
|---|---|---|
| "Isso é gestão em saúde com vocabulário de IA." | Parcialmente válida. | O título, introdução, metodologia e seção de contribuições foram reposicionados em torno de artefato computacional, modelagem de eventos, validação temporal e avaliação de DSS. |
| "A literatura já tem previsão de tempo de espera e XAI ambulatorial." | Válida. | A V2 afirma explicitamente que a novidade não está em prever tempo de espera ou usar SHAP, mas em modelar fluxos de regulação e explicar comportamentos problemáticos. |
| "Já existe ML brasileiro para priorização de cirurgia cardíaca." | Válida e séria. | A V2 inclui Gagliotti e Gutierrez como concorrente metodológico e diferencia a proposta por fluxo multiestado, regulação, múltiplos desfechos e apoio humano à decisão. |
| "Teoria das filas, simulação e otimização já são maduras." | Válida. | A V2 remove qualquer pretensão de novidade em queueing/otimização e trata cenário retrospectivo como componente condicional. |
| "A arquitetura de regulação SUS já existe." | Parcialmente válida. | A V2 cita Cardoso et al. e posiciona a tese como camada analítica e avaliativa sobre dados de regulação, não como arquitetura de sistema. |
| "Pode ser apenas aplicação local de modelos conhecidos." | Risco válido. | A V2 define artefato transferível: representação, taxonomia, tarefas, baselines, validação, explicabilidade e métricas. |
| "Dados podem ser insuficientes." | Risco alto. | A V2 explicita o conjunto mínimo viável e torna campos adicionais opcionais. Também prevê excluir desfechos não observáveis com confiabilidade. |
| "Comportamento problemático é amplo demais." | Válida. | A V2 restringe o núcleo inicial a quatro famílias de desfechos. |
| "Apoio à decisão sem implantação pode não provar utilidade." | Parcialmente válida. | A V2 define avaliação retrospectiva de utilidade operacional, comparação com baselines, trajetórias históricas e identificação precoce de problemas. |
| "Pode ser útil, mas não generalizável." | Parcialmente válida. | A V2 separa validação empírica local de contribuição transferível, destacando componentes reutilizáveis em diferentes sistemas de regulação. |

## Mudanças por seção

| Seção | Mudança realizada |
|---|---|
| Linha de pesquisa, tema e orientador | O tema foi ajustado para incluir explicitamente modelagem baseada em eventos, IA explicável e apoio à decisão. |
| Título | O título passou a abrir com "Arcabouço Computacional Baseado em Eventos", deslocando o centro da proposta para Computação. |
| Introdução | A motivação foi reescrita para mostrar que filas são fluxos regulatórios de eventos, não apenas listas ou tempos de espera. |
| Problema de pesquisa | A pergunta central agora enfatiza representação evento-estado-transição, validação temporal e apoio explicável à decisão. |
| Estado da arte | A seção agora reconhece explicitamente o que já está resolvido: gestão de filas, telehealth, arquitetura de regulação, ML de espera, XAI e queueing. |
| Lacuna científica | A lacuna foi estreitada para a ausência de um arcabouço computacional reprodutível e transferível para fluxos de regulação SUS. |
| Objetivos | O objetivo geral agora é desenvolver e avaliar um arcabouço, não apenas métodos de IA. Os objetivos específicos foram reorganizados em formalização, taxonomia, modelagem e avaliação. |
| Metodologia | A metodologia passou a seguir uma sequência computacional: artefato, eventos, taxonomia, baselines, modelos, validação temporal, explicabilidade e avaliação retrospectiva. |
| Contribuições | A seção agora define explicitamente artefato computacional, contribuição científica, contribuição transferível e novidade além de aplicação local. |
| Viabilidade | O escopo foi endurecido: sem plataforma nacional, sem priorização autônoma, sem otimização em produção, sem previsão de espera como objetivo central. |
| Referências | Foi incluído Gagliotti e Gutierrez para reconhecer o concorrente direto em ML para lista de espera cirúrgica no Brasil. |

## O que foi removido ou reduzido

- Redução do framing baseado em "gestão de filas" como promessa ampla.
- Redução da centralidade de "prever tempo de espera".
- Redução do risco de parecer otimização automática de filas.
- Redução da lista ampla de desfechos problemáticos.
- Redução do tom de aplicação genérica de aprendizado de máquina.
- Remoção implícita de qualquer expectativa de implantação operacional.

## O que foi fortalecido

- Artefato computacional explícito.
- Lacuna científica mais defensável.
- Contribuição para Ciência da Computação.
- Transferibilidade além de uma base local.
- Reconhecimento honesto de concorrentes.
- Escopo realista e modular.
- Validação temporal como critério central.
- Explicabilidade orientada a gestores/reguladores, não apenas feature importance.

## Resultado estratégico

A V2 é mais conservadora e cientificamente madura que a V1. Ela troca um enquadramento potencialmente vulnerável, "IA para gestão de filas", por um enquadramento mais forte para PPGCC:

> desenvolvimento e avaliação de um arcabouço computacional baseado em eventos para apoio à decisão explicável em fluxos de regulação do SUS.

Essa mudança reduz a chance de a banca rejeitar a proposta como aplicação local de modelos conhecidos e aumenta a clareza de contribuição em Inteligência Computacional.
