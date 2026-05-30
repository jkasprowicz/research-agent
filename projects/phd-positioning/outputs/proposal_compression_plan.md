# Proposal Compression Plan

## Diagnóstico brutal

O problema das versões atuais não é falta de qualidade científica. É **excesso de argumento para o espaço disponível**.

O texto atual tenta fazer ao mesmo tempo:

- contextualização clínica do domínio;
- defesa da continuidade com o mestrado;
- revisão do estado da arte;
- justificativa da lacuna;
- defesa de relevância para Ciência da Computação;
- defesa de viabilidade;
- descrição metodológica relativamente detalhada;
- estratégia de publicação.

Tudo isso é bom em conteúdo, mas ruim para uma peça de seleção com **4 páginas**.

## O que está repetido

### Ideias repetidas várias vezes

As seguintes ideias aparecem de forma redundante:

1. `image-only está saturado`
2. `morfologia continua importante`
3. `o doutorado é continuação natural do mestrado`
4. `multimodalidade é mais aderente ao laboratório real`
5. `robustez e interpretabilidade são centrais`
6. `não é um projeto genérico de LLM`

Essas seis mensagens devem continuar no texto final, mas **cada uma deveria aparecer uma vez de forma forte**, e não em múltiplas reformulações.

## O que cortar ou fundir

### Em `plano_doutorado_ppgcc_final.md`

#### 1. Introdução + Justificativa

**Problema:** hoje funcionam quase como duas introduções.

**Ação:** fundir logicamente.

Manter:

- 1 parágrafo sobre relevância da morfologia na hematologia;
- 1 parágrafo sobre saturação image-only e necessidade de inferência em nível de caso;
- 1 parágrafo curto sobre continuidade com o mestrado e relevância computacional.

Remover:

- reiterações sobre “não ser mudança artificial” em mais de um ponto;
- explicações longas sobre originalidade do acesso a dados;
- duplicação entre “justificativa científica” e “contextualização”.

#### 2. Fundamentação teórica / estado da arte

**Problema:** é a seção mais superdimensionada.

**Ação:** reduzir agressivamente.

Manter apenas quatro movimentos:

1. morfologia permanece central;
2. literatura image-only é madura/saturada;
3. integração morfologia + hemograma/flags é pouco consolidada;
4. robustez multimodal e apoio à decisão ainda são espaços abertos.

Remover:

- desenvolvimento excessivo sobre cada artigo;
- frases que reexplicam a prática hematológica já dita antes;
- duplicação da crítica ao image-only.

#### 3. Metodologia

**Problema:** está boa, mas detalhada demais para seleção.

**Ação:** preservar a estrutura em quatro blocos, não cinco.

Manter:

1. curadoria retrospectiva da base multimodal;
2. definição das tarefas em nível de caso;
3. comparação entre baselines unimodais e modelos multimodais;
4. avaliação de robustez, calibração, incerteza e interpretabilidade.

Mover para defesa oral:

- detalhes finos sobre consistência temporal;
- enumeração extensa de cenários de variação;
- explicação longa da camada opcional de raciocínio;
- menção detalhada a domínios adicionais como eritrócitos/plaquetas.

#### 4. Resultados esperados

**Problema:** mistura contribuição científica, translacional e estratégia de publicação.

**Ação:** encurtar e deixar mais seletivo.

Manter:

- base multimodal retrospectiva;
- métodos de fusão multimodal;
- evidências de robustez/interpretabilidade;
- 3 ou 4 artigos previstos.

Remover:

- formulações muito descritivas sobre “quatro níveis principais”;
- linguagem excessivamente explicativa.

## O que não contribui diretamente para seleção

Estes conteúdos são bons para conversa oral, mas ocupam espaço demais no texto:

- explicações detalhadas sobre por que LLMs não serão o centro;
- enumeração longa do que está “fora do escopo”;
- justificativa estendida do acesso retrospectivo;
- refinamentos de tarefas secundárias;
- desdobramentos opcionais da tese.

No plano escrito, basta **uma frase de contenção de escopo bem formulada**.

## Alocação ideal por página

### Página 1

Conteúdo exato recomendado:

- Título
- Introdução e contextualização
- Justificativa
- Problema de pesquisa

Objetivo da página:

- convencer rapidamente que o tema é relevante;
- mostrar que o image-only já não é o melhor espaço;
- mostrar que o salto para multimodalidade é natural e maduro.

### Página 2

Conteúdo exato recomendado:

- Objetivos
- Fundamentação teórica / estado da arte

Objetivo da página:

- mostrar claramente a lacuna;
- ancorar a proposta em 6 a 8 referências fortes;
- deixar explícito por que isso é doutorado e não continuação linear simples.

### Página 3

Conteúdo exato recomendado:

- Metodologia

Objetivo da página:

- mostrar execução concreta;
- mostrar desenho modular e retrospectivo;
- mostrar comparação entre unimodal e multimodal;
- mostrar robustez e interpretabilidade como eixo computacional.

### Página 4

Conteúdo exato recomendado:

- Resultados esperados
- Cronograma resumido
- fechamento curto embutido em resultados ou cronograma

Objetivo da página:

- demonstrar viabilidade;
- mostrar foco em publicação;
- encerrar com clareza de contribuição para Ciência da Computação.

## Orçamento de palavras recomendado

- `1. Título`: 10 a 15 palavras
- `2. Introdução e contextualização`: 180 a 220 palavras
- `3. Justificativa`: 180 a 220 palavras
- `4. Problema de pesquisa`: 50 a 70 palavras
- `5. Objetivos`: 120 a 150 palavras
- `6. Fundamentação teórica / estado da arte`: 260 a 330 palavras
- `7. Metodologia`: 300 a 360 palavras
- `8. Resultados esperados`: 120 a 150 palavras
- `9. Cronograma resumido`: 70 a 100 palavras

Meta total:

- **1550 a 1700 palavras**

## Melhor estratégia de fusão entre versões

### Manter de `refined_four_page_plan_v2.md`

- a formulação estratégica central;
- a defesa de que a lacuna está em inferência multimodal em nível de caso;
- a ligação mais forte com o artigo Springer e com a revisão sistemática;
- a defesa clara da contribuição computacional.

### Manter de `plano_doutorado_ppgcc_final.md`

- a organização formal em português;
- a aderência ao formato esperado;
- o cronograma já encaixado;
- a clareza de objetivos e resultados.

### Reescrever

- introdução;
- justificativa;
- fundamentação teórica;
- metodologia.

Essas são as seções onde o ganho de compressão será decisivo.

## Regra final de poda

Se um parágrafo não fizer **uma** destas três coisas, ele deve sair:

1. provar relevância da lacuna;
2. provar maturidade e viabilidade do candidato;
3. provar contribuição clara para Ciência da Computação.

Todo o resto é secundário para seleção.
