# ==============================================================================
# PYTHON UYGULAMA SORULARI VE ÇÖZÜMLERİ
# ==============================================================================

# Başlangıç Değişkenleri
x, y, z = 2, 5, 10
numaralar = 1, 5, 7, 10, 6


# ------------------------------------------------------------------------------
# SORU 1: Kullanıcıdan alınan iki sayının çarpımı ile x, y, z toplamının farkı?
# ------------------------------------------------------------------------------
# Kullanıcıdan input alırken sayısal işlem yapabilmek için int() ile tam sayıya çeviriyoruz.
a = int(input("1. sayıyı giriniz: "))
b = int(input("2. sayıyı giriniz: "))

toplam_xyz = x + y + z
carpim_ab = a * b

result_1 = carpim_ab - toplam_xyz
print(f"Soru 1 Sonucu: {result_1}")


# ------------------------------------------------------------------------------
# SORU 2: y'nin x'e kalansız (tam) bölümünü hesaplayınız.
# ------------------------------------------------------------------------------
# '//' operatörü bölme işlemini yapar ve sadece tam kısım sonucunu verir (Taban Bölme).
result_2 = y // x
print(f"Soru 2 Sonucu (Tam Bölme): {result_2}")  # 5 // 2 = 2


# ------------------------------------------------------------------------------
# SORU 3: x, y, z toplamının mod 3'ünü (3'e bölümünden kalanı) alınız.
# ------------------------------------------------------------------------------
# '%' operatörü mod alma işlemidir, bölmeden kalan sayıyı verir.
toplam = x + y + z  # 2 + 5 + 10 = 17
result_3 = toplam % 3
print(f"Soru 3 Sonucu (Mod 3): {result_3}")  # 17'nin 3'e bölümünden kalan 2'dir.


# ------------------------------------------------------------------------------
# SORU 4: y'nin x. kuvvetini (üssünü) hesaplayınız.
# ------------------------------------------------------------------------------
# '**' operatörü üs alma işlemidir.
result_4 = y ** x
print(f"Soru 4 Sonucu (Üs Alma): {result_4}")  # 5 üssü 2 = 25


# ------------------------------------------------------------------------------
# SORU 5: x, *y, z = numaralar işlemine göre z'nin küpü kaçtır?
# ------------------------------------------------------------------------------
# 'Extended Unpacking' (Genişletilmiş Demet Çözme):
# x ilk elemanı (1), z son elemanı (6) alır. 
# Başında yıldız olan *y ise ortada kalan tüm elemanları bir liste olarak içine toplar.

numaralar = 1, 5, 7, 10, 6
x, *y, z = numaralar

print(f"Soru 5 - Ortada kalan y listesi: {y}")  # Çıktı: [5, 7, 10]
print(f"Soru 5 - Sondaki z değeri: {z}")        # Çıktı: 6

# z'nin küpünü (3. kuvvetini) hesaplayalım:
z_nin_kupu = z ** 3
print(f"Soru 5 Sonucu (z'nin küpü): {z_nin_kupu}")  # 6 * 6 * 6 = 216
