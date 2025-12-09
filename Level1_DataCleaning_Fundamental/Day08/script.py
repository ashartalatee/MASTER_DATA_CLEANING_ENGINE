import pandas as pd

# Load dataset
df = pd.read_csv("dataset_raw.csv")

# 1. INFO AWAL
print("DATA INFO SEBELUM CLEANING")
print(df.info())
print("\n Jumlah baris sebelum cleaning:", len(df))

# 2. Cek duolicate
duplicate_rows = df[df.duplicated()]
num_duplicates = len(duplicate_rows)

print("Duplikat terdeteksi")
print(f"Jumlah baris duplikat: {num_duplicates}")

if num_duplicates > 0:
    print("\nContoh baris duplikat:")
    print(duplicate_rows.head())

# 3. Hapus Duplikat
df_clean = df.drop_duplicates()

print("Sesudah hapus duplikat")
print("Jumlah baris:", len(df_clean))

# Simpan file cleaned
df_clean.to_csv("dataset_clean.csv", index=False)

print("\n File cleaned tersimpan sebagai 'dataset_cleaned.csv'")

# Ringkasa Perubahan
summary = {
    "rows_before": len(df),
    "rows_after": len(df_clean),
    "duplicates_removed": num_duplicates
}

summary_df = pd.DataFrame([summary])
summary_df.to_csv("day08_summary.csv", index=False)

print("Ringkasan perubahan tersimpan di 'day08_summary.csv'")