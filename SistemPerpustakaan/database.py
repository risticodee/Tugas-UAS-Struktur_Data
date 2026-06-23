import csv
import os

FILE_CSV = "data_buku.csv"


def load_data():
    data = {}

    if not os.path.exists(FILE_CSV):
        with open(FILE_CSV, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["ID", "Judul", "Penulis", "Tahun", "Status"])
        return data

    with open(FILE_CSV, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            data[row["ID"]] = {
                "judul": row["Judul"],
                "penulis": row["Penulis"],
                "tahun": row["Tahun"],
                "status": row["Status"]
            }

    return data


def save_data(data):
    with open(FILE_CSV, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        writer.writerow(["ID", "Judul", "Penulis", "Tahun", "Status"])

        for id_buku, buku in data.items():
            writer.writerow([
                id_buku,
                buku["judul"],
                buku["penulis"],
                buku["tahun"],
                buku["status"]
            ])