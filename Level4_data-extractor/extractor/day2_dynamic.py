from playwright.sync_api import sync_playwright, TimeoutError

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    
    try:
        page.goto("https://quotes.toscrape.com/js/", timeout=15000)  # 15 detik
        page.wait_for_selector(".quote", timeout=15000)  # tunggu elemen muncul
    except TimeoutError:
        print("Error: Elemen '.quote' tidak muncul.")
        browser.close()
        exit(1)
    
    quotes = page.query_selector_all(".quote")
    if not quotes:
        print("Error: Tidak ada elemen '.quote' ditemukan.")
        browser.close()
        exit(1)
    
    results = []
    for q in quotes:
        text_el = q.query_selector(".text")
        author_el = q.query_selector(".author")
        tag_els = q.query_selector_all(".tag")
        
        # Pastikan elemen tidak None
        text = text_el.inner_text() if text_el else ""
        author = author_el.inner_text() if author_el else ""
        tags = [t.inner_text() for t in tag_els] if tag_els else []
        
        results.append({"text": text, "author": author, "tags": tags})
    
    print(f"Total quotes captured: {len(results)}")
    for r in results[:5]:  # tampilkan 5 pertama
        print(r)
    
    browser.close()
