import requests
import json
import pandas as pd
from datetime import datetime

BASE_URL = "https://jsonplaceholder.typicode.com/posts"

def fetch_api(user_id):
    try:
        response = requests.get(BASE_URL, params={"userId": user_id}, timeout=10)
        response.raise_for_status() # raise error kalau satatus != 200
        return response.json()
    except requests.exceptions.RequestException as e:
        log_error(user_id, e)
        return []

def log_error(user_id, error):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("api_error.log", "a") as f:
        f.write(f"[{timestamp}] Error for userId={user_id}: {error}\n")
    print(f"Error tercatat untuk userId={user_id}")

all_data = []

for uid in range(1, 4): # ambil userId 1-3
    print(f"Fetching userId={uid}")
    data = fetch_api(uid)
    all_data.extend(data)

# Simpan raw JSON
with open("raw/api_response.json", "w", encoding="utf-8") as f:
    json.dump(all_data, f, indent=2)

# JSON DataFrame CSV
df = pd.DataFrame(all_data)
df.to_csv("posts_day6_resilient.csv", index=False)

print("Extractor resilient selesai. Total data:", len(df))