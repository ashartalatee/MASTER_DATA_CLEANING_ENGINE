import pandas as pd

df = pd.read_csv("../data/raw/client_dataset_raw.csv")

df = df.drop_duplicates()

df.to_csv("../data/processed/step1_no_duplicates.csv", index=False)

print("Step 1 → duplicates removed")
