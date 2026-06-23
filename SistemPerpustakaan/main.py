from database import load_data
from crud import *
from queue_pinjam import *

data = load_data()

while True:

    print("\n")
    print("=" * 40)
    print(" SISTEM PERPUSTAKAAN ")
    print("=" * 40)
    print("1. Tambah Buku")
    print("2. Lihat Buku")
    print("3. Update Buku")
    print("4. Hapus Buku")
    print("5. Cari Buku")
    print("6. Sorting Buku")
    print("7. Pinjam Buku")
    print("8. Lihat Antrian")
    print("9. Keluar")

    pilihan = input("Pilih menu : ")

    if pilihan == "1":
        tambah_buku(data)

    elif pilihan == "2":
        lihat_buku(data)

    elif pilihan == "3":
        update_buku(data)

    elif pilihan == "4":
        hapus_buku(data)

    elif pilihan == "5":
        cari_buku(data)

    elif pilihan == "6":
        sorting_buku(data)

    elif pilihan == "7":
        pinjam_buku(data)

    elif pilihan == "8":
        lihat_antrian()

    elif pilihan == "9":
        print("Program selesai.")
        break

    else:
        print("Pilihan tidak valid!")