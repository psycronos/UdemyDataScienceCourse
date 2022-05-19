#STRING METODLARI - LEN

"""

mvk="gelecegi_yazanlar"

a=9
b=10

a*b

print(len(mvk))  #17 doner cunku uzunlugunu yazdirdim ustteki cumlenin

"""

#STRING METODLARI - upper() & lower()

"""

gel_yaz= "Gelecegi_yazanlar"

print(gel_yaz)

gel_yaz=gel_yaz.upper()

print(gel_yaz)

gel_yaz=gel_yaz.lower()

print(gel_yaz)

print(gel_yaz.islower())  #mesela bu true döner çünkü islower mı diye kontrol ediyorum ona göre true yada false döndürüyor
                          #isupper() da kullanabilirsin buda büyükmü tüm karakterler diye kontrol eder
                          
 """                         
 
#STRING METODLARI - replace()
""" 
gel_yaz="gelecegi_yazanlar"
 
gel_yaz=gel_yaz.replace("e", "a")
 
print(gel_yaz)
"""

#STRING METODLARI - strip()  #strip() istenmeyen kısımları kırpmaya,silmeye yarar
"""
gel_yaz = "gelecegi_yazanlar"
gel_yaz=gel_yaz.strip()

gel_yaz= "*gelecegi_yazanlar*"
gel_yaz=gel_yaz.strip("*") #burda yıldız işaretini direkt default olarak boşluk atadı

print(gel_yaz)

gel_yaz= "lgelecegi_yazanlarl"
gel_yaz=gel_yaz.strip("l") #burda yıldız işaretini direkt default olarak boşluk atadı

print(gel_yaz)

"""


#METODLARA GENEL BAKIS
"""
gel_yaz= "gelecegi_yazanlar"

print(dir(gel_yaz))  #stringin metodlarına dir() ile printte yazdırdığımızda ulaşabiliriz o değişken türüne ait metodlara

print("\n")

print(gel_yaz.capitalize())
print(gel_yaz.title())

"""

#SUBSTRINGLER   #stringlerin alt kümelerini alır, alt kümelere erişir
"""
gel_yaz= "gelecegi_yazanlar"

print(gel_yaz[0]) #0 baslangic noktasidir her zaman
print(gel_yaz[1])

print(gel_yaz[0:3]) #0 dan 3 e kadar 0 dahil 3. index(4. degisken) dahil degil

print(gel_yaz[3:7])

a=gel_yaz[0:3]+gel_yaz[3:7]
print(a)
"""

#DEGISKENLER
"""
a=99999
b="ali_uzaya_git"
c=a*6

print(type(100))

print(type(100.2))

print(type(1+2j))      #j nin anlamı başka burada complex sayılardan

a=100.2
print(type(a))

"""

#TYPE_DONUSUMLERI
"""
birinci_sayi=input("Bir sayi giriniz: ")         #string olarak alınır bu değişkenler
 
ikinci_sayi=input("Ikinci sayiyi giriniz: ")

print(birinci_sayi+ikinci_sayi)   #burda string olduğu için birleştirme işlemi yapar

print(int(birinci_sayi)+int(ikinci_sayi)) #burda ise int koydugum icin 2 side int toplama islemi yapar donusum yaptım


print(int(11.3)) #float degeri int e cevirdik

print(float(10)) #int degeri floata cevirdik 10.0 oldu

print(str(12)+"a") #stringe cevirir buda

"""

#Print
"""
print("gelecegi","yazanlar")

print("gelecegi","yazanlar", sep = "_" ) #sep sayesiinde _ veya ne istersek onla birleştiriyor print içindekileri
"""



#VERI YAPILARI

#Listeler #Listeler #Listeler #Listeler #Listeler #Listeler


#[]
#list()

"""
notlar=[90,80,70,50]

print(type(notlar)) #list turundedir

liste=["a",19.3,90]


liste_genis=["a",19.3,90, notlar]

print(len(liste_genis)) # 4 eleman vardır "a" 19.3 90 ve içinde ayrı bir liste olan notlar vardır toplam 4 olur 
                        #yani notlar icindekiler ayrı elemanlar degilde liste icinde bir butun liste olarak tanimlanir


print(type(liste_genis[0])) #liste icindeki elemanlarin tipinede boyle bakabiliriz 


tum_liste=[liste,liste_genis]  #************listeleri birlestirme islemi 2 listeyi boyle birlestirebiliriz


print(tum_liste)

del tum_liste # kod icerisinde bu listeyle ilgili herseyi siler yer kaplamasini engeller isimiz bittiginde bir nevi
              #ornegin bundan sonra tekrar listeyi yazdirmaya calisirsan hata verecektir

#print(tum_liste) #bu cikti hata verir cunku ustte deleteledim
"""


#Listeler - Eleman Islemleri
"""

liste = [10,20,30,40,50]

liste[0] #10
liste[1] #20

liste[0:2] #10,20

liste[2:] #30 40 50

yeni_liste= ["a",10,[20,30,40]]

print(yeni_liste[2])  #[20,30,40]

print(yeni_liste[0:2]) # ["a",10] 

        

    #****alt elemana erişmek****
print(yeni_liste[2][1])    #liste icindeki listeye erismek istiyoruz ornegin 30 degerine 

"""

#Listeler - Eleman Degistirme
"""

liste= ["ali","veli","berkcan","ayse"]

liste[1]="velinin babasi" #"veli" yi "velinin babasiyla" degistirmek istedim

print(liste)

liste[1]="veli"

#bu sekilde ilk 3 elemani direkt tek satirda degistirebildik
liste[0:3] = "alinin_babasi","velinin_babasi","berkcanin_babasi"  #3 elemanın babalarınıda buraya koymak

print(liste) 


liste= liste + ["kemal"] #ekleme icin istersek liste.append("adasd") #yapabiliriz
print(liste)


del liste[2] #3. eleman olan berkcanin babasini siler
print(liste)

"""

#Listeler - Liste Metodlari
"""
liste=["ali","veli","isik"]

#ekleme(append)
liste.append("kemal")
print(liste)

#silme(remove)
liste.remove("veli")  #icine silmek istedigimiz degiskenin adini yaziyoruz
print(liste)

"""

#insert

"""
liste=["ali","veli","isik"]

                         
liste.insert(0,"ayse")   #hangi indexe hangi elemani eklemek istedigimizi yaziyoruz
                         #bu 0. ya ekleyip digerlerini saga iteler direkt liste[0]="ayse" yapsak ustune yaziyor
print(liste)

liste.insert(2,"mehmet") #3. elemanin yerine mehmeti ekle 3 eleman dahil digerlerini saga kaydir
print(liste)            #yani liste[2]= gibi elemani degistirmiyor oraya ekliyor diger eleman hala duruyor


liste.insert(len(liste),"berk") #sona eleman ekleme 5 eleman varsa son index 4 dur ama insert ile 5 e eklememiz lazim sona eklemek icin
print(liste)                    #boyle bir kucuk trick tarzi birsey 

liste.insert(len(liste),"beren") #bu sayede eleman sayilarini saymadan sona ekleyebiliriz
print(liste)            


#pop

liste.pop(0)  #indexini girdigimiz elemani siler
print(liste)    

liste.pop(4)  #4. indekste yani 5. elemanda berk var suanda listede
print(liste)    

"""

#count

"""
liste=["ali","veli","isik","ali","veli"]

print(liste.count("ali")) #bu objeden kactane oldugunu yaziyor

print(liste.count("isik"))

#copy

liste_yedek=liste.copy()# boyle yapmak atamaktan farklı bunda birinde yaptigin
                        #degisiklik digerini etkilemez adres atamasi yok bunda ama
                        # liste_yedek=liste yaparsan birindeki degisiklik digerindede olur


#extend

liste.extend(["a","b",10]) #listeye bu girilen elemanlari tek tek ekler listeyi genisletir
print(liste) 

#index

print(liste.index("ali")) #girilen elemanin ilk bulundugu indexi dondurur
  
#reverse 

liste.reverse() #listenin elemanlarini ters cevirir
print(liste)

#sort

#liste.sort() #listeyi siralamaya yarar ama listede hem int hem string degerler oldugundan yapmadi siralamayi


#clear

liste.clear() #listeyi tamamen temizler hic eleman birakmaz
print(liste)


"""
  

#Veri Yapilari - Tuple

"""

t= ("ali","veli",1,2,3.2,[1,2,3,4]) #tuple olusturmanin 3 yolu vardir bu 1. alttada diger 2 yol var


t="ali","veli",1,2,3.2,[1,2,3,4]

#tuple()

t=("eleman",)  #sonuna virgul koymaz isek string olarak algiliyor bunu ondan tek elemanda , koymamiz sart tuple oldugunu belirtmek icin
print(type(t))


#Tuple Eleman Islemleri

t= ("ali","veli",1,2,3,[1,2,3,4])
print(t)


print(t[1])
print(t[0:3])

#t[2]=99  #burda hata cikar cunku tuple degisiklige izin vermez listeler gibi atama islemi yapamayiz
          #kisaca tuple amaci veri yapisi sabit dursun degisiklik olmasin olustugu haliyle kalsin istiyoruz sabit sekilde


"""



#Veri Yapilari - Dictionary (Sozluk)


#listelerde olduğu gibi index işlemi yapılamaz

"""
sozluk={"REG": "Regresyon Modeli",         #key degerlere karsilik onlarin tuttugu degerler kisaca
        "LOJ": "Lojistik Regresyon",
        "CART": "Classification and Reg"
        }

print(sozluk)

print(len(sozluk))



sozluk={"REG": ["RMSE",10],         
        "LOJ": ["MSE",20],
        "CART": ["SSE",30],          #sözlük içinde istersek keylere karşılık listelerde getirebiliriz
        "Yas": 21
        }

print(sozluk)

print(len(sozluk))

print(sozluk["REG"]) #sozlukten eleman secme boyle yapilir 0 1 2 3 gibi indexler yoktur 



sozluk={"REG": {"RMSE": 10,
                "MSE":20,
                "SSE":30 },  
        
        "LOJ": {"RMSE": 10,
                "MSE":20,
                "SSE":30 },
        
        "CART": {"RMSE": 10,
                "MSE":20,
                "SSE":30}          
        }

#sozluk icinde sozluk olusturduk ilki icin 

print(sozluk["REG"]["RMSE"])  # bu sekilde sozluk icinde baska sozlugu tutan ilk degiskenin keyini kullanarak 10 degerine ulasmis oldum

"""


#SOZLUK - Eleman Ekleme & Degistirmek
"""
sozluk={"REG": "Regresyon Modeli",         
        "LOJ": "Lojistik Regresyon",
        "CART": "Classification and Reg"
        }

sozluk["GBM"] = "Gradient Boosting Mac" #Boyle eleman eklemis oldum istedigim keye sahip

print(sozluk)


print("\n")

sozluk["REG"] = "Coklu Dogrusal Regresyon" #eleman degistirme

print(sozluk)

#DİKKAT
sozluk[1] = "Yapay sinir Aglari" #bu 1 indeks olarak dusunulmemeli sozlukde 1 keyine sahip bir deger

print("\n")

print(sozluk)


t= ("tuple",) #string olmadigini tuple oldugunu anlamasi icin tuplelara  ,  koyuyorduk unutma

sozluk[t]="yeni bir sey"

print("\n")

print(sozluk)
"""

#Veri Yapilari - Setler

#Set olusturmak
"""
s= set()

l=[1,"a","ali",123]

s=set(l)


t=("a","ali")

s=set(t)
print(s)

ali="lutfen_ata_bakma_uzaya_git"
print(type(ali))

s=set(ali) #birden fazla tekrar eden degiskenleri set tekillestirir ozellestirir her degisken 1 kere yazilir yani
print(s)

print("\n \n")
l=["ali","lutfen","ata","bakma","uzaya","git","git","ali","git"]
s=set(l)

print(l,"\n") #l yi yazdirdim
print(s)  #l yi set edip tekrar yazdirdim olan fark apacik ortada 

print("\n")
print(l[0])
#print(s[0]) #burda hata aliriz cunku setler indeks desteklemez ve rastgele siralar degerleri o yuzden indeks islemi yapilmaz

"""

#Eleman ekleme & cikarma
"""
l=["gelecegi","yazanlar"]

s=set(l)



s.add("gelecege_git") #rastgele oldugu icin setler rastgele biryere eklenir sirasiz olarak
print(s)

s.add("ile")
print(s)

s.add("ile") #var olan elemani bir daha eklemez mesela yukarda ile ekledim birdaha yazdirdim ama eklenmez zaten var
print(s)

s.remove("ile") #buda en basitinden eleman cikarma
print(s)

s.discard("ile") #buda eleman cikarma yapar ama bu hata vermez remove o eleman yoksa hata verir kod akisini keser

"""

#Setler - Klasik Kume Islemleri

# =============================================================================
# #--------------------------------
# #difference() ile iki kumenin farkini yada "-" ifadesi
# #intersection() iki kume kesisimi ya da "&" ifadesi
# #union() iki kumenin birlesimi
# #symetric_difference() ikisinde de olmayanlari

# =============================================================================


#difference
"""
set1=set([1,3,5])
set2=set([1,2,3])

print(set1.difference(set2)) #set1 de olup set 2 de olmayanlari getirir bu set1-set2 farki yani kume islemi gibi CIKARMA DEGIL

print(set2.difference(set1)) #burdada 2 de olup 1 de olmayan eleman 2 dir 


print(set1.symmetric_difference(set2)) #burdada set1 ve set 2 de birbirinde bulunmayan elemanlar gelir 2 ve 5 ortak degil mesela


# print(set1-set2) # fark alma islemlerini istersek böylede yapabiliriz bize kalmis 
# print(set2-set1)

"""

#intersection & union (kesisim ve birlesim)
"""
set1=set([1,3,5])
set2=set([1,2,3])

print(set1.intersection(set2))  #kesisim olan elemanlari aliyor yani 2 settede bulunan
print(set2.intersection(set1))
print(set1 & set2)  #boylede kesisim alabiliriz
 

print(set1.union(set2)) #kumelerin birlesimi buda 2 kumenin tum elemanlarini birlestiriyor ayni kumeler mantigi her elemandan 1 tane

"""

#Set Sorgu Islemleri
"""
set1=set([7,8,9])
set2=set([5,6,7,8,9,10])


#iki kumenin kesisiminin bos olup
#olmadiginin sorgulanmasi

print(set1.isdisjoint(set2)) #kumenin kesisimi varsa false doner kesisim yoksa true doner


#bir kumenin elemanlarinin diger kume icinde yer alip almadigi
#kisaca alt kume olup olmadigi

print(set1.issubset(set2)) #burda true doner cunku set1 de ki tum elemanlar set2 de var
print(set2.issubset(set1)) #false doner cunku set2 de set1 de olmayan elemanlar var


#bir kumenin diger bir kumeyi kapsayip kapsamadigi
print(set2.issuperset(set1)) #true doner set2 set1 i kapsar set1 deki her eleman set2 dede var cunku
"""


#FONKSIYONLARA GIRIS VE FONKSIYON OKURYAZARLIGI
    
#Fonksiyon Nasil Yazilir
"""
def kare_al(x):
    print(x**2)


kare_al(5)
"""

#Bilgi Notuyla cikti uretmek
"""

def kare_al(x):
    print("Girilen sayi:",x,"'un karesi: ",x**2)


kare_al(10)


def kare_al(x):
    return x**2

print("8 in karesi: ",kare_al(8))

"""

#Iki Argumanli Fonksiyon Tanimlamak
"""    
def carpma_yap(x,y):
    print(x*y)
    

carpma_yap(6,8)

"""

#On tanimli Argumanlar
"""
def carpma_yap(x,y=1):
    print(x*y)

carpma_yap(3,4)
carpma_yap(3) #normalde tek arguman hata verir ama on tanimli yaptigim icin y yi hata vermedi y yi direkt deger atanmazsa 1 e
              #esitledim deger yollarsak gene ayni islemi gorur

#Argumanlarin Siralanmasi

def carpma_yap(x,y=1):
    print(x*y)

carpma_yap(y=2,x=3) #argumanlarin siralamasini bilmiyorsak boylede tanimlayaabiliriz istersek

"""

#Ne Zaman Fonksiyon Yazilir ?
"""
#isi, nem, sarj

print((40+25)/90)

def direk_hesap(isi,nem,sarj):
    print((isi+nem)/sarj) 

direk_hesap(25,40,70)
"""



#Local ve Global Degiskenler

"""
x = 10
y = 20


def carpma_yap(x,y):
    return x*y

print(carpma_yap(2, 3))
"""

#Local Etki Alanlarindan Global Etki Alanini Degistirmek
"""
x= []

def eleman_ekle(y):
    x.append(y)                 #globaldeki x e etki etti local fonksiyonda oncelikle fonksiyona bakar locale bulamazsa globale bakar ordada bulamazsa hata verir
    print(y,"ifadesi eklendi")


eleman_ekle("ali")

eleman_ekle("veli")

print(x)

"""


#KARAR VE KONTROL YAPILARI

#True-False Sorgulamaları
"""
sinir=5000

print(sinir==4000) #false doner sinir 4000 e esitmi sorusudur == soru sorar yani
"""

#if - else 
"""
sinir=50000
gelir=40000

if(gelir<sinir):
    print("geliriniz sinir degerden daha kucuktur")
else:
    print("gelir sinirdan buyuktur")
"""


#elif
"""
#ornek 1
sinir=50000
gelir=50000

if (gelir==sinir):
    print("gelir sinira esittir")
    
elif(gelir>sinir):
    print("gelir sinirdan buyuktur")
    
else:
    print("gelir sinirdan kucuktur ")

#ornek 2
sinir=50000
gelir=60000

if (gelir==sinir):
    print("gelir sinira esittir")
    
elif(gelir>sinir):
    print("gelir sinirdan buyuktur")
    
else:
    print("gelir sinirdan kucuktur ")

#ornek 3
sinir=50000
gelir=40000

if (gelir==sinir):
    print("gelir sinira esittir")
    
elif(gelir>sinir):
    print("gelir sinirdan buyuktur")
    
else:
    print("gelir sinirdan kucuktur ")

"""

# =============================================================================
# #DONGULER - For
# =============================================================================

"""
ogrenci=["ali","veli","isik","berk"]

for i in ogrenci:
    print(i)       #print(ogrenci[0]) print(ogrenci[1]) print(ogrenci[2])
"""         

#for - devam
"""
maaslar= [1000,2000,3000,4000,5000]        

for maas in maaslar:     #burda maas yazmam onemli degil istersem "i in maaslar" da yazabilirim o degisken farketmez
    print(maas)
"""


#break & continue
"""
maaslar= [8000,5000,2000,1000,3000,7000,1000]

#maasi 3000 tl ye kadar olanlarla ilgilenicez diyelim 3000 de durmak istiyoruz

maaslar.sort() #listeyi siraladik once
print(maaslar)

for i in maaslar:
    if i==3000:
        print("kesildi")
        break
    print(i)

print("\n")

for i in maaslar:
    
    if i==3000:          #continue da direkt o adimi atla demek eger kosul saglanirsa adimlari atlayip basa doner
        print("atlandi")
        continue
    print(i)
"""

#while
"""
sayi = 0

while sayi < 10:
    sayi += 1 
    print(sayi)     #sayi 10 oldugunda direkt donguden atar alttaki islem bittiginde tekrar basa dondugunde atar donguden
"""

