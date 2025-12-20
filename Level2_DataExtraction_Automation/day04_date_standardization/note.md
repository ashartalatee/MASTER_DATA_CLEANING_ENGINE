# Day 4: Date Standardization Engine

## Tujuan
Otomatis mengubah semua kolom tanggal ke format standar ISO (YYYY-MM-DD)

## Kenapa penting
- Tanggal sering berantakan (dd/mm/yyyy, mm-dd-yyyy, 01 Jan 2025)
- Pipeline gagal jika format tanggal tidak konsisten
- Diperlukan untuk scraping, API, dan Excel custom date
- Skill langka untuk Data Engineer

## Tips
- Gunakan dateutil.parser untuk fleksibilitas parsing
- Cek dataset besar untuk format tidak standar
