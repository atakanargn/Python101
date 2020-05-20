# Düz yıldız
adim = int(input("ADIM SAYISI : "))
for i in range(1,adim+1,1):
    print("*"*i)

# E HARFİ
for i in range(1,5+1,1):
    if(i==1 or i==5):
        print("#"*6)
    elif(i==2 or i==4):
        print("#")
    else:
        print("#"*4)

# Z HARFİ

for i in range(1,4+1,1):
    if(i==1 or i==4):
        print("#"*4)
    elif(i==2):
        print("  #")
    elif(i==3):
        print(" #")