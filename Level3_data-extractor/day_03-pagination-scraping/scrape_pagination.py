import requests
from bs4 import BeautifulSoup
import pandas as pd
import os

BASE_URL = "https://books.toscrape.com/catalogue/page-{}.html"

books = []

os.makedirs("raw/pages", exist_ok=True)

for page in range(1, 6): # ambil 5 halaman dulu
    print(f"Scraping page {page}")

    url = BASE_URL.format(page)
    response = requests.get(url)

    if response.status_code != 200:
        print(f"Page {page} gagal diambil")
        continue

    html = response.text

    with open(f"raw/pages/page_{page}.html", "w", encoding="utf-8") as f:
        f.write(html)

    soup = BeautifulSoup(html, "html.parser")

    for item in soup.select("article.product_pod"):
        title = item.h3.a["title"]
        price = item.select_one("p.price_color").text

        books.append({
            "title": title,
            "price": price,
            "page": page
        })

df = pd.DataFrame(books)
df.to_csv("books_day3_all_pages.csv", index=False)

print("Scraping selesai. Total data:", len(df))