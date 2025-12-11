# Day 14 – Compare Before vs After

## Masalah Awal
- Duplicate: ID 1 & 4
- Missing Email: ID 3
- Typo Email: ID 5 (`eve@exmaple.com`)
- Missing Amount: ID 7
- Format tanggal tidak konsisten (DD-MM-YYYY & YYYY/MM/DD)

## Langkah Cleaning
1. Hapus duplicate
2. Isi missing values:
   - Email → "unknown@example.com"
   - Amount → 0
3. Koreksi typo email (exmaple → example)
4. Standarisasi format tanggal ke YYYY-MM-DD

## Hasil
- Duplicate dihapus
- Missing values diisi
- Typo diperbaiki
- Format tanggal konsisten
- Total rows: 6 (awal 7)
- Total columns: 5 (tidak berubah)

## Insight
- Bisa lihat perbedaan jelas sebelum dan sesudah cleaning
- Bandingkan sebelum/ sesudah penting untuk evaluasi kualitas data
- Notes jelas membantu saat revisi atau automation nanti
