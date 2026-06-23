from database import save_data


def tambah_buku(data):
    print("\n=== TAMBAH BUKU ===")

    id_buku = input("ID Buku : ")

    if id_buku in data:
        print("ID sudah ada!")
        return

    judul = input("Judul : ")
    penulis = input("Penulis : ")
    tahun = input("Tahun : ")

    data[id_buku] = {
        "judul": judul,
        "penulis": penulis,
        "tahun": tahun,
        "status": "Tersedia"
    }

    save_data(data)
    print("Buku berhasil ditambahkan!")


def lihat_buku(data):
    print("\n=== DAFTAR BUKU ===")

    if not data:
        print("Data kosong")
        return

    print("-" * 80)

    for id_buku, buku in data.items():
        print(
            f"{id_buku} | "
            f"{buku['judul']} | "
            f"{buku['penulis']} | "
            f"{buku['tahun']} | "
            f"{buku['status']}"
        )


def update_buku(data):
    print("\n=== UPDATE BUKU ===")

    id_buku = input("ID Buku : ")

    if id_buku not in data:
        print("Data tidak ditemukan!")
        return

    data[id_buku]["judul"] = input("Judul Baru : ")
    data[id_buku]["penulis"] = input("Penulis Baru : ")
    data[id_buku]["tahun"] = input("Tahun Baru : ")

    save_data(data)

    print("Data berhasil diperbarui!")


def hapus_buku(data):
    print("\n=== HAPUS BUKU ===")

    id_buku = input("ID Buku : ")

    if id_buku not in data:
        print("Data tidak ditemukan!")
        return

    del data[id_buku]

    save_data(data)

    print("Data berhasil dihapus!")


def cari_buku(data):
    print("\n=== CARI BUKU ===")

    keyword = input("Masukkan ID/Judul : ").lower()

    ditemukan = False

    for id_buku, buku in data.items():
        if keyword in id_buku.lower() or keyword in buku["judul"].lower():

            print("\nData ditemukan:")
            print("ID      :", id_buku)
            print("Judul   :", buku["judul"])
            print("Penulis :", buku["penulis"])
            print("Tahun   :", buku["tahun"])
            print("Status  :", buku["status"])

            ditemukan = True

    if not ditemukan:
        print("Data tidak ditemukan!")


def sorting_buku(data):
    print("\n=== SORTING ===")
    print("1. Judul")
    print("2. Tahun")

    pilihan = input("Pilih : ")

    daftar = list(data.items())

    if pilihan == "1":
        daftar.sort(key=lambda x: x[1]["judul"])

    elif pilihan == "2":
        daftar.sort(key=lambda x: x[1]["tahun"])

    else:
        print("Pilihan salah!")
        return

    print("\nHasil Sorting:")

    for id_buku, buku in daftar:
        print(
            f"{id_buku} | "
            f"{buku['judul']} | "
            f"{buku['penulis']} | "
            f"{buku['tahun']} | "
            f"{buku['status']}"
        )