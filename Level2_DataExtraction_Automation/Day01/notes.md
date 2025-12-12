# Day 1 — Mindset Automation & Pattern Extraction

## Tujuan
Menganalisis ulang dataset Level 1 untuk menemukan pola berulang yang bisa
diotomatisasi di Level 2.

---

## 1. Dataset yang Dianalisis
- transaksi.csv  
- users_raw.xlsx  
- ecommerce_data.csv  
- produk_list.xlsx  
- survey_raw.csv  
- ... (tambahkan sesuai Level 1)

---

## 2. Pola Berulang yang Ditemukan

### A. Kolom (Column Issues)
- Nama kolom tidak konsisten (uppercase/lowercase).
- Banyak spasi, karakter aneh.
- Ada typo pada nama kolom.

### B. Missing Values
- Banyak kolom memiliki NA.
- Tipe numerik → hilang secara acak.
- Tipe kategorikal → banyak blank string.

### C. Format Tidak Konsisten
- Tanggal memiliki 4–5 format berbeda.
- Angka menggunakan koma/titik berbeda.
- Boolean tidak konsisten antar dataset.

### D. Duplicates
- Banyak data duplikat persis.
- Ada dataset yang duplikat berdasarkan ID saja.

### E. Typo Values
- Kota: *Jakrta*, *Bandunng*, *Surabyaa*
- Email tidak valid.

### F. Outliers
- Nilai umur ekstrem (0, 200).
- Harga negatif.

---

## 3. Insight untuk Level 2 Automation

| Pola | Konsekuensi | Solusi Automasi | Modul |
|------|-------------|------------------|-------|
| Kolom tidak konsisten | Error saat merge/join | Column Standardizer | `standardize_columns.py` |
| Missing values | Model gagal analisa | Auto fill strategy | `clean_missing.py` |
| Format tanggal acak | Analisis waktu error | Auto detect parser | `normalize_format.py` |
| Duplikat | Hasil analisa palsu | Auto de-dupe + log | `clean_duplicates.py` |
| Typo | Banyak noise | Rule-based correction | `/engine/rules/` |
| Outlier | Insight salah | Validator + warning | `validation.py` |

---

## 4. Kenapa Day 1 Penting
Day 1 adalah fondasi seluruh automation Level 2.

Jika pola tidak dipahami:
 Engine akan acak-acakan  
 Error di Level 3–10  
 Tidak reusable untuk klien  

Dengan memahami pola:
 kamu bisa membangun ENGINE seperti perusahaan besar  
 setiap modul punya tujuan jelas  
 scaling & batch automation jadi mudah  

---

## 5. Next Step (Day 2)
Membangun struktur folder profesional:
`engine/`, `input/`, `output/`, `logs/`, `config/`.
