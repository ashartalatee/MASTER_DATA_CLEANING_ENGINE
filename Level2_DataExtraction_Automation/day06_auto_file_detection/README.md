# Auto File Detection Pipeline - Level 2 Day 6

## Deskripsi
Pipeline otomatis mendeteksi jenis file dataset:
- CSV
- XLS/XLSX
- TSV

Pipeline kemudian menjalankan cleaning:
1. Column Cleaner
2. Missing Values Handler
3. Numeric Cleaner
4. Date Standardization

## Struktur Folder
- data_input/: file mentah
- data_output/: file hasil clean
- cleaning_functions.py: semua fungsi reusable
- file_loader.py: load file otomatis
- main.py: jalankan pipeline

## Cara Pakai
1. Taruh file CSV/XLS/XLSX/TSV di data_input/
2. Jalankan `python main.py`
3. File bersih tersimpan di data_output/
