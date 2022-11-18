import math
cappucino = 25000
vanillaLatte = 22000
americano = 30000
brewedCoffe = 20000
print("==========CAFE========== \n======Masukan Jumlah Pesanan=====\n")
pesananSatu = int(input("Cappucino \t\t Diskon 50% \t Rp 25.000\t :"))
pesananDua = int(input("Vanilla Latte \t\t Diskon 65% \t Rp 22.000\t :"))
pesananTiga = int(input("Americano \t\t Diskon 35% \t Rp 30.000\t :"))
pesananEmpat = int(input("Brewed Coffe \t\t Diskon 40% \t Rp 20.000\t :"))

print("==========Total==========\n")
print ("Total Cappucino \t : Rp",int((cappucino-cappucino*50/100)*pesananSatu))
print ("Total Vanilla Latte \t : Rp",int((vanillaLatte-vanillaLatte*65/100)*pesananDua))
print ("Total Americano \t : Rp",int((americano-americano*35/100)*pesananTiga))
print ("Total Brewed Coffe \t : Rp",int(brewedCoffe-brewedCoffe*40/100*pesananEmpat))
jumlahTotal =int((cappucino-cappucino*50/100)*pesananSatu)+int((vanillaLatte-vanillaLatte*65/100)*pesananDua)+int((americano-americano*35/100)*pesananTiga)+int(brewedCoffe-brewedCoffe*40/100*pesananEmpat)
print("Jumlah Total biaya yang harus di bayarkan adalah Rp ",jumlahTotal)
