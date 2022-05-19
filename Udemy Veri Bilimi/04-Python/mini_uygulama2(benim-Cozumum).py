# =============================================================================
# #Dongu ve Fonksiyonlarin birlikte kullanimi
# =============================================================================

def kare_al(x):
    print(x**2)

kare_al(2)

maaslar= [1000,2000,3000,4000,5000]        

for maas in maaslar:
    print(maas)


                                     
#maaslara yuzde 20 zam yapilacak gerekli kodlari yaziniz  


                    #COZUM
#benim burda yaptigim cozum yontemi fonksiyon tanimlayip icine maaslar listesini gondermek oldu ve x turunde aldim bu listeyi
#sonra o listenin dongu ile her elemanina %20 zam yaptim i= i+i*(20/100) isleminden
#sonra ben her degiskeni yeni bir listeye atadim dongu icinde zamli hallerini ve zamli bir liste olusturdum
#o listeyi en son fonksiyonda return ettim bu sayede fonksiyonu cagirdigim zaman maaslari bu fonksiyona atayabildim
#ve yeni maaslar listesini olusturmus oldum

def zam_yap(x):
    yeni_liste=[]
    
    for i in x:
         i=i+i*(20/100)
         yeni_liste.append(i)
         
    return yeni_liste
         

print(maaslar)

maaslar=zam_yap(maaslar)

print(maaslar)