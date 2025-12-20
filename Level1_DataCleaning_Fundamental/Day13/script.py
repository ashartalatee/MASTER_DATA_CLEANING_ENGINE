import pandas as pd
import re

# 1. load data
def load_data(path="dataset_raw.csv"):
    df = pd.read_csv(path)
    return df

# 2. Cleaning functions
def clean_text(x):
    if isinstance(x, str):
        return x.strip()
    return x

def clean_name(name):
    if not isinstance(name, str):
        return name
    name = re.sub(r'[^A-Za-z\s]', '', name) # hapus simbol/angka
    name = re.sub(r'\s+', ' ', name) # spasi ganda
    return name.title().strip()

def clean_city(city):
    if not isinstance(city, str):
        return city
    city = city.lower().strip()
    mapping = {
        "jkt": "jakarta",
        "jakrta": "jakarta",
        "jakarta": "jakarta"
    }
    return mapping.get(city, city)

def clean_category(cat):
    if not isinstance(cat, str):
        return cat
    cat = cat.lower().strip()
    mapping = {
        "pending": "pending",
        "pendingg": "pending"
    }
    return mapping.get(cat, cat)

def clean_date(date):
    try:
        dt = pd.to_datetime(date, errors="coerce")
        return dt.strftime("%Y-%m-%d")
    except:
        return None

# 3. Main cleaning pipeline
def clean_data(df):

    # Clean all text
    df = df.applymap(clean_text)

    # Column-Wise cleaning
    if 'name' in df.columns:
        df['name'] = df['name'].apply(clean_name)

    if 'city' in df.columns:
        df['city'] = df['city'].apply(clean_city)

    if 'category' in df.columns:
        df['category'] = df['category'].apply(clean_category)

    if 'date' in df.columns:
        df['date'] = df['date'].apply(clean_date)

    return df

# 4. Save
def save_data(df, path="dataset_clean.csv"):
    df.to_csv(path, index=False)
    print(f"Data berhasil disimpan ke {path}")

# 5. Main program
def main():
    print("Memuat data...")
    df = load_data()

    print("Membersihkan data...")
    df_clean = clean_data(df)

    print("Menyimpan data...")
    save_data(df_clean)

    print("Proses Day 13 selesai!")

if __name__ == "__main__":
    main()