import pandas as pd
import os

# Path file CSV
csv_path = "dataset_raw.csv"

# Cek file ada atau tidak
if not os.path.exists(csv_path):
    print(f" File '{csv_path}' tidak ditemukan. Pastikan ada di folder ini: {os.getcwd()}")
    exit()

# Load dataset
try:
    df = pd.read_csv(csv_path)
except Exception as e:
    print(" Error saat membaca CSV:", e)
    exit()

# Basic info
print(" DATASET BASIC INFO")
print(df.info())

print(" SAMPLE DATA (5 ROWS)")
print(df.head())

# Descriptive summary
print(" DESCRIPTIVE SUMMARY")

# Untuk semua versi pandas
print(df.describe(include='all'))

# Simpan struktur kolom ke file
col_file = "column_structure.txt"
with open(col_file, "w", encoding="utf-8") as f:
    f.write("Kolom & Tipe Data Saat Ini:\n")
    for col in df.columns:
        f.write(f"{col} -> {df[col].dtype}\n")

print(f"\n File '{col_file}' telah dibuat untuk dokumentasi kolom dan tipe data.")
