import requests
import pandas as pd
import json
import os
from datetime import datetime

BASE_URL = "https://jsonplaceholder.typicode.com/posts"

def fetch_data():
    response = requests.get(BASE_URL, timeout=10)
    response.raise_for_status()
    return response.json()

def main():
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_dir = "raw"
    os.makedirs(output_dir, exist_ok=True)

    data = fetch_data()

    # Simpan raw JSON
    json_path = f"{output_dir}/posts_{timestamp}.json"
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

    # JSON CSV
    df = pd.DataFrame(data)
    csv_path = f"posts_{timestamp}.csv"
    df.to_csv(csv_path, index=False)

    print(f"Extractor jalan otomatis. Output: {csv_path}")

if __name__ == "__main__":
    main()