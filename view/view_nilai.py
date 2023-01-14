from model.daftar_nilai import data
from tabulate import tabulate

def tampilkan():
    print(tabulate(data.values(),headers=("Nama","NIM","Tugas","Uts","Uas","Nilai Akhir"),tablefmt="double_grid"))
    kembali = input("Kembali Tekan [enter]")
def cetak_hasil_pencarian(nama):
    datas = {}
    for key, value in data.items():
        if nama in value:
            datas[key] = value
            print(tabulate(datas.values(),headers=["Nama", "NIM", "Tugas", "Uts", "Uas", "Nilai Akhir"],tablefmt="double_grid"))
        else:
            print("Data Tidak Ditemukan!!")
            kembali = input('Kembali Tekan [enter]')
            return True
