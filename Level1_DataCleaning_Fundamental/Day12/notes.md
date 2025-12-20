# Day 12 – Normalisasi Kolom (Nama, Email, Phone)

## Tujuan Hari Ini
- Membuat format nama konsisten dan mudah dibaca.
- Membersihkan dan menormalisasi email (lowercase, tanpa spasi).
- Menstandarkan nomor telepon:
  - Buang simbol
  - Buang 0 di depan
  - Pastikan format internasional (+62)

---

## Masalah pada Dataset
Ditemukan beberapa masalah:
1. Nama:
   - Banyak spasi ganda
   - Ada karakter asing
   - Format campur uppercase / lowercase

2. Email:
   - Ada spasi di tengah
   - Huruf kapital
   - Format tidak konsisten

3. Phone:
   - Format bervariasi:
     - 0812-3456-7890
     - +6281234567890
     - 81234567890
     - (0812) 3456 7890
   - Mengandung simbol dan spasi

---

## Langkah-langkah Normalisasi
1. Membersihkan seluruh spasi berlebih.
2. Nama → Title Case (kecuali brand tertentu)
3. Email → lowercase + hapus whitespace
4. Phone:
   - Hapus simbol: `() - .`
   - Jika mulai dari 0 → ubah ke +62
   - Jika mulai dari 62 → tambahkan + di depan
   - Jika mulai dari 8 → tambahkan +62

---

## Hasil Setelah Cleaning
- Semua nama rapi dan seragam.
- Email aman untuk analisis / login / CRM.
- Nomor telepon sudah dalam format internasional: +62xxxxxxxxxx

---

## Yang Masih Membingungkan
(Tulis sesuai kondisimu)
Contoh:
- Cara menangani nomor telepon yang terlalu pendek / terlalu panjang.
- Cara deteksi nomor fake.

---

## Catatan untuk Masa Depan
- Phone normalization wajib ketika integrasi data WA/CRM.
- Lowercase email = menghindari duplikat palsu.
- Title Case nama memudahkan readability di dashboard dan laporan.

