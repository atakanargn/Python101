#open()
dosya=open("dosyamiz.txt")
dosya.readline()

# Imleç
dosya.seek(21)
dosya.readline()

# Dosyayı baştan sona okumak
dosya.seek(0)
for satir in dosya:
    print(satir)

# Dosyayı satır satır diziye atamak
dizi=dosya.readlines()

# Dosya işlem kipleri
# r : sadece okuma
# w : yazma
# a : sonuna ekleme
# a+, w+, r+ : dosya güncelleme (hem okuma hem yazma)

dosya=open("yeniDosya.txt","w")
dosya.write("\n")
dosya.write("2.Satır\n")
dosya.write("Hadi bu da 3 olsun!")

dosya.seek(0)

dizi=dosya.readlines()
metin=""

for satir in dizi:
    metin+=satir
dosya.close()


# Dosyayı baştan sona okuyup, değştrmek
# Dosyayı açtık
dosya=open("dosyamiz.txt","r")
# Tüm satırları diziye atadık
dizi=dosya.readlines()

metin=""
for satir in dizi:
    metin+=satir
dosya.close()

# metin stringi içinde istediğimiz değişikliği yapabiliriz,
# yeni satır ekleyebiliriz, string üstüne ekleme yaparak.
metin+="Yeni satır ekleme\n"

# metin stringi içinde yaptığımız değişiklikleri, aşağıdaki yöntemle kaydedebiliriz.
dosya=open("dosyamiz.txt","w")
dosya.write(metin)
dosya.close()
# BU KADAR.

# Alıştırma olarak;
# Bugün öğrendiğimiz konuları kullanarak,
# Öğrencilerin (numara, ad, soyad)
# bilgilerini içeren bir otomasyon oluşturunuz.
