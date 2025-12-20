import pandas as pd

# Load data
df = pd.read_csv("../../datasets/dataset_raw.csv")

print("\n DATA PREVIEW")
print(df.head())

print("\n INFO DATASET")
print(df.info())

print("\n MISSING VALUES")
print(df.isnull().sum())

print("\n DUPLICATE ROWS")
print(df.duplicated().sum())

print("\n UNIQUE VALUES PER COLUMN")
for col in df.columns:
    print(f"{col}: {df[col].unique()}")