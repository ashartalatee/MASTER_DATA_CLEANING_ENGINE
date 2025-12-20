# Full Cleaning Pipeline V1 - Level 2 Day 5

## Deskripsi
Pipeline otomatis end-to-end: 
1. Rename kolom
2. Handle missing values
3. Convert numeric
4. Standardize date

## Struktur Folder
- `data_input/` : file mentah
- `data_output/` : file hasil clean lengkap
- `cleaning_functions.py` : semua fungsi reusable
- `main.py` : jalankan full pipeline

## Cara Pakai
1. Taruh file CSV di `data_input/`
2. Jalankan `python main.py`
3. File bersih tersimpan di `data_output/`
