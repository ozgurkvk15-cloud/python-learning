# BANKAMAETİK UYGULAMASI
#-----------------------

özgür_hesap={
    "ad":"özgür",
    "hesap_no":"123456",
    "bakiye": 3000,
    "ek_hesap":2000
}


merve_hesap={
    "ad":"merve",
    "hesap_no":"2345678",
    "bakiye": 6000,
    "ek_hesap":3000
}

def para_cek (hesap,miktar):
    print(f"merhaba {hesap['ad']}")

    if hesap['bakiye'] >= miktar:
        hesap['bakiye']-=miktar
        print("paranızı alabilirsiniz.")
    else:
        toplam=hesap['bakiye'] + hesap['ek_hesap'] 

        if toplam >= miktar:
            ek_hesap_kullanimi=input("ek hesabınızdaki bakiyeyi kullanmak istiyormusunuz ?  (e/h)")

            if ek_hesap_kullanimi == 'e':
                bakiye=hesap['bakiye']
                ek_hesap_kullanilacak_miktar=miktar-bakiye
                hesap['bakiye']=0
                hesap['ek_hesap']-=ek_hesap_kullanilacak_miktar
                print("paranızı alabilirsiniz.")
            else:
                print(f"{hesap['hesap_no']} no lu hesabınızda {hesap['bakiye']} TL bulunmaktadır.")  
        else:
            print("maalesef bakiyeniz yetersiz.")          


def bakiye_sorgula(hesap):
    print(f"{hesap['hesap_no']} hesabınızda {hesap['bakiye']} TL bulunmaktadır. ek hesap litiminiz ise {hesap['ek_hesap']} TL bulunmaktadır")




para_cek(özgür_hesap,3000)
bakiye_sorgula(özgür_hesap)
print("*"*50)
para_cek(özgür_hesap,2000)
bakiye_sorgula(özgür_hesap)

