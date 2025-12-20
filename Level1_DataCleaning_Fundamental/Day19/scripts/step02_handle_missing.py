import pandas as pd

df = pd.read_csv("../data/processed/dataset_step1_no_duplicates.csv")

# Handle missing age (replace with median)
df['age'] = df['age'].fillna(df['age'].median())

# Handle empty name → "Unknown"
df['name'] = df['name'].fillna("Unknown")

df.to_csv("../data/processed/dataset_step2_missing_handled.csv", index=False)

print("Step 2 done: missing values handled")
