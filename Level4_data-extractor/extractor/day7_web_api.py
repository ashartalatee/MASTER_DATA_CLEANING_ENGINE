import csv
import requests
from day5_modular import scrape_quotes, clean_quotes

# 1. Data dari web
web_raw = scrape_quotes(max_pages=2)
web_clean = clean_quotes(web_raw)

web_standard = []
for item in web_clean:
    web_standard.append({
        "text": item["text"],
        "author": item["author"],
        "tags": ",".join(item["tags"]),
        "source": "web"
    })

# 2. DATA DARI API
api_url = "https://api.quotable.io/quotes?limit=20"

try:
    response = requests.get(api_url, timeout=10, verify=False)
    response.raise_for_status()
    data = response.json()
except Exception as e:
    print("API ERROR:", e)
    data = {"results": []}

api_standard = []
for row in data.get("results", []):
    api_standard.append({
        "text": row["content"].strip(),
        "author": row["author"].strip(),
        "tags": ",".join(row.get("tags", [])),
        "source": "api"
    })


# 3. gabung dan dedup
combined = web_standard + api_standard

seen = set()
final_data = []
for item in combined:
    key = item["text"]
    if key not in seen:
        seen.add(key)
        final_data.append(item)

# 4. Simpan
output_path = "../output/quotes_web_api_cleaned.csv"
with open(output_path, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(
        f,
        fieldnames=["text", "author", "tags", "source"]
    )
    writer.writeheader()
    writer.writerows(final_data)

print(f"Web + API dataset saved:{len(final_data)} rows")