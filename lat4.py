isinim = input("Masukkan NIM yang mau dicari : ")
file = open("datamhs.txt", "r")
data = file.readlines()
for i in range(len(data)):
    mhs = data[i]
    nim, nama, alamat = mhs.split("|")
    if isinim == nim :
        print("Data Mahasiswa")
        print("NIM    : ", nim, "\nNama   : ", nama,"\nAlamat : ", alamat)
        break
    else :
        break
if isinim not in nim:
    print("Data mahasiswa tidak ditemukan")
