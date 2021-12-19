# while döngüsü
""" Belirlenen koşul sağlandığı sürece çalışan döngüdür
komutları döngü bloğunun içinde olmalıdır.
Pythonda tab'lar çok önemlidir.
"""

# 1) 10'dan 1'e geriye doğru saydırma
# FOR - WHILE -

# genelse sayaç bu harfler olarak tanımlanır i, j, k
for i in range(10,0,-1):
    print(i)

# 2) 1'den kullanıcıdan alınan değere kadar olan sayıları toplama
eKadar = int( input("Kaça kadar toplayayım ? : ") )
toplam = 0
for i in range(1,eKadar,1):
    print(toplam,"+",i)
    toplam += i
print("TOPLAMI",toplam)

eKadar = int( input("Kaça kadar toplayayım ? : ") )
toplam = 0
i = 1
while i < eKadar:
    print(toplam,"+",i)
    toplam += i
    i += 1
print("TOPLAMI",toplam)

# 3) kullanıcıdan alınan sayı
# çiftse 0'dan alınan sayıya kadar çift sayıların toplamı
# tek ise 1'den alınan sayıya kadar tek sayıların toplamı

sayi = int( input("SAYI GİRİNİZ : ") )

if sayi % 2 == 0:
    print("SAYI ÇİFT")
    baslangic=0
else:
    print("SAYI TEK")
    baslangic=1

toplam = 0
0+2+4+6+8
for i in range(baslangic,sayi,2):
    print(i)
    toplam += i

print("TOPLAMI",toplam)

# WHILE ile sizde yazın

# while ' ın yanlış kullanımı:
toplam = 0
sayi = int( input("SAYI : ") )

while True:
    if(sayi == 0):
        break
    toplam = toplam + sayi
    sayi = int( input("SAYI : ") )
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

# 1) 0'dan kullanıcıdan alınan sayıya kadar toplayalım



# 2) kullanıcıdan alınan 3 sayıyı toplayalım

toplam = 0
for i in range(0,3,1): # 0, 1, 2
    sayi = float( input("SAYI GİRİNİZ : ") )
    toplam += sayi

print("GİRDİĞİNİZ 3 SAYININ TOPLAMI :",toplam)

# SONSUZ DÖNGÜ
durum=True
while durum==True:
    print("BU BİR SONSUZ DÖNGÜDÜR!")

# 3) kullanıcı 0 girene kadar sayıları toplayalım
sayac  = 0
sayi   = 1
toplam = 0

while True:
    sayi = int( input("SAYI GİRİNİZ : ") )
    if(sayi!=0):
        sayac += 1
        toplam += sayi
    else:
        break

print("GİRDİĞİNİZ",sayac,"KADAR SAYININ TOPLAMI : ",toplam)

# *1) kullanıcıdan alınan sayı
# çiftse 0'dan alınan sayıya kadar çift sayıların toplamı
# tek ise 1'den alınan sayıya kadar tek sayıların toplamı



# *2) 1-100 arasındaki 1 ile 100 dahil, sayıların 3 katının 7 fazlası, 2 veya 3'e tam bölünen sayıları bulan program

for i in range(1,100+1,1):
    sayi = (i*3) + 7
    if(sayi%2==0 or sayi%3==0):
        print(i)

# *3) 1'den 100'e kadar olan tüm asal sayıları yazdıran programı yazınız
# KENDİNİZE ÖDEV

