from random import randint

# randint(aralık) // ARALIK (0,5), (100,900) GIBI
rastgeleSayi=randint(0,5)

hak=5
while(hak>0):
    sayi=int(input("Tahminin (0,5) : "))
    if(sayi >= 0 and sayi <= 5):
        if(sayi==rastgeleSayi):
            print("Doğru bildin!")
            break
        elif(sayi < 0 or sayi > 5):
            print("Geçersiz giriş")
        else:
            print("Tahminin yanlış!")
            hak-=1
            print(str(hak)+" hakkın kaldı!")
print("Cevap olacaktı : "+str(rastgeleSayi))
