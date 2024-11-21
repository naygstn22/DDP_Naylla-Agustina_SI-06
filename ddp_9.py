#nomer 1
print ("soal nomer 1")
def celcius_ke_fahrenheit(celcius):
    print(celcius * 9/5 +32 )
celcius_ke_fahrenheit(0)
celcius_ke_fahrenheit(100)

print("soal nomer 2")

def is_genap(genap):
    print(genap %2 == 0)

is_genap(4)
is_genap(5)

print("soal nomer 3")
# rata" nilai kelulusan 79
def skor(nilai):
     if nilai >= 80:
         print("lulus")
     else:
         print("gagal")

skor(80)
skor(60)

print("soal nomer 4")

def bil_ganjil(ganjil):
    for i in range(1, ganjil+1, 2):
        print(i, end=" ")
bil_ganjil(20)