bolunen=int(input("Sayı1 : "))
bolen=int(input("Sayı2 : "))

bolum=0
kalan=0

while(bolunen>bolen):
    bolunen-=bolen
    bolum+=1

kalan=bolunen
print("Bölüm : "+str(bolum)+"\nKalan : "+str(kalan))

