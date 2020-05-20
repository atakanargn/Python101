# Modüller
### 1) Kendi tanımladığımız modüller
### 2) Hazır modüller

# Hazır modüller de ikiye ayrılır.
### 1) Standart kütüphane modülleri
###### Doğrudan Python geliştiricileri tarafından yazılmış kütüphanelerdir.
###### Bu kütüphaneleri istediğimiz an, ek bir kurulum gerekmeden kullanabiliriz.
###### Standart kütüphanelere şu adresten ulaşabilirsiniz : https://docs.python.org/3/library/
### 2) Üçüncü şahıs modüller
###### Python geliştiricileri dışındaki geliştiriciler tarafından geliştirilen kütüphanelerdir.
###### Işimizi yapacak kütüphane bulamazsak bizde kendi kütüphanemizi yazabiliriz.
###### 'pip' aracının deposu, PyPi : https://pypi.org/

# Kütüphanenin içe aktarılması
import os

# Kütüphanenin barındırdığı fonksiyonları şu şekilde görebiliriz
dir(os)

# os kütüphanesi içinden bir kaç fonksiyon
os.name # işletim sistemini öğrenmek için kullanabiliriz
        # posix çıktısını verirse : Linux tabanlıdır
        # nt çıktısını verirse    : Windows tabanlıdır
        # gibi...

# Yazılımımızın sadece Linux tabanlı işletim sistemlerinde kullanılmasını istersek
# --> isletimSistemi_kontrol.py

# Bir kaç os fonksiyonu
os.makedirs("KlasörAdı") # Yeni klasör oluşturma   : mkdir KlasörAdı
os.chdir("..")          # Klasörler arası gezinme : cd ..
os.listdir()             # Dizin listeleme 
os.getcwd()              # Python dosyasının bulunduğu dizin

# Kütüphane isimlerini kısaltma
import pyautogui as pag 
# PyAutoGui kütüphanesi ile mouse hareket ettirme
pag.moveTo(500,500,1)
# Aynı kütüphane ile ekran görüntüsü alıp, kaydetme
ekranGoruntusu = pag.screenshot()
ekranGoruntusu.save("ss.png")

# Kütüphane içinden istediğimiz fonksiyonları çekme
from os import system, getcwd, listdir
# Kütüphane içindeki fonksiyonları bu şekilde çağırıyorsak
# Örnek olarak; os.system() değilde direk system() şeklinde kullanmalıyız.
os.system("ls -al") # ÇALIŞMAZ
system("ls -al")    # ÇALIŞIR

# Bu şekilde tüm fonksiyonları aktarma
from os import *

#### Kendimiz modül tanımlayalım
import os
os.__file__
# os kütüphanesi içindeki '__file__' değişkeni
# bize kütüphanelerin kurulu olduğu konumu verecektir
# Kütüphaneler genelde bu konuma kurulur
# Ancak kütüphane bizim Python dosyamızla aynı dizindeyse
# bu kütüphaneyi de çağırabiliriz.

# 'HesapMakinesi' isimli
# 4 işlem için ayrı fonksiyonlara sahip bir modül yazalım

#### Işlem sırası
# Öncelikle bulunduğumuz dizine;
# HesapMakinesi.py adında bir dosya açalım
# Dosya içinde topla,fark,carp,bol isimli fonksiyonlar tanımlayalım
# Bu fonksiyonları tanımlayıp, yazdıktan sonra
# Bulunduğunuz dizinde 'python' komutuyla 'Python Interactive Shell' açın
import HesapMakinesi # Modülü/Kütüphaneyi çağırma
dir(HesapMakinesi)   # Modül içindeki fonksiyonlar ve değişkenler vs..
HesapMakinesi.topla(1,2,3,4,5) # toplama fonksiyonu
HesapMakinesi.yazar # yazar değişkeni

#### Üçüncü şahıs kütüphaneler
# Bu tarz kütüphaneler için en geniş kaynak; 
# https://pypi.python.rg/pypi oadresidir.
# Zaten 'pip' aracı ile;
pip install numpy
# Python3 için;
pip3 install numpy
# şeklinde kullanarak bu adresteki kütüphanelere daha öncede ulaşmıştık

#### Pythonda öğrenilmesi gereken kütüphaneler
## Standart kütüphaneler
# os       : Operation System
# sys      : System 
# random   : Rastgele yapılabilecek sayı işlemleri, seçme işlemleri vs
# datetime : Tarih (gün,ay,yıl,saat,vs..) kütüphanesi
# time     : Zaman kütüphanesi, çok sık kullandığımız sleep() fonksiyonu buradan geliyor.

## Üçüncü şahıs kütüphaneler
# numpy      : Veri merkezli uygulamalarda sık kullanılır.
# pandas     : Veri yapıları için çok uygundur,
#              Numpydaki veri yapısı, Excel ve SQL gibi ilişkisel veri yapılarını işleyebilir.
# matplotlib : Grafik işlemleri ve iki boyutlu görselleştirme işlemleri
#              için en çok kullanılan Python kütüphanesidir. 
# Ipython    : python interaktif kabuğunu daha görsel ve işlevsel hale getiren kütüphane.
# SciPy      : integral ve diferansiyel denklem çözümleri, 
#              lineer cebir, optimizasyon problemleri, sinyal işleme, istatistik fonksiyonları
#              ve testleri için için kullanılır.
# Numpy ve SciPy kütüphaneleri birlikte kullanıldığında MatLAB programına benzer işlevler görür.

#### Bunlar dışında;
## Farklı dil ve mimariler ile kodlama
# Jython
# IronPython

## Oyun geliştirme
# Pygame

## GUI (Arayüz) Tasarlama
# PyGTK
# PyQT
# Tkinter

## Web programlama
# Django
# Flask

