
# =============================================================================
# NESNE YONELIMLI PROGRAMLAMA
# =============================================================================

#Sinif nedir ?
"""
class VeriBilimci():
    print("Bu bir siniftir")


VeriBilimci()
"""

#Sinif Ozellikleri (Class attributes)
"""
class Veribilimci():
    bolum=""
    sql="Evet"
    deneyim_yili=0
    bildigi_diller=[]
    

#siniflarin ozelliklerine erismek
Veribilimci.sql
Veribilimci.bolum

#Siniflarin ozelliklerini degistirmek
Veribilimci.sql="Hayir"

print(Veribilimci.sql)
"""
                                      #BU COK ONEMLİ BİR ORNEK
#Sinif Orneklendirmesi (instantiation)
"""
class Veribilimci():
    bolum=""
    sql="Evet"
    deneyim_yili=0
    bildigi_diller=[]
    

ali= Veribilimci()     #ali bu classin ozelliklerini aldi nesne olusturduk classdan yani

print(ali.sql)

ali.bildigi_diller.append("python")

print(ali.bildigi_diller)

Veli= Veribilimci() #Gordugunuz uzere burda hata var Veli normalde python bilmiyor ama ornek uzerinden yaptigimiz islem
print(Veli.sql)     #tum classi etkiledi ve artik veli ornegide ali yuzunden python biliyor gibi gozuktu bu cok buyuk bir yanlistir
print(Veli.bildigi_diller)
"""

#Ornek Ozellikleri         #ustteki sorunun cozumu pythonda self mantigi var classlarda
"""
class Veribilimci():
    bolum=" "
    sql=" "
    deneyim_yili=0
    def __init__(self):
        self.bildigi_diller=["SQL"] #otomatik olarak buna her classda olacak SQL adinda bir degisken ekledim
        self.bolum=" "

ali=Veribilimci()
ali.bildigi_diller.append("python")
print("Alinin bildigi dil",ali.bildigi_diller)         #goruldugu uzere alinin bildigi dillerde python bilgisi geldi ama altta velide yok


veli=Veribilimci()
print(veli.bildigi_diller)

veli.bildigi_diller.append("R")
print("Velinin bildigi dil",veli.bildigi_diller)

print(Veribilimci().bildigi_diller)


print(Veribilimci.bolum)
ali.bolum="istatistik"
print(Veribilimci.bolum)
print(ali.bolum)
print(veli.bolum)
veli.bolum="end muh"
print(veli.bolum)

"""


#Ornek Metodlari
"""
class Veribilimci():
    Calisanlar=[]
    def __init__(self):
        self.bildigi_diller=[] #otomatik olarak buna her classda olacak SQL adinda bir degisken ekledim
        self.bolum=""

    def dil_ekle(self,yeni_dil):                #class icinde fonksiyon tanimlama METOD yani goruldugu uzere selfde ekledim
        self.bildigi_diller.append(yeni_dil) #cunku kisiden kisiye degisecegi ici




ali=Veribilimci()
print(ali.bildigi_diller)
print(ali.bolum)


veli=Veribilimci()
print(veli.bildigi_diller)
print(veli.bolum)


ali.dil_ekle("R")

veli.dil_ekle("Python")

print("Ali dil:",ali.bildigi_diller)
print("Veli dil:",veli.bildigi_diller)

"""
#Miras Yapilari (inheritance)

class Employees():
    def __init__(self):
        self.FirstName = ""
        self.LastName =  ""
        self.Address = ""
        


class DataScience(Employees):     #DataScience classi bu sekilde Employees classini inherit almis oldu mira alıyor yani ust class Employees 
    def __init__(self):
        self.Programming= ""

veribilimci1= DataScience()
#veribilimci1.


class Marketing(Employees):      #burdada marketing gene employee 'i inherit etti yani onun ozelliklerini miras aldi
    def __init__(self):
        self.StoryTelling = ""


mar1=Marketing()
#mar1.


########################## Constructor

class Employees():      #fonksiyonel yapida yapmak istiyorsak bu isi boyle yapabiliriz
    def __init__(self,FirstName,LastName,Address):#bir nevi constructor yani 3 tane degeri tanimlarken vermek zorundayiz
        self.FirstName = FirstName
        self.LastName =  LastName
        self.Address = Address

ali = Employees("ali", "erdogan", "istanbul") #burda tanimlarken constructori bu 3 degeri vermek zorundayiz bos gonderemeyiz yani

print(ali.FirstName,ali.LastName,ali.Address) 
