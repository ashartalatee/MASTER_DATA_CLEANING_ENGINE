from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    
    try:
        page.goto("https://quotes.toscrape.com/js/")
        all_results = []

        while True:
            page.wait_for_selector(".quote")
            quotes = page.query_selector_all(".quote")
            for q in quotes:
                text = q.query_selector(".text").inner_text()
                author = q.query_selector(".author").inner_text()
                tags = [t.inner_text() for t in q.query_selector_all(".tag")]
                all_results.append({"text": text, "author": author, "tags": tags})

            next_button = page.query_selector(".next > a")
            if next_button:
                next_button.click()
                time.sleep(1)
            else:
                break

        print(f"Total quotes captured: {len(all_results)}")
        for r in all_results[:5]:
            print(r)

    except Exception as e:
        print("Error during scraping:", e)
    
    finally:
        # Tutup browser TANPA cek is_closed()
        try:
            browser.close()
        except Exception:
            pass  # Abaikan error tutup browser di Windows
