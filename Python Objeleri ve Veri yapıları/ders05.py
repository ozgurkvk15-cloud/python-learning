# ============================================
# PYTHON DERS 5
# Konu: Veri Tipi Dönüşümleri (Type Conversion)
# ============================================

# Python'da bazen bir veri tipini başka bir veri tipine dönüştürmemiz gerekir.
# Bunun için int(), float() ve str() fonksiyonlarını kullanırız.


# ============================================
# String -> Integer
# ============================================

yas = "22"

print(type(yas))          # <class 'str'>

yas = int(yas)

print(type(yas))          # <class 'int'>
print(yas + 5)            # 27


print("---------------------------------")


# ============================================
# String -> Float
# ============================================

boy = "1.78"

print(type(boy))          # <class 'str'>

boy = float(boy)

print(type(boy))          # <class 'float'>
print(boy)


print("---------------------------------")


# ============================================
# Integer -> Float
# ============================================

sayi = 100

print(type(sayi))

sayi = float(sayi)

print(type(sayi))
print(sayi)


print("---------------------------------")


# ============================================
# Float -> Integer
# ============================================

ortalama = 85.90

print(type(ortalama))

ortalama = int(ortalama)

print(type(ortalama))
print(ortalama)

# Dikkat!
# int() ondalık kısmı siler.
# 85.90 -> 85


print("---------------------------------")


# ============================================
# Integer -> String
# ============================================

numara = 100

print(type(numara))

numara = str(numara)

print(type(numara))
print(numara)


print("---------------------------------")


# ============================================
# Float -> String
# ============================================

maas = 25000.75

print(type(maas))

maas = str(maas)

print(type(maas))
print(maas)


print("---------------------------------")


# ============================================
# String Birleştirme
# ============================================

yas = 22

print("Yaşım : " + str(yas))

# Sayıları doğrudan string ile birleştiremeyiz.
# Bu yüzden str() kullanırız.


print("---------------------------------")


# ============================================
# Uygulama Örneği
# ============================================

sayi1 = "50"
sayi2 = "20"

# String olarak toplarsak

print(sayi1 + sayi2)

# Integer'a çevirerek toplarsak

print(int(sayi1) + int(sayi2))