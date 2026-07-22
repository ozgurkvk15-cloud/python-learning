# 1. Value Type (Değer Tipi) Örneği
def change_name(name):
    """
    Metinler (string) değiştirilemez (immutable) değer tipleridir.
    Fonksiyon içinde yapılan değişiklik orijinal değişkeni etkilemez.
    """
    name = "Özgür"


name = "Kavak"
change_name(name)
print(name)  # Çıktı: 'Kavak'


# 2. Reference Type (Referans Tipi) Örneği
def change(n):
    """
    Listeler değiştirilebilir (mutable) referans tipleridir.
    Fonksiyona listenin adresi gönderildiği için yapılan değişiklik
    orijinal listeyi de günceller.
    """
    n[0] = "Adana"


sehirler = ["Ankara", "İstanbul"]
change(sehirler)
print(sehirler)  # Çıktı: ['Adana', 'İstanbul']


# 3. Default Parameter (Varsayılan Parametre) Örneği
def add(a, b, c=0):
    """
    'c' parametresine varsayılan olarak 0 değeri atanmıştır.
    Üçüncü argüman girilmezse c=0 kabul edilir.
    """
    return sum((a, b, c))


print(add(10, 20))      # c yazılmadığı için 0 kabul edildi -> Çıktı: 30
print(add(10, 20, 30))  # c için 30 gönderildi -> Çıktı: 60