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

 # Day 8 — Retry, Timeout & Circuit Breaker

## Tujuan
Meningkatkan extractor dari **“bisa jalan”** menjadi **“tahan error & layak produksi”**  
dengan menerapkan pola dasar **resilient system**:

- Retry otomatis
- Timeout yang jelas
- Circuit breaker (pengaman saat API rusak)

---

## Masalah Dunia Nyata yang Disimulasikan
- API sering:
  - SSL error
  - Timeout
  - Tidak stabil
- Jika tidak diantisipasi:
  - Script hang
  - Pipeline mati
  - Automation gagal total

Day 8 mengajarkan:
> **Error itu pasti. Sistem yang baik sudah siap sebelum error datang.**

---

## Konsep Teknis yang Diterapkan

## Retry dengan Backoff
- Request API dicoba beberapa kali
- Jika gagal → tunggu → coba lagi
- Waktu tunggu meningkat setiap percobaan

Tujuan:
- Tidak langsung menyerah
- Tidak membanjiri server

---

## Timeout
- Request dibatasi waktu (`timeout=5`)
- Jika lewat batas → dianggap gagal

Tujuan:
- Script tidak freeze
- Pipeline tetap mengalir

---

### Circuit Breaker (Versi Sederhana)
- Jika API gagal berkali-kali:
  - Sistem **berhenti mencoba**
  - Source dianggap “mati sementara”
- Pipeline tetap jalan tanpa API

Tujuan:
- Melindungi sistem utama
- Fokus ke reliability, bukan ego script

---

## Flow Sistem

1. Request API dengan retry & timeout
2. Jika sukses → data diproses
3. Jika gagal berulang:
   - Circuit breaker aktif
   - API dilewati
4. Sistem tetap menghasilkan output CSV

# Day 9 — Data Validation & Schema Enforcement

## Tujuan
Membangun **QUALITY GATE** pada data hasil extraction agar:
- Hanya data valid yang lolos
- Data rusak / tidak sesuai schema **ditolak**
- Pipeline stabil dan siap naik level (warehouse / AI / business system)

Hari ini adalah **pemisah antara scraper dan Data Engineer**.

---

## Konsep Utama

### Schema Enforcement
Data **HARUS** mengikuti kontrak berikut:

| Field   | Aturan Wajib                          |
|--------|----------------------------------------|
| text   | String, tidak kosong                   |
| author | String, tidak kosong                   |
| tags   | List                                  |
| source | Hanya `web` atau `api`                 |

Jika satu saja melanggar → **row ditolak**

---

### Validation Rule (Rule-Based)
- Tidak pakai tebakan
- Tidak pakai asumsi
- Semua aturan eksplisit & konsisten

---

### Quality > Quantity
> 20 data valid > 1.000 data sampah

# Day 10 — Final Extraction Pipeline  
## Level 4: Data Extractor Advanced (COMPLETE)

---

## Tujuan Day 10
Menyatukan seluruh proses **Level 4 (Day 3–Day 9)** menjadi **SATU PIPELINE UTUH**:

> **One command → data siap pakai**

Pipeline ini bukan sekadar script,
melainkan **MESIN EKSTRAKSI DATA tahan error**.

---

## Masalah Dunia Nyata yang Diselesaikan

- Data datang dari **banyak sumber**
- API bisa error / SSL bermasalah
- Web bisa berubah
- Data mentah sering rusak

 Solusi: **Pipeline modular, fault-tolerant, dan tervalidasi**
