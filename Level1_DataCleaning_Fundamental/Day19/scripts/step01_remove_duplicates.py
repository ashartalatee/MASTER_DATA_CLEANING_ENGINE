import pandas as pd

df = pd.read_csv("../data/raw/dataset_raw.csv")

# Remove duplicates
df_no_dupes = df.drop_duplicates()

df_no_dupes.to_csv("../data/processed/dataset_step1_no_duplicates.csv", index=False)

print("Step 1 done: duplicates removed")
