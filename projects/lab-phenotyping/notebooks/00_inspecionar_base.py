import pandas as pd
from collections import Counter

ARQUIVO = "/Users/joaokasprowicz/Documents/cardio/data/raw/base_laboratorial_consolidada.csv"
CHUNKSIZE = 300_000

contagem_linhas = Counter()
contagem_atendimentos = {}
contagem_pacientes = {}

for i, chunk in enumerate(pd.read_csv(
    ARQUIVO,
    sep=";",
    encoding="utf-8",
    chunksize=CHUNKSIZE,
    low_memory=False
)):
    print(f"Processando chunk {i+1}")

    chunk.columns = chunk.columns.str.strip()

    # usar Nome do Exame (mais robusto globalmente)
    exames = chunk["Nome do Exame"].astype(str)

    # contagem de linhas
    contagem_linhas.update(exames)

    # atendimentos únicos por exame
    grp = chunk.groupby("Nome do Exame")["Número do Atendimento"].nunique()
    for k, v in grp.items():
        contagem_atendimentos[k] = contagem_atendimentos.get(k, 0) + v

    # pacientes únicos por exame (se tiver identificador)
    if "patient_id" in chunk.columns:
        grp_p = chunk.groupby("Nome do Exame")["patient_id"].nunique()
        for k, v in grp_p.items():
            contagem_pacientes[k] = contagem_pacientes.get(k, 0) + v

# ============================================================
# CONVERTER PARA DATAFRAME
# ============================================================

df = pd.DataFrame({
    "exame": list(contagem_linhas.keys()),
    "linhas": list(contagem_linhas.values())
})

df["atendimentos"] = df["exame"].map(contagem_atendimentos)

if contagem_pacientes:
    df["pacientes"] = df["exame"].map(contagem_pacientes)

# ordenar
df = df.sort_values("linhas", ascending=False)

# top 50
top50 = df.head(50)

print("\n=== TOP 50 EXAMES ===")
print(top50)

top50.to_csv("/Users/joaokasprowicz/Documents/cardio/data/processed/top50_exames.csv", index=False)