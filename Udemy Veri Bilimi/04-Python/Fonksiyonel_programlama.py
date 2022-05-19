#Python'da Fonksiyonel Programlama

#Fonksiyonlar dilin bastacidir
#(Birinci sinif nesnelerdir)
#Yan etkisiz fonksiyonlar. (stateless, girdi-cikti)
#Yuksek seviye fonksiyonlar.
#Vektorel operasyonlar.


#Yan etkisiz Fonksiyonlar (Pure Functions) #disaridan herhangi birseyden etkilenmeyen fonksiyonlar
"""
#Ornek1: Yan Etki     #hoca acikliyor pure ne impure ne ders videolarindan izle tanimlari anlamak icin
                      #104 105 ... dersler
A=9

def impure_sum(b):
    return b+A

def pure(a,b):
    return a+b

print(impure_sum(6))    #burdaki cikti disaridaki A degiskeninden etkileniyor A degisirse buda degisir

print(pure(3, 4))
"""

#Ornek2: Olumcum yan etkiler

#ders 105 de hoca yazdi ben bu kodu yazmadim dosya islemleride oldugu icin burayi tekrar izle



#Isimsiz Fonksiyonlar (Anonymous Functions) Ders 106
"""
def old_sum(a,b):
    return a+b

print(old_sum(4,5))


new_sum=lambda a,b : a+b   #lambda fonksiyon boyle daha basit tanimlanmasi esnek

print(new_sum(4,5))


sirasiz_liste=[("b",3),("a",8),("d",12),("c",1)]
print(sirasiz_liste)


print(sorted(sirasiz_liste,key=lambda x: x[1])) #2. deger [1]. indexe göre siraladi lambda fonks ile sorted() fonk ile
                                                #burasi biraz karisik ders 106 yi izle unutursan
"""


#Vektorel Operasyonlar (Vectorel Operations)
"""
a=[1,2,3,4]
b=[2,3,4,5]

ab=[]

range(0,len(a))

for i in range(0,len(a)):   #range(0,4) son deger dahil degil 0 dan 3 e kadar 3 dahil i olarak gezinecek i =0 1 2 3 olacak yani ve normal carpma yaptik
    ab.append(a[i]*b[i])

print(ab)

#FP (functional Programming yolu usttekinin daha basit yontemi fonksiyonlar ile yaptik carpmayi sadece numpy list olarak tanimladik daha basit)

import numpy as np

a=np.array([1,2,3,4])
b=np.array([2,3,4,5])

print(a*b)

"""

#map & filter & reduce
"""
# =============================================================================
# #map        ders 108 bu kisim onemli anladim ama unutursan tekrar izle mantigini
# =============================================================================
liste= [1,2,3,4,5]

for i in liste:
    print(i+10)


print(list(map(lambda x: x+10,liste  ))) #MAP fonksiyonu verilen bir nesnenin uzerinden tanimlanacak olan bir fonksiyonu calistirma imkani verir


# =============================================================================
# #filter (iteratif bir nesne alarak calisir)
# =============================================================================

liste = [1,2,3,4,5,6,7,8,9,10]

print(list(filter(lambda x: x%2 == 0 ,liste)))  #2 ye bolumunden kalanlari 0 olanlari yani sadece 2 ye tam bolunenleri aldi  filtreledi filterin gorevide bu



# =============================================================================
# #reduce (indirgeme islemi yapar)
# =============================================================================

from functools import reduce

liste=[1,2,3,4]
print(reduce(lambda a,b: a+b,liste)) #reduce ifadesi once geldi 1 le 2 yi ondan sonra diger ifadeyi ondan sonra diger ifadeyi toplayip 10 degerini dondu

"""


#Modul Olusturmak

#DERS 109 ben bu derste sadece izledim ekstra bir sayfa acmadim bu kismi biliyorum ama genede ilerde izle hatirlamak amaciyla.



#Hatalar /  Istisnalar (exceptions)

"""
#ZeroDivisionError hatasi
a=10
b=0

#print(a/b)


try:
    print(a/b)
    
except ZeroDivisionError:
    
    print("paydada 0 olmaz")




#tip hatasi


a=10
b="2"

#print(a/b)
    
try:
    print(a/b)
    
except TypeError:
    
    print("Sayi ve String problemi")

"""





