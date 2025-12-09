# Day 8 — Menghapus Duplikat (Manual + Python)

## 1. Pengertian Duplikat
Duplikat adalah baris data yang sama persis dengan baris lainnya.
Masalah ini sangat umum pada:
- Data customer
- Data transaksi
- Data lead marketing
- Export dari CRM
- Excel yang digabung dari banyak sumber

## 2. Temuan Hari Ini
- Jumlah baris awal: (isi setelah menjalankan script)
- Jumlah duplikat: (isi dari day08_summary.csv)
- Jumlah baris akhir: (isi dari day08_summary.csv)

## 3. Cara Manual di Excel (yang saya lakukan)
1. Select seluruh tabel
2. Menu → Data → Remove Duplicates
3. Pilih kolom yang ingin dicek
4. Klik OK
5. Catat berapa baris hilang

## 4. Cara Python (yang saya lakukan)
- Menggunakan `df.duplicated()`
- Menampilkan contoh baris duplikat
- Menghapus menggunakan `df.drop_duplicates()`
- Menyimpan `dataset_clean.csv`

## 5. Insight Hari Ini
- Duplikat sering terlihat sepele tapi sangat merusak analisis
- Tanpa remover duplikat, angka penjualan/UMKM bisa meleset besar
- Automasi Python jauh lebih cepat daripada Excel

## 6. Rencana Day 9
Kita akan masuk ke:
➡ **Handling Missing Values**  
(Bagian paling fundamental dari data cleaning)
