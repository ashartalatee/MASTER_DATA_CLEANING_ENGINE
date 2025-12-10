import pandas as pd
import re

df = pd.read_csv("dataset_raw.csv")

# 1. Bersihkan spasi berlebih pada semua kolom teks
df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)

# 2. Normalisasi Nama
def clean_name(name):
    if not isinstance(name, str):
        return name
    name = re.sub(f'[^A-Za-z\s]', '', name) # hapus simbol/angka
    name = re.sub(r'\s+', ' ', name) # spasi ganda
    return name.title().strip()

if 'name' in df.columns:
    df['name'] = df['name'].apply(clean_name)

# 3. Normalisasi Email
def clean_email(email):
    if not isinstance(email, str):
        return email
    email = email.replace(" ", "").lower()
    return email

if 'email' in df.columns:
    df['email'] = df['email'].apply(clean_email)

# 4. Normalisasi Nomor telephone format +62
def clean_phone(phone):
    if not isinstance(phone, str):
        return phone
    
    # Hapus semua simbol
    phone = re.sub(r'[^0-9]', '', phone)

    # Aturan semua simbol
    if phone.startswith("0"):
        phone = "+62" + phone[1:]
    elif phone.startswith("62"):
        phone = "+" + phone
    elif phone.startswith("8"):
        phone = "+62" + phone
    else:
        phone = None #jika tidak masuk logika

    return phone

if 'phone' in df.columns:
    df['phone'] = df['phone'].apply(clean_phone)

# Export hasil
df.to_csv("dataset_clean.csv", index=False)
print("Cleaning day 12 selesai! file dataset_clean.csv berhasil dibuat.")