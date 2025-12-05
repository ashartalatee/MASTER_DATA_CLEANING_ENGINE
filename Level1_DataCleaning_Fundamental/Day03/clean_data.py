import pandas as pd

# 1. Load data
df = pd.read_csv('../../datasets/dataset_raw.csv')

print("DATA AWAL:", df.shape)

# 2. Hapus duplikat
df = df.drop_duplicates()
print("SETELAH HAPUS DUPLICATE:", df.shape)

# 3. Standarisasi text (hapus spasi & samakan huruf)
for col in df.select_dtypes(include='object').columns:
    df[col] = df[col].astype(str).str.strip().str.lower()

print("TEXT STANDARDIZED")

# 4. Fix wrong data type (contoh: age)
if 'age' in df.columns:
    df['age'] = pd.to_numeric(df['age'], errors='coerce')

# 5. Handle missing value
df = df.fillna("unknown")

print("MISSING HANDLED")

# 6. Save cleaned version
df.to_csv('cleaned_priview.csv', index=False)

print("DATA CLEANING SELESAI. FILE saved: cleaned_preview.csv")