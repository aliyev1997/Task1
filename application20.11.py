from mehsul import Mehsul
from firma import Firma

from kategoriya import mehsullar,firmalar

def searchMehsulKategoriya(kateqoriya_adi):
    for mehsul in mehsullar:
        if mehsul.kategoriya==kateqoriya_adi:
            print(mehsul.firma)
            break
        else:
           print('Teesuf ki, bele bir mehsul yoxdur')


def searchFirmaKategoriyasi(firma_adi):
    for firma in firmalar:
        if firma.ad==firma_adi:
           print(firma.kategoriya)
        else:
            ('Bele firma adi yoxdur.')

kateqoriyya_adi=input('Kategoriya adini daxil edin: ')

firma_adi=input("Firma adini daxil edin: ")

searchMehsulKategoriya(kateqoriyya_adi)
searchFirmaKategoriyasi(firma_adi)
