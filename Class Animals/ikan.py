from Animals import*

class ikan(animals):
    def __init__(self, nama, makanan, hidup, berkembang_biak, warna_ikan, jenis_ikan):
        super().__init__(nama, makanan, hidup, berkembang_biak,)
        self.warna_ikan = warna_ikan
        self.jenis_ikan = jenis_ikan

    def cetak_ikan(self):
        super().cetak()
        print(f'warna ikan ini adalah warna {self.warna_ikan} dan hewan ini jenisnya ikan {self.jenis_ikan} ')

nemo = ikan('ikan nemo', 'plankton', 'air', 'bertelur', 'orange', 'air laut')
nemo.cetak_ikan()

paus = ikan('ikan paus', 'ikan kecil', 'air', 'melahirkan', 'abu-abu', 'air laut')
paus.cetak_ikan()

mas = ikan('ikan mas', 'pelet', 'air', 'bertelur', 'kuning', 'air tawar')
mas.cetak_ikan()