import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

INPUT = "/Users/joaokasprowicz/Documents/cardio/data/processed/clusters_kmeans_robust_final_with_care_setting.csv"
OUT_DIR = "/Users/joaokasprowicz/Documents/cardio/outputs/figuras"

vars_model = [
    "LEUCO", "PLAQ", "CREATININA", "UREIA",
    "PCR", "TGO", "TGP", "idade"
]

df = pd.read_csv(INPUT)

# ============================================================
# 1. BOXPLOTS POR CLUSTER — ESCALA LOG PARA BIOMARCADORES
# ============================================================

for var in vars_model:
    temp = df[["cluster", var]].dropna().copy()

    if var != "idade":
        temp[var] = np.log1p(temp[var])
        ylabel = f"log1p({var})"
    else:
        ylabel = "idade"

    plt.figure(figsize=(6, 5))
    temp.boxplot(column=var, by="cluster")
    plt.title(f"{var} by cluster")
    plt.suptitle("")
    plt.xlabel("Cluster")
    plt.ylabel(ylabel)
    plt.tight_layout()
    plt.savefig(f"{OUT_DIR}/boxplot_{var}_by_cluster.png", dpi=300)
    plt.close()

# ============================================================
# 2. HEATMAP DE MEDIANAS PADRONIZADAS
# ============================================================

profile = df.groupby("cluster")[vars_model].median()

# log nos biomarcadores para visualização
profile_log = profile.copy()
for var in vars_model:
    if var != "idade":
        profile_log[var] = np.log1p(profile_log[var])

# padronizar por variável
profile_z = (profile_log - profile_log.mean()) / profile_log.std()

plt.figure(figsize=(9, 4))
plt.imshow(profile_z, aspect="auto")
plt.colorbar(label="Standardized median")
plt.xticks(range(len(profile_z.columns)), profile_z.columns, rotation=45, ha="right")
plt.yticks(range(len(profile_z.index)), [f"Cluster {c}" for c in profile_z.index])
plt.title("Standardized laboratory profile by cluster")
plt.tight_layout()
plt.savefig(f"{OUT_DIR}/heatmap_cluster_profiles.png", dpi=300)
plt.close()

# ============================================================
# 3. BARRAS EMPILHADAS — CLUSTER POR CONTEXTO ASSISTENCIAL
# ============================================================

if "care_setting" in df.columns:
    tab = pd.crosstab(df["care_setting"], df["cluster"], normalize="index") * 100

    ax = tab.plot(kind="bar", stacked=True, figsize=(8, 5))
    plt.ylabel("Proportion of encounters (%)")
    plt.xlabel("Care setting")
    plt.title("Distribution of laboratory phenotypes across care settings")
    plt.legend(title="Cluster", bbox_to_anchor=(1.05, 1), loc="upper left")
    plt.tight_layout()
    plt.savefig(f"{OUT_DIR}/stacked_bar_cluster_by_care_setting.png", dpi=300)
    plt.close()

# ============================================================
# 4. BARRAS EMPILHADAS — SEXO POR CLUSTER
# ============================================================

if "sexo" in df.columns:
    tab_sex = pd.crosstab(df["cluster"], df["sexo"], normalize="index") * 100

    ax = tab_sex.plot(kind="bar", stacked=True, figsize=(7, 5))
    plt.ylabel("Proportion (%)")
    plt.xlabel("Cluster")
    plt.title("Sex distribution by cluster")
    plt.legend(title="Sex", bbox_to_anchor=(1.05, 1), loc="upper left")
    plt.tight_layout()
    plt.savefig(f"{OUT_DIR}/stacked_bar_sex_by_cluster.png", dpi=300)
    plt.close()

# ============================================================
# 5. SCATTER CLÍNICO — RENAL VS INFLAMATÓRIO
# ============================================================

plt.figure(figsize=(7, 5))
plt.scatter(
    np.log1p(df["CREATININA"]),
    np.log1p(df["PCR"]),
    c=df["cluster"],
    s=6,
    alpha=0.5
)
plt.xlabel("log1p(CREATININA)")
plt.ylabel("log1p(PCR)")
plt.title("Renal-inflammatory laboratory space")
plt.tight_layout()
plt.savefig(f"{OUT_DIR}/scatter_creatinina_pcr_clusters.png", dpi=300)
plt.close()

# ============================================================
# 6. SCATTER CLÍNICO — HEPÁTICO
# ============================================================

plt.figure(figsize=(7, 5))
plt.scatter(
    np.log1p(df["TGO"]),
    np.log1p(df["TGP"]),
    c=df["cluster"],
    s=6,
    alpha=0.5
)
plt.xlabel("log1p(TGO)")
plt.ylabel("log1p(TGP)")
plt.title("Hepatic laboratory space")
plt.tight_layout()
plt.savefig(f"{OUT_DIR}/scatter_tgo_tgp_clusters.png", dpi=300)
plt.close()

print("Figuras salvas em:", OUT_DIR)