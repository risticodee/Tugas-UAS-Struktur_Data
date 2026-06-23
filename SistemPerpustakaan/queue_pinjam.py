from collections import deque
from database import save_data

antrian = deque()


def pinjam_buku(data):
    print("\n=== PINJAM BUKU ===")

    id_buku = input("ID Buku : ")

    if id_buku not in data:
        print("Buku tidak ditemukan!")
        return

    if data[id_buku]["status"] == "Dipinjam":
        print("Buku sedang dipinjam!")
        return

    nama = input("Nama Peminjam : ")

    antrian.append((nama, id_buku))

    data[id_buku]["status"] = "Dipinjam"

    save_data(data)

    print("Peminjaman berhasil!")


def lihat_antrian():
    print("\n=== ANTRIAN PEMINJAMAN ===")

    if not antrian:
        print("Belum ada antrian.")
        return

    nomor = 1

    for nama, id_buku in antrian:
        print(f"{nomor}. {nama} -> {id_buku}")
        nomor += 1