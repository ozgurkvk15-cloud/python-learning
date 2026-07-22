# 1. Basit Karşılama Fonksiyonu
def say_hello(name):
    """Kullanıcıya ismiyle selam verir."""
    print(f"Hello, {name}!")


say_hello("Özgür")


# 2. İki Sayıyı Toplayan Fonksiyon
def total(num1, num2):
    """Verilen iki sayıyı toplayarak sonucu döndürür."""
    return num1 + num2


result = total(10, 20)
print(result)


# 3. Yaş Hesaplayan Fonksiyon
def yas_hesapla(dogum_yili):
    """Doğum yılına göre güncel yaşı hesaplar."""
    return 2026 - dogum_yili


age_ozgur = yas_hesapla(2004)
print(age_ozgur)


# 4. Emeklilik Süresini Hesaplayan Fonksiyon
def emeklilik_kac_yil_kaldi(dogum_yili, isim):
    """
    Kullanıcının doğum yılına ve ismine göre 
    emekliliğe kaç yılı kaldığını hesaplar ve yazdırır.
    """
    yas = yas_hesapla(dogum_yili)
    emeklilik = 65 - yas

    if emeklilik > 0:
        print(f"Sayın {isim}, emekliliğinize {emeklilik} yıl kaldı.")
    else:
        print(f"Sayın {isim}, zaten emekli oldunuz.")


# Fonksiyon çağrısı: doğum yılı (sayı) ve isim (metin)
emeklilik_kac_yil_kaldi(1983, "Özgür")