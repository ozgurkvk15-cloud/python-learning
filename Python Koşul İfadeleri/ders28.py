# ==============================================================================
# PYTHON KOŞULLU DURUMLAR - GİRİŞ (if - elif - else)
# ==============================================================================

# Koşullu durumlar, belirli şartlar doğru (True) veya yanlış (False) olduğunda 
# programın farklı kod bloklarını çalıştırmasını sağlar.
# Python'da bloklar girintilerle (Indent - Genellikle 4 boşluk) belirlenir.

# ------------------------------------------------------------------------------
# 1. EN TEMEL YAPI: Tek Başına 'if' Kullanımı
# ------------------------------------------------------------------------------
print("--- 1. Örnek ---")
yas = 20

# Eğer koşul sağlanırsa (True dönerse) altındaki girintili kod çalışır.
if yas >= 18:
    print("Ehliyet alabilirsiniz.")  # Bu satır sadece yaş 18 veya büyükse çalışır.


# ------------------------------------------------------------------------------
# 2. İKİLİ İHTİMAL: 'if - else' Yapısı
# ------------------------------------------------------------------------------
# Şart sağlanıyorsa 'if' bloğu, sağlanmıyorsa GERİYE KALAN tüm durumlarda 'else' bloğu çalışır.
print("\n--- 2. Örnek ---")
not_ortalamasi = 45

if not_ortalamasi >= 50:
    print("Dersi geçtiniz.")
else:
    print("Maalesef dersten kaldınız.")


# ------------------------------------------------------------------------------
# 3. ÇOKLU İHTİMAL: 'if - elif - else' Yapısı (Else-If)
# ------------------------------------------------------------------------------
# İkiden fazla ihtimal veya koşul varsa araya 'elif' (else if) blokları eklenir.
# Python yukarıdan aşağıya doğru kontrol eder, İLK DOĞRU KOŞULU bulunca o bloğu çalıştırıp çıkar.
print("\n--- 3. Örnek ---")
hava_durumu = "yagmurlu"  # Değiştirip test edebilirsin: "gunesli", "karli", "ruzgarli"

if hava_durumu == "gunesli":
    print("Hava açık, dışarı çıkıp yürüyüş yapabilirsiniz.")
elif hava_durumu == "yagmurlu":
    print("Şemsiyenizi almayı unutmayınız.")
elif hava_durumu == "karli":
    print("Sıkı giyinin, dışarısı soğuk.")
else:
    # Yukarıdaki hiçbir koşula uymazsa (Örneğin: "ruzgarli" ise) burası çalışır.
    print("Hava durumu sistemde tanımlı değil, evde kalmak en güvenlisi.")


# ------------------------------------------------------------------------------
# 4. PRATİK UYGULAMA: Kullanıcı Giriş Simülasyonu
# ------------------------------------------------------------------------------
# Mantıksal operatörleri (and) burada if-else yapısı ile birleştiriyoruz.
print("\n--- 4. Örnek (Sistem Girişi) ---")
db_kullanici = "admin_kanka"
db_sifre = "1234"

input_kullanici = input("Kullanıcı adınızı giriniz: ")
input_sifre = input("Şifrenizi giriniz: ")

if (input_kullanici == db_kullanici) and (input_sifre == db_sifre):
    print("Giriş Başarılı. Yönetim paneline yönlendiriliyorsunuz.")
else:
    print("Hatalı kullanıcı adı veya şifre. Lütfen tekrar deneyin.")