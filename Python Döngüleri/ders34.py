# ==============================
# WHILE DÖNGÜSÜ UYGULAMALARI
# ==============================

sayilar = [1, 2, 3, 4, 5, 56, 66, 78, 88, 99]

# ----------------------------------
# Soru 1
# Sayılar listesini while döngüsü ile ekrana yazdırın.

print("Soru 1")

i = 0

while i < len(sayilar):
    print(sayilar[i])
    i += 1


# ----------------------------------
# Soru 2
# Başlangıç ve bitiş değerlerini kullanıcıdan alıp
# aradaki tek sayıları yazdırın.

print("\nSoru 2")

baslangic = int(input("Başlangıç: "))
bitis = int(input("Bitiş: "))

i = baslangic

while i <= bitis:
    if i % 2 == 1:
        print(i)
    i += 1


# ----------------------------------
# Soru 3
# 100'den 1'e kadar sayıları yazdırın.

print("\nSoru 3")

i = 100

while i >= 1:
    print(i)
    i -= 1


# ----------------------------------
# Soru 4
# Kullanıcıdan 5 sayı alıp küçükten büyüğe sıralayın.

print("\nSoru 4")

numbers = []

i = 0

while i < 5:
    sayi = int(input(f"{i + 1}. sayıyı giriniz: "))
    numbers.append(sayi)
    i += 1

numbers.sort()

print("Sıralı Liste:", numbers)


# ----------------------------------
# Soru 5 (Ekstra)
# Kullanıcıdan alınan 5 sayının toplamını ve ortalamasını bulun.

print("\nSoru 5")

toplam = 0
i = 0

while i < len(numbers):
    toplam += numbers[i]
    i += 1

ortalama = toplam / len(numbers)

print("Toplam:", toplam)
print("Ortalama:", ortalama)

# Soru 6
# Kullanıcı 0 girene kadar sayı almaya devam edin.
# Girilen sayıların toplamını ekrana yazdırın.



#-----------------------#
print("\nSoru 6")

toplam = 0

while True:
    sayi = int(input("Sayı gir (Çıkmak için 0): "))

    if sayi == 0:
        break

    toplam += sayi

print("Girilen sayıların toplamı:", toplam)