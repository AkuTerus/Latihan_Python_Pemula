# suhu = float(input('Masukan Suhu : '))

# if suhu < 32:
#     print('meninggal')
# elif suhu < 36:
#     print('bahaya hipotermia')
# elif suhu < 38:
#     print('Normal')
# elif suhu < 41:
#     print('demam')
# else :
#     print('meninggal 2')

# bilangan = int(input('Masukan sebuah bilangan : '))

# if bilangan > 0 :
#     print("positif ")
# elif bilangan < 0 : 
#     print('negatif ')
# else:
#     print('nol')

# bilangan = int(input('Masukan sebuah bilangan : '))

# jarak = bilangan%10


# if jarak== 0 or jarak == 1 or jarak== 2 or jarak==8 or jarak==9:
#     print('dekat')
# else:
#     print('jauh')
# jumlahUbin1 = int(input('Masukan Ubin 1 : '))
# jumlahUbin2 = int(input('Masukan Ubin 5 : '))

# panjangLantai = int(input('Masukan Panjang lantai : '))

# if panjangLantai <= (jumlahUbin1*1 + jumlahUbin2*5):
#     if (panjangLantai//5) <= jumlahUbin2 and (panjangLantai%5 == 0):
#         print('BISA')
#     elif(panjangLantai%5)<= jumlahUbin1:
#         print('BISA')
#     else : 
#         print('tidak bisa')
# else:
#     print('tidak bisa')

namaPertama = input('Masukan Nama 1 : ')
namaKedua = input('Masukan Nama 2 : ')
namaKetiga = input('Masukan Nama 3 : ')

panjang_nama1=len(namaPertama)
panjang_nama2=len(namaKedua)
panjang_nama3=len(namaKetiga)

if panjang_nama1 > panjang_nama2 and panjang_nama1 > panjang_nama3:
    print(namaPertama)
elif panjang_nama2> panjang_nama1 and panjang_nama2 > panjang_nama3:
    print(namaKedua)
else:
    print(namaKetiga)
    
    
    

  a = int(input('Masukan a : '))
b = int(input('Masukan b : '))
c = int(input('Masukan c : '))

total = 0

if a != b and a != c and b != c:
    total=a+b+c
elif a==b == c :
    total = 0
elif a == b:
    total = c
elif a==c :
    total = b
else:
    total = a
print(total)
