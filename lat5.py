filelama = open("fileangka.txt", "r") 
filebaru = open("Hasil Nomer 5.txt", "w")
data = filelama.readlines()
for i in range(len(data)):
    angka = data[i]
    a, b = angka.split("|")
    c = int(a)
    d = int(b)
    jumlah = c + d
    total = str(jumlah)
    filebaru.write(total)
    filebaru.write("\n")
filebaru.close()
tujuan = open("Hasil Nomer 5.txt", "r")
tujuan.read()
tujuan.close()
