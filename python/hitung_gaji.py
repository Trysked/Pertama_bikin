print ("PROGRAM HITUNG GAJI KARYAWAN")
nama = input ("Nama Karyawan : ")
golongan = input ("Golongan Jabatan [1/2/3] : ")
pendidikan = input ("Pendidikan [SMA/D1/D3/S1] : ")
if golongan =="1":
    jabatan=300000*0.05
    if pendidikan == "SMA" or pendidikan=="sma":
        tunjangan = 300000*0.025
    elif pendidikan == "D1" or pendidikan=="d1":
        tunjangan = 300000*0.05
    elif pendidikan == "D3" or pendidikan=="d3":
        tunjangan = 300000*0.2
    else :
        tunjangan = 300000*0.3
elif golongan =="2":
    jabatan=300000*0.10
    if pendidikan == "SMA" or pendidikan=="sma":
        tunjangan = 300000*0.025
    elif pendidikan == "D1" or pendidikan=="d1":
        tunjangan = 300000*0.05
    elif pendidikan == "D3" or pendidikan=="d3":
        tunjangan = 300000*0.2
    else :
        tunjangan = 300000*0.3
elif golongan =="3":
    jabatan=300000*0.15
    if pendidikan == "SMA" or pendidikan=="sma":
        tunjangan = 300000*0.025
    elif pendidikan == "D1" or pendidikan=="d1":
        tunjangan = 300000*0.05
    elif pendidikan == "D3" or pendidikan=="d3":
        tunjangan = 300000*0.2
    else :
        tunjangan = 300000*0.3
else :
    tunjangan = 300000*0.15
jamker=int(input("Jumlah Jam Kerja :"))
if jamker>=8:
    total=(jamker-8)*3500
else :
    total=0
a = 300000+jabatan+tunjangan+total
print("")
print ("karyawan yang bernama       : ",nama)
print ("Honor yang diterima")
print ("Tunjangan Jabatan    Rp. ",jabatan)
print ("Tunjangan Pendidikan Rp", tunjangan)
print ("Honor Lembur         Rp", total)
print("                          -----------------+")
print("total gaji            Rp. %.0f" %a)
