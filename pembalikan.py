kalimat = input("Masukan kata atau angka: ")
for i in range(len(kalimat), 0, -1):
    print(kalimat[i-1], end="")