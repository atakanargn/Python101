# Boş dizi tanımlama
diller = []

# Dizinin sonuna eleman ekleme : append() fonksiyonu
diller.append("C")
diller.append("Java")
diller.append("Python")

# Tanımladığımız dizinin son hali
diller = ["C", "Java", "Python"]

# Dizideki elemanların bulunduğu sıraya index denir.

print(diller[0])  #ÇIKTI// C
print(diller[2])  #ÇIKTI// Python
print(diller[1])  #ÇIKTI// Java

print(diller[-1]) #ÇIKTI// Python
print(diller[-2]) #ÇIKTI// Java
print(diller[-3]) #ÇIKTI// C

print(diller[-5])  #ÇIKTI// ???

# Dizilerde dilimleme (slicing)
# dizi[ başlangıç indisi : bitiş indisi,dahil değil ]
pasta = [1,2,3,4,5,6,7,8,9,10]

print(pasta)    # Dizinin tamamı
print(pasta[:10])  # Dizinin tamamı
print(pasta[0:])   # Dizinin tamamı
print(pasta[0:10]) # Dizinin tamamı

print(pasta[3:10]) # 3.elemandan, 10.elemana kadar; 10 dahil değil

print(pasta[6:7])  # 6.elemandan, 7.elemana kadar; 7 dahil değil yani sadece 6

# Elemanları değiştirebiliriz
diller[0]="C++"

# Dizinin son hali
diller = ["C++", "Java", "Python"]

# Bildiklerimizi kullanarak diziyi listeleme
i=0
elemanSayisi=3
while i < elemanSayisi: print(diller[i]); i+=1

# Daha anlaşılabilir
i=0
elemanSayisi = len(diller)
while i < elemanSayisi:
    print(diller[i])
    i+=1

# Eleman sayısı len() fonksiyonu ile bulunabilir
len(diller)

# in operatörü
"Delphi" in diller #False
"Java" in diller #True

diller.append("Delphi")
"Delphi" in diller #True

# in operatörü ile listeleme
for dil in diller: print(dil)

for dil in diller:
    print(dil)

# Dizinin son elemanını silmek : pop() fonksiyonu
# pop() fonksiyonu son elemanı siler ve sildiği elemanı ekrana yazdırır
# veya bu değeri değişkene atayabilirsiniz
diller.pop() #ÇIKTI// 'Delphi'
sonDeger=diller.pop() #ÇIKTI VERMEZ// sonDeger="Python"

# Dizinin son hali
diller = ["C++","Java"]

# Diziden istenilen elemanı silme : remove()
# Elemanı siler, çıktı vermez.
diller.remove("C++")

# Dizinin son hali
diller=["Java"]

########################################################

cuzdan=["tc kimlik","ehliyet","kredi kartı","gülkart","pena","pena","pena",5,5,20,10,10,10,50]

# Tekrarlayan elemanları bildiğimiz yoldan saydırmak
i=0
for eleman in cuzdan:
    if(eleman==5):
        i+=1
print(i)

# Tekrarlayan elemanları saydırma : count()
cuzdan.count(5)           #ÇIKTI// 2
cuzdan.count(10)          #ÇIKTI// 3
cuzdan.count("pena")      #ÇIKTI// 3
cuzdan.count("tc kimlik") #ÇIKTI// 1

# Bir elemanın listedeki konumu
i=0
for eleman in cuzdan:
    if(eleman==5):
        print(i)
        break
    i+=1

# Bir elemanın listedeki konumu : index()
cuzdan.index("gülkart")

# Istenilen konuma eleman ekleme
cuzdan.insert(7,200)

# etiketleme
cz = cuzdan
cz.pop() #?????

# copy
cuzdan2 = cuzdan.copy()

# Liste toplama, genişletme
sinif = []
AGrubu = ["Ahmet", "Ayşe", "Mehmet", "Ali"]
BGrubu = ["Mehmet", "Veli", "Fadime", "Irem"]

sinif.extend(AGrubu)
sinif.extend(BGrubu)
# veya
# + toplar, * çoğaltır
sinif = AGrubu + BGrubu

# Sayıların karesini alıp şu şekilde başka bir diziye aktarabiliyoruz
dizi   = [1,2,3,4,5,6,7,8,9,10]
karesi = []
for sayi in dizi:
    karesi.append(sayi**2)

# Ancak bu işlemi tek adımda da yapabiliriz
dizi   = [1,2,3,4,5,6,7,8,9,10]
karesi = [sayi**2 for sayi in dizi]

# dizi içinden sadece çift sayıları almak istersek
dizi    = [1,2,3,4,5,6,7,8,9,10]
ciftler = []
for sayi in dizi:
    if(sayi%2==0):
        ciftler.append(sayi)

# Bunu yine tek adımda kolayca yapabiliriz
ciftler = [sayi for sayi in dizi if sayi%2==0]

# Örnek olarak;
# girilen 5 sayıdan tek olanları toplayan bir program yazalım
girilenler=[]
for i in range(0,5,1):
    girilenler.append(int(input("Sayi girin : ")))

tekler = [sayi for sayi in girilenler if sayi%2==1]

toplam = sum(tekler)
print(toplam)