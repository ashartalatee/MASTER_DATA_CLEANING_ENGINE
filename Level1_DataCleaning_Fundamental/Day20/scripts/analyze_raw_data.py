import pandas as pd

df = pd.read_csv("../data/raw/client_dataset_raw.csv")

print("=== RAW DATA INFO ===")
print(df.info())
print("\n=== HEAD ===")
print(df.head())
print("\n=== MISSING VALUES ===")
print(df.isnull().sum())
print("\n=== DUPLICATES ===")
print(df.duplicated().sum())
print("\n=== UNIQUE VALUES ===")
print(df.nunique())
