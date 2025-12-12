import pandas as pd

df = pd.read_csv("../data/processed/step1_no_duplicates.csv")

# Fill missing name
df['name'] = df['name'].fillna("Unknown")

# Fill missing purchase_total — replace with median
df['purchase_total'] = df['purchase_total'].fillna(df['purchase_total'].median())

df.to_csv("../data/processed/step2_missing_fixed.csv", index=False)

print("Step 2 → missing values handled")
