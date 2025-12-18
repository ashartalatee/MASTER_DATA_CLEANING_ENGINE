import requests
from bs4 import BeautifulSoup

def fetch_page(url):
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    return response.text

def parse_books(html, page):
    soup = BeautifulSoup(html, "html.parser")
    books = []

    for item in soup.select("article.product_pod"):
        books.append({
            "title": item.h3.a["title"],
            "price": item.select_one("p.price_color").text,
            "page": page
        })

    return books