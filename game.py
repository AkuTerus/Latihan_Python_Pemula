import random


def generate_angka_komputer(batas):
    hasil =random.randrange(0,batas+1)
    return hasil
def game(angka_komputer,nyawa):
    print('===Program Tebak Angka===')
    menang = False
    nyawa = 5
    while menang == False:
        tebakan = int(input('Masukan tebakan anda : '))
        nyawa = nyawa-1
        if tebakan== angka_komputer:
            menang = True
        else:

            print('tebakan anda salah silahkan coba lagi')
            if tebakan> angka_komputer:
                print(f'tebakan anda terlalu besar, sisa nyawa anda {nyawa}')
            else:print(f'tebakan anda terlalu kecil, sisa nyawa anda{nyawa}')
            if nyawa == 0:
                break
    if menang == True:
        print(f'anda menang sisa nyawa anda {nyawa}')
    else:
        print(f'anda kalah. nyawa anda habis')
            

level = int(input('Masukan Level : 1/2/3: '))
if level == 1 :
    batas = 100
    nyawa = 5
elif level == 2:
    batas = 1000
    nyawa = 7
elif level == 3:
    batas= 10_000
    nyawa=14
else:
    batas= 1_000_000
    nyawa = 28



angka_komputer = generate_angka_komputer(batas)
print(angka_komputer)
game(angka_komputer,nyawa)