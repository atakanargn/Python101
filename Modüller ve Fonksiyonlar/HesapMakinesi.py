""" Bu modul ile 4 islem yapabilirsiniz. """

__all__ = ['topla','carp','fark','bol','yazar']

yazar="Atakan"
dizi=["abcd",1,2,3]
sozluk={"key":"item"}

def topla(*sayilar):
    """ Bu fonksiyon toplama işlemi yapar. """
    toplam=0
    for sayi in sayilar:
        toplam+=sayi
    return toplam

def fark(*sayilar):
    pass

def carp(*sayilar):
    pass

def bol(*sayilar):
    pass