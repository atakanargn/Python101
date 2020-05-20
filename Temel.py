# BU KOD TÜRKÇE KARAKTER SORUNUNU ÇÖZER
# -*- coding: utf-8 -*-

# Python'ı yaratan Yazılımcı "Guido Van Russom"
# Hollandalı bir Yazılımcı
# 90'lı yıllarda ortaya çıkıyor
# Günümüzde 2 versiyonu var; Python2 ve Python3

# Lemniskat Python Dersleri
# < işareti ile açıklama satırları oluşturabilirsiniz.

"""
Aynı zamanda 3 tane çift tırnak işareti ile de
çok satırlı açıklama
satırları oluşturabilirsiniz.
"""

# ARITMETIK İŞLEMLER
print(21+2)    # Toplama işlemi
print(1293-25) # Çıkartma işlemi
print(16*400)  # Çarpma işlemi
print(22/7)    # Bölme işlemi
print(22//7)   # Ondalıksız bölme işlemi
print(17%5)    # Mod alma : Bölümden kalan
print(3**3)    # Üs alma

# Matematiksel işlemleri kolaylaştıran
# math modülü
import math

# Üs almaya yarar
math.pow(2,2) 
2**2

# Kök almaya yarar
math.sqrt(4)  
4**(1/2)

# pi ve e sayıları
math.pi
math.e

# Kaçış karakterleri
"""
\n -> Alt satıra geçme (Enter karakteri)
\t -> Paragraf girişi (Tab karakteri)
\\ -> \ işareti
"""
print("Ilk satır\nYeni satır\n\n2 alt satırda\n\tAlt satırda ve ileride")

"""
print() fonksiyonunun
sep yani separator
ve
end parametreleri
"""
print(2,0,0,1,sep="",end="")
print(10,11,1998,sep="/",end=".")
print(2,0,0,1,sep=".",end="\n")
print("Bu","bir","cümledir",sep=" ",end=".\n")
print("Bu","kelimeler","alt","altadır",sep="\n")

# Python versiyonu öğrenme
import sys
print("Python versiyon : ",sys.version)

# Çok satırlı yazdırma
print("""
3 adet çift tırnak ile çok satırlı yorum yapmanın yanında,
çok satırlı string'te tanımlayabiliriz,
yani print() fonksiyonu içinde de kullanabiliriz
""")

# DEĞİŞKEN TANIMLAMA VE VERİ TİPLERİ
tamsayi = 2            # int()   -> integer
ondalikli_sayi = 3.14  # float() -> float
kelime = "Lemniskat"   # str()   -> string

# Yukarıdaki tanımlamalarda değişkenlere değerlere atanmıştır.
# = işareti atama operatörü olarak geçmektedir.

# değişkenler del komutu ile silinebilir
del tamsayi

# sağdaki işlem yapılır sonra solda bulunan değişkene atanır
# eşittir anlamına gelmez çünkü matematikte aşağıdaki
# gibi bir eşitlik söz konusu değildir.
toplam = 0
toplam = toplam + 3

# STRINGLER ( KARAKTER DİZİLERİ, DİZELER, CÜMLELER, KELİMELER )
isim = "Atakan Argın"
isim[0]  # A
isim[-1] # n

# TUPLE ( ÇOKUZ )
test = ("Python","C","C++")
test[0]
test[-1]
test[0][2]

# STRING ve TUPLE'ların ortak özellikleri
# elemanlarının değiştirilemez oluşlarıdır
isim[0] = "B"
test[1] = "C#"

# LISTELER
liste = list()
liste = []
liste = ["Python","C","C++"]
liste[0] = "Java"
liste[-1] = "F#"

# SÖZLÜKLER
sozluk = {"araba":"car",
          "computer":"bilgisayar"}
sozluk['araba']

# KULLANICIDAN VERİ ALMA
# string - kelime
isim = str( input("Isminiz?\n>> ") )
# integer - tamsayı
tamsayi = int( input("Yaşınız?\n>> ") )
# float - ondalıklı sayı
boy = float( input("Boyunuz?\n>> ") )
# eval - integer, float olduğunu kendisi anlayabiliyor

# ARITMETİK OPERATÖRLER
+
-
*
/
// -> Ondalıksız bölme
%  -> Mod alma : bölümden kalan
** -> Üs alma
# math kütüphanesi de kullanılabilir

# MANTIKSAL OPERATÖRLER
# BOOLEAN CEBİRİ
not
and
or 
# örnekler
a = True
b = False
a and b
a or b
a and not(b)

# KARŞILAŞTIRMA OPERATÖRLERİ
> -> BÜYÜKTÜR
< -> KÜÇÜKTÜR

>= -> BÜYÜKTÜR VE EŞİTTİR
> and ==

<= -> KÜÇÜKTÜR VE EŞİTTİR
== -> EŞİTTİR
!= -> EŞİT DEĞİLDİR

= -> ATAMA OPERATÖRÜ 
# ÖRNEKLER
...

# in operatörü
"p" in "Python"
"P" in "Python" 
"Ja" in "Java"

# KARAR YAPILARI
# Eğer durum True değerindeyse komutlar çalışır
if durum==True:
    komutlar

# Eğer durum True değerindeyse komutlar çalışır
if durum==True:
    komutlar
# Değilse 2.komutlar çalışır
else:
    2.komutlar

if durum:
    komutlar
elif durum2:
    2.komutlar
elif durum3:
    3.komutlar
else:
    4.komutlar

# DÖNGÜLER

# while döngüsü
""" Belirlenen koşul sağlandığı sürece çalışan döngüdür
komutları döngü bloğunun içinde olmalıdır.
Pythonda tab'lar çok önemlidir.
"""
while durum ya da koşul:
    komutlar
    
sayac = 0
while sayac<10:
    sayac = sayac + 1
    print(sayac)

sayac = 0
while sayac<10:
    print(sayac)
    sayac += 1

# Örnekler

# 10'dan 1'e geriye doğru saydırma
sayac = 10
while sayac > 1:
    print(sayac)
    sayac = sayac - 1

# 1'den kullanıcıdan alınan değere kadar olan sayıları toplama

sayac = 1
sayi = int( input("SAYI GİRİNİZ : ") )
toplam = 0
while sayac < sayi:
    toplam = toplam + sayac
    sayac = sayac + 1
print(toplam)

# kullanıcıdan alınan sayı
# çiftse 0'dan alınan sayıya kadar çift sayıların toplamı
# tek ise 1'den alınan sayıya kadar tek sayıların toplamı
sayi = int( input("SAYI GİRİNİZ : ") )
if sayi%2==0:
    sayac=0
else:
    sayac=1

toplam = 0
while sayac <= sayi:
    toplam = toplam + sayac
    sayac = sayac + 2
print(toplam)

# while - else kullanımı
""" Döngü koşulu sağlanmadığı ilk durumda
else içerisindeki komutlar 1 kez çalıştırılır. """
sayac = 0
while sayac < 10:
    sayac += 1
    print(sayac)
else:
    print("1'den 10'a kadar saydım.")

# for döngüsü
# Belirtilen aralıkta işlem yapmaya yarar
# range() içerisinde
# ilk parametre, başlangıç değeri (dahil)
# ikinci parametre, bitiş (dahil değil)
# üçüncüsü ise artış miktarıdır
"""
for sayac in range(başlangıç,bitiş,artış_miktarı):
    komutlar
    komutların içinde sayac değişkeni kullanılabilir
"""

for sayac in range(0,10+1,1):
    print(sayac)

# çift sayıları saydıralım
for sayac in range(0,10+1,2):
    print(sayac)

# tek sayıları saydıralım
for sayac in range(1,10+1,2):
    print(sayac)

# 0'dan kullanıcıdan alınan sayıya kadar toplayalım
sayi = int(input("SAYI GİRİNİZ : "))
toplam = 0
for sayac in range(0,sayi+1,1):
    toplam = toplam + sayac
print(toplam)

# kullanıcıdan alınan 3 sayıyı toplayalım
toplam = 0
for sayac in range(1,3+1):
    sayi = int(input("SAYI : "))
    toplam = toplam + sayi
print(toplam)

# kullanıcı 0 girene kadar sayıları toplayalım
toplam = 0
sayi = int( input("SAYI : ") )

while sayi != 0:
    toplam = toplam + sayi
    sayi = int( input("SAYI : ") )
print(toplam)

# Sinan hoca:
toplam = 0
sayi = int( input("SAYI : ") )

while True:
    if(sayi == 0):
        break
    toplam = toplam + sayi
    sayi = int( input("SAYI : ") )
print(toplam)

# while ile yaptığımız alıştırmaları yapalım

# kullanıcıdan alınan sayı
# çiftse 0'dan alınan sayıya kadar çift sayıların toplamı
# tek ise 1'den alınan sayıya kadar tek sayıların toplamı
sayi = int(input("SAYI : "))
if sayi%2==0:
    baslangic = 0
else:
    baslangic = 1

toplam = 0
for sayac in range(baslangic,sayi+1,2):
    toplam += sayac # toplam = toplam + sayac
print(toplam)
# 1-100 arasındaki 1 ile 100 dahil, sayıların 3 katının 7 fazlası, 2 veya 3'e tam bölünen sayıları bulan program
for sayac in range(1,100+1):
    sayi = (sayac*3)+7
    if (sayi%2==0) or (sayi%3==0):
        print(sayac)

# String işlemleri
-> StringIslemleri.py

# Liste işlemleri
-> PythonDiziler.py

# Sözlükler hakkında detaylı bilgi
-> Sozlukler.py

# Tuple detayları
-> Tuple.py

# Fonksiyon tanımlama
""" Fonksiyonlar kod tekrarını önler.
Kod tekrarı önlenirse, hata payı azalır.
Fonksiyon üzerindeki değişiklikler tüm programı etkiler,
defalarca değişiklik yapmaya gerek kalmaz.
Değişken tanımlamaya benzer.
"""

# Modüller
-> Modüller klasörü

# Dosya işlemleri
-> DosyaIslemleri.py

# Hata yakalama
-> HataYakalama.py