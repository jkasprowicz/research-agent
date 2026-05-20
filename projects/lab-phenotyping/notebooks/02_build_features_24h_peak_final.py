import pandas as pd

INPUT = "/Users/joaokasprowicz/Documents/cardio/data/processed/dataset_laboratorial_expandido.csv"
OUTPUT = "/Users/joaokasprowicz/Documents/cardio/data/processed/features_24h_peak_final.csv"

# ============================================================
# VARIÁVEIS FINAIS (OTIMIZADAS)
# ============================================================

vars_keep = [
    "PCR",
    "LEUCO",
    "PLAQ",

    "CREATININA",
    "UREIA",

    "TGO",
    "TGP",
    "FOSFATASE_ALCALINA",
    "BILIRRUBINA",

    "SODIO",
    "POTASSIO",
    "GLICOSE",

    "LDH",
    "CPK",

    "TAP"
]

# ============================================================
# LOAD
# ============================================================

df = pd.read_csv(INPUT, low_memory=False)

df["data_de_entrada"] = pd.to_datetime(df["data_de_entrada"], errors="coerce")
df["valor_num"] = pd.to_numeric(df["valor_num"], errors="coerce")
df["idade"] = pd.to_numeric(df["idade"], errors="coerce")

df = df.dropna(subset=["data_de_entrada", "valor_num", "numero_do_atendimento"])

# ============================================================
# DEFINIR T0
# ============================================================

t0 = df.groupby("numero_do_atendimento")["data_de_entrada"].min().rename("t0")
df = df.merge(t0, on="numero_do_atendimento", how="left")

df["dt_horas"] = (df["data_de_entrada"] - df["t0"]).dt.total_seconds() / 3600

# ============================================================
# FILTRAR 24H
# ============================================================

df_24h = df[(df["dt_horas"] >= 0) & (df["dt_horas"] <= 24)].copy()

# ============================================================
# FILTRAR EXAMES DE INTERESSE
# ============================================================

df_24h = df_24h[df_24h["exame_padronizado"].isin(vars_keep)].copy()

# ============================================================
# PEAK POR ATENDIMENTO
# ============================================================

peak = (
    df_24h.groupby(
        ["numero_do_atendimento", "exame_padronizado"],
        as_index=False
    )["valor_num"].max()
)

# ============================================================
# PIVOT
# ============================================================

features = peak.pivot_table(
    index="numero_do_atendimento",
    columns="exame_padronizado",
    values="valor_num",
    aggfunc="first"
).reset_index()

# ============================================================
# DEMOGRAFIA
# ============================================================

demo = (
    df_24h.sort_values("data_de_entrada")
    .groupby("numero_do_atendimento", as_index=False)[["idade", "sexo", "codigo_da_unidade"]]
    .first()
)

features = features.merge(demo, on="numero_do_atendimento", how="left")

# ============================================================
# FILTRO DE DENSIDADE (CRÍTICO)
# ============================================================

features["n_exames"] = features[vars_keep].notna().sum(axis=1)

features = features[features["n_exames"] >= 6].copy()

# ============================================================
# SALVAR
# ============================================================

features.to_csv(OUTPUT, index=False)

print("\nFEATURES CRIADAS")
print(features.shape)

print("\nMissing por variável:")
print(features[vars_keep].isna().mean().sort_values())