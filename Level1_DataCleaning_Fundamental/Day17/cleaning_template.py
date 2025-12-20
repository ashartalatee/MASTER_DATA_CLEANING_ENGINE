import pandas as pd
import re

# utility functions
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
    email = re.sub(f"@@", "@", email)
    email = email.replace(" ", "")
    return email

# Cleaning pipeline
def clean_dataset(path):
    df = pd.read_csv(path)

    print("Start Cleaning")
    print("Rows before:", len(df))

    # 1. Remove duplicates
    df = df.drop_duplicates()

    # 2. Fix emails
    df["Email"] = df["Email"].apply(clean_email)
    df["Email"] = df["Email"].apply(lambda x: x if "@" in x else "unknown@example.com")

    # 3. Normalize date
    df["JoinDate"] = df["JoinDate"].apply(normalize_date)

    # 4. Fix missing numeric values
    df["Amount"] = pd.to_numeric(df["Amount"], errors="coerce").fillna(0)

    # 5. Clean phone numbers
    df["Phone"] = df["Phone"].apply(clean_phone)

    print("Rows after cleaning:", len(df))
    print("Cleaning Done")

    return df

# Execution Example
if __name__ == "__main__":
    cleaned = clean_dataset("dataset_sample.csv")
    cleaned.to_csv("dataset_clean.csv", index=False)
    print("\nSaved to dataset_clean.csv")