# Program 1

nama = []
nim = []
prodi = []
hadir = []
tugas = []
uts = []
uas = []
akhir = []

def judul():
    print (" Program data mahasiswa ")
    
def menu():
    judul()
    print("1. Input data          ")
    print("2. Menampilkan data    ")
    print("3. Nilai rata-rata     ")
    print("4. Nilai tertinggi     ")
    print("5. Nilai terendah      ")

    pilihan = int(input("Pilih menu: "))
    if pilihan == 1:
        input_mhs()
    elif pilihan == 2:
        tampilkan_data()
        menu()
    elif pilihan == 3:
        nilai_rata_rata()
        menu()
    elif pilihan == 4:
        nilai_tertinggi()
        menu()
    elif pilihan == 5:
        nilai_terendah()
        menu()
   

def input_mhs():
    i_nama = input("Nama : ")
    nama.append(i_nama)
    
    i_nim = input("NIM : ")
    nim.append (i_nim)
    
    i_prodi = input("Prodi : ")
    prodi.append(i_prodi)
    
    i_hadir = float(input ("Jumlah hadir : "))
    t_hadir = ((i_hadir/16)*20/100)*100
    hadir.append(t_hadir)
    
    i_tugas = float(input("Nilai tugas : "))
    t_tugas = i_tugas*(25/100)
    tugas.append(t_tugas)
    
    i_uts = float(input("Nilai uts : "))
    t_uts = i_uts*(25/100)
    uts.append(t_uts)
    
    i_uas = float(input ("Nilai uas: "))
    t_uas = i_uas*(30/100)
    uas.append(t_uas)
    
    total_nilai = t_hadir + t_tugas + t_uts + t_uas
    akhir.append(total_nilai)
    print ("Data tersimpan")
    menu()
    
def tampilkan_data():
    judul()
    print("Data Mahasiswa:")
    for i in range(len(nama)):
        print("Nama   :", nama[i])
        print("NIM    :", nim[i])
        print("Prodi  :", prodi[i])
        print("Hadir  :", hadir[i])
        print("Tugas  :", tugas[i])
        print("UTS    :", uts[i])
        print("UAS    :", uas[i])
        print("Akhir  :", akhir[i])

def nilai_rata_rata():
    total_nilai = sum(akhir)
    rata_rata = total_nilai / len(akhir)
    print("Nilai Rata-rata: {:.2f}".format(rata_rata))

def nilai_tertinggi():
    max_nilai = max(akhir)
    index_max = akhir.index(max_nilai)
    print("Nilai Tertinggi:")
    print("Nama   :", nama[index_max])
    print("NIM    :", nim[index_max])
    print("Prodi  :", prodi[index_max])
    print("Hadir  :", hadir[index_max])
    print("Tugas  :", tugas[index_max])
    print("UTS    :", uts[index_max])
    print("UAS    :", uas[index_max])
    print("Akhir  :", akhir[index_max])
    
def nilai_terendah():
    min_nilai = min(akhir)
    index_min = akhir.index(min_nilai)
    print("Nilai Terendah:")
    print("Nama   :", nama[index_min])
    print("NIM    :", nim[index_min])
    print("Prodi  :", prodi[index_min])
    print("Hadir  :", hadir[index_min])
    print("Tugas  :", tugas[index_min])
    print("UTS    :", uts[index_min])
    print("UAS    :", uas[index_min])
    print("Akhir  :", akhir[index_min])


# Program 2

inventaris = []


def tambah_barang(nama, kode, jumlah):
    barang = {
        'nama': nama,
        'kode': kode,
        'jumlah': jumlah
    }
    inventaris.append(barang)
    print(f"Barang '{nama}' berhasil ditambahkan.")


def tampilkan_semua_barang():
    if not inventaris:
        print("Tidak ada barang dalam inventaris.")
    else:
        for barang in inventaris:
            print(f"Nama: {barang['nama']}, Kode: {barang['kode']}, Jumlah: {barang['jumlah']}")


def cari_barang_berdasarkan_kode(kode):
    for barang in inventaris:
        if barang['kode'] == kode:
            print(f"Barang ditemukan: Nama: {barang['nama']}, Kode: {barang['kode']}, Jumlah: {barang['jumlah']}")
            return
    print(f"Barang dengan kode '{kode}' tidak ditemukan.")


def hapus_barang_berdasarkan_kode(kode):
    for barang in inventaris:
        if barang['kode'] == kode:
            inventaris.remove(barang)
            print(f"Barang dengan kode '{kode}' berhasil dihapus.")
            return
    print(f"Barang dengan kode '{kode}' tidak ditemukan.")


def main():
    while True: 
        print("   Program inventaris barang        ")
        print("1. Tambah barang                    ")
        print("2. Tampilkan semua barang           ")
        print("3. Cari barang berdasarkan kode      ")
        print("4. Hapus barang berdasarkan kode     ")
        print("5. Keluar                           ")

        pilihan = input("pilih menu : ")

        if pilihan == '1':
            nama = input("Masukan nama barang : ")
            kode = input("Masukan kode barang : ")
            jumlah = int(input("Masukan jumlah barang : "))
            tambah_barang(nama, kode, jumlah)
        elif pilihan == '2':
            tampilkan_semua_barang()
        elif pilihan == '3':
            kode = input("Masukan kode barang yang ingin dicari : ")
            cari_barang_berdasarkan_kode(kode)
        elif pilihan == '4':
            kode = input("Masukan kode barang yang ingin di hapus: ")
            hapus_barang_berdasarkan_kode(kode)
        elif pilihan == '5':
            print("Terima kasih")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")



# Program 3

keuangan = []

def tambah_transaksi(jenis, jumlah, keterangan):
    transaksi = {
        'jenis': jenis,
        'jumlah': jumlah,
        'keterangan': keterangan
    }
    keuangan.append(transaksi)
    print(f"Transaksi '{keterangan.upper()}' Berhasil ditambahkan.")


def tampilkan_semua_transaksi():
    if not keuangan:
        print("Tidak ada transaksi dalam keuangan.")
    else:
        for transaksi in keuangan:
            print(f"Jenis: {transaksi['jenis'].upper()}, JUMLAH: {transaksi['jumlah']}, Keterangan: {transaksi['keterangan'].upper()}")


def total_pemasukan():
    total_masuk = sum(transaksi['jumlah'] for transaksi in keuangan if transaksi['jenis'] == 'pemasukan')
    print(f"Total pemasukan: {total_masuk}")
    return total_masuk


def total_pengeluaran():
    total_keluar = sum(transaksi['jumlah'] for transaksi in keuangan if transaksi['jenis'] == 'pengeluaran')
    print(f"Total pengeluaran: {total_keluar}")
    return total_keluar


def saldo_akhir():
    saldo = total_pemasukan() - total_pengeluaran()
    print(f"Saldo akhir: {saldo}")
    return saldo


def utama():
    while True:
        print("   Menu Transaksi            ")
        print("1. Tambah transaksi          ")
        print("2. Tampilkan semua transaksi ")
        print("3. Hitung total pemasukan    ")
        print("4. Hitung total pengeluaran  ")
        print("5. Hitung saldo akhir        ")
        print("6. Keluar                    ")

        pilihan = input("Silahkan pilih menu (1-6): ")

        if pilihan == '1':
            jenis = input("Masukkan jenis transaksi (Pemasukan/Pengeluaran): ")
            jumlah = float(input("Masukkan jumlah transaksi: "))
            keterangan = input("Masukkan keterangan transaksi: ")
            tambah_transaksi(jenis, jumlah, keterangan)
        elif pilihan == '2':
            tampilkan_semua_transaksi()
        elif pilihan == '3':
            total_pemasukan()
        elif pilihan == '4':
            total_pengeluaran()
        elif pilihan == '5':
            saldo_akhir()
        elif pilihan == '6':
            print("Terima kasi telah menggunakan program ini.")
            break
        else:
            print("Pilihan tidak tersedia. Silahkan coba lagi.")



# opsi untuk program ke 1,2, dan 3

print ("1. Program data mahasiswa                  ")
print ("2. Program inventaris barang               ")
print ("3. Program pengelolaan keuangan pribadi    ")

opsi = int(input("Silahkan masukan pilihan (1-3): "))

if opsi == 1:
    menu()
elif opsi == 2:
    main()
elif opsi == 3:
    utama()
else:
    print ("Pilihan tidak tersedia")