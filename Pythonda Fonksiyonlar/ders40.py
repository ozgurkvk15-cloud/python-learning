# uygulamlı fonksiyon soruları..

# soru 1 = gönderilen bir kelimeyi belirtilen kez ekranda gösteren fonksiyonu yazınız.

def yazdir (kelime,adet):
    print(kelime * adet)

yazdir('özgür\n',10)   


# soru 2 = kendisine gönderilen sınırsız sayıdaki parametreyi bir liste haline bir listeye ceviren fonksiyonu yazınız.

def listeye_cevir(*params):
    liste=[]

    for param in params:
        liste.append(param)

    return liste

result=listeye_cevir(10,20,30,40,'merhaba')
print(result)


# soru 3 = gönderilen 2 sayı arasındaki tüm asal sayıları bulun

def asal_sayilari_bul (sayi1,sayi2):
    for sayi in range(sayi1,sayi2+1):
        if sayi > 1:
            for i in range (2,sayi):
                if sayi % i == 0 :
                    break
            else:
                print(sayi)    


sayi1=int(input("1. sayı giriniz :"))
sayi2=int(input("2. sayıyı giriniz :"))

asal_sayilari_bul(sayi1,sayi2)



# soru = 4 kendisine gönderilen bir sayının tam bölenlerini bir liste şeklinde gösteriniz

def tam_bölenleri_bul (sayi):
    tam_bölenler=[]

    for i in range (2,sayi):
        if sayi % i == 0:
            tam_bölenler.append(i)

    return tam_bölenler

print(tam_bölenleri_bul(20))        
