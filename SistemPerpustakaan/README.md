# Sistem Perpustakaan Berbasis CSV

## Deskripsi Proyek

Sistem Perpustakaan merupakan aplikasi berbasis Command Line Interface (CLI) yang dibuat menggunakan bahasa pemrograman Python. Aplikasi ini digunakan untuk mengelola data buku perpustakaan dengan memanfaatkan file CSV sebagai media penyimpanan data. Program mendukung operasi CRUD (Create, Read, Update, Delete), pencarian data, pengurutan data, serta pengelolaan antrian peminjaman buku.

---

## Tampilan Menu Program

Saat program dijalankan, pengguna akan melihat menu berikut:

```text
========================================
      SISTEM PERPUSTAKAAN
========================================
1. Tambah Buku
2. Lihat Buku
3. Update Buku
4. Hapus Buku
5. Cari Buku
6. Sorting Buku
7. Pinjam Buku
8. Lihat Antrian
9. Keluar

Pilih Menu :
```

### Penjelasan Menu

**1. Tambah Buku**
Digunakan untuk menambahkan data buku baru ke dalam sistem.

**2. Lihat Buku**
Menampilkan seluruh data buku yang tersimpan pada database.

**3. Update Buku**
Digunakan untuk mengubah informasi buku yang sudah ada.

**4. Hapus Buku**
Digunakan untuk menghapus data buku berdasarkan ID buku.

**5. Cari Buku**
Mencari buku berdasarkan ID atau judul buku.

**6. Sorting Buku**
Mengurutkan data buku berdasarkan judul atau tahun terbit.

**7. Pinjam Buku**
Mencatat peminjaman buku dan memasukkannya ke dalam antrian peminjaman.

**8. Lihat Antrian**
Menampilkan daftar antrian peminjaman buku.

**9. Keluar**
Mengakhiri program.

---

## Contoh Output Program

```text
=== DAFTAR BUKU ===

--------------------------------------------------------------------------------
B001 | Python Dasar | Andi | 2024 | Tersedia
B002 | Struktur Data | Budi | 2023 | Dipinjam
--------------------------------------------------------------------------------
```

---

## Struktur Data yang Digunakan

### 1. Hash Map (Dictionary)

Digunakan untuk menyimpan data buku dengan ID buku sebagai key sehingga proses pencarian dan pengelolaan data menjadi lebih cepat.

### 2. Queue (Deque)

Digunakan untuk mengelola antrian peminjaman buku dengan prinsip FIFO (First In First Out), yaitu data yang pertama masuk akan diproses terlebih dahulu.

---

## Algoritma yang Digunakan

### Searching

Digunakan untuk mencari data buku berdasarkan ID buku atau judul buku yang dimasukkan oleh pengguna.

### Sorting

Digunakan untuk mengurutkan data buku berdasarkan judul atau tahun terbit sehingga data lebih mudah dibaca.

---

## Struktur Folder

```text
SistemPerpustakaan/
│
├── main.py
├── database.py
├── crud.py
├── queue_pinjam.py
├── data_buku.csv
└── README.md
```

---

## Database

Program menggunakan file CSV sebagai database sederhana untuk menyimpan seluruh data buku.

Nama file:

```text
data_buku.csv
```

Contoh isi file:

```csv
ID,Judul,Penulis,Tahun,Status
B001,Python Dasar,Andi,2024,Tersedia
B002,Struktur Data,Budi,2023,Tersedia
```

---

## Implementasi Sistem

### Create

Menambahkan data buku baru ke dalam sistem dan menyimpannya ke file CSV.

### Read

Menampilkan seluruh data buku yang tersimpan pada database.

### Update

Mengubah data buku yang sudah ada berdasarkan ID buku yang dipilih.

### Delete

Menghapus data buku dari sistem dan memperbarui data pada file CSV.

### Searching

Mencari buku berdasarkan ID atau judul buku.

### Sorting

Mengurutkan data buku berdasarkan judul atau tahun terbit.

### Queue Peminjaman

Mengelola antrian peminjaman buku menggunakan struktur data Queue sehingga peminjaman diproses sesuai urutan.

---

## Cara Menjalankan Program

1. Pastikan Python telah terinstal pada komputer.
2. Simpan seluruh file program dalam satu folder.
3. Jalankan file utama dengan perintah:

```bash
python main.py
```

4. Pilih menu yang tersedia sesuai kebutuhan.

---

## Kesimpulan

Aplikasi Sistem Perpustakaan berhasil menerapkan konsep CRUD menggunakan database CSV, struktur data Hash Map dan Queue, serta algoritma Searching dan Sorting. Program ini dapat membantu pengelolaan data buku perpustakaan secara sederhana melalui antarmuka Command Line Interface (CLI).
