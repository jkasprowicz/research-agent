import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.impute import KNNImputer
from sklearn.preprocessing import RobustScaler
import umap
from pathlib import Path

INPUT = "/Users/joaokasprowicz/Documents/cardio/data/processed/clusters_kmeans_robust_final_with_care_setting.csv"
OUT_DIR = Path("/Users/joaokasprowicz/Documents/cardio/outputs/figuras")
OUT_DIR.mkdir(parents=True, exist_ok=True)

vars_model = [
    "LEUCO", "PLAQ", "CREATININA", "UREIA",
    "PCR", "TGO", "TGP", "idade"
]

df = pd.read_csv(INPUT)

X = df[vars_model].copy()

for col in ["LEUCO", "PLAQ", "CREATININA", "UREIA", "PCR", "TGO", "TGP"]:
    X[col] = np.log1p(X[col])

imputer = KNNImputer(n_neighbors=5)
X_imp = imputer.fit_transform(X)

scaler = RobustScaler()
X_scaled = scaler.fit_transform(X_imp)

reducer = umap.UMAP(
    n_neighbors=35,
    min_dist=0.08,
    metric="euclidean",
    random_state=42
)

embedding = reducer.fit_transform(X_scaled)

df["UMAP1"] = embedding[:, 0]
df["UMAP2"] = embedding[:, 1]

# Amostragem para reduzir overplotting
df_plot = (
    df.groupby("cluster", group_keys=False)
      .apply(lambda x: x.sample(min(len(x), 5000), random_state=42))
      .reset_index(drop=True)
)

colors = {
    0: "#D55E00",  # vermillion
    1: "#0072B2",  # blue
    2: "#009E73"   # green
}

names = {
    0: "Inflammatory–renal phenotype",
    1: "Hepatic phenotype",
    2: "Baseline phenotype"
}

plt.figure(figsize=(8.5, 6.8))

for cluster in sorted(df_plot["cluster"].unique()):
    sub = df_plot[df_plot["cluster"] == cluster]

    plt.scatter(
        sub["UMAP1"],
        sub["UMAP2"],
        s=6,
        alpha=0.28,
        color=colors[cluster],
        edgecolors="none",
        label=f"Cluster {cluster}: {names[cluster]}"
    )

# centroides usando dataset completo
for cluster in sorted(df["cluster"].unique()):
    sub_all = df[df["cluster"] == cluster]

    cx = sub_all["UMAP1"].median()
    cy = sub_all["UMAP2"].median()

    plt.scatter(
        cx,
        cy,
        s=230,
        color=colors[cluster],
        edgecolors="black",
        linewidths=1.1,
        marker="X",
        zorder=5
    )

    plt.text(
        cx + 0.08,
        cy + 0.08,
        f"C{cluster}",
        fontsize=11,
        fontweight="bold",
        color="black",
        zorder=6
    )

plt.title(
    "UMAP projection of laboratory-derived phenotypes",
    fontsize=15,
    fontweight="bold",
    pad=12
)

plt.xlabel("UMAP dimension 1", fontsize=12)
plt.ylabel("UMAP dimension 2", fontsize=12)

plt.legend(
    frameon=False,
    fontsize=9,
    loc="lower left",
    markerscale=2
)

plt.grid(False)

for spine in ["top", "right"]:
    plt.gca().spines[spine].set_visible(False)

plt.tight_layout()

plt.savefig(OUT_DIR / "figure1_umap_clusters_paper_ready.png", dpi=600)
plt.savefig(OUT_DIR / "figure1_umap_clusters_paper_ready.svg")
plt.savefig(OUT_DIR / "figure1_umap_clusters_paper_ready.pdf")

plt.show()

print("Figuras salvas em:")
print(OUT_DIR / "figure1_umap_clusters_paper_ready.png")
print(OUT_DIR / "figure1_umap_clusters_paper_ready.svg")
print(OUT_DIR / "figure1_umap_clusters_paper_ready.pdf")