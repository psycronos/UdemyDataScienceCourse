#Mini Uygulama

sinir=50000

magaza_adi=input("Magaza adi Giriniz: ")
gelir=int(input("Gelirinizi Giriniz: ")) #gelirde assagida kiyaslama yapacagimiz icin inte cevirmek lazim string olarka gelir inputta
                                         #unutma bunu sakin bu onemli


if(gelir>sinir):
    print("Tebrikler",magaza_adi,"adli magazanizin  geliri sinirdan daha buyuk")
elif(gelir==sinir):
    print(magaza_adi,"adli magazanizin  geliri sinira esit")
else:
    print("Uzgunuz",magaza_adi,"adli magazanizin  geliri sinir degerden daha kucuk")