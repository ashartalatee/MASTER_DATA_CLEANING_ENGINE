from playwright.sync_api import sync_playwright
import pandas as pd

def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        page.goto("https://quotes.toscrape.com/js/")

        page.wait_for_selector(".quote")

        quotes = []
        for quote in page.query_selector_all(".quote"):
            text = quote.query_selector(".text").inner_text()
            author = quote.query_selector(".author").inner_text()

            quotes.append({
                "quote": text,
                "author": author
            })

        browser.close()

    df = pd.DataFrame(quotes)
    df.to_csv("quotes_dynamic_day10.csv", index=False)
    print("Dynamic extraction selesai.")

if __name__ == "__main__":
    main()