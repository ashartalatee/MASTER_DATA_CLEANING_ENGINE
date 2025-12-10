# Day 10 – Standarisasi Format (Tanggal & Teks)

## Tujuan Hari Ini
- Memahami pentingnya konsistensi format sebelum analisis.
- Standarisasi format tanggal ke format universal: YYYY-MM-DD.
- Merapikan format teks (nama, email, kategori).

---

## Masalah pada Dataset
Dari dataset yang saya gunakan hari ini, ditemukan masalah:
1. Format tanggal tidak konsisten:
   - Ada format: 12/01/2024
   - Ada format: 2024-01-12
   - Ada format: 12 Jan 24
2. Kolom nama masih campur uppercase/lowercase.
3. Email banyak spasi + huruf kapital.
4. Kolom kategori tidak seragam:
   - "Paid", " paid", "PAID", "paid ".

---

## Langkah-langkah Cleaning
1. Menghapus spasi di kiri–kanan semua kolom teks.
2. Mengubah nama menjadi Title Case → lebih mudah dibaca.
3. Mengubah email menjadi lowercase → penting untuk validasi duplikat.
4. Membersihkan kategori menjadi lowercase & tanpa spasi.
5. Mengubah semua format tanggal menjadi standar YYYY-MM-DD menggunakan `pd.to_datetime`.

---

## Hasil Setelah Cleaning
- Semua tanggal sukses diubah ke format YYYY-MM-DD.
- Nama konsisten dan rapi.
- Email aman untuk analisis & kampanye.
- Kategori bersih, siap untuk grouping dan analisis.

---

## Hal yang Masih Membingungkan
(Tulis jujur)
Contoh:
- Cara mendeteksi format tanggal otomatis ketika sangat beragam.
- Mengapa beberapa tanggal berubah menjadi NaT (Not a Time).

---

## Catatan Penting untuk Masa Depan
- Sebelum join/merge dataset lain, selalu samakan format tanggal dulu.
- Kolom email harus lowercase sebelum cek duplikat.
- Title Case untuk kolom nama meningkatkan readability.
- Standarisasi format adalah fondasi utama sebelum automation.

---
