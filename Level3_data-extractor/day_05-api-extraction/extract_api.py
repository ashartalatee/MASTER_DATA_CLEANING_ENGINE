import requests
import json
import pandas as pd

URL = "https://jsonplaceholder.typicode.com/posts"

response = requests.get(URL)
print("Status Code:", response.status_code)

data = response.json()

# Simpan raw JSON
with open("raw/api_response.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2)

print("Raw API response disimpan.")

# JSON DataFrame
df = pd.DataFrame(data)

print(df.head())
print(df.info())

# Simpan ke csv
df.to_csv("posts_day5_api.csv", index=False)
print("Data API berhasil disimpan ke csv.")