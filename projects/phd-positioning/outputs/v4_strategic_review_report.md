# Revisão Estratégica para V4

## Veredito Executivo

O `plano_doutorado_v3.md` está cientificamente sólido e bem defendido contra críticas de escopo, mas ficou ligeiramente excessivo na linguagem de negação: em vários pontos, o texto evita tão fortemente a ideia de sistema, plataforma, implantação ou automação que pode reduzir a percepção de contribuição computacional concreta. Essa cautela foi útil para afastar o risco de parecer um projeto de desenvolvimento de software, mas agora precisa ser recalibrada diante da possibilidade real de acesso a bases estaduais de regulação do SUS.

A V4 deve preservar a tese como **arcabouço computacional baseado em eventos, IA explicável e apoio humano à decisão**, mas substituir parte da linguagem defensiva por uma formulação mais produtiva: o trabalho **não promete implantação operacional**, mas pode desenvolver **protótipos analíticos, dashboards demonstradores, ferramentas de validação e artefatos computacionais experimentais** como meios de avaliar e comunicar o arcabouço.

## A. Trechos Que Restringem Excessivamente Futuras Contribuições

| Trecho no V3 | Problema estratégico | Avaliação |
|---|---|---|
| Linha 17: "não substitui sistemas institucionais, não altera regras de acesso e não realiza priorização autônoma de pacientes" | A frase é correta, mas acumula três negações e pode sugerir que o artefato não terá interface prática com sistemas reais. | Manter o limite ético, mas reformular como camada analítica complementar e acoplável. |
| Linha 25: "sem duplicar a infraestrutura de regulação" | Boa distinção em relação a Cardoso et al., mas poderia explicitar melhor que a proposta pode operar sobre dados/arquiteturas existentes. | Trocar "sem duplicar" por "como camada analítica complementar". |
| Linha 29: "não se propõe uma arquitetura de sistema" | Necessário para diferenciar de Cardoso et al., mas pode soar como recuo excessivo quando o projeto poderia produzir artefatos computacionais avaliáveis. | Reformular para "não se concentra na arquitetura transacional; concentra-se na camada analítica e avaliativa". |
| Linha 54: "sem autorizar, negar ou reordenar automaticamente o acesso" | Restrição importante e deve permanecer. | Manter, mas pode ser formulada como "sem efeito automático sobre decisões de acesso". |
| Linha 56: "sem implantação em produção nem otimização automática da fila" | Correto para controlar escopo, mas fecha espaço para protótipos ou dashboards de validação. | Substituir por "sem pressupor implantação em produção; protótipos podem ser usados como instrumentos experimentais". |
| Linha 66: "A contribuição não será a criação de um novo algoritmo universal, a implantação de uma plataforma nacional..." | Boa defesa contra overclaiming, mas a sucessão de negações enfraquece a ambição computacional. | Reescrever positivamente: contribuição metodológica, avaliativa e instrumental, com protótipos demonstradores quando úteis. |
| Linha 70: "Não se pretende automatizar..., otimizar..., substituir..., construir..., prometer..." | É o ponto mais defensivo do plano. A frase protege escopo, mas pode parecer que o projeto evita qualquer artefato computacional. | Reescrever como delimitação equilibrada: pesquisa retrospectiva, sem entrega operacional obrigatória, mas com possibilidade de demonstradores. |

## B. Redações Alternativas Recomendadas

| Finalidade | Redação alternativa |
|---|---|
| Substituir negações acumuladas na introdução | "O arcabouço é concebido como uma camada analítica complementar e acoplável a arquiteturas de regulação existentes; regras de acesso e decisões regulatórias permanecem sob governança institucional e humana." |
| Diferenciar de Cardoso et al. sem parecer anticódigo | "Em contraste com Cardoso et al. (2026), o foco não é a arquitetura transacional de regulação, mas a camada analítica e avaliativa que pode operar sobre registros produzidos por ecossistemas desse tipo." |
| Permitir protótipos sem prometer produto | "Poderão ser desenvolvidos protótipos analíticos, painéis demonstradores ou ferramentas experimentais para validar, comunicar e avaliar o arcabouço, sem caracterizar implantação operacional." |
| Abrir validação estadual/multi-regional | "Sempre que disponíveis e autorizadas, bases estaduais ou multi-regionais poderão ser usadas para avaliar estabilidade temporal, heterogeneidade entre contextos e adaptabilidade do arcabouço." |
| Abrir Santa Catarina sem promessa | "Bases de Santa Catarina ou de outros estados parceiros poderão ser consideradas conforme disponibilidade institucional, aprovação ética e adequação dos dicionários de dados." |
| Preservar limite ético | "As saídas terão finalidade de apoio humano, auditoria e análise; não produzirão efeito automático sobre autorização, negação ou reordenação do acesso." |

## C. Validação em Bases Estaduais, Multi-Regionais, Santa Catarina ou Outros Estados

O plano deve explicitar essa possibilidade, porque ela fortalece muito a proposta para admissão. A existência potencial de bases estaduais de regulação muda a percepção de viabilidade e ambição científica: o projeto deixa de parecer dependente de uma base local incerta e passa a ter caminho para avaliar heterogeneidade, estabilidade temporal e adaptabilidade do arcabouço.

Recomendação:

- **Incluir "bases estaduais ou multi-regionais" no encaminhamento metodológico.**
- **Mencionar Santa Catarina com cautela**, como possibilidade condicionada, não como promessa: "incluindo eventualmente Santa Catarina ou outros estados parceiros".
- **Evitar afirmar validação nacional ou generalização ampla.**
- **Usar a validação multi-base como oportunidade científica**, não como requisito mínimo.

Formulação ideal:

> "Quando houver acesso institucional e aprovação ética, a validação poderá utilizar bases estaduais ou multi-regionais, incluindo eventualmente Santa Catarina ou outros estados parceiros. Essa possibilidade permitirá avaliar estabilidade temporal, heterogeneidade entre contextos e adaptabilidade do modelo evento-estado-transição, sem transformar a tese em comparação nacional de sistemas de regulação."

## D. Aproximação com o Ecossistema de Cardoso et al. (2026)

Cardoso et al. (2026) deve ser tratado como **oportunidade estratégica**, não ameaça. O artigo demonstra que já existem arquiteturas multi-regionais com interoperabilidade, transparência, monitoramento e acesso para gestores. Isso reforça que:

- há maturidade institucional para dados de regulação;
- o problema não é inventar uma plataforma;
- a lacuna está em extrair, representar, validar e explicar comportamentos a partir dos registros gerados por tais ecossistemas;
- o arcabouço pode ser uma camada analítica sobre arquiteturas existentes.

O plano não deve dizer "não se propõe uma arquitetura" de forma seca. Melhor dizer:

> "Enquanto arquiteturas como a descrita por Cardoso et al. (2026) organizam a infraestrutura transacional, interoperável e de monitoramento, esta proposta investiga a camada computacional analítica: como transformar registros desses ecossistemas em eventos, tarefas, modelos explicáveis e critérios de utilidade operacional."

Essa formulação maximiza aderência ao orientador e às oportunidades reais de dados sem virar extensão da arquitetura de Cardoso et al.

## Risco Se Nada For Alterado

Se o V3 for mantido integralmente, a banca provavelmente ainda o verá como competitivo. O risco não é rejeição por escopo excessivo; o risco é perder pontos de ambição computacional e de alinhamento com uma oportunidade concreta de dados estaduais. O texto atual comunica "não farei plataforma" com força demais e comunica "posso produzir artefatos computacionais úteis para validar a pesquisa" de menos.

## Risco Se Alterar Demais

Se a V4 prometer dashboard operacional, implantação, integração com sistemas estaduais ou transferência tecnológica garantida, a proposta volta a parecer projeto de desenvolvimento de software. Isso prejudicaria a aderência ao PPGCC e aumentaria risco ético/institucional.

## Direção Recomendada para V4

A V4 deve fazer quatro ajustes cirúrgicos:

1. Trocar negações repetidas por linguagem de camada analítica complementar.
2. Abrir espaço para protótipos, dashboards demonstradores e ferramentas experimentais de validação.
3. Explicitar possibilidade de bases estaduais ou multi-regionais, inclusive Santa Catarina quando viável.
4. Reposicionar Cardoso et al. (2026) como infraestrutura/ecossistema sobre o qual a contribuição analítica pode operar, sem duplicar arquitetura.

Com esses ajustes, a proposta fica mais forte para seleção: mais alinhada ao orientador, mais realista em relação ao acesso a dados, mais computacional em termos de artefatos, e ainda conservadora quanto a implantação e automação.

## Controle de Tamanho

A V4 proposta aumenta o corpo do plano de aproximadamente **2.182** para **2.308 palavras**, ou seja, um acréscimo de cerca de **126 palavras** antes das referências. O aumento é estrategicamente justificável porque melhora a aderência às oportunidades reais de dados e à possibilidade de artefatos computacionais demonstradores. Antes de submissão final, caso a V4 substitua a V3, recomenda-se renderizar novamente em DOCX com Times New Roman 12, espaço simples e A4 para confirmar a permanência no limite de quatro páginas sem referências.
