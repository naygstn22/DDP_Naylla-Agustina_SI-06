#nomer 1
angka= int(input("masukan bilangan bulat:"))

if angka % 2 ==0:
    print("bilangan genap")
elif angka % 2!=0:
    print("bilangan ganjil")
else:
    print("input tidak valid") 

#nomer 2
nilaiujian =int(input("masukkan nilai ujian"))

if nilaiujian >=75:
    print("lulus")

else:
    print("tidak lulus")

#nomer 3
usia= int(input("masukkan usia anda"))
if usia >= 18:
        print("dewasa")
elif usia < 18 and usia > 13:
        print("remaja")
else:
      print("anak-anak")

#nomer 4
statusanggota = input("masukkan status anggota anda: ")
if statusanggota == "gold" or statusanggota == "silver":
    print("selamat anda mendapatkan diskon") 
elif statusanggota == "bronze":
     print("maaf anda tidak mendapatkan diskon")
else:
     print("input tidak valid")

#nomer 5
jumlahpembelian = int(input("masukkan jumlah pembelian"))
hargaitem = 1000
hargadiskon = hargaitem * jumlahpembelian * (10/100)
hargatotal = hargaitem * jumlahpembelian
total = hargatotal - hargadiskon

print(f"anda mendapat diskon 10%, harga per item {hargaitem} jadi total yang harus di bayar {total}") if jumlahpembelian > 100 else print (f"harga per item {hargaitem},jadi total yang dibayar adalah {hargatotal}")
     
