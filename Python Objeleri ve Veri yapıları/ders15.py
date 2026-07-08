# ============================================================
# Ders 15 - Python Liste Metotları Uygulamaları
#
# Bu derste:
# - Listeye eleman ekleme
# - Liste elemanı silme
# - Eleman arama
# - Listeyi sıralama
# - Listeyi ters çevirme
# - String ifadeyi listeye dönüştürme
# - count(), clear() metotları
# - Kullanıcıdan veri alarak liste oluşturma
# ============================================================


# ------------------------------------------------------------
# Başlangıç Listeleri
# ------------------------------------------------------------

names = ["Ali", "Yağmur", "Hakan", "Deniz"]
years = [1998, 2000, 1998, 1987]


# ------------------------------------------------------------
# 1. "Cenk" ismini listenin sonuna ekleyin.
# ------------------------------------------------------------

names.append("Cenk")
print("1.", names)


# ------------------------------------------------------------
# 2. "Sena" ismini listenin başına ekleyin.
# ------------------------------------------------------------

names.insert(0, "Sena")
print("2.", names)


# ------------------------------------------------------------
# 3. "Deniz" ismini listeden silin.
# ------------------------------------------------------------

names.remove("Deniz")
print("3.", names)


# ------------------------------------------------------------
# 4. "Hakan" isminin index numarasını bulun.
# ------------------------------------------------------------

print("4.", names.index("Hakan"))


# ------------------------------------------------------------
# 5. "Ali" listenin bir elemanı mı?
# ------------------------------------------------------------

print("5.", "Ali" in names)


# ------------------------------------------------------------
# 6. Liste elemanlarını ters çevirin.
# ------------------------------------------------------------

names.reverse()
print("6.", names)


# ------------------------------------------------------------
# 7. Listeyi alfabetik olarak sıralayın.
# ------------------------------------------------------------

names.sort()
print("7.", names)


# ------------------------------------------------------------
# 8. Years listesini küçükten büyüğe sıralayın.
# ------------------------------------------------------------

years.sort()
print("8.", years)


# ------------------------------------------------------------
# 9. String ifadeyi listeye dönüştürün.
# ------------------------------------------------------------

brands = "Chevrolet,Dacia".split(",")

print("9.", brands)


# ------------------------------------------------------------
# 10. Years listesinin en büyük ve en küçük elemanını bulun.
# ------------------------------------------------------------

print("10. En Büyük:", max(years))
print("10. En Küçük:", min(years))


# ------------------------------------------------------------
# 11. Years listesinde kaç tane 1998 vardır?
# ------------------------------------------------------------

print("11.", years.count(1998))


# ------------------------------------------------------------
# 12. Years listesindeki tüm elemanları silin.
# ------------------------------------------------------------

years.clear()
print("12.", years)


# ------------------------------------------------------------
# 13. Kullanıcıdan 3 marka alıp listeye ekleyin.
# ------------------------------------------------------------

brands = []

brands.append(input("1. Marka: "))
brands.append(input("2. Marka: "))
brands.append(input("3. Marka: "))

print("13.", brands)