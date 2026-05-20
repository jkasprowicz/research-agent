import pandas as pd
import numpy as np
from scipy.stats import mannwhitneyu, chi2_contingency
from pathlib import Path

INPUT = "../data/processed/clusters_kmeans_robust_final_with_care_setting.csv"
OUT = Path("../outputs/tabelas")
OUT.mkdir(parents=True, exist_ok=True)

df = pd.read_csv(INPUT)

# ============================================================
# FAIXA ETÁRIA
# ============================================================

bins = [0, 18, 40, 60, 200]
labels = ["<18", "18-39", "40-59", "≥60"]

df["faixa_etaria"] = pd.cut(
    df["idade"],
    bins=bins,
    labels=labels,
    right=False
)

# ============================================================
# FUNÇÕES
# ============================================================

def med_iqr(x):
    x = x.dropna()
    return f"{x.median():.2f} ({x.quantile(0.25):.2f}-{x.quantile(0.75):.2f})"

def n_pct(series, category):
    n = (series == category).sum()
    pct = n / series.notna().sum() * 100
    return f"{n} ({pct:.1f}%)"

def p_mann_whitney(var):
    f = df[df["sexo"] == "F"][var].dropna()
    m = df[df["sexo"] == "M"][var].dropna()
    if len(f) == 0 or len(m) == 0:
        return np.nan
    return mannwhitneyu(f, m, alternative="two-sided").pvalue

def p_chi2(var):
    tab = pd.crosstab(df[var], df["sexo"])
    if tab.shape[0] < 2 or tab.shape[1] < 2:
        return np.nan
    return chi2_contingency(tab)[1]

def format_p(p):
    if pd.isna(p):
        return ""
    if p < 0.001:
        return "<0.001"
    return f"{p:.3f}"

# ============================================================
# TABELA
# ============================================================

rows = []

# N
rows.append([
    "N",
    f"{len(df)}",
    f"{(df['sexo'] == 'F').sum()}",
    f"{(df['sexo'] == 'M').sum()}",
    ""
])

# idade contínua
rows.append([
    "Idade, mediana (IQR)",
    med_iqr(df["idade"]),
    med_iqr(df[df["sexo"] == "F"]["idade"]),
    med_iqr(df[df["sexo"] == "M"]["idade"]),
    format_p(p_mann_whitney("idade"))
])

# faixas etárias
p_age = p_chi2("faixa_etaria")
for cat in labels:
    rows.append([
        f"Faixa etária {cat}, n (%)",
        n_pct(df["faixa_etaria"], cat),
        n_pct(df[df["sexo"] == "F"]["faixa_etaria"], cat),
        n_pct(df[df["sexo"] == "M"]["faixa_etaria"], cat),
        format_p(p_age) if cat == labels[0] else ""
    ])

# exames
vars_lab = [
    "LEUCO",
    "PLAQ",
    "PCR",
    "CREATININA",
    "UREIA",
    "TGO",
    "TGP"
]

for var in vars_lab:
    rows.append([
        f"{var}, mediana (IQR)",
        med_iqr(df[var]),
        med_iqr(df[df["sexo"] == "F"][var]),
        med_iqr(df[df["sexo"] == "M"][var]),
        format_p(p_mann_whitney(var))
    ])

# cluster por sexo
p_cluster = p_chi2("cluster")
for cl in sorted(df["cluster"].dropna().unique()):
    rows.append([
        f"Cluster {cl}, n (%)",
        n_pct(df["cluster"], cl),
        n_pct(df[df["sexo"] == "F"]["cluster"], cl),
        n_pct(df[df["sexo"] == "M"]["cluster"], cl),
        format_p(p_cluster) if cl == sorted(df["cluster"].dropna().unique())[0] else ""
    ])

table = pd.DataFrame(
    rows,
    columns=["Variável", "Total", "Feminino", "Masculino", "p-valor"]
)

# salvar
table.to_csv(OUT / "tabela1_por_sexo.csv", index=False)
table.to_excel(OUT / "tabela1_por_sexo.xlsx", index=False)

print("\n=== TABELA 1 — CARACTERÍSTICAS POR SEXO ===")
print(table.to_string(index=False))

print("\nArquivos salvos:")
print(OUT / "tabela1_por_sexo.csv")
print(OUT / "tabela1_por_sexo.xlsx")