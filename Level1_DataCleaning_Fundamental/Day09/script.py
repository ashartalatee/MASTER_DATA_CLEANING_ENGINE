import pandas as pd

# 1. Load Dataset
df = pd.read_csv("duplicates.csv")
print("INFO DATA AWAL")
print(df.info())

print("\nJumlah baris awal:", len(df))

# 2. cek missing values
missing_report = df.isna().sum().reset_index()
missing_report.columns = ["column", "missing_count"]

print("Laporan missing values")
print(missing_report)

# simpan laporan
missing_report.to_csv("day09_missing_report.csv", index=False)
print("\n Laporan missing disimpan di 'day09_missing_report.csv'", )

# 3. Strategi handling mising
df_clean = df.copy()

for col in df_clean.columns:
    missing = df_clean[col].isna().sum()
    dtype = df_clean[col].dtype

    # Tidak ada missing, lewati
    if missing == 0:
        continue

    # Jika kolom numerik ganti dengan median
    if dtype != 'object':
        median_value = df_clean[col].median()
        df_clean[col] = df_clean[col].fillna(median_value)
        print(f"{col}: Missing diganti median ({median_value})")

    # Jika kolom kategori ganti dengan mode
    else:
        mode_value = df_clean[col].mode()[0]
        df_clean[col] = df_clean[col].fillna(mode_value)
        print(f"{col}: Missing diganti mode ({mode_value})")

print("Info sesudah cleaning")
print(df_clean.info())

# 4. Simpan file clean
df_clean.to_csv("dataset_clean.csv", index=False)
print("\n dataset_clean.csv berhasil dibuat!")

print("\nDay 9 selesai")