# Day 13 – Script Python Sederhana (Awal Automation)

## Tujuan Hari Ini
- Membuat script Python yang bisa:
  - Membaca data
  - Membersihkan data dasar
  - Menyimpan data bersih otomatis
- Memulai kebiasaan menulis script reusable.

---

## Konsep yang Dipelajari
1. Struktur script yang rapi.
2. Separation of concerns:
   - Bagian load data
   - Bagian cleaning
   - Bagian export
3. Fungsi (def) untuk modularisasi.
4. Pola "input → proses → output".

---

## Masalah dalam Dataset
- Spasi berlebih
- Huruf kapital tidak konsisten
- Format date tidak seragam
- Kolom city dan category tidak rapi

Datasetnya memang sederhana, tapi latihan ini untuk memulai automation.

---

## Langkah Script
1. Definisikan fungsi `load_data()`
2. Definisikan fungsi `clean_data()`
3. Definisikan fungsi `save_data()`
4. Definisikan `main()` agar script bisa dieksekusi langsung

---

## Hasil
- Script berhasil jalan tanpa error.
- Data otomatis dibersihkan.
- Tidak ada lagi buka Excel manual.

---

## Yang Masih Bingung
(Tulis sesuai kondisi)
Contoh:
- Cara membuat argumen dinamis (misal path dataset).
- Bagaimana membuat fungsi menjadi class.

---

## Catatan Penting
- Ini fondasi automation.
- Hari ini bukan fokus pada teknik cleaning yang sulit,
  tapi mindset membuat script yang reusable dan rapi.
