from playwright.sync_api import sync_playwright
import time
import csv
import os


def scrape_quotes(max_pages=None):
    """Scrape quotes from quotes.toscrape.com/js/"""
    all_results = []

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://quotes.toscrape.com/js/")
        page_number = 1

        while True:
            page.wait_for_selector(".quote")
            quotes = page.query_selector_all(".quote")

            for q in quotes:
                text = q.query_selector(".text").inner_text().strip()
                author = q.query_selector(".author").inner_text().strip()
                tags = [
                    t.inner_text().strip().lower()
                    for t in q.query_selector_all(".tag")
                ]

                all_results.append({
                    "text": text,
                    "author": author,
                    "tags": tags
                })

            next_button = page.query_selector(".next > a")
            if next_button and (max_pages is None or page_number < max_pages):
                next_button.click()
                page_number += 1
                time.sleep(1)
            else:
                break

        browser.close()

    return all_results


def clean_quotes(data):
    """Clean scraped quotes: remove duplicates & missing fields"""
    seen = set()
    cleaned = []

    for item in data:
        if item["text"] not in seen:
            seen.add(item["text"])
            cleaned.append(item)

    final_data = [
        item for item in cleaned
        if item["text"] and item["author"]
    ]

    return final_data


def save_to_csv(data, path="../output/quotes_modular.csv"):
    """Save cleaned data to CSV (auto-create folder)"""

    os.makedirs(os.path.dirname(path), exist_ok=True)

    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=["text", "author", "tags"]
        )
        writer.writeheader()

        for row in data:
            row_copy = row.copy()
            row_copy["tags"] = ",".join(row_copy["tags"])
            writer.writerow(row_copy)


if __name__ == "__main__":
    raw_data = scrape_quotes(max_pages=3)
    cleaned_data = clean_quotes(raw_data)
    save_to_csv(cleaned_data)

    print(f"Modular pipeline done: {len(cleaned_data)} rows")
