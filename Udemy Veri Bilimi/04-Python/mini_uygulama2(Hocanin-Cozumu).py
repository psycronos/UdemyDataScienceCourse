# =============================================================================
# #Dongu ve Fonksiyonlarin birlikte kullanimi
# =============================================================================

def kare_al(x):
    print(x**2)

kare_al(2)

maaslar= [1000,2000,3000,4000,5000]        

for maas in maaslar:
    print(maas)

print("\n")
                                     
#maaslara yuzde 20 zam yapilacak gerekli kodlari yaziniz  

                             #COZUM
#hocanin cozumu daha basit benimkinden ben herseyi tek fonskiyonda hallettim hem 
#fonksiyon tanimi hem dongu hoca ise icine gonderilen degerin %20 zamli halini alan
#bir fonksiyon yazdi oncelikle sonra ise bir dongu yazip o dongude bu fonksiyonu cagirdi
#ve dongu icinde fonksiyona maaslar listesini atti
                             


#dongu yazilacak
#fonksiyon yazilacak

def yeni_maas(x):
    print(x*20/100+x)

#yeni_maas(1000)
#yeni_maas(2000)
#yeni_maas(3000)

for i in maaslar:
    yeni_maas(i)
    
#tabi hocaninki kalici cozum degil maaslari aslinda arttirmadi sadece zamli halini printle
#yazdirmis oldu maaslari tekrar yazdirmak istersen zamsiz olarak gozukur

#print(maaslar) 
    

    