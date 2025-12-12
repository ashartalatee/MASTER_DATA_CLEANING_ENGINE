# Numeric Cleaner Engine - Level 2 Day 3

## Deskripsi
Project ini otomatis convert kolom numeric ke tipe float/int.
Mendukung pipeline data automation Level 2.

## Struktur Folder
- `data_input/` : file mentah
- `data_output/` : file hasil clean + numeric
- `cleaning_functions.py` : fungsi reusable
- `main.py` : run column cleaner + NaN handler + numeric conversion

## Cara Pakai
1. Taruh file CSV di `data_input/`
2. Jalankan `python main.py`
3. File bersih + numeric conversion tersimpan di `data_output/`
