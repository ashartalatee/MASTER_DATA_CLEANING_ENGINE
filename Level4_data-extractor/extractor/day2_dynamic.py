from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    # Buka halaman
    page.goto("https://quotes.toscrape.com/js/")

    # Tunggu semua quote muncul
    page.wait_for_selector(".quote")

    results = []
    for q in quotes:
        text = q.query_selector(".text").inner_text()
        author = q.query_selector(".author").inner_text()
        tags = [t.inner_text() for t in q.query_selector_all(".tag")]
        results.append({"text": text, "author": author, "tags": tags})

    print(f"Total quotes captured: {len(results)}")
    for r in results[:5]: # Tampilkan 5 pertama
        print(r)

    browser.close()