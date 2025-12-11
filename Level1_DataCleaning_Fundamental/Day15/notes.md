# Day 15 – Checklist Data Cleaning (Versi Profesional)

## Tujuan Hari Ini
- Menyusun checklist data cleaning agar proses berpikir selalu rapi.
- Menganalisis dataset menggunakan skrip otomatis.
- Membiasakan pola pikir sistematis sebelum cleaning.

---

## Dataset yang Digunakan
Nama file: `dataset.csv`  
Jumlah baris: **5**  
Jumlah kolom: **6**

---

## Hasil Analisa (Output script_checklist.py)

### Basic Info
- Ada 4 kolom bertipe object
- Ada 1 kolom bertipe int64
- Ada 1 kolom bertipe float64  
- Kolom `FullName` dan `Amount` memiliki missing values

### Shape
- Baris: **5**
- Kolom: **6**

### Missing Values
- `FullName`: 1 missing
- `Amount`: 1 missing

### Duplicate Check
Hasil visual menunjukkan **duplikat pada baris ID 1 & 4** (Alice Johnson – sama persis).

### Sample Rows
Dataset menunjukkan:
- Format tanggal tidak konsisten:
  - `2023/02/01`
  - `01-02-2023`
  - `2023-02-01`
  - `03/02/23`
- Email bermasalah:
  - `bob@example` (tidak valid)
  - `eve@@example.com` (dobel @)
- Phone tidak konsisten:
  - `0812-3456-789`
  - `0812 9999 000`
  - `8123456780`
  - `628123456789`

---

## Checklist Data Cleaning (Yang Dibuat Hari Ini)
1. **Struktur Dataset**
   - Cek shape, tipe data, ID unik

2. **Missing Values**
   - Identifikasi kolom yang missing
   - Pilih strategi (drop/fill)

3. **Duplicate**
   - Cek duplicate full-row
   - Cek duplicate berdasarkan ID/email/phone

4. **Standarisasi Format**
   - Tanggal harus YYYY-MM-DD
   - Email lowercase dan valid
   - Nama Title Case
   - Phone distandarisasi (tanpa spasi/simbol)

5. **Typo & Validasi**
   - Validasi email dengan regex
   - Cek typo umum
   - Normalisasi phone jadi format +62xxx

6. **Business Rules**
   - Amount tidak boleh kosong
   - Date tidak boleh future date

7. **Final Review**
   - Cek ulang shape
   - Pastikan missing sudah ditangani
   - Simpan dataset_clean.csv

---

## Insight Hari Ini
1. Checklist membuat pola kerja repetitif jadi otomatis dan profesional.  
2. Script otomatis membantu menganalisa struktur data dengan cepat.  
3. Dataset kecil seperti ini sudah banyak masalah — cocok untuk latih intuisi.

---

## Hal yang Masih Bingung
Tuliskan sendiri:
- …
- …

---

## File Hari Ini
- `dataset.csv`
- `checklist_template.md`
- `notes.md`
- `script_checklist.py`
