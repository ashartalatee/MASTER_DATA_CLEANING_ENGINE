import pandas as pd
import re

def normalize_date(date_str):
    try:
        return pd.to_datetime(date_str, errors='coerce')
    except:
        return pd.NaT

def clean_phone(phone):
    if pd.isna(phone):
        return phone
    cleaned = re.sub(r"\D", "", str(phone))
    if cleaned.startswith("0"):
        cleaned = "62" + cleaned[1:]
    elif not cleaned.startswith("62"):
        cleaned = "62" + cleaned
    return cleaned

def clean_email(email):
    if pd.isna(email):
        return "unknown@example.com"
    email = email.strip().lower()
    email = re.sub(r"@@", "@", email)
    email = email.replace(" ", "")
    return email

def clean_dataset(df):
    df = df.copy()

    # remove duplicates
    df = df.drop_duplicates()

    # clean email
    df["Email"] = df["Email"].apply(clean_email)
    df["Email"] = df["Email"].apply(lambda x: x if "@" in x else "unknown@example.com")

    # normalize date
    df["SignupDate"] = df["SignupDate"].apply(normalize_date)

    # numeric
    df["TotalSpend"] = pd.to_numeric(df["TotalSpend"], errors="coerce").fillna(0)

    # phone
    df["Phone"] = df["Phone"].apply(clean_phone)

    return df
