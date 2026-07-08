# ============================================================
# Ders 19 - Sets (Kümeler)
#
# Bu derste:
# - Set oluşturma
# - Tekrarlayan elemanlar
# - add()
# - update()
# - remove()
# ============================================================


# Set oluşturma
numbers = {1, 2, 3, 4, 5}
print(numbers)


# Tekrarlayan elemanlar tutulmaz
numbers = {1, 2, 2, 3, 4, 4, 5}
print(numbers)


# Farklı veri tipleri
fruits = {"Elma", "Armut", "Muz"}
print(fruits)


# add() -> Yeni eleman ekler
fruits.add("Kiraz")
print(fruits)


# update() -> Birden fazla eleman ekler
fruits.update(["Portakal", "Çilek"])
print(fruits)


# remove() -> Eleman siler
fruits.remove("Muz")
print(fruits)