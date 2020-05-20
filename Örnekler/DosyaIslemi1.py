try:
    islem = int(input(" Yapmak istediginiz islem\n\
\t 1 > Okuma\n\
\t 2 > Yazma\n\
 >> "))
except ValueError:
    print("Gecerli bir islem girmediniz!")

if(islem==1):

    try:
        dosyaIsim = input("Dosya ismi : ")
        dosya = open(dosyaIsim,"r")
        metin = dosya.read()
        print(metin)
    except UnicodeDecodeError:
        print("Karakter hatasi!")
    except FileNotFoundError:
        print("Boyle bir dosya yok!")
    finally:
        dosya.close()

elif(islem==2):
    try:
        dosyaIsim = input("Dosya ismi : ")
        dosya = open(dosyaIsim,"a+")
        metin = dosya.read()
        ekleme = input("Ne eklemek istersiniz : ")
        if(ekleme!=""):
            dosya.write(ekleme)
    except UnicodeDecodeError:
        print("Karakter hatasi!")
    except FileNotFoundError:
        print("Boyle bir dosya yok!")
    finally:
        dosya.close()
        
else:
    print("Gecerli bir islem girmediniz!")