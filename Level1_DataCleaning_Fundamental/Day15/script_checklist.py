import pandas as pd

df = pd.read_csv("dataset.csv")

print("Basic Info")
print(df.info())
print("\nShape:", df.shape)

print("\nMissing Values")
print(df.isna().sum())

print("\nDuplicate rows")
print(df.head())

print("\nQick Column Overview")
for col in df.columns:
    print(f"{col}: {df[col].unique()[:5]}")