# Reviewer Attack Points

## Achados principais

Os pontos abaixo são vulnerabilidades reais que uma banca pode explorar. Eles estão organizados do mais perigoso para o menos perigoso em termos de impacto sobre a aceitação.

## 1. “Onde está a contribuição nova para Ciência da Computação?”

### Risco

Se o texto ficar muito centrado em hematologia, workflow e integração de dados, um revisor pode concluir que a proposta é uma aplicação bem contextualizada, mas ainda pouco explícita em novidade computacional.

### O que a banca pode dizer

- “Isso parece mais aplicação de IA em laboratório do que pesquisa de doutorado em Computação.”
- “Qual é a pergunta metodológica central além de integrar modalidades?”
- “O que exatamente será proposto em termos de modelagem, e não apenas implementado?”

### Como fortalecer

O texto final precisa nomear com mais firmeza:

- fusão multimodal em nível de caso;
- robustez sob variabilidade laboratorial;
- calibração e incerteza em sistemas multimodais;
- interpretabilidade multimodal orientada à decisão.

O ideal é que a metodologia diga claramente que a contribuição não é só integrar dados, mas **comparar estratégias de fusão e caracterizar quando e por que a multimodalidade agrega valor sob shift de domínio**.

## 2. “Isso não é só uma continuação incremental do mestrado?”

### Risco

A continuidade com o mestrado é uma força, mas também pode ser reinterpretada como incrementalismo se o ganho científico não estiver muito bem explicitado.

### O que a banca pode dizer

- “Você apenas está adicionando CBC ao que já fazia com morfologia.”
- “Qual é o salto de complexidade que justifica doutorado?”

### Como fortalecer

O plano precisa insistir que o salto não é:

- de uma arquitetura para outra;
- de um dataset para outro;
- de mais classes para mais classes.

O salto é:

- de nível celular para nível de caso;
- de unimodal para multimodal;
- de acurácia para confiabilidade e decisão.

Esse ponto deve aparecer de forma frontal, não apenas implícita.

## 3. “Por que multimodalidade é realmente necessária?”

### Risco

Se a proposta não explicitar uma tarefa concreta, a multimodalidade pode parecer apenas “mais dados para tentar melhorar performance”.

### O que a banca pode dizer

- “Por que não basta um bom sistema de morfologia?”
- “Qual decisão laboratorial exige de fato integração?”

### Como fortalecer

A proposta precisa amarrar multimodalidade a **uma ou duas tarefas centrais muito claras**, por exemplo:

- priorização de revisão manual;
- detecção de discordância entre morfologia e analisador;
- identificação de casos suspeitos em nível de triagem.

Sem isso, a multimodalidade fica conceitualmente correta, mas operacionalmente vaga.

## 4. “A viabilidade depende de dados que talvez não estejam bem garantidos”

### Risco

Este é um ponto sensível. O texto fala bem de dados retrospectivos reais, mas não prova que o vínculo entre esfregaço, hemograma, flags e metadados está prontamente acessível e limpo.

### O que a banca pode dizer

- “Os dados realmente existem de forma integrada?”
- “Qual é o custo de curadoria?”
- “Há risco de a tese ficar travada em infraestrutura de dados?”

### Como fortalecer

O plano precisa enfatizar:

- abordagem retrospectiva;
- escopo mínimo de variáveis;
- modularidade do desenho;
- possibilidade de começar com um subconjunto bem definido de casos.

Também ajuda dizer que a tese não depende de um único grande estudo prospectivo.

## 5. “O escopo ainda pode parecer grande demais”

### Risco

Mesmo com as fronteiras já discutidas, ainda há material nas versões atuais que sugere muita coisa ao mesmo tempo: multimodalidade, robustez, interpretabilidade, apoio à decisão, possíveis extensões de raciocínio, domínios morfológicos adicionais.

### O que a banca pode dizer

- “É tese demais para quatro anos e para alguém que trabalha em tempo integral.”
- “Qual é o núcleo exato? Dataset? modelo? robustez? decisão?”

### Como fortalecer

O plano escrito precisa parecer que tem **um núcleo e três desdobramentos**, não cinco teses acopladas.

Núcleo recomendado:

- integração multimodal em nível de caso.

Desdobramentos:

- robustez;
- interpretabilidade;
- apoio à decisão.

Tudo além disso deve parecer secundário e condicional.

## 6. “A metodologia está correta, mas ainda não está suficientemente afiada”

### Risco

As versões atuais descrevem etapas sensatas, mas ainda em um nível um pouco amplo demais para maximizar impacto seletivo.

### O que a banca pode dizer

- “Quais tarefas, exatamente?”
- “Quais comparações serão indispensáveis?”
- “Como saberemos se multimodalidade realmente melhorou algo?”

### Como fortalecer

O texto deve fixar:

- comparação obrigatória entre unimodal imagem, unimodal tabular e multimodal;
- avaliação de robustez/calibração como parte central, não opcional;
- pelo menos um caso de uso laboratorial primário.

## 7. “Há risco de excesso de literatura para pouco espaço”

### Risco

Se o texto mantiver muito estado da arte, o revisor pode sentir que há mais revisão do que projeto.

### O que a banca pode dizer

- “O candidato conhece a literatura, mas onde está o plano?”

### Como fortalecer

No plano final, a literatura deve servir só para provar:

1. morfologia continua relevante;
2. image-only está maduro;
3. multimodalidade em hematologia ainda é pouco consolidada;
4. há sinais de viabilidade translacional.

Qualquer coisa além disso deve sair.

## 8. “Pode soar defensivo demais contra LLM hype”

### Risco

Insistir demais que não é um projeto de LLM pode gerar o efeito contrário: parecer que o texto está respondendo a um problema que ninguém perguntou.

### O que a banca pode dizer

- “Se isso nem é o eixo, por que o texto gasta espaço se defendendo disso?”

### Como fortalecer

Basta uma frase curta de delimitação de escopo. Mais do que isso vira desperdício de página.

## Resposta estratégica final

Para blindar a proposta contra os principais ataques, o texto final deve fazer cinco coisas com extrema clareza:

1. nomear uma contribuição computacional central;
2. explicar o salto do mestrado como mudança de nível inferencial, não de tema;
3. justificar multimodalidade por uma tarefa real;
4. demonstrar viabilidade retrospectiva e modular;
5. conter o escopo com rigor.
