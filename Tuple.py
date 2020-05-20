# Tuple türü diziler, Türkçesiyle Demetler
# Iki şekilde tanımlanabilir

demet = ("~/Python Dersleri", "127.0.0.1", "8080")
demet = "~/Python Dersleri", "127.0.0.1", "8080"

# tuple() fonksiyonu
harfler=tuple("abcdefghijklmnoprstuvyzqw")

# Liste türünde diziler tuple() fonksiyonu ile demetlere dönüşebilir
demet = tuple(["Python","Java","C"])

# demet dizisinin türüne bakalım
type(demet)

# Tek öğeli demet oluşturmak
demet = ("Tek")
# Bu bir karakter dizisidir

# Tek öğeli demet şu şekilde oluşturulur
demet = ("Tek",)
# veya
demet = "Tek",

# Demet ve Listelerin farkı
# birbirlerine benzerler ancak
# Listeler 'mutable' yani değiştirilebilir veri tipidir
# Demetler 'immutable' yani değiştirilemez veri tipidir
# Değiştirmeyi deneyelim
demet = ("~/Python Dersleri", "127.0.0.1", "8080")
demet[0] = "~/Python Dersleri/4.hafta"

# Değiştirmek mümkün değil ancak Demetler üzerinde
# işlem yapmak Listelere göre daha hızlıdır
# Performans avantajı nedeniyle kullanmak isteyebilirsiniz

# Ancak Demetleri sıfırdan tanımlamak mümkün olduğundan
# eklemeler yapabiliriz
demet = demet + ("~/Indirilenler") # Bu tanımlama hata verecektir
demet = demet + ("~Indirilenler",) # Sondaki virgülü unutmayalım

# KULLANIM ALANI
# Örneğin; Python için yazılmış Django : web framework
# ile çalışacak olursanız, projelerin ayar dosyalarında
# Listeler yerine Demetler kullanıldığını görebilirsiniz