import requests
import pandas as pd
from playwright.sync_api import sync_playwright

def extract_web_data():
    data = []

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("https://quotes.toscrape.com/js/")

        quotes = page.query_selector_all(".quote")

        for q in quotes:
            text = q.query_selector(".text").inner_text()
            author = q.query_selector(".author").inner_text()
            tags = [t.inner_text() for t in q.query_selector_all(".tag")]

            data.append({
                "text": text,
                "author": author,
                "tags": tags,
                "source": "web"
            })

        browser.close()

    return data


# ini penting supaya tidak auto-run saat di-import
if __name__ == "__main__":
    result = extract_web_data()
    df = pd.DataFrame(result)
    df.to_csv("output/raw_web.csv", index=False)
    print(f"Web dataset saved: {len(df)} rows")
