# Day 17 – Template Script Cleaning (Versi Profesional)

## Tujuan Hari Ini
- Membuat dasar script cleaning yang bisa dipakai untuk berbagai dataset.
- Mulai membangun pola “pipeline cleaning” seperti engineer beneran.
- Menyiapkan pondasi untuk automasi (Level 2 & 3).

---

## Isi Script
Script memiliki modul:
1. **normalize_date()** → standarisasi tanggal
2. **clean_phone()** → ubah jadi format 62, hilangkan simbol/spasi
3. **clean_email()** → perbaiki typo, lowercase, hilangkan spasi
4. **clean_dataset()** → pipeline utama:
   - Remove duplicate  
   - Clean email  
   - Clean phone  
   - Fix missing numeric  
   - Normalize date  

Output akhir:
- dataset_clean.csv

---

## Insight
Tulis minimal 3:
1. Saya mulai melihat pola automasi: cleaning = pipeline.
2. Fungsi modular membuat pekerjaan rapi dan aman.
3. Script ini akan sangat membantu untuk Day18–Day21.

---

## Hal yang Masih Bingung
- …
- …

---

## File Hari Ini
- dataset_sample.csv  
- cleaning_template.py  
- notes.md  
