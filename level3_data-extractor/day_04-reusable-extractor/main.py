import pandas as pd
from extractor import fetch_page, parse_books
from config import BASE_URL, START_PAGE, END_PAGE, OUTPUT_FILE

all_books = []

for page in range(START_PAGE, END_PAGE + 1):
    print(f"Processing page {page}")
    url = BASE_URL.format(page)

    try:
        html = fetch_page(url)
        books = parse_books(html, page)
        all_books.extend(books)
    except Exception as e:
        print(f"Error on page {page}: {e}")

df = pd.DataFrame(all_books)
df.to_csv(OUTPUT_FILE, index=False)

print("Extractor selesai. Total data:", len(df))