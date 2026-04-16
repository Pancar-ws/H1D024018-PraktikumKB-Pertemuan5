# Sistem Pakar Diagnosa Penyakit THT

## Penjelasan Source Code sisPak_2.py

Sistem ini merupakan aplikasi **Expert System** (Sistem Pakar) untuk mendiagnosa penyakit Telinga, Hidung, dan Tenggorokan (THT) berdasarkan gejala yang dialami oleh pengguna.

---

## Struktur dan Fungsi Utama

### 1. **Fungsi `tampilkan_daftar_gejala()`**
```python
def tampilkan_daftar_gejala():
```

**Fungsi:**
- Menampilkan daftar lengkap gejala yang tersedia dalam sistem
- Menyimpan 37 gejala (G1 - G37) dalam kamus/dictionary yang berisi kode gejala dan deskripsinya

**Gejala yang tersedia:**
- G1: Nafas abnormal
- G2: Suara serak
- G3: Perubahan kulit
- G4: Telinga penuh
- ...dan 33 gejala lainnya hingga G37

**Proses:**
1. Membuat dictionary dengan pasangan kode gejala dan deskripsi gejala
2. Menampilkan header sistem pakar dengan garis pemisah
3. Menampilkan gejala dalam format 2 kolom untuk kemudahan dibaca
4. Mengembalikan dictionary gejala

---

### 2. **Fungsi `diagnosa(gejala_input)`**
```python
def diagnosa(gejala_input):
```

**Fungsi:**
- Melakukan diagnosa dan mencocokkan gejala yang diinputkan dengan database penyakit
- Menghitung persentase kecocokan antara gejala input dan kriteria penyakit

**Database Penyakit (23 penyakit):**
Sistem memiliki database 23 penyakit THT, antara lain:
- Tonsilitis (G37, G12, G5, G27, G6, G21)
- Sinusitis (4 jenis: Maksilaris, Frontalis, Edmoidalis, Sfenoidalis)
- Kanker Laring, Kanker Tonsil, Kanker Leher & Kepala
- Otitis Media Akut, Meniere, Vertigo Postular
- Dan lainnya...

**Algoritma Pencocokan:**
1. Untuk setiap penyakit, mencari irisan (intersection) antara gejala input dan gejala penyakit
2. Menghitung persentase kecocokan: `(jumlah gejala cocok / total gejala penyakit) × 100%`
3. Menyimpan hasil dalam list berisi: nama penyakit, persentase kecocokan, dan gejala yang cocok
4. Mengurutkan hasil berdasarkan persentase kecocokan dari tertinggi ke terendah

---

### 3. **Fungsi `main()`**
```python
def main():
```

**Alur Program:**

1. **Tampilkan Daftar Gejala**
   - Memanggil `tampilkan_daftar_gejala()` untuk menampilkan opsi gejala

2. **Input dari Pengguna**
   - Meminta user memasukkan kode gejala (misal: G37, G12, G5)
   - Input dipisahkan dengan koma
   - Mengubah input menjadi uppercase dan membersihkan spasi
   - Split berdasarkan koma untuk mendapatkan list kode gejala

3. **Validasi Input**
   - Memeriksa apakah kode gejala yang diinputkan valid (ada dalam dictionary)
   - Jika tidak ada gejala valid, program berhenti

4. **Tampilkan Gejala yang Dipilih**
   - Menampilkan daftar gejala yang telah divalidasi beserta deskripsinya

5. **Proses Diagnosa**
   - Memanggil fungsi `diagnosa()` dengan gejala yang valid
   - Menampilkan hasil diagnosa (3 penyakit teratas dengan persentase kecocokan tertinggi)
   - Untuk setiap hasil, ditampilkan:
     - Nama penyakit
     - Persentase kecocokan
     - Daftar gejala yang cocok

---

## Cara Kerja Sistem

### Contoh Input dan Output:

**Input:**
```
Masukkan kode gejala: G37, G12, G5
```

**Output:**
```
Gejala yang Anda alami:
- G37: Demam
- G12: Sakit kepala
- G5: Nyeri bicara menelan

HASIL DIAGNOSA:
1. Penyakit: Tonsilitis (Kecocokan: 50.00%)
   Gejala cocok: Demam, Sakit kepala, Nyeri bicara menelan
2. Penyakit: Laringitis (Kecocokan: 40.00%)
   Gejala cocok: Demam, Nyeri bicara menelan
...
```

---

## Fitur Utama

1. **Interface Interaktif** - User-friendly dengan format tampilan yang rapi
2. **Database Penyakit** - 23 penyakit THT dengan kriteria gejala masing-masing
3. **Fuzzy Matching** - Menghitung persentase kecocokan, bukan hanya pencocokan 100%
4. **Validasi Input** - Memastikan input gejala valid sebelum proses diagnosa
5. **Hasil Terurut** - Menampilkan hasil berdasarkan tingkat akurasi/kecocokan

---

## Teknologi yang Digunakan

- **Bahasa:** Python 3
- **Tipe Sistem:** Expert System (Rule-based System)
- **Metode Diagnosa:** Similarity Matching dengan perhitungan persentase

---

## Cara Menjalankan

```bash
python sisPak_2.py
```

---