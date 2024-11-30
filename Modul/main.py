import math

def l_persegi(sisi):
    luas = sisi*sisi 
    keliling = sisi*sisi*sisi*sisi
    print(f'luas persegi {sisi} * {sisi} = {luas}')
    print(f'keliling persegi adalah {keliling}')


def l_persegipanjang(panjang, lebar):
    ls = panjang * lebar
    print(f'luas persegi panjang {panjang} * {lebar} = {ls}')

def l_segitiga(alas, tinggi):
    luassgt = 1/2 * alas * tinggi
    print(f'luas segitiga adalah {1/2}, {alas}, {tinggi} = {luassgt}')

def l_belahketupat(d1, d2):
    luasblh = 1/2 * d1 * d2
    print(f'luas belah ketupat {1/2}, {d1}, {d2} = {luasblh}')

def l_layanglayang(d1, d2):
    luaslyg = 1/2 * d1 * d2
    print(f'luas layang layang {1/2}, {d1}, {d2} = {luaslyg}')

def l_balok(panjang, lebar, tinggi):
    luasbalok = 2 * (panjang*lebar) + (panjang*tinggi) +  (lebar*tinggi)
    print(f'luas balok adalah {luasbalok}')

def l_kubus(sisi):
    luaskubus = 6 * (sisi*sisi) 
    print(f'luas kubus adalah {luaskubus}')

def l_tabung(jari2, tinggi):
    luastabung = 2 * 22/7 * (jari2*tinggi) 
    print(f'luas tabung adalah {luastabung}')

def l_limassegiempat(sisi, sisitegak):
    luaslimassgempt = (sisi*sisi) + (4*sisitegak)
    print(f'Luas Limas Segiempat adalah {luaslimassgempt}')

def l_primasegitiga(luasalas, sisitegak):
    luasprismasgt = (2*luasalas) + (3*sisitegak)
    print(f'Luas Prisma Segitiga Adalah {luasprismasgt}')