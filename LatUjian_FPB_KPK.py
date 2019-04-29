angka_1 = int(input('Ketik angka pertama: '))
angka_2 = int(input('Ketik angka kedua: '))

# membuat list kosong untuk menampung faktorisasi angka
list_angka1 = []
list_angka2 = []

# mencari FPB
for i in range (1,angka_1+1):
    if angka_1 % i == 0:
        list_angka1.append(i)
    else:
        pass

for i in range (1,angka_2+1):
    if angka_2 % i == 0:
        list_angka2.append(i)
    else:
        pass

FPB = []
for i in list_angka1:
    for j in list_angka2:
        if i == j:
            FPB.append(i)

# mencari KPK
fpb = FPB[-1]

KPK = int((angka_1 * angka_2)/fpb)

# mengeluarkan hasil
print('FPB dari {} dan {} adalah = {}'.format(angka_1, angka_2, FPB[-1]))
print('KPK dari {} dan {} adalah = {}'.format(angka_1, angka_2, KPK))