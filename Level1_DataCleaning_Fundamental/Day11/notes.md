# Day 11 – Perbaikan Typo & Data Acak

## Tujuan Hari Ini
- Mendeteksi dan memperbaiki typo umum di data.
- Mengidentifikasi nilai-nilai yang tidak wajar (outliers teks).
- Membersihkan karakter acak, simbol, atau input yang tidak relevan.
- Mengenali pola kesalahan manusia dalam input data.

---

## Masalah pada Dataset
Dari dataset hari ini, ditemukan:
1. Nama terdapat angka atau simbol (contoh: "A$har", "Bu-di2")
2. Email mengandung karakter tidak valid (contoh: "rosi@@mail.com")
3. Kategori berisi varian typo (contoh: "pendng", "pendding", "pendng ")
4. Ada nilai random seperti:
   - "???"
   - "-"
   - "none"
   - "asdf123"

---

## Langkah-langkah Perbaikan
1. Menghapus karakter non-alfabet pada kolom nama.
2. Menghapus simbol tidak relevan (misal: "%", "$", "#", "!").
3. Menormalisasi kolom kategori menggunakan dictionary mapping.
4. Menghapus baris yang benar-benar rusak/tidak bisa diselamatkan.
5. Memvalidasi email dengan pola regex.

---

## Hasil Setelah Cleaning
- Tidak ada lagi karakter asing pada nama.
- Email invalid difilter atau diperbaiki jika memungkinkan.
- Kategori sudah konsisten setelah mapping.
- Data acak sudah dibersihkan atau ditandai.

---

## Yang Masih Membingungkan
(isi sesuai kondisimu)
Contoh:
- Cara memperbaiki email rusak, tidak hanya membuangnya.
- Cara deteksi typo otomatis tanpa mapping manual.

---

## Catatan untuk Masa Depan
- Data manusia selalu mengandung typo.
- Gunakan pendekatan regex + mapping untuk mempercepat cleaning.
- Typo handling adalah dasar dari data normalization.

