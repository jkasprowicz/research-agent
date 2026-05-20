import pandas as pd
import unicodedata
import hashlib
from pathlib import Path

ARQUIVO = "/Users/joaokasprowicz/Documents/cardio/data/raw/base_laboratorial_consolidada.csv"
OUTPUT = "/Users/joaokasprowicz/Documents/cardio/data/processed/dataset_laboratorial_expandido.csv"

Path("data/processed").mkdir(parents=True, exist_ok=True)

CHUNKSIZE = 300_000

def norm(x):
    x = str(x).strip()
    x = unicodedata.normalize("NFKD", x).encode("ASCII", "ignore").decode()
    return x.upper()

def hash_patient(row):
    raw = f"{row.get('CPF do Paciente', '')}_{row.get('Nome do Paciente', '')}_{row.get('Data de Nascimento', '')}"
    return hashlib.sha256(raw.encode("utf-8")).hexdigest()

hemograma_vars = [
    "LEUCO", "PLAQ", "HB", "HT",
    "SEG", "SEG%", "LINFO", "LINFO%",
    "MONO", "MONO%", "EOSI", "EOSI%",
    "BASO", "BASO%"
]

def mapear_exame(row):
    var = row["variavel_norm"]
    exame = row["exame_norm"]

    # Hemograma: usar Nome da Variável
    if var in hemograma_vars:
        return var

    # Inflamatório
    if "PROTEINA C REATIVA" in exame or "PCR" in exame:
        return "PCR"

    # Renal
    if "CREATININA" in exame:
        return "CREATININA"
    if "UREIA" in exame:
        return "UREIA"

    # Hepático / lesão
    if "TGO" in exame or "AST" in exame:
        return "TGO"
    if "TGP" in exame or "ALT" in exame:
        return "TGP"
    if "GGT" in exame or "GAMA GLUTAMIL" in exame:
        return "GGT"
    if "FOSFATASE ALCALINA" in exame:
        return "FOSFATASE_ALCALINA"
    if "BILIRRUBINAS" in exame:
        # Se quiser detalhar frações depois, usar Nome da Variável.
        # Para clustering inicial, agrupar como bilirrubina.
        return "BILIRRUBINA"
    if "DESIDROGENASE LATICA" in exame or "LDH" in exame:
        return "LDH"

    # Metabólico / eletrólitos
    if "SODIO" in exame:
        return "SODIO"
    if "POTASSIO" in exame:
        return "POTASSIO"
    if "GLICOSE" in exame:
        return "GLICOSE"

    # Muscular/cardíaco
    if "CPK" in exame or "CREATINOFOSFOQUINASE" in exame:
        return "CPK"
    if "CKMB" in exame or "CK" in exame and "MB" in exame:
        return "CKMB"
    if "TROPONINA" in exame:
        return "TROPONINA"

    # Coagulação
    if "TAP" in exame or "TEMPO DE PROTROMBINA" in exame:
        return "TAP"
    if "KPTT" in exame or "TROMBOPLASTINA" in exame:
        return "KPTT"

    # Pancreático
    if "AMILASE" in exame:
        return "AMILASE"

    return None

# termos amplos para pré-filtrar sem aplicar mapear em tudo
termos_exame = [
    "PROTEINA C REATIVA", "PCR",
    "CREATININA", "UREIA",
    "TGO", "AST", "TGP", "ALT", "GGT", "GAMA GLUTAMIL",
    "FOSFATASE ALCALINA", "BILIRRUBINAS", "DESIDROGENASE", "LDH",
    "SODIO", "POTASSIO", "GLICOSE",
    "CPK", "CREATINOFOSFOQUINASE", "CKMB", "TROPONINA",
    "TAP", "TEMPO DE PROTROMBINA", "KPTT", "TROMBOPLASTINA",
    "AMILASE"
]

partes = []

for i, chunk in enumerate(pd.read_csv(
    ARQUIVO,
    sep=";",
    encoding="utf-8",
    chunksize=CHUNKSIZE,
    low_memory=False
)):
    print(f"Processando chunk {i+1}")

    chunk.columns = chunk.columns.str.strip()

    # opcional: se quiser só urgência/emergência, mantenha. Se quiser base geral, comente.
    # chunk = chunk[chunk["Código da Unidade"].isin([4, 5, 6])].copy()

    chunk["exame_norm"] = chunk["Nome do Exame"].apply(norm)
    chunk["variavel_norm"] = chunk["Nome da Variável"].apply(norm)

    filtro_hemo = chunk["variavel_norm"].isin(hemograma_vars)

    regex_exames = "|".join(termos_exame)
    filtro_exames = chunk["exame_norm"].str.contains(regex_exames, na=False)

    chunk = chunk[filtro_hemo | filtro_exames].copy()

    if chunk.empty:
        continue

    chunk["exame_padronizado"] = chunk.apply(mapear_exame, axis=1)
    chunk = chunk.dropna(subset=["exame_padronizado"]).copy()

    chunk["data_de_entrada"] = pd.to_datetime(chunk["Data de Entrada"], errors="coerce")
    chunk["data_nascimento"] = pd.to_datetime(chunk["Data de Nascimento"], errors="coerce")

    chunk["idade"] = ((chunk["data_de_entrada"] - chunk["data_nascimento"]).dt.days / 365.25).round(1)

    chunk["valor_num"] = pd.to_numeric(chunk["Valor do Resultado"], errors="coerce")
    chunk = chunk.dropna(subset=["valor_num"]).copy()

    if "patient_id" not in chunk.columns:
        chunk["patient_id"] = chunk.apply(hash_patient, axis=1)

    keep = [
        "data_de_entrada",
        "Código da Unidade",
        "Número do Atendimento",
        "Nome do Exame",
        "Nome da Variável",
        "Valor do Resultado",
        "valor_num",
        "Sexo",
        "patient_id",
        "idade",
        "exame_padronizado",
        "arquivo_origem"
    ]

    keep = [c for c in keep if c in chunk.columns]
    chunk = chunk[keep].copy()

    chunk = chunk.rename(columns={
        "Código da Unidade": "codigo_da_unidade",
        "Número do Atendimento": "numero_do_atendimento",
        "Nome do Exame": "nome_do_exame",
        "Nome da Variável": "nome_da_variavel",
        "Valor do Resultado": "valor_do_resultado",
        "Sexo": "sexo"
    })

    partes.append(chunk)

df_final = pd.concat(partes, ignore_index=True)

df_final.to_csv(OUTPUT, index=False)

print("\nDataset expandido salvo em:", OUTPUT)
print(df_final.shape)

print("\nExames finais:")
print(df_final["exame_padronizado"].value_counts())

print("\nAtendimentos por exame:")
print(
    df_final.groupby("exame_padronizado")["numero_do_atendimento"]
    .nunique()
    .sort_values(ascending=False)
)
