import os
import csv
from day5_modular import scrape_quotes, clean_quotes


# CONFIG
BASE_DIR = os.path.dirname(__file__)

INPUT_CSV = os.path.join(BASE_DIR, "../input/external_quotes.csv")
OUTPUT_DIR = os.path.join(BASE_DIR, "../output")
OUTPUT_FILE = "quotes_cleaned.csv"


# 1. AMBIL DATA DARI WEB
print("🔄 Scraping data from web...")

web_raw = scrape_quotes(max_pages=2)
web_clean = clean_quotes(web_raw)

web_standard = []
for item in web_clean:
    web_standard.append({
        "text": item["text"].strip(),
        "author": item["author"].strip(),
        "tags": ",".join(item["tags"]),
        "source": "web"
    })

print(f"✅ Web data: {len(web_standard)} rows")


# 2. AMBIL DATA DARI CSV (OPTIONAL)
csv_standard = []

if os.path.exists(INPUT_CSV):
    print("🔄 Loading external CSV...")

    with open(INPUT_CSV, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            csv_standard.append({
                "text": row["quote_text"].strip(),
                "author": row["author_name"].strip(),
                "tags": row["topic"].strip().lower(),
                "source": "external_csv"
            })

    print(f"✅ External CSV data: {len(csv_standard)} rows")

else:
    print("⚠️ External CSV not found → skipped")


# 3. GABUNGKAN & DEDUPLICATE
print("🔄 Merging & deduplicating data...")

combined = web_standard + csv_standard

seen = set()
final_data = []

for item in combined:
    key = item["text"]
    if key not in seen:
        seen.add(key)
        final_data.append(item)

print(f"✅ Final dataset: {len(final_data)} rows")


# 4. SIMPAN OUTPUT (AUTO CREATE FOLDER)
os.makedirs(OUTPUT_DIR, exist_ok=True)

output_path = os.path.join(OUTPUT_DIR, OUTPUT_FILE)

with open(output_path, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(
        f,
        fieldnames=["text", "author", "tags", "source"]
    )
    writer.writeheader()
    writer.writerows(final_data)

print("💾 Dataset saved successfully")
print(f"📂 Location: {output_path}")


# DONE
print("🚀 Day 6 Multi-source pipeline DONE")
