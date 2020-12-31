file = input("Masukkan nama file : ")
n = int(input("Masukkan n         : "))
data = open(file, "r")
baca = data.read()
list1 = list(baca)
passwrd = []
for i in list1 :
    a = ord(i)
    if a == 32:
        b = a
    else :
        b = a + n
        if b > 122 :
            b = b - 26
        elif b > 90 and b < 97:
            b = b - 26
    sandi = chr(b)
    passwrd = passwrd + [sandi]
    if not list1 :
        break
tambah = "".join(passwrd)
tutup = open("Hasil Nomer 6.txt", "w")
tutup.write(tambah)
tutup.close()
