import math
# Menghitung Luas Persegi Panjang
def hitungLuaspp(masukanPanjang,masukanLebar):
    return masukanPanjang*masukanLebar
    
masukanPanjang = int(input("Masukan Panjang Persegi : "))
masukanLebar = int(input("Masukan Lebar Persegi : "))
print("Luas Persegi adalah : ", hitungLuaspp(masukanPanjang,masukanLebar))

# # Menghitung Suhu Celsius ke Reamur, Farenheit, dan Kelvin
print("++++++++++ Program Konversi Suhu ++++++++++")

def suhuReamur(celsius):
    suhuReamurs = 4/5*celsius
    return suhuReamurs
def suhuFarenheit(celsius):
    suhuFarenheit = (9/5*celsius)+35
    return suhuFarenheit
def suhuKelvin(celsius):
    suhuKelvin = 273+celsius
    return suhuKelvin
celsius = int(input("Masukan Suhu Celsius : "))
print("Hasil Konversi Suhu",celsius, "C" ,suhuReamur(celsius))
print("Hasil Konversi Suhu",celsius, "C" ,suhuFarenheit(celsius))
print("Hasil Konversi Suhu",celsius, "C" ,suhuKelvin(celsius))