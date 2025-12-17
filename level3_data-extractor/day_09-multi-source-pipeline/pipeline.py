import os
import pandas as pd
from bs4 import BeautifulSoup
import json

# Folders & Files
HTML_FOLDER = "raw/html_pages"
API_FILE = "raw/api_data.json"
OUTPUT_FOLDER = "output"
OUTPUT_FILE = os.path.join(OUTPUT_FOLDER, "combined_data.csv")

os.makedirs(HTML_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# Step 1: Parse HTML Pages
html_data = []

if os.path.exists(HTML_FOLDER):
    html_files = [f for f in os.listdir(HTML_FOLDER) if f.endswith(".html")]
    if html_files:
        for filename in html_files:
            with open(os.path.join(HTML_FOLDER, filename), "r", encoding="utf-8") as f:
                soup = BeautifulSoup(f.read(), "html.parser")
                for item in soup.select("article.product_pod"):
                    html_data.append({
                        "title": item.h3.a["title"],
                        "price": item.select_one("p.price_color").text,
                        "source": "web"
                    })
        print(f"HTML data rows: {len(html_data)}")
    else:
        print(f"Tidak ada file HTML di {HTML_FOLDER}, skip HTML parsing")
else:
    print(f"Folder {HTML_FOLDER} tidak ditemukan, skip HTML parsing")

df_html = pd.DataFrame(html_data)

# Step 2: Load API Data
df_api = pd.DataFrame()

if os.path.exists(API_FILE):
    with open(API_FILE, "r", encoding="utf-8") as f:
        api_json = json.load(f)
    if api_json:
        df_api = pd.DataFrame(api_json)
        df_api["source"] = "api"
        print(f"API data rows: {len(df_api)}")
    else:
        print("API file kosong, skip API")
else:
    print(f"API file {API_FILE} tidak ditemukan, skip API")

# Step 3: Combine & Validate
if not df_html.empty or not df_api.empty:
    df_combined = pd.concat([df_html, df_api], ignore_index=True)

    # Basic validation
    required_columns = ["title", "source"]
    missing = df_combined[required_columns].isnull().any(axis=1)
    duplicates = df_combined.duplicated(subset=["title"], keep=False)
    df_invalid = df_combined[missing | duplicates]
    df_valid = df_combined[~(missing | duplicates)]

    # Save output
    df_valid.to_csv(OUTPUT_FILE, index=False)
    print(f"Pipeline selesai. Output saved at: {OUTPUT_FILE}")
    print(f"Valid rows: {len(df_valid)}, Invalid rows: {len(df_invalid)}")
else:
    print("Tidak ada data HTML atau API, pipeline tidak menghasilkan output")
