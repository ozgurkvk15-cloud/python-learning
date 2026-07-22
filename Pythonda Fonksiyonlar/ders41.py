# 1. LAMBDA (Tek Satırlık İsimsiz Fonksiyonlar)
# Normal fonksiyon yazmak yerine tek satırda pratikçe tanımlanır.

# Normal fonksiyon:
def square_normal(num):
    return num ** 2


# Lambda versiyonu:
square = lambda num: num ** 2

print(f"Normal ile 3'ün karesi: {square_normal(3)}")
print(f"Lambda ile 3'ün karesi: {square(3)}")


# 2. MAP (Listenin Her Elemanına Bir Fonksiyon Uygulama)
# Bir listedeki her elemanı alıp fonksiyondan geçirir ve yeni bir liste döner.

numbers = [1, 3, 5, 9, 10]

# Harici fonksiyon kullanarak map kullanımı:
square_numbers = list(map(square_normal, numbers))

# Doğrudan lambda ile map kullanımı (En yaygın yöntem):
square_numbers_lambda = list(map(lambda num: num ** 2, numbers))

print(f"Kareleri alınan liste: {square_numbers_lambda}")


# 3. FILTER (Koşula Göre Eleman Eleme)
# Sadece koşulu True (doğru) sağlayan elemanları tutar, diğerlerini eler.

numbers_list = [1, 3, 5, 8, 10, 12]

# Çift sayıları bulma (harici fonksiyon ile):
def check_even(num):
    return num % 2 == 0


even_numbers = list(filter(check_even, numbers_list))

# Çift sayıları bulma (lambda ile):
even_numbers_lambda = list(filter(lambda num: num % 2 == 0, numbers_list))

print(f"Çift sayılar: {even_numbers_lambda}")