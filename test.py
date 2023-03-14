def pagar_vertikal(n):
    print('Pagar Vertikal')
    for i in range(n):
        print('#',end='')
    print()

def pagar_horizontal(n):
    print('Pagar Vertikal')
    for i in range(n):
        print('#',end='')
    print()

def pagar_horizontalxVertikal(n):
    for i in range(n):
        for j in range(n):
            print('#',end='')
        print()

def kosng_tengah(n):
    for baris in range(1,n+1):
        if baris == 1 or baris == n:
            for j in range(1,n+1):
                print('#', end='')
        else:
            spasi = n - 2
            print('#', end='')
            for i in range(spasi):
                print(' ',end='')
            print('#',end='')
        print()
    print()
print()

def hurufX(n):
    for baris in range(1,n+1):
        for kolom in range(1,n+1):
            if baris==kolom:
                print('#',end='')
            elif baris+kolom == n+1:
                print('#',end='')
            else:
                print(' ',end='')
        print()
    print()

def hurufZ(n):
     for baris in range(1,n+1):
        for kolom in range(1,n+1):
            if baris==1 or baris==n:
                print('#',end='')
            elif baris+kolom == n+1:
                print('#',end='')
            else:
                print(' ',end='')
        print()
    

def hurufN(n):
    for baris in range(1,n+1):
        for kolom in range(1,n+1):
            if kolom==1 or kolom==n:
                print('#',end='')
            elif baris == kolom:
                print('#',end='')
            else:
                print(' ',end='')
        print()
    print()

def tambah(n):
    tengah = 1 + (n//2)
    for baris in range(1,n+1):
        for kolom in range(1,n+1):
            if baris==tengah or kolom== tengah:
                print('#',end='')
            else:
                print(' ',end='')
        print()
    print()

def segitiga_kiri(n):
    for baris in range(1,n+1):
        for kolom in range(1,baris+1):
            print('#',end='')
        print()
    print()

def segitiga_kanan(n):
    for baris in range(1,n+1):
        pagars = baris
        spasi = n - pagars
        for kolom in range(spasi):
            print(' ',end='')
        for kolom in range(pagars):
            print('#',end='')    
        print()
    print()

def segitiga_rata(n):
    for baris in range(1,n+1):
        spasi = n -baris
        pagar = 2*baris-1
        for i in range(spasi):
            print(' ',end='')
        for i in range(pagar):
            print('#',end='')
        print()
    print()



def zigzag(n):
    for baris in range(1,n+1):
        for kolom in range(1,n+1):
            if baris %2 ==1 :
                print('#',end='')
            elif baris % 4 == 0:
                print('#',end='')
                break
            else:
                if kolom==n :
                    print('#',end='')
                else:
                    print(' ',end='')
                pass       
        print()
    print()
    



n = int(input('Masukan n : '))


pagar_vertikal(n)
pagar_horizontal(n)
pagar_horizontalxVertikal(n)
kosng_tengah(n)
hurufX(n)
hurufZ(n)
hurufN(n)
tambah(n)
segitiga_kiri(n)
segitiga_kanan(n)
segitiga_rata(n)
zigzag(n)