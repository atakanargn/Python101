# Sözlük (dictionary) tanımlama
sozluk = {}
kelime = {"kitap" : "book","defter": "notebook","dil"   : "language"} # Böyle hoş durmadı
# Düzenleme
kelime = {"kitap" : "book",
          "defter": "notebook",
          "dil"   : "language"}

type(sozluk)
type(kelime)

# Sözlük elemanı sayma
len(kelime)
len(sozluk)

# Sözlük elemanlarına erişmek
sözlük[sözlük_öğesinin_adı]

# Deneyelim
print(kelime['kitap'])
print(kelime['defter'])
print(kelime['dil'])

# Sözlüklere eleman ekleme
kelime['bilgisayar']="pc"

# Sözlüklerin elemanlarını değiştirme
kelime['bilgisayar']="computer"

# Bir sözlüğe değer olarak bütün veri tipleri verilebilir
insan = {"ad" : "Atakan", "soyad" : "Argın", "yaş" : 19, "programlama_dilleri" : ("Python","Temel C","Temel C++")}

# Harfleri sıra numarasına göre sözlüğe atalım
harfler = 'abcdef'

harfSozluk={}
for harf in harfler:
    harfSozluk[harf]=harfler.index(harf)
# veya
harfSozluk = {harf: harfler.index(harf) for harf in harfler}

# Isim listesinde isimlerin harf sayısını sözlükle gösterme
isimler = ["ahmet", "mehmet", "atakan", "zeynep", "selma", "abdullah", "cem"]
isimUzunluk = {isim: len(isim) for isim in isimler}

# Sözlüklerin fonksiyonları

# keys(), anahtar kelimeleri listeler
kelime.keys()

# values(), anahtar kelimelere karşılık gelen değerleri listeler
kelime.values()

# items(), anahtar ve değerleri beraber listeler
kelime.items()

# get(), kelime yoksa hata mesajı döndürür
kelime.get("bilgisayar", "Kelime yok!")

# clear(), temizleme
kelime.clear()

# copy(), kopyalar
word = kelime # Bu durum sadece etiket olduğundan herhang birinde yapılan işlem diğerini de etkiler.
# copy() komutu burda devreye girer
word = kelime.copy()

# fromkeys()
anahtarlar = "Deger1","Deger2","Deger3"
sozluk = dict.fromkeys(anahtarlar, "Varsayilan")

# pop(), kullanımı listelerden farklı
kelime.pop("bilgisayar")
# hata mesajıyla beraber
kelime.pop("kitap","Anahtar yok!")

# popitem(), rastgele bir anahtar siler
kelime.popitem()

# setdefault()
kelime.setdefault("ornek", "example")

# update(), sözlük değerlerini güncelleme
kelime = {"kitap" : "book",
          "defter": "notebook",
          "dil"   : "language"}

yKelime = {"kitap" : 1,
          "defter": 2,
          "dil"   : 3}