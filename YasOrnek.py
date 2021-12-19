yas = int( input("Yaşınız : ") )

if (yas < 0):
    print("Geçersiz bir yaş girdiniz.")
elif yas < 7:
    print("Okula başlayamaz.")
elif yas >= 7 and yas <= 14:
    print("Ilkokula gidebilir.")
elif yas >= 15 and yas <= 18:
    print("Liseye gidebilir")
elif yas > 18 and yas < 26:
    print("Üniversite")
else:
    print("Sen yaşlanmışsın kardeşim.")