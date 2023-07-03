print("============LIST DAFTAR KEBERANGKATAN KERETA API===============")
print("Nama Kereta Api       |     Relasi      |  Kelas    |  Tarif  |")
print("===============================================================")
print("1. Argo Bromo Anggrek | Gambir-Surabaya | Eksekutif |  75000  |")
print("2. Purwojaya          | Gambir-Cilacap  | Eksekutif |  70000  |")
print("3. Cirebon Express    | Gambir-Cirebon  | Eksekutif |  80000  |")
print("4. Argo Jati          | Gambir-Cirebon  | Ekonomi   |  65000  |")
print("5. Tegal Bahari       | Gambir-Tegal    | Ekonomi   |  60000  |")
print("6. Argo Sindoro       | Gambir-Semarang | Eksekutif |  78000  |")
print("7. Argo Lawu          | Gambir-Solo     | Eksekutif |  82000  |")
print("===============================================================")
print("")
nama=input("Nama Pembeli :")
nomor=input("No Telepon : ")
tgl=input("Tanggal Keberangkatan :")
kereta=input("Nama Kereta :")
tujuan=input("Relasi :")
kelas=input("Kelas :")
harga=input("Tarif :")

pilihan=int(input("Masukkan Pilihan Kereta :"))

if pilihan ==1:
    kereta ="Argo Bromo Anggrek"
    tujuan =="Gambir-Surabaya"
    kelas ==("Eksekutif")
    harga =75000
elif pilihan ==2:
    kereta =="Purwojaya"
    tujuan =="Gambir-Cilacap"
    kelas =="Eksekutif"
    harga=70000
elif pilihan ==3:
    kereta =="Cirebon Express"
    tujuan =="Gambir-Cirebon"
    kelas =="Eksekutif"
    harga=80000
elif pilihan ==4:
    kereta =="Argo Jati"
    tujuan =="Gambir-Cirebon"
    kelas ==("Ekonomi")
    harga=65000
elif pilihan ==5:
    kereta =="Tegal Bahari"
    tujuan =="Gambir-Tegal"
    kelas =="Ekonomi"
    harga=60000
elif pilihan ==6:
    kereta =="Argo Sindoro"
    tujuan =="Gambir-Semarang"
    kelas =="Eksekutif"
    harga =78000
elif pilihan ==7:
    kereta =="Argo Lawu"
    tujuan =="Gambir-Solo"
    kelas =="Eksekutif"
    harga =82000
else :
    print("Nama Kereta Tidak Tersedia")

jumlah =int (input("Jumlah Pembelian :"))

if jumlah ==2:
    potongan =(jumlah*harga)*0.1
elif jumlah ==3:
    potongan =(jumlah*harga)*0.12
elif jumlah ==4:
    potongan =(jumlah*harga)*0.15
else:
    potongan =0
total= int(jumlah*harga-potongan)
def garis():
    print("=================================")
garis()
print("PEMESANAN E-TICKET")
garis()
print("Nama Pembeli :", nama)
print("Nomor Telepon :", nomor)
print("Tanggal Keberangkatan :", tgl)
print("Nama Kereta Api :", kereta)
print("Relasi :", tujuan)
print("Kelas :", kelas)
print("Jumlah Beli :", jumlah)
garis()
print("Harga Tiket : Rp", harga)
print("Potongan : Rp", potongan)
print("STRUK PEMESANAN E-TICKET")
uang=int(input("Masukan pembayaran : Rp."))
garis()
kembalian=uang-total
print("Uang Kembalian : Rp.", kembalian)
garis()
print("SEMOGA SELAMAT SAMPAI TUJUAN")
print("TERIMA KASIH")



            


    



    



      
