import pandas as pd

# Load data
df = pd.read_csv("dataset_raw.csv")

# 1. Hapus spasi di kiri-kanan untuk semua teks
df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)

# 2. Standarisasi Nama title case
if 'name' in df.columns:
    df['name'] = df['name'].str.title()

# 3. Standarisasi Email lowercase
if 'email' in df.columns:
    df['email'] = df['email'].str.lower()

# 4. Standarisasi kolom kategori
# Lowercase + hapus spasi
if 'category' in df.columns:
    df['category'] = df['category'].str.lower().str.replace(" ", "")

# 5. Standarisasi format tanggal YYY-MM-DD
if 'date' in df.columns:
    df['date'] = pd.to_datetime(df['date'], errors='coerce')
    df['date'] = df['date'].dt.strftime("%Y-%m-%d")

# Export hasil
df.to_csv("dataset_clean.csv", index=False)
print("Cleaning Day 10 selesai! File tersimpan sebagai dataset_clean.csv")