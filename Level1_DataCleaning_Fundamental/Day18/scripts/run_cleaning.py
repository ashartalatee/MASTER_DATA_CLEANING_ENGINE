import pandas as pd
from datetime import datetime
from cleaning_template import clean_dataset

RAW_PATH = "data/raw/dataset_raw.csv"
CLEAN_PATH = "data/clean/dataset_clean.csv"
LOG_PATH = "logs/run_log.txt"

df_raw = pd.read_csv(RAW_PATH)

df_clean = clean_dataset(df_raw)
df_clean.to_csv(CLEAN_PATH, index=False)

with open(LOG_PATH, "a") as log:
    log.write(f"[{datetime.now()}] Cleaning executed. Rows: before={len(df_raw)}, after={len(df_clean)}\n")

print("Cleaning done. Output saved to:", CLEAN_PATH)
