angka = input("Masukkan angka: ")
angka_hitung = input("Masukkan angka yang dihitung: ")

muncul = 0
for i in range(len(angka)):
    if angka[i] == angka_hitung:
        muncul += 1
        
print(f"angka {angka_hitung} muncul sebanyak {muncul} kali")