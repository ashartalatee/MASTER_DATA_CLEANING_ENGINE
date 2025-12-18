# Level 4 — Day 1: Playwright Setup

Tujuan:
- Memastikan Playwright berjalan
- Mengambil data dari web JavaScript-rendered

Hasil:
- Browser otomatis terbuka
- Data quote & author berhasil diambil

# Level 4 — Day 2: Dynamic Page Scraping (JS-rendered)

## Tujuan
- Mengambil **banyak data** dari halaman web yang **dibuat dengan JavaScript**.
- Melatih **kontrol browser otomatis** menggunakan Playwright.
- Memahami pentingnya **wait / selector** agar scraper tidak gagal saat elemen muncul terlambat.

## Website Target
- [Quotes to Scrape (JS)](https://quotes.toscrape.com/js/)

## Fokus Praktek
1. Mengambil semua elemen `.quote` dari halaman.
2. Mendapatkan:
   - `text` → isi quote
   - `author` → penulis quote
   - `tags` → list tag per quote
3. Menampilkan 5 elemen pertama untuk pengecekan.
4. Push hasil ke GitHub setiap selesai.

# Level 4 — Day 3: Pagination & Infinite Scroll

## Tujuan
Hari ini fokus pada:
- Mengambil data dari **multi-halaman** (pagination) di web JS-rendered.
- Melatih kontrol **loop, stop condition, dan delay**.
- Memastikan data **≥100 item** bisa diambil otomatis.
- Persiapan untuk tahap **cleaning pipeline** di Day 4.

## Website Target
- [Quotes to Scrape (JS)](https://quotes.toscrape.com/js/)
- Dinamis (JavaScript-rendered)
- Memiliki tombol `Next` untuk pagination

## Script
- `extractor/day3_pagination.py`
- Menggunakan **Playwright (sync API)**
- Looping halaman hingga **tidak ada tombol Next**
- Mengambil data:
  - `text` → isi quote
  - `author` → nama pengarang
  - `tags` → list tag quote
- Output terminal menampilkan total quotes dan beberapa data contoh

## Hasil
- Total quotes captured: 100  
- Contoh data:
```json
{
  "text": "“The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.”",
  "author": "Albert Einstein",
  "tags": ["change", "deep-thoughts", "thinking", "world"]
}
