from Animals import *

class burung(animals):
    def __init__(self, nama, makanan, hidup, berkembang_biak, jenis_bulu, bunyi):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.jenis_bulu =jenis_bulu
        self.bunyi = bunyi

    def cetak_burung(self):
        super().cetak()
        print(f'hewan ini berbulu {self.jenis_bulu} dan hewan ini berbunyi {self.bunyi}')

print('=========cetak burung===========')
print('=========object pertama===========')
beo = burung('Burung beo', 'biji-bijian', 'udara', 'bertelur', 'blue and orange', 'kamu jelek')
beo.cetak_burung()

print('=========object kedua===========')
merak = burung('Burung merak', 'biji-bijian', 'darat', 'bertelur', 'hijau dan biru', 'ang ang ang')
merak.cetak_burung()

print('=========object ketiga===========')
elang = burung('Burung elang', 'ikan', 'udara', 'bertelur', 'coklat', 'ngak ngak ngak')
elang.cetak_burung()


