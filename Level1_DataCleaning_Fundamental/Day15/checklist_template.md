# Data Cleaning Checklist – Template

Gunakan checklist ini untuk setiap dataset sebelum mulai cleaning.

---

## 1. Struktur Dataset
- [ ] Cek jumlah baris & kolom
- [ ] Cek tipe data per kolom
- [ ] Identifikasi kolom ID (unik atau tidak)

---

## 2. Missing Values
- [ ] Identifikasi kolom yang punya missing value
- [ ] Tentukan strategi (drop / fill / placeholder)
- [ ] Catat alasan memilih metode

---

## 3. Duplicate
- [ ] Cek duplikat berdasarkan seluruh baris
- [ ] Cek duplikat berdasarkan kolom ID / Email / Phone
- [ ] Tentukan mana yang harus dibuang atau digabung

---

## 4. Format Konsisten
- [ ] Tanggal → YYYY-MM-DD
- [ ] Phone → tanpa spasi / tanda / uniform
- [ ] Email → lowercase & valid format
- [ ] Nama → Title Case
- [ ] Amount → numeric

---

## 5. Typo & Validasi
- [ ] Validasi email (regex)
- [ ] Perbaiki typo yang umum
- [ ] Normalisasi nama (hapus karakter aneh)
- [ ] Normalisasi phone (hapus simbol, convert ke +62)

---

## 6. Business Rules (Opsional)
- [ ] Amount tidak boleh negatif
- [ ] JoinDate tidak mungkin di masa depan
- [ ] Phone minimal panjang 9 digit

---

## 7. Final Review
- [ ] Hitung ulang shape data
- [ ] Pastikan tidak ada duplikat
- [ ] Pastikan missing values sesuai ekspektasi
- [ ] Simpan `dataset_clean.csv`
- [ ] Dokumentasi lengkap di `notes.md`

---

Checklist ini wajib kamu bawa terus sampai Level 2 & Level 3.
