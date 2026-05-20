import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

INPUT = "/Users/joaokasprowicz/Documents/cardio/data/processed/features_24h_peak_final.csv"

vars_model = [
    "LEUCO",
    "PLAQ",
    "CREATININA",
    "UREIA",
    "PCR",
    "TGO",
    "TGP",
    "idade"
]

df = pd.read_csv(INPUT)

# ============================================================
# RESUMO ESTATÍSTICO
# ============================================================

print("\n=== DESCRITIVO ===")
desc = df[vars_model].describe(percentiles=[0.01,0.05,0.25,0.5,0.75,0.95,0.99]).T
print(desc)

# ============================================================
# ASSIMETRIA (SKEWNESS)
# ============================================================

print("\n=== SKEWNESS ===")
skew = df[vars_model].skew()
print(skew.sort_values(ascending=False))

# ============================================================
# OUTLIERS (IQR)
# ============================================================

print("\n=== PROPORÇÃO DE OUTLIERS (IQR) ===")

def calc_outliers(series):
    q1 = series.quantile(0.25)
    q3 = series.quantile(0.75)
    iqr = q3 - q1
    lower = q1 - 1.5 * iqr
    upper = q3 + 1.5 * iqr
    return ((series < lower) | (series > upper)).mean()

for col in vars_model:
    prop = calc_outliers(df[col].dropna())
    print(f"{col}: {prop:.3f}")

# ============================================================
# HISTOGRAMAS (ANTES E DEPOIS DO LOG)
# ============================================================

for col in vars_model:
    fig, ax = plt.subplots(1, 2, figsize=(10,4))

    # original
    ax[0].hist(df[col].dropna(), bins=50)
    ax[0].set_title(f"{col} (original)")

    # log
    if (df[col] > 0).any():
        ax[1].hist(np.log1p(df[col].dropna()), bins=50)
        ax[1].set_title(f"{col} (log1p)")
    else:
        ax[1].set_visible(False)

    plt.tight_layout()
    plt.show()

# ============================================================
# BOXPLOTS
# ============================================================

plt.figure(figsize=(12,6))
df[vars_model].boxplot(rot=45)
plt.title("Boxplot - Variáveis")
plt.show()