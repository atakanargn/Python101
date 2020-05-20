import math as mt

def yuvarla(x):
    deger=x-int(x)
    if(deger>=0.5):
        return mt.ceil(x)
    else:
        return mt.floor(x)

yuvarlanacak = float( input("Yuvarlanacak sayıyı gir >> ") )
deger=yuvarla( yuvarlanacak )

print(deger)