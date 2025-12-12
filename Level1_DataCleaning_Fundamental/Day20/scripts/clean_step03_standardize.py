import pandas as pd

df = pd.read_csv("../data/processed/step2_missing_fixed.csv")

# Phone — keep only digits
df['phone'] = df['phone'].str.replace(r'\D+', '', regex=True)

# Standardize email
df['email'] = df['email'].str.replace("@@", "@")
df['email'] = df['email'].str.replace("gmail", "gmail.com")

# Standardize date format
df['signup_date'] = pd.to_datetime(df['signup_date'], errors='coerce')

df.to_csv("../data/processed/client_dataset_clean.csv", index=False)

print("Step 3 → standardized format applied")
