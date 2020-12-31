file = open("datamhs.txt", "r")
data = file.readlines()
dataMhs = {}
listMhs = []
for i in range(len(data)):
    mhs = data[i].split("|")
    mhs[2] = mhs[2].replace("\n", "")    
    dtMhs = {"nim" : mhs[0], "nama" : mhs[1], "alamat" : mhs[2]}
    dataMhs = dtMhs
    listMhs.append(dataMhs)
print(listMhs)
file.close()
