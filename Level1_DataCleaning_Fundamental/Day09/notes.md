# Day 9 — Handling Missing Values (Remove / Replace)

## 1. Kenapa Missing Values Berbahaya?
- Bikin perhitungan statistik salah
- Chart / Dashboard error
- Machine learning tidak bisa dilatih
- Bisa membuat analisis bisnis meleset jauh

## 2. Jenis Missing Values
- NaN (null)
- Empty string ""
- Format yang gagal dibaca (tanggal invalid)
- Placeholder seperti: "?", "-", "none"

## 3. Strategi Hari Ini
### Numerik → median  
Kenapa?
- Median lebih stabil dibanding mean
- Tidak terpengaruh outlier

### Kategori → mode  
Kenapa?
- Mode = nilai paling umum
- Cocok untuk gender, kota, kategori, status

### Drop?  
Tidak dipakai hari ini, hanya jika:
- Baris benar-benar rusak
- Kolom tidak penting

## 4. Temuan Hari Ini
- Kolom mana saja yang missing
- Berapa banyak
- Bagaimana cara memperbaikinya

## 5. Output
- dataset_clean.csv → sudah tidak ada missing
- day09_missing_report.csv → laporan lengkap

## 6. Rencana Day 10
➡ **Standarisasi Format (tanggal, teks, angka)**  
Ini bagian penting sebelum masuk normalisasi dan typology fixes.
