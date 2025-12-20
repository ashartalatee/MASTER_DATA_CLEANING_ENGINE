# Missing Values Handler - Level 2 Day 2

## Deskripsi
Project ini menghandle missing values secara otomatis setelah kolom rapi.
Mendukung pipeline data automation di Level 2.

## Struktur Folder
- `data_input/` : file mentah
- `data_output/` : file hasil clean + NaN handled
- `cleaning_functions.py` : fungsi reusable
- `main.py` : run column cleaner + NaN handler

## Cara Pakai
1. Taruh file CSV di `data_input/`
2. Jalankan `python main.py`
3. File bersih + NaN handled tersimpan di `data_output/`
