data = {}

def tambah_data(nama, nim, tugas, nilaiUTS, nilaiUAS, nilaiAkhir):
    data[nama] = nama, nim, tugas, nilaiUTS, nilaiUAS, nilaiAkhir

def hapus_data(nama):
    if nama in data.keys():
        del data[nama]
        print(f"Data {nama} berhasil Dihapus")
        kembali = input('Kembali Tekan [enter]')
        return True
    else:
        print(f'Data dangan Nama {nama} tidak ditemukan!!')
        kembali = input('Kembali Tekan [enter]')
        return False

def ubah_data(nama):
    if nama in data.keys():
        del data[nama]
        from view.input_nilai import ubah
        ubah()
    else:
        print(f"Data dengan Nama {nama} tidak ada!!")
        Kembali = input('Kembali Tekan [enter]')
        return False