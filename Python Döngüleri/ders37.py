#-----------------
# SAYI TAHMİN OYUNU
#-----------------

# 1 - 100  arasında rasgele sayı üretilecek bir sayıyı aşağı ve yukarı ifadeleri ile buldurmaya çalışın

# 100 üzerinden puanlama yaoın her soru 20 puan
# hak bilgisi kulllanıcıdan alın ve her soru belitrilen can sayısı üzerinden hesaplayınız

import random

# 1 - 100 arasında rastgele sayı üretimi
sayi = random.randint(1, 100)

can = int(input("Kaç hak kullanmak istersiniz: "))
hak = can
sayac = 0

while hak > 0:
    hak -= 1
    sayac += 1
    tahmin = int(input(f"{sayac}. Tahmininiz: "))

    if sayi == tahmin:
        # Doğru puan hesabı: Her yanlış tahminde (can başına düşen puan) kadar eksilir.
        # İlk seferde bilinirse (sayac=1, can=5 ise) -> 100 - (20 * 0) = 100 puan kalır.
        puan = 100 - (100 / can) * (sayac - 1)
        print(f"\nTebrikler! {sayac}. defada bildiniz.")
        print(f"Toplam Puanınız: {puan}")
        break
    elif sayi > tahmin:
        print("Yukarı ↑")
    else:
        print("Aşağı ↓")

    if hak == 0:
        print(f"\nHakkınız bitti! Tutulan sayı: {sayi}")