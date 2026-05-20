import pandas as pd
import numpy as np
from sklearn.impute import KNNImputer
from sklearn.preprocessing import RobustScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

INPUT = "/Users/joaokasprowicz/Documents/cardio/data/processed/features_24h_peak_emergency.csv"

vars_model = [
    "LEUCO","PLAQ","CREATININA","UREIA","PCR","TGO","TGP","idade"
]

df = pd.read_csv(INPUT)
X = df[vars_model].copy()

# ----------------------------
# CLIPPING (IQR k=3)
# ----------------------------
def clip_iqr(df, cols, k=3.0):
    out = df.copy()
    for c in cols:
        q1 = out[c].quantile(0.25)
        q3 = out[c].quantile(0.75)
        iqr = q3 - q1
        lo = q1 - k*iqr
        hi = q3 + k*iqr
        out[c] = out[c].clip(lo, hi)
    return out

X = clip_iqr(X, vars_model[:-1])  # exclui idade

# ----------------------------
# LOG TRANSFORM
# ----------------------------
for c in ["LEUCO","PLAQ","CREATININA","UREIA","PCR","TGO","TGP"]:
    X[c] = np.log1p(X[c])

# ----------------------------
# IMPUTAÇÃO
# ----------------------------
imputer = KNNImputer(n_neighbors=5)
X_imp = imputer.fit_transform(X)

# ----------------------------
# SCALING ROBUSTO
# ----------------------------
scaler = RobustScaler()
X_scaled = scaler.fit_transform(X_imp)

# ----------------------------
# ESCOLHA DE K (avaliar, não aceitar cegamente)
# ----------------------------
scores = {}
for k in range(2, 7):
    km = KMeans(n_clusters=k, random_state=42, n_init=100)
    labels = km.fit_predict(X_scaled)
    scores[k] = silhouette_score(X_scaled, labels)

print("Silhouette:", scores)

# escolha prática: k=3 ou 4 (evitar k=2 se colapsar)
k = 3

km = KMeans(n_clusters=k, random_state=42, n_init=200)
df["cluster"] = km.fit_predict(X_scaled)

print("\nDistribuição clusters:")
print(df["cluster"].value_counts())

print("\nSilhouette final:", silhouette_score(X_scaled, df["cluster"]))

df.to_csv("data/processed/clusters_kmeans_robust_final.csv", index=False)