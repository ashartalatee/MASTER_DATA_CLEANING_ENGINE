import pandas as pd
import os

INPUT_PATH = "raw/input_data.csv"

VALID_PATH = "validated/valid_data.csv"
INVALID_PATH = "invalid/invalid_data.csv"

os.makedirs("validated", exist_ok=True)
os.makedirs("invalid", exist_ok=True)

df = pd.read_csv(INPUT_PATH)

print("Total rows:", len(df))

# Rule dasar kualitas data
required_columns = ["userId", "id", "title", "body"]

# Cek kolom wajib
missing_columns = [col for col in required_columns if col not in df.columns]
if missing_columns:
    raise ValueError(f"Kolom wajib hilang: {missing_columns}")

# Cek missing value
invalid_missing = df[df[required_columns].isnull().any(axis=1)]

# Cek duplikasi
invalid_duplicate = df[df.duplicated(subset=["id"], keep=False)]

# Gabungkan invalid
invalid_df = pd.concat([invalid_missing, invalid_duplicate]).drop_duplicates()

# Data valid = selain invalid
valid_df = df.drop(invalid_df.index)

# Simpan
valid_df.to_csv(VALID_PATH, index=False)
invalid_df.to_csv(INVALID_PATH, index=False)

print("Valid data:", len(valid_df))
print("Invalid data:", len(invalid_df))
