import pandas as pd
import matplotlib.pyplot as plt
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
# TABELA
# ============================================================

table_data = []

# Total
table_data.append(["Total de atendimentos", f"{df.shape[0]:,}"])

# Sexo
sexo = df["sexo"].value_counts(normalize=True) * 100

table_data.append([
    "Sexo feminino",
    f"{sexo.get('F',0):.1f}%"
])

table_data.append([
    "Sexo masculino",
    f"{sexo.get('M',0):.1f}%"
])

# Faixa etária
faixa = df["faixa_etaria"].value_counts(normalize=True) * 100

for cat in labels:
    table_data.append([
        f"Faixa etária {cat}",
        f"{faixa.get(cat,0):.1f}%"
    ])

# Variáveis contínuas
vars_cont = [
    "idade",
    "LEUCO",
    "PLAQ",
    "PCR",
    "CREATININA",
    "UREIA",
    "TGO",
    "TGP"
]

for var in vars_cont:

    med = df[var].median()
    q1 = df[var].quantile(0.25)
    q3 = df[var].quantile(0.75)

    table_data.append([
        var,
        f"{med:.2f} ({q1:.2f}-{q3:.2f})"
    ])

# ============================================================
# DATAFRAME FINAL
# ============================================================

table_df = pd.DataFrame(
    table_data,
    columns=["Variável", "Valor"]
)

# salvar csv/excel
table_df.to_csv(
    OUT / "tabela1_coorte.csv",
    index=False
)

table_df.to_excel(
    OUT / "tabela1_coorte.xlsx",
    index=False
)

# ============================================================
# FIGURA TABELA
# ============================================================

fig, ax = plt.subplots(figsize=(8, 10))

ax.axis("off")

table = ax.table(
    cellText=table_df.values,
    colLabels=table_df.columns,
    loc="center",
    cellLoc="left"
)

table.auto_set_font_size(False)
table.set_fontsize(10)
table.scale(1, 1.5)

# header
for (row, col), cell in table.get_celld().items():

    if row == 0:
        cell.set_text_props(weight="bold")
        cell.set_facecolor("#EAEAEA")

plt.title(
    "Tabela 1. Características da coorte",
    fontsize=14,
    weight="bold",
    pad=20
)

plt.tight_layout()

plt.savefig(
    OUT / "tabela1_coorte.png",
    dpi=600,
    bbox_inches="tight"
)

plt.savefig(
    OUT / "tabela1_coorte.pdf",
    bbox_inches="tight"
)

plt.close()

print("Arquivos salvos em:")
print(OUT)