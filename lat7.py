file = input("Masukkan nama file : ")
n = int(input("Masukkan n         : "))
data1 = open(file, "r")
baca = data1.read()
list1 = list(baca)
passwrd = []
for i in list1 :
    a = ord(i)
    if a == 32 :
        b = a
    else :
        b = a - n
        if b < 65 :
            b = b + 26
        elif b < 90 and b > 97 :
            b = b + 26
    sandi = chr(b)
    passwrd = passwrd + [sandi]
tambah = "".join(passwrd)
tutup = open("Hasil Nomer 7.txt", "w")
tutup.write(tambah)
tutup.close()
