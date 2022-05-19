#mini uygulama 
#if, for ve fonksiyonlari birlikte kullanmak

maaslar= [1000,2000,3000,4000,5000]  

#maasi 3000 tl den yuksek olanlara %10 zam 
#maasi 3000 tl den az olanlara %20 zam


def maas_ust(x):
    print(x*10/100+x)
    
    
def maas_alt(x):
    print(x*20/100+x)
    
    
for i in maaslar:      # normal maaslar
    print(i)
    
for i in maaslar:     #zamli maaslar
    
    if(i>3000):
        maas_ust(i)
    
    elif(i<=3000):
        maas_alt(i)