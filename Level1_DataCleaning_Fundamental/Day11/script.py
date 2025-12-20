import pandas as pd
import re

df = pd.read_csv("dataset_raw.csv")

# 1. Bersihkan spasi kiri kanan
df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)

# 2. Perbaikan Nama hapus angka & simbol
def clean_name(name):
    if not isinstance(name, str):
        return name
    # Hanya biarkan huruf dan spasi
    cleaned = re.sub(r'[^A-Za-z\s]', '', name)
    return cleaned.title()

if 'name' in df.columns:
    df['name'] = df['name'].apply(clean_name)

# 3. Validasi email hapus yang tidak valid
def is_valid_email(email):
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return bool(re.match(pattern, email))

if 'email' in df.columns:
    df['email'] = df['email'].str.replace(" ", "")
    df = df[df['email'].apply(is_valid_email)]

# 4. Mapping kategori typo "pending"
category_mapping = {
    "pending": "pending",
    "pendng": "pending",
    "pnding": "pending",
    "pendingg": "pending",
    "???": None,
    "none": None
}

if 'category' in df.columns:
    df['category'] = df['category'].str.lower()
    df['category'] = df['category'].map(category_mapping)

# 5. Bersihkan nama kota dari typo sederhana
city_mapping = {
    "jakarta": "jakarta",
    "jkarta": "jakarta",
    "jkt": "jakarta",
    "none": None
}

if 'city' in df.columns:
    df['city'] = df['city'].str.lower()
    df['city'] = df['city'].map(city_mapping).fillna(df['city'])

# Export hasil
df.to_csv("dataset_clean.csv", index=False)
print("Cleaning Day 11 selesai! file dataset_clean.csv berhasil dibuat.")