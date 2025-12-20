# Cleaning Engine V2 - Level 2 Day 7 (Professional)

## Deskripsi
Pipeline akhir Level 2 untuk Data Cleaning Automation:
- Column Cleaner
- Missing Values Handler
- Numeric Cleaner
- Date Standardization
- Auto file detection
- Configurable via config.json
- Logging & auto rename output

## Struktur Folder
- config.json: konfigurasi rules pipeline
- data_input/: dataset mentah
- data_output/: hasil clean dengan prefix + timestamp
- logs/: log proses cleaning
- cleaning_functions.py: semua fungsi reusable
- file_loader.py: load file otomatis
- main.py: jalankan pipeline

## Cara Pakai
1. Taruh file CSV/XLS/XLSX/TSV di data_input/
2. Jalankan `python main.py`
3. File bersih tersimpan di data_output/ dengan auto rename
4. Cek log di folder logs/
