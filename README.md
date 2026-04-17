# Sistem Pakar Diagnosa Penyakit THT

Sistem ini merupakan aplikasi **Expert System** (Sistem Pakar) yang memiliki fungsi untuk mendiagnosa penyakit Telinga, Hidung, dan Tenggorokan (THT) berdasarkan gejala yang dialami oleh pengguna.

## Daftar File

| File | Deskripsi |
|------|-----------|
| `sisPak_2.py` | Versi command-line (CLI) dari sistem pakar |
| `sisPak_gui.py` | Versi graphical user interface (GUI) dari sistem pakar |
| `README.md` | Dokumentasi sistem |

---

## sisPak_2.py - Versi CLI

Sistem pakar CLI ini memiliki fitur sebagai berikut:
- Database: 37 gejala (G1-G37) dan 23 penyakit THT
- Algoritma: Set intersection matching dengan persentase kecocokan
- Input: Kode gejala dipisahkan koma (contoh: G37, G12, G5)
- Output: Hasil diagnosa terurut berdasarkan tingkat kecocokan

---

## sisPak_gui.py - Versi GUI

Sistem pakar dengan gui menggunakan tkinter juga memiliki fitur diantaranya:
- Database: Sama seperti sisPak_2.py
- Input: Pilih gejala dari listbox (multiple selection)
- Komponen: Title label, instruction label, scrollable listbox, diagnosis button, scrolled text result
- Window: 650x550 pixel
- Output: Hasil diagnosa dengan nama penyakit, persentase kecocokan, dan gejala yang cocok

---

## Fitur Utama

1. **Database Lengkap** - 37 gejala & 23 penyakit THT
2. **Similarity Matching** - Perhitungan persentase kecocokan gejala
3. **Hasil Terurut** - Menampilkan diagnosa dari akurasi tertinggi ke terendah
4. **Validasi Input** - Memastikan input gejala valid
5. **Dual Interface** - Command-line & graphical options

---

## Cara Menjalankan

**Versi CLI:**
```bash
python sisPak_2.py
```
Input kode gejala (G1-G37) dipisahkan koma. Tampil hasil diagnosa terurut.

**Versi GUI:**
```bash
python sisPak_gui.py
```
Pilih gejala dari list, klik tombol "Mulai Diagnosa", lihat hasil di area teks.

---

## Perbandingan

| Aspek | sisPak_2.py | sisPak_gui.py |
|-------|------------|-------------|
| Interface | Command-line | Graphical (tkinter) |
| Input | Ketik kode gejala | Pilih dari list |
| User-Friendly | Medium | High |
| Dependencies | Python standard | + tkinter |