bilSat = int(input("Masukan Bilangan Bulat Pertama"))
bilDua= int(input("Masukan Bilangan Bulat Kedua"))
bilTig = int(input("Masukan Bilangan Bulat Ketiga"))
hasilPyta = (bilSat*bilSat)+(bilDua*bilDua)
if hasilPyta == bilTig*bilTig:
    print("Merpakan Pytagoras")
else :
    print("tidak pytagoras")