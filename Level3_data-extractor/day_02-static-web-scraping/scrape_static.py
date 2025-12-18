import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://books.toscrape.com/"
response = requests.get(url)

print("Status Code:", response.status_code)

html_content = response.text

# Simpan HTML mentah
with open("raw/html_response.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("HTML berhasil disimpan.")

# Parse HTML
soup = BeautifulSoup(html_content, "html.parser")

books = []

for item in soup.select("article.product_pod"):
    title = item.h3.a["title"]
    price = item.select_one("p.price_color").text

    books.append({
        "title": title,
        "price": price
    })

# Ubah ke DataFrame
df = pd.DataFrame(books)

print("\nPreview Data:")
print(df.head())

# Simpan ke csv
df.to_csv("books_day2.csv", index=False)
print("\nData buku berhasil disimpan ke books_day2.csv")