import pandas as pd

df = pd.read_csv("../data/processed/dataset_step2_missing_handled.csv")

# Standardize phone number: keep digits only
df['phone'] = df['phone'].str.replace(r'\D+', '', regex=True)

# Standardize email: fix common typos
df['email'] = df['email'].str.replace("gmailcom", "gmail.com")
df['email'] = df['email'].str.replace("@@", "@")

# Standardize dates
df['join_date'] = pd.to_datetime(df['join_date'], errors='coerce')

df.to_csv("../data/processed/dataset_step3_standardized.csv", index=False)

print("Step 3 done: format standardized")
