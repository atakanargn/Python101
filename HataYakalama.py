# Hata yakalama,
# Uygulamanın çalışması sırasında oluşan hataların yakalanıp,
# düzeltilme şansı varsa düzeltilerek ya da ekrana hata mesajları vererek
# programı kullanan kişiye fayda sağlar.

# Sonuçta herkes Yazılımcı değil
# veya Python bilmeden, Python scriptlerini
# denemek isteyen arkadaşlarımıza bu şekilde yardımcı olabiliriz.

# En basitinden int(input()) ile kullanıcıdan veri aldığımız esnada,
# kullanıcı tamsayı değeri dışında bir değer girerse,
# ValueError alıyor.
sayi = int(input("Sayi giriniz : "))

# Gördüğünüz gibi:
# ValueError: invalid literal for int() with base 10: 'girilen değer'
# şeklinde bir uyarı aldık ve program bitti.

# Hata Ayıklama kullanımı

# try bloğu içine hata yakalanacak olan kod kısımlarını giriyoruz
try:
    """ Kod Bloğu """
# except bloğu ise beklenen hata geldiğinde yapılacak işlemler,
except HataAdı:
    """ Kod Bloğu """

# Hata yakalama tam olarak bu noktada devreye giriyor.
# bu durumda biz ValueError hatası bekliyoruz.
try:
    sayi1  = int(input("1.Sayiyi girin : "))
    sayi2  = int(input("2.Sayiyi girin : "))
    bolum = sayi1/sayi2
    print(bolum)
except ValueError:
    print("Lutfen tamsayi disinda deger girmeyin!")

# Bu durum tamam ancak bölme işlemi yaparken alabileceğimiz bir hata daha var.
# ZeroDivisionError : Hiç bir sayı sıfıra bölünemez!
# O zaman:
try:
    sayi1  = int(input("1.Sayiyi girin : "))
    sayi2  = int(input("2.Sayiyi girin : "))
    toplam = sayi1/sayi2
    print(toplam)
except ZeroDivisionError:
    print("Hic bir sayi sifira bolunemez.")

# Bu seferde sadece sıfıra bölme hatasına yakaladık,
# Hala ValueError alıyoruz.

# Şanslıyız ki Python mantıklı olarak 2 hatayı da yakalamamıza izin veriyor.
try:
    sayi1  = int(input("1.Sayiyi girin : "))
    sayi2  = int(input("2.Sayiyi girin : "))
    toplam = sayi1/sayi2
    print(toplam)
except ValueError:
    print("Lutfen tamsayi disinda deger girmeyin!")
except ZeroDivisionError:
    print("Hic bir sayi sifira bolunemez.")

# Bazı durumlarda hatanın açıklaması yanında
# orjinal hata metnini de yazdırmak isteyebiliriz.
# Hata ismi gözükmez ancak hatanın neden kaynaklandığı gözükecektir.
# Bu durumda devreye gibi anlamına gelen 'as' giriyor.
#   'as' operatörünü daha önce modül içe aktarırken,
#   isim kısaltması içinde kullanmıştık.
    import numpy as np
    import pyautogui as pag

# Gelelim kullanıma
# try... except... as...
try:
    """ Kod Bloğu """
except HataAdı as atanacağıDeğişken:
    """ Kod Bloğu """
    print(atanacağıDeğişken)

# Örnekle pekiştirelim
try:
    sayi1  = int(input("1.Sayiyi girin : "))
    sayi2  = int(input("2.Sayiyi girin : "))
    toplam = sayi1/sayi2
    print(toplam)
except ValueError as hata:
    print("\t Lutfen tamsayi disinda deger girmeyin!")
    print("\t Orjinal hata : "+str(hata))
except ZeroDivisionError as hata:
    print("\t Hic bir sayi sifira bolunemez.")
    print("\t Orjinal hata : "+str(hata))

try:
    sayi1  = int(input("1.Sayiyi girin : "))
    sayi2  = int(input("2.Sayiyi girin : "))
    toplam = sayi1/sayi2
    print(toplam)
except:
    print("\t Bir hata oluştu!")

# try... except... else...
# 'else'i daha önce 'koşullu ifadelerde'(if-elif-else) kullanmıştık.
# Burda da aynı anlama geliyor ve
# hatalarımızı tek blokta değilde adım adım
# kontrol ettirmemize yarıyor.
# Kullanımı;
try:
    """ 1.Adım Kod Bloğu """
except Hata1:
    """ Kod Bloğu """
else:
    try:
        """ 2.Adım Kod Bloğu """
    except Hata2:
        """ Kod Bloğu """

# Aynı örneği düzenleyelim:
try:
    sayi1  = int(input("1.Sayiyi girin : "))
    sayi2  = int(input("2.Sayiyi girin : "))
    #toplam = sayi1/sayi2
    #print(toplam)
except ValueError as hata:
    print("\t Lutfen tamsayi disinda deger girmeyin!")
    print("\t Orjinal hata : "+str(hata))
else:
    try:
        toplam = sayi1/sayi2
        print(toplam)
    except ZeroDivisionError as hata:
        print("\t Hic bir sayi sifira bolunemez.")
        print("\t Orjinal hata : "+str(hata))

# try... except... finally...
# Kullanım
try:
    """ Kod Bloğu """
except hataAdı:
    """ Hata ile karşılaşında yapılacak işlemler """
finally:
    """ Hata olsada olmasada yapılacak işlemler """

# Bunu en güzel örnek olarak dosya işlemlerinde kullanabiliriz.
# Dosya üzerinde işlem yaparken işimiz bittiğinde dosyayı kapatmasını istiyoruz,
# ancak işlemler sırasında aldığımız bir hata yüzünden dosya kapanmazsa,
# ilk derste bahsettiğimiz "Runtime Error" hatalarıyla karşılaşabiliriz.
# Dosya üstünde değişiklik yaparken IOError hatası alabiliriz.
try:
    dosya = open("dosya.txt","w")
    """ Bu kısımda bir sürü dosya işlemi yaptık """
except IOError: #Girdi/Çıktı hatası
    print("Bir hata oluştu!")
finally:
    dosya.close()

# raise
# Pythonda olmayan ancak kendi hatalarımızı üretmeye yarayan deyimdir.
sayi1=int(input("Sayi 1 : "))
sayi2=int(input("Sayi 2 : "))

if(sayi1==0 or sayi2==0):
    raise Exception("Artik 0 sayisiyla toplamayi denemek istemiyorum!")
else:
    pass
print(sayi1+sayi2)

# Exception yerine kendi hata mesajı ismimizi yazmayı deneyelim
sayi1=int(input("Sayi 1 : "))
sayi2=int(input("Sayi 2 : "))

if(sayi1==0 or sayi2==0):
    raise SifirlaToplama("Artik 0 sayisiyla toplamayi denemek istemiyorum!")
else:
    pass
print(sayi1+sayi2)

# Gördüğünüz gibi program hata verdi.
# Çünkü raise deyimi Pythonda tanımlı hata isimleriyle sınırlıdır.
sayi1=int(input("Sayi 1 : "))
sayi2=int(input("Sayi 2 : "))

if(sayi1==0 or sayi2==0):
    raise ValueError("Artik 0 sayisiyla toplamayi denemek istemiyorum!")
else:
    pass
print(sayi1+sayi2)

# Tüm hataları yakalamak
# try... except...
try:
    """ Kod Bloğu """
except:
    print("Bir hata oluştu!")