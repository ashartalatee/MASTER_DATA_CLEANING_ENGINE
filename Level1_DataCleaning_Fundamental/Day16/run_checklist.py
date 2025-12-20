import pandas as pd

df = pd.read_csv("dataset_raw.csv")

print("\nData info")
print(df.info())

print("\nShape:", df.shape)

print("\nMissing values")
print(df.isna().sum())

print("\nDuplicate check (full row)")
print(df.head())

print("\nUnique per column (First 5 Values)")
for col in df.columns:
    print(f"\n{col}: {df[col].unique()[:5]}")

print("\nPotential errors")
#Email basic validation
invalid_email = df[~df['Email'].str.contains("@", na=False)]
print("Invalid Emails:\n", invalid_email)

# Numeric validation
non_numeric = df[pd.to_numeric(df['TotalSpend'], errors='coerce').isna()]
print("\nNon-numeric TotalSpend:\n", non_numeric)