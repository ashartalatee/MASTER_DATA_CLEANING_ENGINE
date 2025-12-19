import pandas as pd
from day8_retry_circuit import fetch_api_with_retry
from day9_validation_schema import validate_row
from day7_web_api import extract_web_data

API_URL = "https://api.quotable.io/quotes?limit=20"

def run_pipeline():
    all_data = []

    print("[PIPELINE] Extracting WEB data...")
    web_data = extract_web_data()
    all_data.extend(web_data)

    print("[PIPELINE] Extracting API data...")
    api_result = fetch_api_with_retry(API_URL)
    if api_result:
        for item in api_result.get("results", []):
            all_data.append({
                "text": item.get("content"),
                "author": item.get("author"),
                "tags": item.get("tags"),
                "source": "api"
            })

    print("[PIPELINE] Total raw rows:", len(all_data))

    df = pd.DataFrame(all_data)

    print("[PIPELINE] Validating data...")
    valid_rows = []
    rejected = 0

    for _, row in df.iterrows():
        if validate_row(row):
            valid_rows.append(row)
        else:
            rejected += 1

    final_df = pd.DataFrame(valid_rows)
    final_df.to_csv("output/final_dataset.csv", index=False)

    print("[PIPELINE] Final rows saved:", len(final_df))
    print("[PIPELINE] Rejected rows:", rejected)

if __name__ == "__main__":
    run_pipeline()