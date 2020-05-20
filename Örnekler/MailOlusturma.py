ad = str(input("Ad : "))
soyad = str(input("Soyad : "))
dogumYili = int(input("Doğum yılı : "))
alanAdi = str(input("Alan adı : "))

dogumYili = str(dogumYili)
ilkKisim='.'.join([ ad,soyad, dogumYili ])
mail='@'.join([ilkKisim, alanAdi])

mail = mail.lower()

mail = mail.replace("ı", "i")

print("Mail oluşturuldu : %s" % mail)

