adSoyad = "Atakan Argın"
ad = adSoyad[:6]
soyad = isim[7:]

#Karakter sayısı
i=0
for harf in adSoyad:
    i+=1
#Karakter sayısı
len(adSoyad)

#Harf arama örneği yapalım.

# String tipi değişkenlerde "in" operatörü
# Dizilerle aynı şekilde kullanılır.
cumle="Bu değişken string tipindedir."
"d" in cumle #ÇIKTI : // True
"değişken" in cumle  #ÇIKTI : // True
"tanımlama" in cumle #ÇIKTI : // False
"değişken" and "string" in cumle #ÇIKTI : // True
"değişken" or "tanımlama" in cumle #ÇIKTI : //'değişken'

# çift tırnak ve tek tırnak
# Aşağıdaki cümlede "Malatyalı" kelimesini tırnak içinde gösterelim.
cumle="Malatyalıların ortak özelliği hepsinin Malatyalı olmasıdır."

cumle="Malatyalıların ortak özelliği hepsinin "Malatyalı" olmasıdır."

cumle='Malatyalıların ortak özelliği hepsinin "Malatyalı" olmasıdır.'

cumle="Malatyalıların ortak özelliği hepsinin 'Malatyalı' olmasıdır."

cumle="Malatyalıların ortak özelliği hepsinin \"Malatyalı\" olmasıdır."

cumle='Malatyalıların ortak özelliği hepsinin \'Malatyalı\' olmasıdır.'

# Yani kuralımız şu;
# Ters bölü kullandıktan
# sonraki karakter asıl anlamında kullanılmaktadır.

kacis="Bu birinci satır\nbu da ikinci"

kacis="Bu birinci satır\\nbu artık ikinci satır değil!"

altAlta = "Cümleleriniz tek satıra sığmıyorsa \n\
\n\
\n\
\n\
ters bölü karakterini koyarak alt satırdan devam edebilirsiniz."

uzunMetin="""Uzun bir metin
veya görünümü bozmadan şiir falan
yazmak istiyorsanız, \"\"\" kullanabilirsiniz. """

# Cümle biçimlendirme
algNot="AA"
trNot="AA"
matNot="DD"
print("Algoritma notum "+algNot+", TeknikResim notum "+trNot+" \
ve Matematik notum "+matNot)

print("Algoritma notum %s, TeknikResim notum %s \
ve Matematik notum %s" % (algNot, trNot, matNot))

# Burda;
# string ifadeler için %s,
# integer ifadeler için %d > double veya %i > integer
# float ifadeler için %f kullanılır.

# yine float bir ifadenin
# istediğimiz kadar rakamını yazdırmak için
# %virgülden önceki rakam sayısı . virgülden sonraki rakam sayısı f
# ÖRN : %0.2f
from math import pi
print("%.2f"%pi)

# format() fonksiyonu
print("A : Adama bak, {3} programlama dilini kayda \
değer seviyede kullanabiliyormuş!\n\
B : Hangi dillermiş ?\n\
A : {2},{0},{1}".format("Java","Python","C",3))

# format() fonksiyonu diziden çekme
dizi=["Matematik","Fizik","Algoritma","Lineer Cebir","Yapay Zeka"]
print("Dizinin 3.elemanı {2},\n5.elemanı {4}".format( *dizi ))

# upper(), lower(), title()
soyad="soyad"
print(soyad.upper())

kelime="tÜm hARflErİ KüÇÜk yAPSaK dAHa iyİ OlACak GiBİ."
print(kelime.lower())

baslik="mühendislik fakültesi"
print(baslik.title())

# find()
cumle="find fonksiyonu string içinde arama yapmaya yarar."
aranan="fonksiyon"
cumle.find(aranan)
# Kelime yoksa -1 döndürür.

# Cümle parçalama
cumle="domates, biber, patlıcan"
cumle.split()
cumle.split(",")

# Cümle birleştirme
# Mail örneği
mail=['argin.atakan','gmail.com']
'@'.join(mail)
# Mail listesi örneği
mailler = ['l1712709013@sdu.edu.tr',
           'l1814567892@sdu.edu.tr',
           'l1343632013@sdu.edu.tr',
           'l1123636263@sdu.edu.tr',
           'l1923876933@sdu.edu.tr',
           'l1012516236@sdu.edu.tr']
alici=';'.join(mailler)

# replace() fonksiyonu
# replace(belirtilen, yerine konulacak)
cumle="cümle"
cumle.replace("ü","u")

cumle="aradaki boşlukları yerine _ koyalım"
cumle.replace(" ","_")

# Strip fonksiyonu
# Cümle başındaki ve sonundaki boşlukları siler.
cumle="      Merhaba Python      "
cumle.strip()

# isnumeric() sadeec sayılardan mı oluşuyor ?
cumle="a123"
cumle.isnumeric() # False

cumle="123"
cumle.isnumeric() # True

# isim soyisim ve doğum yılına göre
# kurallara uygun mail adresi oluşturalım
# Kurallar;
# Boşluk olmayacak "_" veya "." kullanılabilir
# Tüm harfler küçük
# Sadece sayı içermeyecek
# Türkçe karakter içermeyecek
# Alan adını kendi seçebilir