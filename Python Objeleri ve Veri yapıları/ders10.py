"""
====================================================
            PYTHON STRING METOTLARI
====================================================

Bu dosyada Python'da en sık kullanılan string
(karakter dizisi) metotları örneklerle gösterilmiştir.

✔ upper()
✔ lower()
✔ title()
✔ capitalize()
✔ strip()
✔ split()
✔ find()
✔ startswith()
✔ endswith()
✔ center()
"""

# ==================================================
# Örnek String
# ==================================================

message = "benim adım özgür mesleğim yazılım geliştirici"

print("Orijinal Metin:")
print(message)

print("-" * 60)

# ==================================================
# upper()
# Tüm karakterleri büyük harfe çevirir.
# ==================================================

print("upper()")
print(message.upper())

print("-" * 60)

# ==================================================
# lower()
# Tüm karakterleri küçük harfe çevirir.
# ==================================================

print("lower()")
print(message.lower())

print("-" * 60)

# ==================================================
# title()
# Her kelimenin ilk harfini büyük yapar.
# ==================================================

print("title()")
print(message.title())

print("-" * 60)

# ==================================================
# capitalize()
# Sadece ilk harfi büyütür.
# ==================================================

print("capitalize()")
print(message.capitalize())

print("-" * 60)

# ==================================================
# strip()
# Baştaki ve sondaki boşlukları siler.
# ==================================================

text = "      Python Öğreniyorum      "

print("strip()")
print(text.strip())

print("-" * 60)

# ==================================================
# split()
# String'i belirtilen karaktere göre parçalar.
# Varsayılan olarak boşluğa göre böler.
# ==================================================

print("split()")

words = message.split()

print(words)

print("-" * 60)

# ==================================================
# find()
# Aranan kelimenin başladığı index'i döndürür.
# Bulamazsa -1 döndürür.
# ==================================================

print("find()")

index = message.find("mesleğim")

print(index)

print("-" * 60)

# ==================================================
# startswith()
# Belirtilen ifade ile başlıyor mu?
# True / False döndürür.
# ==================================================

print("startswith()")

print(message.startswith("benim"))

print("-" * 60)

# ==================================================
# endswith()
# Belirtilen ifade ile bitiyor mu?
# True / False döndürür.
# ==================================================

print("endswith()")

print(message.endswith("geliştirici"))

print("-" * 60)

# ==================================================
# center()
# Yazıyı belirtilen uzunlukta ortalar.
# Boş kalan alanı istenilen karakterle doldurur.
# ==================================================

print("center()")

print(message.center(80, "*"))

print("-" * 60)