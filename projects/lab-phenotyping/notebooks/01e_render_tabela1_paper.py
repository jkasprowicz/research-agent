import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

INPUT = "../outputs/tabelas/tabela1_por_sexo.xlsx"

OUT = Path("../outputs/figuras")
OUT.mkdir(parents=True, exist_ok=True)

df = pd.read_excel(INPUT)

# ============================================================
# FIGURA
# ============================================================

fig_height = max(8, len(df) * 0.42)

fig, ax = plt.subplots(
    figsize=(14, fig_height)
)

ax.axis("off")

table = ax.table(
    cellText=df.values,
    colLabels=df.columns,
    loc="center",
    cellLoc="left",
    colLoc="center"
)

# ============================================================
# ESTILO
# ============================================================

table.auto_set_font_size(False)
table.set_fontsize(10)

table.scale(1, 1.6)

for (row, col), cell in table.get_celld().items():

    # header
    if row == 0:
        cell.set_text_props(weight="bold", color="black")
        cell.set_facecolor("#EAEAEA")
        cell.set_height(0.05)

    # primeira coluna
    if col == 0 and row > 0:
        cell.set_text_props(weight="bold")

    # linhas suaves
    cell.set_edgecolor("#CFCFCF")
    cell.set_linewidth(0.5)

# ============================================================
# TÍTULO
# ============================================================

plt.title(
    "Tabela 1. Características demográficas e laboratoriais da coorte estratificadas por sexo",
    fontsize=16,
    weight="bold",
    pad=30
)

plt.tight_layout()

# ============================================================
# EXPORTAR
# ============================================================

png = OUT / "tabela1_paper_ready.png"
pdf = OUT / "tabela1_paper_ready.pdf"
svg = OUT / "tabela1_paper_ready.svg"

plt.savefig(
    png,
    dpi=600,
    bbox_inches="tight"
)

plt.savefig(
    pdf,
    bbox_inches="tight"
)

plt.savefig(
    svg,
    bbox_inches="tight"
)

plt.close()

print("\nFiguras salvas:")
print(png)
print(pdf)
print(svg)