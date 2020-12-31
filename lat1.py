file = open("isifiletext.txt", "r")
fileAngka = file.readlines()
angkaGenap = []
angkaGanjil = []
for i in range(len(fileAngka)):
    angka = fileAngka[i].replace("\n","")
    if (int(angka)%2)==0:
        angkaGenap.append(fileAngka[i])
    else :
        angkaGanjil.append(fileAngka[i])
print("Banyaknya bilangan genap : ", len(angkaGenap))
print("Banyaknya bilangan ganjil : ", len(angkaGanjil))
