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