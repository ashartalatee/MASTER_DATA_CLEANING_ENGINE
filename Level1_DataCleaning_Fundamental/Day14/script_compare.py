import pandas as pd

# Load datasets
raw = pd.read_csv("dataset_raw.csv")
clean = pd.read_csv("dataset_clean.csv")

# shape
print("Raw data shape:", raw.shape)
print("Clean data shape: clean.shape")

# Missing values
print("\nMissing values (raw):\n", raw.isna().sum())
print("\nMissing values (clean):\n", clean.isna().sum())

# Duplicate rows
print("\nDuplicate rows (Raw):", raw.duplicated().sum())
print("Duplicate rows (Clean):", clean.duplicated().sum())

# Example changes
print("\nSample rows before cleaning:")
print(raw.head(5))

print("\nSample rows after cleaning:")
print(clean.head(5))