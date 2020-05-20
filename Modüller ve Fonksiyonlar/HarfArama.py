#String içinde harf arama
# Bu örnek girilen harfin index'ini verir
cumlemiz="Harf arama örneği"
harfimiz=input("Harf : ")

def harfAra(cumle, arananHarf):
    i=0
    for harf in cumle:
        if(harf==arananHarf):
            return i
        i+=1
    return -1

print( harfAra(cumlemiz,harfimiz) )