import pandas as pd

# caminhos RELATIVOS (você está dentro de scripts/)
CLUSTERS = "/Users/joaokasprowicz/Documents/cardio/data/processed/clusters_kmeans_robust_final_with_care_setting.csv"
FEATURES = "/Users/joaokasprowicz/Documents/cardio/data/processed/features_24h_peak_emergency.csv"

df_c = pd.read_csv(CLUSTERS)
df_f = pd.read_csv(FEATURES)

# garantir que não duplica colunas
df_c = df_c[["numero_do_atendimento", "cluster"]]

df = df_c.merge(
    df_f,
    on="numero_do_atendimento",
    how="inner"
)

vars_model = [
    "LEUCO", "PLAQ", "CREATININA", "UREIA",
    "PCR", "TGO", "TGP", "idade"
]

def med_iqr(x):
    return f"{x.median():.2f} ({x.quantile(0.25):.2f}-{x.quantile(0.75):.2f})"

profile = df.groupby("cluster")[vars_model].agg(med_iqr).T

print("\n=== PERFIL FINAL (ESCALA ORIGINAL CORRETA) ===")
print(profile)