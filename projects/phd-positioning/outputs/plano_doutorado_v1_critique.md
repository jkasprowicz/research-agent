# Crítica da Versão 1 do Plano de Doutorado

Arquivo avaliado: `outputs/plano_doutorado_v1.md`

## 1. Aderência ao edital

| Requisito | Avaliação | Risco |
|---|---|---|
| Estrutura exigida | Atende. O plano contém linha de pesquisa, tema, orientador, título, introdução/motivação/problema, objetivos, estado da arte, metodologia, contribuições para Computação, viabilidade/cronograma e referências. | Baixo. |
| Limite de 4 páginas, referências excluídas | Provavelmente atende. O corpo possui cerca de 2.070 palavras antes das referências, abaixo da meta conservadora de 2.350-2.500 palavras. | Baixo a moderado, pois a confirmação visual depende da renderização final em Word/PDF. |
| Times New Roman 12, espaçamento simples, A4, coluna única, margens 2 cm | Deve ser atendido no `.docx` gerado. | Baixo, se a versão submetida for conferida visualmente antes do envio. |
| Ausência de identificação do candidato | Atende. Não há nome, trajetória pessoal, publicação própria, experiência profissional ou menção a reuniões. | Baixo. |
| Aderência à linha de pesquisa | Forte. A linha `Inteligência Computacional` aparece no início, e o texto enfatiza IA explicável, modelagem temporal, validação e apoio à decisão. | Baixo. |
| Aderência ao tema do orientador | Boa. O plano se posiciona como IA aplicada à saúde e domínio específico, sem depender de operações puramente administrativas. | Baixo a moderado. |

## 2. Nota esperada por critério

| Critério do edital | Nota estimada | Justificativa |
|---|---:|---|
| Aderência aos temas de pesquisa | 9,0/10 | O texto deixa claro o vínculo com Inteligência Computacional, IA explicável, saúde digital e apoio à decisão. A saúde aparece como domínio, não como substituto da contribuição computacional. |
| Metodologia e fundamentação | 8,6/10 | A metodologia é coerente, inclui modelagem baseada em eventos, baselines, validação temporal, calibração e explicabilidade. O principal risco é a ausência de maior detalhe sobre fonte concreta dos dados, inevitável nesta fase. |
| Relevância e viabilidade | 8,8/10 | O problema é relevante para o SUS e o escopo é modular, retrospectivo e sem promessa de implantação. A viabilidade depende de acesso a dados mínimos de regulação. |
| Nota média estimada | 8,8/10 | Plano competitivo para V1, com boa margem para aperfeiçoamento na V2. |

## 3. Pontos fortes

- O plano evita a armadilha de propor apenas “previsão de tempo de espera”, posicionando a tese como apoio à decisão explicável baseado em eventos.
- A contribuição para Computação está explícita: representação de eventos, taxonomia de comportamentos problemáticos, modelos explicáveis, validação temporal e avaliação operacional.
- O texto é conservador em escopo: não promete implantação, escala nacional, priorização autônoma ou substituição de protocolos.
- A metodologia é modular e defensável caso os dados disponíveis sejam incompletos.
- A fundamentação combina evidência nacional do SUS com literatura computacional de filas, simulação, predição e XAI.

## 4. Fragilidades

- A fonte de dados ainda é descrita de modo genérico. Isso protege a anonimização e evita prometer acesso, mas pode levar a banca a questionar exequibilidade.
- A seção metodológica é forte, porém compacta; alguns avaliadores podem querer mais clareza sobre a unidade de análise principal: solicitação, paciente, especialidade, fila ou evento.
- A noção de “comportamento problemático” está bem exemplificada, mas ainda pode parecer ampla. Na V2, pode ser útil priorizar 3 ou 4 desfechos centrais.
- A simulação aparece como componente condicional, corretamente, mas ainda pode ser atacada como escopo adicional. Se houver risco de página, ela pode ser ainda mais reduzida.
- A avaliação por subgrupos é mencionada de forma prudente, mas não há discussão aprofundada sobre viés histórico dos dados. Isso pode aparecer na arguição.

## 5. Pontos de ataque prováveis da banca

| Pergunta provável | Risco | Melhor resposta estratégica |
|---|---|---|
| “Por que isso é Ciência da Computação e não gestão em saúde?” | Alto se a resposta enfatizar impacto SUS demais. | Destacar representação computacional de eventos, modelagem temporal, validação, XAI, calibração, robustez e desenho de apoio à decisão. |
| “Quais dados estarão disponíveis?” | Médio. | Explicar o conjunto mínimo viável: solicitação, datas, status, especialidade/procedimento e desfecho; variáveis adicionais entram como camadas opcionais. |
| “O projeto vai decidir quem passa na frente?” | Médio. | Reforçar que não há priorização autônoma; o sistema produz indicadores e explicações para análise humana. |
| “Isso já não foi resolvido por telemedicina/regulação remota?” | Médio. | Explicar que esses estudos avaliam intervenções, enquanto a proposta modela comportamento dinâmico da fila e gera apoio explicável à decisão. |
| “Por que não basta usar FIFO ou prioridade registrada?” | Médio. | Mostrar que FIFO/prioridade são baselines; o objetivo é identificar risco de estagnação, gargalo, dados inválidos e espera excessiva antes que se tornem invisíveis em indicadores agregados. |
| “Como validar utilidade sem implantação?” | Médio. | Defender validação retrospectiva temporal, comparação com baselines, calibração, análise de erro e cenários retrospectivos, sem promessa de implantação. |
| “O escopo é amplo demais?” | Médio. | Responder que o núcleo é evento + predição explicável + validação temporal; simulação e subgrupos são condicionais à qualidade dos dados. |

## 6. Recomendações para V2

1. Definir uma pergunta central explícita em uma frase destacada, logo após o problema de pesquisa.
2. Reduzir a lista de desfechos centrais para um núcleo mínimo: espera excessiva, estagnação, saída não resolutiva/no-show/cancelamento e gargalo por especialidade.
3. Especificar melhor a unidade de análise: evento de regulação e solicitação em fila, com agregações por especialidade/serviço.
4. Manter simulação apenas como avaliação condicional, sem dar a ela peso de contribuição principal.
5. Inserir uma frase curta sobre governança de dados, pseudonimização e aprovação ética na seção de viabilidade.
6. Conferir visualmente o `.docx` em Word/LibreOffice antes da submissão para confirmar que o corpo termina até a quarta página.
7. Se a V2 precisar ser mais agressiva para seleção, fortalecer a frase de originalidade: “não é previsão isolada de espera, mas um arcabouço explicável e validado temporalmente para apoio à decisão em regulação”.

## 7. Veredito

A V1 é competitiva, madura e segura para a fase de admissão. O principal ganho para a V2 não é adicionar conteúdo, mas tornar ainda mais nítidos o conjunto mínimo de dados, os desfechos centrais e a fronteira entre contribuição computacional e impacto em saúde. O plano já está bem posicionado para evitar os três riscos mais perigosos: parecer gestão em saúde sem Computação, prometer implantação irrealista ou propor priorização autônoma de pacientes.
