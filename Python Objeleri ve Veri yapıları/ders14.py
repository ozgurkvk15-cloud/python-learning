# ============================================================
# Ders 14 - Python Liste Metotları
#
# Bu derste:
# - min() ve max() fonksiyonları
# - Liste dilimleme (Slicing)
# - append() metodu
# - insert() metodu
# - remove() metodu
# - sort() metodu
# - reverse() metodu
# ============================================================


# ------------------------------------------------------------
# Sayı ve harf listeleri oluşturma
# ------------------------------------------------------------

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
letters = ["a", "b", "c", "d", "e", "f"]


# ------------------------------------------------------------
# min() ve max() fonksiyonları
# Listenin en küçük ve en büyük elemanını bulur.
# ------------------------------------------------------------

print("En Küçük Sayı :", min(numbers))
print("En Büyük Sayı :", max(numbers))

print("Alfabetik Olarak İlk Harf :", min(letters))
print("Alfabetik Olarak Son Harf :", max(letters))

print("-" * 50)


# ------------------------------------------------------------
# Liste Dilimleme (Slicing)
# 3. indexten başlayıp 5. indexe kadar olan elemanları alır.
# ------------------------------------------------------------

slice_list = numbers[3:6]

print("Liste Dilimleme Sonucu:")
print(slice_list)

print("-" * 50)


# ------------------------------------------------------------
# append()
# Listenin sonuna yeni eleman ekler.
# ------------------------------------------------------------

numbers.append(40)

print("append() Sonrası:")
print(numbers)

print("-" * 50)


# ------------------------------------------------------------
# insert()
# Belirtilen indexe yeni eleman ekler.
# ------------------------------------------------------------

numbers.insert(3, 78)

print("insert() Sonrası:")
print(numbers)

print("-" * 50)


# ------------------------------------------------------------
# remove()
# Belirtilen değeri listeden siler.
# ------------------------------------------------------------

numbers.remove(78)

print("remove() Sonrası:")
print(numbers)

print("-" * 50)


# ------------------------------------------------------------
# sort()
# Listeyi küçükten büyüğe sıralar.
# ------------------------------------------------------------

numbers.sort()

print("sort() Sonrası:")
print(numbers)

print("-" * 50)


# ------------------------------------------------------------
# reverse()
# Listenin sırasını tersine çevirir.
# ------------------------------------------------------------

numbers.reverse()

print("reverse() Sonrası:")
print(numbers)

print("-" * 50)