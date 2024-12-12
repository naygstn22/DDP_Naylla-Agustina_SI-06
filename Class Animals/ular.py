from Animals import *

class ular(animals):
    def __init__(self, nama, makanan, hidup, berkembang_biak, warna_sisik, jenis_gigi):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.warna_sisik = warna_sisik
        self.jenis_gigi = jenis_gigi

    def cetak_ular(self):
        super().cetak()
        print(f'warna sisik ular ini adalah warna {self.warna_sisik} dan jenis gigi ular ini {self.jenis_gigi}')

cobra = ular('ular cobra', 'tikus', 'darat', 'bertelur', 'hitam dan abu-abu', 'bertaring')
cobra.cetak_ular()

zaitun = ular('ular zaitun', 'belut conger', 'laut', 'bertelur', 'biru dan hitam', 'bertaring')
zaitun.cetak_ular()

