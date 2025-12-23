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

## DAY 6 — Validator: Data Type

### Tujuan Hari Ini
Mencegah **silent error** akibat tipe data salah.

### Yang Sudah Bisa
- Engine bisa mendeteksi data yang “kelihatan benar tapi salah”
- Bisa memisahkan tugas validator vs cleaner
- Tidak lagi percaya data mentah

### Yang Dikerjakan
- Menambahkan validasi tipe data berbasis schema
- Menolak dataset dengan tipe tidak sesuai
- Menghentikan pipeline sebelum data berbohong

### Kenapa Harus Begini?
- Error diam-diam lebih berbahaya dari error keras
- Analisis salah tapi tidak sadar = bencana bisnis
- Validator harus galak, cleaner baru ramah

> DAY 6 adalah hari engine belajar **tidak percaya data**.

## DAY 7 — Validator: Range & Logic (FINAL)

### Tujuan Hari Ini
Mencegah data yang **secara teknis valid tetapi tidak masuk akal secara logika**.

### Yang Sudah Bisa
- Engine bisa menolak nilai mustahil (negative amount, future date, dll)
- Bisa membedakan:
  - valid secara tipe
  - valid secara makna
- Engine tidak lagi “percaya buta” pada angka

### Yang Dikerjakan
- Menambahkan validasi range (min / max)
- Menambahkan validasi logika (future date tidak boleh)
- Menghentikan pipeline jika nilai melanggar akal sehat

### Kenapa Harus Begini?
- Data salah lebih berbahaya dari data kosong
- Angka valid tapi salah bisa merusak keputusan bisnis
- Validator bertugas menjaga **makna data**, bukan tampilannya

### Posisi DAY 7 di Engine
Urutan validasi WAJIB:
1. Required columns
2. Data type
3. Range & logic
4. Baru masuk cleaning

Jika urutan dibalik → engine tidak jujur.

> DAY 7 adalah hari engine belajar **berpikir waras**.

## DAY 8 — Missing Value Strategy

### Tujuan Hari Ini
Menangani data kosong **secara sadar dan terkontrol**.

### Yang Sudah Bisa
- Engine bisa membedakan NaN yang boleh hidup vs harus mati
- Tidak lagi menyamaratakan missing value
- Cleaning berbasis aturan, bukan insting

### Yang Dikerjakan
- Menentukan strategi missing value per kolom
- Mengisi, membuang, atau mempertahankan data sesuai makna
- Menjaga integritas data setelah validasi

### Kenapa Harus Begini?
- NaN adalah sinyal, bukan error
- Salah isi lebih berbahaya dari tidak isi
- Data bisnis butuh keputusan sadar, bukan tebakan

> DAY 8 adalah hari engine belajar **menghormati kekosongan**.

## DAY 9 — Duplicate Logic

### Tujuan Hari Ini
Menentukan apa arti **kejadian yang sama** dalam data.

### Yang Sudah Bisa
- Engine tidak lagi naif terhadap duplicate
- Duplicate ditentukan oleh aturan bisnis
- Data unik dijaga secara sadar

### Yang Dikerjakan
- Mendefinisikan subset kolom penentu duplicate
- Menghapus duplicate berdasarkan makna, bukan baris
- Menjaga konsistensi data transaksi

### Kenapa Harus Begini?
- Duplicate ≠ baris identik
- Kesalahan duplicate bisa menggandakan nilai bisnis
- Engine harus tahu apa yang dianggap satu kejadian

> DAY 9 adalah hari engine belajar **memahami identitas data**.

## DAY 10 — Outlier Handling

### Tujuan Hari Ini
Menangani nilai ekstrem **tanpa merusak makna bisnis**.

### Yang Sudah Bisa
- Engine bisa mendeteksi outlier berbasis statistik
- Bisa memilih buang atau potong nilai ekstrem
- Tidak lagi menyapu bersih data besar

### Yang Dikerjakan
- Implementasi outlier handling dengan metode IQR
- Aksi outlier ditentukan lewat rule
- Menjaga keseimbangan antara kebersihan dan makna data

### Kenapa Harus Begini?
- Outlier kadang kesalahan, kadang peluang
- Membersihkan tanpa aturan = bias
- Engine profesional harus adil

> DAY 10 adalah hari engine belajar **tidak gegabah**.

## DAY 11 — Text Standardization

### Tujuan Hari Ini
Menyatukan makna teks tanpa mengubah arti bisnis.

### Yang Sudah Bisa
- Engine bisa menyatukan variasi teks yang sama maknanya
- Tidak lagi ada kategori palsu
- Konsistensi data terjaga

### Yang Dikerjakan
- Normalisasi teks (lowercase, strip)
- Mapping nilai eksplisit berbasis aturan
- Memisahkan format logic ke formatter module

### Kenapa Harus Begini?
- Analisis rusak karena teks tidak konsisten
- Cantik tidak penting, konsisten wajib
- Formatter menjaga tampilan, bukan logika

> DAY 11 adalah hari engine belajar **berbicara satu bahasa**.

## DAY 12 — Date Standardization

### Tujuan Hari Ini
Menyeragamkan semua tanggal ke satu realita waktu.

### Yang Sudah Bisa
- Semua tanggal diparse ke datetime
- Format tanggal konsisten
- Error parsing bisa dikontrol lewat rule

### Yang Dikerjakan
- Parsing tanggal dengan pandas
- Handling error (raise / coerce)
- Formatting output tanggal

### Kenapa Harus Begini?
- Analisis waktu sangat sensitif
- Kesalahan tanggal = insight palsu
- Standarisasi mencegah bug laten

> DAY 12 memastikan engine memahami waktu dengan benar.
