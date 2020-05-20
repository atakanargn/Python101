ogrenciNo = {"1712709013"  : "Atakan Argın",
             "1214594923"  : "Ibrahim Leylek",
             "1245356569"  : "Uygar Usta",
             "1656769542"  : "Furkan Öncü"}

kisi = input("Okul numarasi girin : ")

cevap = "{} numarasi, \"{}\" isimli ogrenciye ait."

print(cevap.format(kisi, ogrenciNo[kisi]))
