# ==============================================================================
# PYTHON KARŞILAŞTIRMA OPERATÖRLERİ (Comparison Operators)
# ==============================================================================

# Başlangıç Değişkenleri
a, b, c, d = 5, 5, 2, 6
admin = "özgür"
sifre = "1234"

# ------------------------------------------------------------------------------
# 1. EŞİTTİR OPERATÖRÜ (==)
# ------------------------------------------------------------------------------
result = (a == b)
print("a == b :", result)  # Çıktı: True (5, 5'e eşittir)

result = (a == c)
print("a == c :", result)  # Çıktı: False (5, 2'ye eşit değildir)

result = ("özg" == admin)
print("'özg' == admin :", result)  # Çıktı: False ("özg", "özgür" ile birebir aynı değil)

result = ("özgür" == admin)
print("'özgür' == admin :", result)  # Çıktı: True (Metinler birebir aynı)


# ------------------------------------------------------------------------------
# 2. EŞİT DEĞİLDİR OPERATÖRÜ (!=)
# ------------------------------------------------------------------------------
result = (a != b)
print("a != b :", result)  # Çıktı: False (5, 5'ten farklı değildir, o yüzden False)

result = (a != c)
print("a != c :", result)  # Çıktı: True (5, 2'den farklıdır)


# ------------------------------------------------------------------------------
# 3. BÜYÜKTÜR / KÜÇÜKTÜR OPERATÖRLERİ (> , <)
# ------------------------------------------------------------------------------
result = (a > b)
print("a > b :", result)  # Çıktı: False (5, 5'ten büyük değildir)

result = (a < c)
print("a < c :", result)  # Çıktı: False (5, 2'den küçük değildir)


# ------------------------------------------------------------------------------
# 4. BÜYÜK-EŞİT / KÜÇÜK-EŞİT OPERATÖRLERİ (>= , <=)
# ------------------------------------------------------------------------------
# DİKKAT: 'result(a>=b)' kullanımı hatalıdır. Değer atamak için '=' kullanılmalıdır.

result = (a >= b)
print("a >= b :", result)  # Çıktı: True (5, 5'ten büyük değildir ama EŞİTTİR)

result = (a <= b)
print("a <= b :", result)  # Çıktı: True (5, 5'ten küçük değildir ama EŞİTTİR)