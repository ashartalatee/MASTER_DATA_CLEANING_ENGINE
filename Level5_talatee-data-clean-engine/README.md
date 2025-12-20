# Talatee Data Clean Engine
LEVEL 5 — DATA CLEANER (PROFESSIONAL)

 Repo: `talatee-data-clean-engine`  
 Prinsip: **1 Repo → 1 Engine → Dipoles 30 Hari**

Engine ini **bukan kumpulan script**, tapi **mesin pembersih data berbasis aturan (rule-based)**  
yang siap dipakai ulang, dikembangkan, dan dipertanggungjawabkan.

---

## DAY 1 — Struktur Repo Profesional

### Tujuan Hari Ini
Memahami bahwa **engine butuh struktur sejak awal**, bukan nanti.

### Yang Sudah Bisa
- Paham kenapa project data **tidak boleh tumbuh liar**
- Bisa membedakan:
  - engine
  - config
  - data
  - logs
- Paham bahwa struktur = disiplin berpikir

### Yang Dikerjakan
Membuat struktur folder final (TIDAK diubah sembarangan):


### Kenapa Harus Begini?
- **Tanpa struktur → engine berubah jadi script sekali pakai**
- Folder memaksa kita **berpikir modular**
- Ini struktur yang **Level 6–7 tidak perlu bongkar ulang**

> DAY 1 bukan tentang coding.  
> DAY 1 adalah tentang **mendisiplinkan otak sebelum nulis kode**.

---

## DAY 2 — Filosofi & Rule Cleaning

### Tujuan Hari Ini
Memahami bahwa **data cleaning ≠ coding**,  
tapi **mendefinisikan apa itu “data benar”**.

### Yang Sudah Bisa
- Paham bahwa cleaning harus berbasis **aturan (rules)**
- Bisa membedakan:
  - data kotor
  - data salah
  - data tidak valid
- Tidak lagi langsung nulis kode saat lihat data rusak

### Yang Dikerjakan
- Menentukan **prinsip dasar Talatee Clean Engine**, seperti:
  - Data harus dicegah sebelum dipakai
  - Lebih baik fail fast daripada silent error
  - Rule dulu, kode belakangan

### Kenapa Harus Begini?
- Kode bisa berubah, **aturan tidak**
- Tanpa filosofi:
  - tiap dataset diperlakukan beda
  - engine tidak konsisten
- Engine profesional **punya pendirian**

> DAY 2 membangun **karakter engine**, bukan fiturnya.

---

## DAY 3 — Cleaning Rules Config (`cleaning_rules.yaml`)

### Tujuan Hari Ini
Memisahkan **aturan cleaning** dari **kode engine**.

### Yang Sudah Bisa
- Paham kenapa rule **HARUS di config**
- Bisa membaca dan memahami struktur rule
- Paham bahwa engine harus **fleksibel tanpa diubah kodenya**

### Yang Dikerjakan
- Membuat `config/cleaning_rules.yaml`
- Menaruh hal-hal seperti:
  - required columns
  - data type
  - range logika
  - strategi missing value

### Kenapa Harus Begini?
- Dataset berubah → **engine tetap**
- Rule bisa diubah tanpa sentuh Python
- Ini yang membedakan:
  - **engine** vs **script pembersih**

> DAY 3 adalah momen engine mulai “hidup”.

---

## DAY 4 — Data Schema (Definisi Data Ideal)

### Tujuan Hari Ini
Mendefinisikan **seperti apa data yang BENAR**,  
bukan cuma membersihkan yang salah.

### Yang Sudah Bisa
- Bisa mendefinisikan:
  - nama kolom
  - tipe data
  - ekspektasi nilai
- Paham bahwa **data buruk harus dikenali, bukan ditoleransi**

### Yang Dikerjakan
- Menuliskan schema data:
  - kolom wajib
  - tipe: numeric / text / date
- Menjadikan schema sebagai **patokan validasi**

### Kenapa Harus Begini?
- Tanpa schema:
  - validator tidak punya pegangan
  - data salah bisa lolos diam-diam
- Schema adalah **kontrak antara data dan engine**

> DAY 4 memastikan engine tahu **apa yang ia lindungi**.

---

## BENANG MERAH DAY 1–4

Jika diringkas:

- **DAY 1** → Disiplin struktur
- **DAY 2** → Disiplin berpikir
- **DAY 3** → Disiplin aturan
- **DAY 4** → Disiplin definisi data

Belum banyak kode — **dan itu disengaja**.

> Engine kuat bukan karena banyak fitur,  
> tapi karena **fondasinya tidak goyah**.

---

## Catatan untuk Ashar (6 Bulan ke Depan)

Kalau kamu baca ini lagi dan merasa:
> “Oh iya… masuk akal.”

Berarti kamu **berhasil**.

Kalau kamu bingung:
- Jangan lanjut fitur
- Kembali ke DAY 2 (filosofi)

---

 **Status:**  
DAY 1–4 ✔️ PAHAM  
Engine siap masuk **validasi & enforcement (DAY 5+)**

## DAY 5 — Validator: Required Columns

### Tujuan Hari Ini
Mencegah data rusak **masuk ke engine sejak awal**.

### Yang Sudah Bisa
- Engine bisa **menolak dataset tidak sah**
- Bisa membedakan error fatal vs error bisa dibersihkan
- Paham bahwa missing column = STOP

### Yang Dikerjakan
- Membuat `DataValidator`
- Validasi `required_columns` dari config
- Raise error kalau kolom wajib hilang

### Kenapa Harus Begini?
- Kolom hilang tidak bisa ditebak
- Semua logic setelahnya akan salah
- Data salah **lebih berbahaya** dari data kosong

> DAY 5 adalah titik engine mulai punya **wibawa**.
