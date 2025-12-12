# Day 2: Missing Values Handler

## Tujuan
Otomatisasi handling missing values setelah kolom rapi.

## Kenapa penting
- NaN menyebabkan perhitungan gagal
- Join / merge / filter data gagal
- Model AI gagal jika ada missing value

## Strategi
1. Fill: isi NaN dengan default value (contoh: 0, "unknown")
2. Drop: hapus baris dengan NaN
