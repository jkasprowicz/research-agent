# Resultados

## Descrição da amostra

Foram incluídos 26.414 atendimentos na análise final. A coorte apresentou mediana de idade de 49,50 anos (IQR 30,50-67,90), com 56,7% de atendimentos do sexo feminino e 43,3% do sexo masculino. Houve heterogeneidade importante entre os analitos, com maior disponibilidade relativa para parâmetros hematológicos e menor completude para alguns marcadores bioquímicos, justificando o uso de imputação multivariada após o filtro mínimo de densidade laboratorial.

## Tabela 1

A Tabela 1 apresenta a caracterização demográfica e laboratorial global, bem como a distribuição por sexo e por fenótipo laboratorial na versão analítica final do estudo.

## Completude das variáveis analíticas

No conjunto analítico final, os parâmetros hematológicos apresentaram completude muito alta, com observação direta em `99,1%` dos atendimentos para leucócitos e `99,1%` para plaquetas. Entre os marcadores bioquímicos utilizados no clustering, a creatinina esteve disponível em `90,2%` dos atendimentos, a idade em `87,2%`, a ureia em `83,2%`, a proteína C reativa em `80,9%`, a TGO em `80,3%` e a TGP em `76,0%`. Esses valores indicam que a solução final se apoia majoritariamente em variáveis centrais com boa observação direta, embora parte relevante dos marcadores inflamatórios e hepáticos ainda dependa de imputação em uma fração não desprezível da coorte. O resumo completo de observação e ausência por variável é apresentado na Tabela Suplementar S1.

## Identificação dos fenótipos laboratoriais

A análise por K-means indicou que a solução com três agrupamentos ofereceu o melhor equilíbrio entre separação geométrica e interpretabilidade clínica, com silhueta de 0,29. Na versão final dos materiais, os clusters corresponderam a 5.837 atendimentos (22,1%) no fenótipo inflamatório-renal, 5.029 (19,0%) no fenótipo hepático e 15.548 (58,9%) no fenótipo basal.

## Caracterização dos clusters

Os três agrupamentos apresentaram perfis distintos e clinicamente plausíveis. Em escala laboratorial original (Tabela 2), o fenótipo inflamatório-renal exibiu maior idade mediana (`70,8` anos), creatinina (`1,44`), ureia (`63,24`) e proteína C reativa (`28,87`), além de leucócitos relativamente elevados (`9590`). O fenótipo hepático concentrou as maiores medianas de TGO (`62,2`) e TGP (`52,6`), acompanhadas de menores contagens de leucócitos (`4665`) e plaquetas (`139000`). O fenótipo basal reuniu a maior parcela da amostra, com idade mais baixa (`40,6` anos), menor creatinina (`0,78`), ureia (`29,44`) e transaminases mais discretas, além de plaquetas relativamente mais altas (`258000`). Em conjunto, esses achados sugerem um gradiente entre maior disfunção inflamatório-renal, maior sinal hepatocelular e um perfil laboratorial globalmente menos perturbado.

## Distribuição por sexo

A distribuição por sexo não foi uniforme entre os clusters. O fenótipo inflamatório-renal mostrou maior participação relativa de homens (3.236 de 5.837 atendimentos; aproximadamente `55,4%`), enquanto o fenótipo basal concentrou maior participação relativa de mulheres (9.707 de 15.548 atendimentos; aproximadamente `62,4%`). O fenótipo hepático apresentou distribuição intermediária entre os sexos. Esse padrão sugere que a heterogeneidade laboratorial capturada pelo modelo não se distribui de forma aleatória entre homens e mulheres, reforçando a possibilidade de interação entre carga inflamatória, função renal, idade e composição biológica da coorte.

## Visualização em baixa dimensionalidade

A projeção por UMAP demonstrou separação parcial entre os três grupos, com sobreposição relevante entre regiões adjacentes (Figura 1). O fenótipo basal ocupou a região mais extensa e densa da projeção, ao passo que os fenótipos inflamatório-renal e hepático se distribuíram em áreas mais periféricas. Esse padrão é compatível com heterogeneidade clínica contínua, e não com fronteiras rígidas entre estados fisiopatológicos.

![Figura 1. Projeção UMAP dos fenótipos laboratoriais](../../figures/figure1_umap_clusters_paper_ready.png)

**Figura 1.** Projeção bidimensional por UMAP do espaço latente derivado das oito variáveis utilizadas no clustering. A figura ilustra separação parcial entre os três grupos e sobreposição relevante entre regiões adjacentes, reforçando o caráter contínuo da heterogeneidade clínica observada. Os eixos do UMAP não possuem interpretação clínica direta.

## Associação com contexto assistencial

A distribuição dos clusters variou segundo o contexto assistencial categorizado na versão analítica final. A associação foi estatisticamente significativa (`qui-quadrado=108,3; p<0,001`), porém com tamanho de efeito pequeno (`V de Cramér=0,052`), indicando relação fraca entre as categorias de contexto assistencial e os perfis laboratoriais identificados. Por esse motivo, essa análise deve ser interpretada como descritiva e exploratória, e não como evidência de independência entre essas dimensões.

## Análises de robustez

Nas análises de sensibilidade, a retirada da variável `idade` reduziu a silhueta da solução de três clusters de aproximadamente `0,29` para `0,2427`, indicando contribuição relevante da estrutura etária para a separação geométrica. Ainda assim, o agrupamento inflamatório-renal permaneceu identificável sem idade, preservando o padrão relativo de maior PCR, creatinina e ureia em comparação aos demais grupos. A análise restrita ao primeiro atendimento por paciente mostrou mudança de prevalência entre os fenótipos, com aumento do fenótipo basal de `58,9%` na análise por todos os atendimentos para `63,9%` na análise por primeiro atendimento, acompanhado de redução relativa dos fenótipos inflamatório-renal e hepático. Além disso, o critério `n_exames >= 6` reteve `34,2%` dos atendimentos candidatos, caracterizando a coorte analítica como um subconjunto com maior densidade laboratorial. As tabelas detalhadas da análise sem idade, da comparação entre todos os atendimentos versus primeiro atendimento e da distribuição de intensidade de testagem são apresentadas no material suplementar.
