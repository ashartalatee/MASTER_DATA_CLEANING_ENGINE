# Day 6 — Analisis Struktur Kolom & Tipe Data

## 1. Struktur Umum Dataset
- Jumlah baris: (isi setelah menjalankan script)
- Jumlah kolom: (isi setelah menjalankan script)
- Nama-nama kolom:
  - col1
  - col2
  - col3
  - ...

## 2. Tipe Data Saat Ini (Hasil df.info())
Tuliskan seperti:

- name -> object (seharusnya string ✓)
- age -> object (salah, harus integer)
- price -> object (salah, harus float)
- date_joined -> object (salah, harus datetime)
- gender -> object (perlu standarisasi)
- phone -> object (harus dinormalisasi)

## 3. Masalah yang Ditemukan
Contoh masalah (sesuaikan dataset kamu):

- Umur berisi teks campur angka → tidak konsisten
- Format tanggal campur: `12-03-2023`, `2023/03/12`
- Kolom price pakai simbol `Rp` → dianggap string
- Gender tidak konsisten: `M`, `Male`, `Pria`
- Phone number campuran `08`, `+62`, dan teks
- Ada kolom kosong tanpa makna
- Ada angka yang seharusnya float tapi disimpan sebagai string

## 4. Apa yang Harus Diperbaiki (Persiapan Day 7)
- Konversi umur ke integer
- Standarisasi format tanggal
- Bersihkan simbol mata uang pada price
- Standarisasi gender
- Normalisasi nomor HP
- Hilangkan kolom tidak penting
- Re-assign tipe data yang benar

## 5. Kesimpulan Hari Ini
Masukkan pemahamanmu contoh:

Hari ini saya lebih paham bahwa:
- Data terlihat rapi tapi tipe datanya sering salah
- df.info() sangat penting sebelum cleaning
- Struktur kolom menentukan strategi cleaning
- Besok saya siap membuat laporan masalah lengkap (Day 7)
