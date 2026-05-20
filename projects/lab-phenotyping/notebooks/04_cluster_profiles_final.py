import pandas as pd
import numpy as np
from scipy.stats import chi2_contingency
import matplotlib.pyplot as plt

# ============================================================
# INPUT
# ============================================================

INPUT = "data/processed/clusters_kmeans_robust_final.csv"

OUTPUT_TABLE_RAW = "/Users/joaokasprowicz/Documents/cardio/outputs/tabelas/cluster_care_setting_raw.csv"
OUTPUT_TABLE_ROW = "/Users/joaokasprowicz/Documents/cardio/outputs/tabelas/cluster_care_setting_row_percent.csv"
OUTPUT_STATS = "/Users/joaokasprowicz/Documents/cardio/outputs/tabelas/cluster_care_setting_stats.csv"
OUTPUT_FIG = "/Users/joaokasprowicz/Documents/cardio/outputs/figuras/cluster_care_setting_stacked_bar.png"

df = pd.read_csv(INPUT)

# ============================================================
# CRIAR CATEGORIA ÉTICA DO CONTEXTO ASSISTENCIAL
# ============================================================

def map_care_setting(x):
    if x == 4:
        return "Emergency-Pediatric"
    elif x in [5, 6]:
        return "Emergency-Adult"
    else:
        return "Outpatient"

df["care_setting"] = df["codigo_da_unidade"].apply(map_care_setting)

# ============================================================
# CHECKS
# ============================================================

print("\n=== DISTRIBUIÇÃO DOS CONTEXTOS ASSISTENCIAIS ===")
print(df["care_setting"].value_counts())
print(df["care_setting"].value_counts(normalize=True))

print("\n=== DISTRIBUIÇÃO DOS CLUSTERS ===")
print(df["cluster"].value_counts())
print(df["cluster"].value_counts(normalize=True))

# ============================================================
# TABELA CLUSTER × CONTEXTO
# ============================================================

ct_raw = pd.crosstab(df["cluster"], df["care_setting"])
ct_row = pd.crosstab(df["cluster"], df["care_setting"], normalize="index") * 100
ct_col = pd.crosstab(df["cluster"], df["care_setting"], normalize="columns") * 100

print("\n=== CLUSTER × CARE SETTING — CONTAGEM ===")
print(ct_raw)

print("\n=== CLUSTER × CARE SETTING — % POR CLUSTER ===")
print(ct_row.round(2))

print("\n=== CLUSTER × CARE SETTING — % POR CONTEXTO ===")
print(ct_col.round(2))

ct_raw.to_csv(OUTPUT_TABLE_RAW)
ct_row.to_csv(OUTPUT_TABLE_ROW)

# ============================================================
# QUI-QUADRADO + CRAMER'S V
# ============================================================

chi2, p, dof, expected = chi2_contingency(ct_raw)

n = ct_raw.values.sum()
cramers_v = np.sqrt(chi2 / (n * (min(ct_raw.shape) - 1)))

stats = pd.DataFrame({
    "chi2": [chi2],
    "dof": [dof],
    "p_value": [p],
    "cramers_v": [cramers_v],
    "n": [n]
})

print("\n=== TESTE DE ASSOCIAÇÃO ===")
print(stats)

stats.to_csv(OUTPUT_STATS, index=False)

# ============================================================
# DISTRIBUIÇÃO POR SEXO
# ============================================================

sex_raw = pd.crosstab(df["cluster"], df["sexo"])
sex_row = pd.crosstab(df["cluster"], df["sexo"], normalize="index") * 100

print("\n=== SEXO POR CLUSTER — CONTAGEM ===")
print(sex_raw)

print("\n=== SEXO POR CLUSTER — % ===")
print(sex_row.round(2))

sex_raw.to_csv("/Users/joaokasprowicz/Documents/cardio/outputs/tabelas/cluster_sex_raw.csv")
sex_row.to_csv("/Users/joaokasprowicz/Documents/cardio/outputs/tabelas/cluster_sex_row_percent.csv")

# ============================================================
# IDADE POR CLUSTER
# ============================================================

def med_iqr(x):
    return f"{x.median():.2f} ({x.quantile(0.25):.2f}-{x.quantile(0.75):.2f})"

idade_cluster = df.groupby("cluster")["idade"].agg(
    n="count",
    median="median",
    q1=lambda x: x.quantile(0.25),
    q3=lambda x: x.quantile(0.75),
    mean="mean",
    std="std"
)

print("\n=== IDADE POR CLUSTER ===")
print(idade_cluster)

idade_cluster.to_csv("/Users/joaokasprowicz/Documents/cardio/outputs/tabelas/cluster_age_summary.csv")

# ============================================================
# PERFIL LABORATORIAL DOS CLUSTERS
# ============================================================

vars_model = [
    "LEUCO",
    "PLAQ",
    "CREATININA",
    "UREIA",
    "PCR",
    "TGO",
    "TGP",
    "idade"
]

vars_model = [v for v in vars_model if v in df.columns]

profile = df.groupby("cluster")[vars_model].agg(med_iqr).T

print("\n=== PERFIL LABORATORIAL DOS CLUSTERS — MEDIANA (IQR) ===")
print(profile)

profile.to_csv("/Users/joaokasprowicz/Documents/cardio/outputs/tabelas/cluster_laboratory_profile.csv")

# ============================================================
# FIGURA — STACKED BAR POR CONTEXTO
# ============================================================

plot_df = pd.crosstab(df["care_setting"], df["cluster"], normalize="index") * 100

ax = plot_df.plot(
    kind="bar",
    stacked=True,
    figsize=(8, 5)
)

plt.ylabel("Proportion of encounters (%)")
plt.xlabel("Care setting")
plt.title("Distribution of laboratory phenotypes across care settings")
plt.legend(title="Cluster", bbox_to_anchor=(1.05, 1), loc="upper left")
plt.tight_layout()
plt.savefig(OUTPUT_FIG, dpi=300)
plt.close()

# ============================================================
# SALVAR DATASET COM CARE_SETTING
# ============================================================

df.to_csv("/Users/joaokasprowicz/Documents/cardio/data/processed/clusters_kmeans_robust_final_with_care_setting.csv", index=False)

print("\nArquivos salvos:")
print(OUTPUT_TABLE_RAW)
print(OUTPUT_TABLE_ROW)
print(OUTPUT_STATS)
print(OUTPUT_FIG)
print("/Users/joaokasprowicz/Documents/cardio/data/processed/clusters_kmeans_robust_final_with_care_setting.csv")