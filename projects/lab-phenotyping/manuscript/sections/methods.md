# Métodos

## Desenho do estudo e fonte de dados

Foi conduzido um estudo retrospectivo observacional com dados laboratoriais provenientes de sistema institucional de informação laboratorial. A base incluiu registros realizados entre janeiro de 2022 e dezembro de 2024. Os dados foram previamente anonimizados e analisados em nível de atendimento clínico.

## Definição da unidade analítica

Cada atendimento foi tratado como unidade independente de análise. Quando havia múltiplas coletas dentro da janela inicial, foi selecionado o maior valor observado para cada variável laboratorial nas primeiras 24 horas após a entrada do atendimento, com o objetivo de representar a maior magnitude de alteração naquele período inicial.

## Variáveis e construção do vetor analítico

A etapa de construção de atributos partiu de um painel laboratorial mais amplo e, na versão analítica final utilizada para clustering, manteve oito variáveis: leucócitos totais, plaquetas, proteína C reativa, creatinina, ureia, TGO, TGP e idade. Sexo e código da unidade foram preservados para caracterização descritiva e análises estratificadas.

## Pré-processamento

Os exames foram padronizados quanto à nomenclatura, unidade e representação numérica. Variáveis hematológicas com escalas divergentes entre registros foram harmonizadas previamente. Atendimentos com menos de seis exames disponíveis no painel candidato foram excluídos antes do clustering. Para os biomarcadores laboratoriais, aplicou-se clipping por intervalo interquartil com `k=3`, seguido de transformação `log1p`. Os dados faltantes foram imputados por `K-nearest neighbors (n_neighbors=5)`, e o conjunto foi posteriormente submetido à padronização robusta por mediana e IQR. Essas etapas buscaram reduzir a influência de assimetria, outliers e incompletude, problemas frequentes em dados laboratoriais do mundo real (Weiskopf & Weng, 2013; Ma et al., 2020; Lewis et al., 2023).

## Análise exploratória da coorte

As variáveis contínuas foram descritas por mediana e intervalo interquartil, e as variáveis categóricas por frequências absolutas e relativas. A coorte foi descrita globalmente e estratificada por sexo. As comparações entre sexos utilizaram o teste de Mann-Whitney para variáveis contínuas e o teste do qui-quadrado de Pearson para variáveis categóricas.

## Clustering e visualização

O agrupamento foi realizado por K-means com `random_state=42`. A seleção do número de clusters considerou a métrica de silhueta para soluções entre dois e seis agrupamentos e a interpretabilidade clínica dos perfis resultantes. A solução final adotou três clusters. Para visualização exploratória, foi utilizada projeção bidimensional por UMAP com `n_neighbors=35`, `min_dist=0,08` e `random_state=42`. Os eixos do UMAP foram interpretados apenas como representação geométrica da estrutura dos dados, sem significado clínico direto (McInnes et al., 2018).

## Contexto assistencial e ética

O contexto assistencial foi derivado do código da unidade e categorizado nos materiais analíticos finais como emergência adulto, emergência pediátrica e ambulatório. A associação entre cluster e contexto assistencial foi avaliada por qui-quadrado e V de Cramér. O estudo utilizou apenas dados secundários anonimizados, sem identificação direta dos pacientes.
