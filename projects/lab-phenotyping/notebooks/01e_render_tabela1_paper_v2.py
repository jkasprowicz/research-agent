import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

INPUT = "../outputs/tabelas/tabela1_por_sexo.xlsx"
OUT = Path("../outputs/figuras")
OUT.mkdir(parents=True, exist_ok=True)

df = pd.read_excel(INPUT)

# ============================================================
# LIMPEZA
# ============================================================

df = df.fillna("")
df["p-valor"] = df["p-valor"].astype(str)
df["p-valor"] = df["p-valor"].replace({"nan": "", "NaN": "", "None": ""})

# trocar nome da coluna
df = df.rename(columns={"p-valor": "p"})

# ============================================================
# INSERIR LINHAS DE SEÇÃO
# ============================================================

section_rows = []

new_rows = []

def add_section(title):
    new_rows.append({
        "Variável": title,
        "Total": "",
        "Feminino": "",
        "Masculino": "",
        "p": ""
    })
    section_rows.append(len(new_rows))  # índice visual depois do header

for _, row in df.iterrows():
    var = str(row["Variável"])

    if var == "N":
        add_section("Características gerais")

    if var.startswith("Faixa etária <18"):
        add_section("Distribuição por faixa etária")

    if var.startswith("LEUCO"):
        add_section("Exames laboratoriais")

    if var.startswith("Cluster 0"):
        add_section("Distribuição dos fenótipos laboratoriais")

    new_rows.append(row.to_dict())

df2 = pd.DataFrame(new_rows)

# ============================================================
# RENOMEAR VARIÁVEIS PARA TEXTO MAIS PUBLICÁVEL
# ============================================================

rename_vars = {
    "N": "Atendimentos, n",
    "Idade, mediana (IQR)": "Idade, mediana (IQR)",
    "Faixa etária <18, n (%)": "<18 anos, n (%)",
    "Faixa etária 18-39, n (%)": "18–39 anos, n (%)",
    "Faixa etária 40-59, n (%)": "40–59 anos, n (%)",
    "Faixa etária ≥60, n (%)": "≥60 anos, n (%)",
    "LEUCO, mediana (IQR)": "Leucócitos, mediana (IQR)",
    "PLAQ, mediana (IQR)": "Plaquetas, mediana (IQR)",
    "PCR, mediana (IQR)": "Proteína C reativa, mediana (IQR)",
    "CREATININA, mediana (IQR)": "Creatinina, mediana (IQR)",
    "UREIA, mediana (IQR)": "Ureia, mediana (IQR)",
    "TGO, mediana (IQR)": "AST/TGO, mediana (IQR)",
    "TGP, mediana (IQR)": "ALT/TGP, mediana (IQR)",
    "Cluster 0, n (%)": "Fenótipo 0, n (%)",
    "Cluster 1, n (%)": "Fenótipo 1, n (%)",
    "Cluster 2, n (%)": "Fenótipo 2, n (%)",
}

df2["Variável"] = df2["Variável"].replace(rename_vars)

# ============================================================
# FIGURA
# ============================================================

fig_height = max(8, len(df2) * 0.42)

fig, ax = plt.subplots(figsize=(15, fig_height))
ax.axis("off")

table = ax.table(
    cellText=df2.values,
    colLabels=["Característica", "Total", "Feminino", "Masculino", "p"],
    loc="center",
    cellLoc="left",
    colLoc="center"
)

table.auto_set_font_size(False)
table.set_fontsize(10)
table.scale(1, 1.55)

# ============================================================
# ESTILO
# ============================================================

section_titles = [
    "Características gerais",
    "Distribuição por faixa etária",
    "Exames laboratoriais",
    "Distribuição dos fenótipos laboratoriais"
]

for (row, col), cell in table.get_celld().items():

    cell.set_edgecolor("#D9D9D9")
    cell.set_linewidth(0.4)

    # Header
    if row == 0:
        cell.set_facecolor("#E6E6E6")
        cell.set_text_props(weight="bold", ha="center")
        cell.set_height(0.055)

    # alinhamento
    if row > 0:
        if col == 0:
            cell.set_text_props(ha="left")
        else:
            cell.set_text_props(ha="center")

    # linhas de seção
    if row > 0:
        value = table[(row, 0)].get_text().get_text()
        if value in section_titles:
            for c in range(5):
                table[(row, c)].set_facecolor("#F2F2F2")
                table[(row, c)].set_text_props(weight="bold", ha="left")
                table[(row, c)].set_linewidth(0.6)

    # primeira coluna em negrito, exceto variáveis internas
    if row > 0 and col == 0:
        value = table[(row, 0)].get_text().get_text()
        if value not in section_titles:
            cell.set_text_props(weight="normal", ha="left")

# ============================================================
# TÍTULO E RODAPÉ
# ============================================================

plt.title(
    "Tabela 1. Características demográficas e laboratoriais da coorte estratificadas por sexo",
    fontsize=15,
    weight="bold",
    pad=25
)

fig.text(
    0.02,
    0.015,
    "Dados apresentados como mediana (intervalo interquartil) ou n (%). "
    "p calculado por teste de Mann–Whitney para variáveis contínuas e qui-quadrado para variáveis categóricas.",
    fontsize=9,
    ha="left"
)

plt.tight_layout(rect=[0, 0.04, 1, 0.97])

# ============================================================
# EXPORTAR
# ============================================================

png = OUT / "tabela1_paper_ready_v2.png"
pdf = OUT / "tabela1_paper_ready_v2.pdf"
svg = OUT / "tabela1_paper_ready_v2.svg"

plt.savefig(png, dpi=600, bbox_inches="tight")
plt.savefig(pdf, bbox_inches="tight")
plt.savefig(svg, bbox_inches="tight")

plt.close()

print("Figuras salvas:")
print(png)
print(pdf)
print(svg)