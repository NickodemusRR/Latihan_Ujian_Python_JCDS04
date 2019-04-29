angka = int(input('Ketik angka: '))

bilangan = ['bulat']
if angka < 0:
    bilangan.append('negatif')
else:
    bilangan.append('cacah')
    if angka == 0:
        bilangan.append('nol')
    else:
        bilangan.append('asli')
        if angka % 2 == 0:
            bilangan.append('genap')
            if angka == 2:
                bilangan.append('prima')
            else:
                bilangan.append('komposit')
        else:
            bilangan.append('ganjil')
            if angka > 1:
                i = 2
                while i < angka:
                    i += 1
                    if i == angka:
                        bilangan.append('prima')
                        break
                    elif angka % i == 0:
                        bilangan.append('komposit')
                        break
                    else:
                        continue
                        
print(bilangan)            