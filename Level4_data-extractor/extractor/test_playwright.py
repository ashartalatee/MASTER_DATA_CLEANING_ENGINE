from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://quotes.toscrape.com/js/")
    page.wait_for_selector(".quote")

    quotes = page.query_selector_all(".quote")

    print("Total quotes:", len(quotes))

    for q in quotes[:3]:
        text = q.query_selector(".text").inner_text()
        author = q.query_selector(".author").inner_text()
        print(text, "-", author)

    browser.close()