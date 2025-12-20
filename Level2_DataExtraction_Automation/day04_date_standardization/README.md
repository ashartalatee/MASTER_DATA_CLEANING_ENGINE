# Date Standardization Engine - Level 2 Day 4

## Deskripsi
Project ini otomatis standardisasi semua kolom tanggal ke format ISO.
Mendukung pipeline data automation Level 2.

## Struktur Folder
- `data_input/` : file mentah
- `data_output/` : file hasil clean + numeric + tanggal standar
- `cleaning_functions.py` : semua fungsi reusable
- `main.py` : run semua fungsi Level 1–4

## Cara Pakai
1. Taruh file CSV di `data_input/`
2. Jalankan `python main.py`
3. File bersih + tanggal standar tersimpan di `data_output/`
