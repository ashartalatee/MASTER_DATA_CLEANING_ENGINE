# Day 7 — Laporan Masalah Dataset

## 1. Tujuan Hari Ini
Membuat laporan lengkap tiap kolom untuk:
- Mengetahui tipe data
- Menemukan missing / duplicate
- Mengecek typo / inkonsistensi
- Menyiapkan panduan cleaning besok

## 2. Ringkasan Masalah (Contoh)
| Column       | Type   | Unique | Issues                                      |
|--------------|--------|--------|---------------------------------------------|
| name         | object | 50     | Possible typo/category inconsistency       |
| age          | object | 40     | Missing values: 2                          |
| price        | object | 30     | Missing values: 1; Possible typo/category |
| date_joined  | object | 25     | None                                        |
| gender       | object | 3      | Possible typo/category inconsistency       |
| phone        | object | 48     | None                                        |

## 3. Insight
- Kolom `age` & `price` perlu konversi tipe data
- `name` & `gender` perlu normalisasi/standarisasi
- `date_joined` perlu format seragam
- Phone number perlu standardisasi

## 4. Rencana Day 8
- Cleaning dasar: missing values, duplicate removal
- Konversi tipe data
- Standarisasi format text & date
- Normalisasi kolom penting
