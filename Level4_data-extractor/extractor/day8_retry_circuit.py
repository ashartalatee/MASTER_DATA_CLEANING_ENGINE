import requests
import time
import pandas as pd

API_URL = "https://api.quotable.io/quotes?limit=20"

MAX_RETRY = 3
TIMEOUT = 5
FAIL_THRESHOLD = 2

api_fail_count = 0
all_data = []

def fetch_api_with_retry(url):
    global api_fail_count

    for attempt in range(1, MAX_RETRY + 1):
        try:
            print(f"[API] Attempt {attempt}")
            response = requests.get(
                url,
                timeout=TIMEOUT,
                verify=False
            )
            response.raise_for_status()
            return response.json()
        
        except Exception as e:
            print(f"[API ERROR] {e}")
            time.sleep(attempt * 2)

    api_fail_count += 1
    return None

# API extraction with circuit breaker
if api_fail_count < FAIL_THRESHOLD:
    api_result = fetch_api_with_retry(API_URL)

    if api_result:
        for item in api_result.get("results", []):
            all_data.append({
                "text": item.get("content"),
                "author": item.get("author"),
                "tags": item.get("tags"),
                "source": "api"
            })
    else:
        print("[CIRCUIT] API failed too many times")
else:
    print("[CIRCUIT] API is OPEN - skipping requests")

    # Save output
df = pd.DataFrame(all_data)
df.to_csv("output/day8_api_retry.csv", index=False)

print(f"Saved {len(df)} rows with retry & circuit breaker")