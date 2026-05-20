import pandas as pd

INPUT = "../data/processed/features_24h_peak_final_units_fixed.csv"
OUTPUT = "../data/processed/features_24h_peak_emergency.csv"

df = pd.read_csv(INPUT)

df = df[df["codigo_da_unidade"].isin([4, 5, 6])].copy()

print("Shape final:", df.shape)

df.to_csv(OUTPUT, index=False)

print("Arquivo salvo:", OUTPUT)