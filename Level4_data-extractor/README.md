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

# Level 4 — Day 4: Cleaning Extracted Data

## Tujuan
- Membersihkan data hasil scraping dari Day 3
- Menghapus duplicate, missing, dan data noise
- Standarisasi format text, author, dan tags
- Menyimpan output CSV siap dipakai pipeline

## Script
File: `extractor/day4_cleaning.py`

### Langkah yang Dilakukan
1. Import data dari Day 3 (`all_results`)
2. Hapus duplicate berdasarkan field `text`
3. Strip whitespace pada `text` dan `author`
4. Standarisasi `tags` menjadi lowercase dan bersih
5. Hapus data yang missing (`text` atau `author`)
6. Simpan hasil akhir ke CSV: `output/quotes_cleaned.csv`

### Output
- CSV `quotes_cleaned.csv` berisi data bersih
- Duplicate dan missing sudah dihapus
- Tags seragam lowercase
- Jumlah row: sesuai hasil terminal

### Cara Jalankan
```bash
python extractor/day4_cleaning.py

# Day 6 — Multi-Source Data Extraction & Cleaning Engine

## Tujuan
Membangun **pipeline data multi-source** yang:
- Mengambil data dari **web scraping**
- Menggabungkan dengan **CSV eksternal (opsional)**
- Membersihkan & standarisasi data
- Menghilangkan duplikasi
- Menyimpan output bersih secara otomatis

Pipeline ini **tidak crash** walau salah satu sumber data tidak tersedia.

---

## Konsep Utama (Level 4 Mindset)
> **Sistem profesional harus tetap hidup walau dunia tidak ideal**

- Sumber data bisa hilang
- File bisa belum ada
- Engine tetap jalan
- Output tetap dihasilkan

# Day 7 — Multi-Source Extraction (Web + API)

## Tujuan
Membangun **pipeline ekstraksi data dari MULTIPLE SOURCE**:
- Web Scraping (dynamic/static)
- Public API  
dengan **struktur data seragam** dan **sistem tetap hidup walau salah satu source bermasalah**.

Ini adalah transisi penting dari:
> “script jalan”  
> “system tetap jalan”

---

## Sumber Data
1. **Web**
   - Website quotes (dynamic content)
   - Diekstrak menggunakan Playwright

2. **API**
   - Public API: `api.quotable.io`
   - Diakses menggunakan `requests`

---

## Struktur Data (Unified Schema)

Semua data, baik dari web maupun API, distandarkan ke format:

| Field   | Description                  |
|--------|------------------------------|
| text   | Isi quote                    |
| author | Nama author                  |
| tags   | List tag terkait             |
| source | Asal data (`web` / `api`)    |

---

## Flow Sistem

1. Ambil data dari **web**
2. Ambil data dari **API**
3. Jika API gagal (SSL / timeout):
   - Sistem **tidak berhenti**
   - Tetap lanjut dengan data web
4. Gabungkan semua data
5. Simpan ke CSV

---

## Error Handling yang Diterapkan

- `try / except` pada API request
- Timeout request
- SSL verification **dimatikan secara sadar** (`verify=False`)
- Sistem tetap menghasilkan output walau API error

 Muncul warning:




