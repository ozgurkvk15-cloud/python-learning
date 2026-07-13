# ==============================================================================
# PYTHON KOŞULLU DURUMLAR - İLERİ SEVİYE UYGULAMA SORULARI (BÖLÜM 2)
# ==============================================================================

print("--- KOŞULLU DURUMLAR İLERİ SEVİYE UYGULAMA TESTİ ---")

# ------------------------------------------------------------------------------
# SORU 1: Gelişmiş Şifre Güvenlik ve Karakter Kontrolü
# Senaryo: Kullanıcıdan yeni bir şifre belirlemesini isteyin. Şifrenin kabul 
# edilmesi için şu 3 şartın AYNI ANDA sağlanması gerekir:
# 1. Şifre en az 8 karakter uzunluğunda olmalıdır.
# 2. Şifre "123456" veya "password" gibi basit ifadeler içermemelidir.
# 3. Şifre boşluk karakteri içermemelidir.
# ------------------------------------------------------------------------------
print("\n[Soru 1 - Şifre Güvenlik Analizi]")
yeni_sifre = input("Lütfen yeni şifrenizi belirleyiniz: ")

if len(yeni_sifre) < 8:
    print("Geçersiz Şifre: Şifreniz en az 8 karakter uzunluğunda olmalıdır.")
elif " " in yeni_sifre:
    print("Geçersiz Şifre: Şifreniz boşluk karakteri içeremez.")
elif yeni_sifre in ["123456", "password", "12345678"]:
    print("Geçersiz Şifre: Çok yaygın/basit bir şifre seçtiniz.")
else:
    print("Şifre Başarılı: Şifreniz güvenlik kriterlerine uygundur.")


# ------------------------------------------------------------------------------
# SORU 2: Abonelik Paket Öneri ve Gelir Segmentasyonu
# Senaryo: Bir yazılım şirketi kullanıcının mesleğine ve aylık bütçesine göre paket öneriyor.
# Kullanıcıdan öğrenci olup olmadığını ve yazılıma ayırabileceği bütçeyi alın.
# - Eğer öğrenciyse ve bütçesi 100 TL altındaysa: "Eğitim Paketi (Ücretsiz)"
# - Eğer öğrenciyse ve bütçesi 100 TL ve üzeriyse: "Öğrenci Plus Paketi (İndirimli)"
# - Öğrenci değilse ve bütçesi 500 TL altındaysa: "Standart Plan"
# - Öğrenci değilse ve bütçesi 500 TL ile 2000 TL arasındaysa: "Profesyonel Plan"
# - Bütçesi 2000 TL üzerindeyse mesleğe bakılmaksızın: "Kurumsal Enterprise Plan"
# ------------------------------------------------------------------------------
print("\n[Soru 2 - Akıllı Paket Öneri Sistemi]")
is_ogrenci = input("Öğrenci misiniz? (evet/hayir): ").lower() == "evet"
butce = float(input("Aylık ayırabileceğiniz maksimum bütçe (TL): "))

if butce > 2000:
    print("Önerilen Paket: Kurumsal Enterprise Plan")
elif is_ogrenci:
    if butce < 100:
        print("Önerilen Paket: Eğitim Paketi (Ücretsiz / Sponsorlu)")
    else:
        print("Önerilen Paket: Öğrenci Plus Paketi (Aylık 100 TL)")
else:
    if butce < 500:
        print("Önerilen Paket: Standart Plan (Aylık 350 TL)")
    else:
        print("Önerilen Paket: Profesyonel Plan (Aylık 1200 TL)")


# ------------------------------------------------------------------------------
# SORU 3: Artık Yıl (Leap Year) Hesaplama Mantığı
# Senaryo: Kullanıcının girdiği bir yılın "Artık Yıl" (Şubat ayının 29 gün çektiği yıl)
# olup olmadığını hesaplayın. 
# Kural: Bir yıl 4'e kalansız bölünmelidir. Ancak 100'e tam bölünen yıllar artık yıl değildir.
# İstisna: Eğer yıl 400'e de tam bölünüyorsa tekrar artık yıl sayılır.
# ------------------------------------------------------------------------------
print("\n[Soru 3 - Artık Yıl Algoritması]")
yil = int(input("Kontrol etmek istediğiniz yılı giriniz: "))

if (yil % 4 == 0 and yil % 100 != 0) or (yil % 400 == 0):
    print(f"Sonuç: {yil} bir artık yıldır. Şubat ayı 29 gün çeker.")
else:
    print(f"Sonuç: {yil} bir artık yıl değildir. Şubat ayı 28 gün çeker.")


# ------------------------------------------------------------------------------
# SORU 4: Akıllı Ev Termostatı ve Eylem Planı
# Senaryo: Evdeki sıcaklık sensöründen ve nem sensöründen değerler simüle ediliyor.
# Sıcaklık 18'den küçükse kombi çalışmalı. Sıcaklık 26'dan büyükse klima çalışmalı.
# Sıcaklık 18 ile 26 arasındaysa sistem stabil kalmalı.
# Ekstra Şart: Sıcaklık stabil olsa bile nem oranı %70'in üzerindeyse "Nem Alma Modu" açılmalı.
# ------------------------------------------------------------------------------
print("\n[Soru 4 - Akıllı Ev Termostat Kontrolü]")
sicaklik = float(input("Mevcut oda sıcaklığını giriniz (Derece): "))
nem = float(input("Mevcut oda nem oranını giriniz (%): "))

if sicaklik < 18:
    print("Sistem Eylemi: Isıtıcı / Kombi aktif hale getirildi.")
elif sicaklik > 26:
    print("Sistem Eylemi: Soğutucu / Klima aktif hale getirildi.")
else:
    if nem > 70:
        print("Sistem Eylemi: Sıcaklık ideal ancak nem yüksek. Nem alma modu aktif.")
    else:
        print("Sistem Eylemi: Sıcaklık ve nem ideal seviyede. Enerji tasarrufu modu aktif.")


# ------------------------------------------------------------------------------
# SORU 5: Gelişmiş Kargo Ücreti ve Hacimsel (Desi) Hesaplama
# Senaryo: Kargo ücreti ürünün ağırlığına veya hacmine (Desi) göre hesaplanır.
# Desi Formülü = (En * Boy * Yükseklik) / 3000
# Kullanıcıdan ağırlık, en, boy ve yükseklik bilgilerini alın.
# Hesaplanan desi ile ağırlıktan HANGİSİ BÜYÜKSE faturalandırma o değer üzerinden yapılır.
# Fiyatlandırma: Kargo matrah değeri (büyük olan) 5'ten küçükse sabit 50 TL,
# 5 ile 20 arasındaysa değer başına 10 TL, 20'den büyükse değer başına 8 TL'dir.
# ------------------------------------------------------------------------------
print("\n[Soru 5 - Lojistik Desi ve Fiyat Hesaplama]")
agirlik = float(input("Paket ağırlığını giriniz (kg): "))
en = float(input("Paket enini giriniz (cm): "))
boy = float(input("Paket boyunu giriniz (cm): "))
yukseklik = float(input("Paket yüksekliğini giriniz (cm): "))

desi = (en * boy * yukseklik) / 3000
print(f"Hesaplanan Hacimsel Değer (Desi): {desi:.2f}")

# Faturalandırmaya esas alınacak büyük değeri seçiyoruz
if agirlik > desi:
    islem_degeri = agirlik
    print(f"Faturalandırma kriteri: Ağırlık ({agirlik} kg)")
else:
    islem_degeri = desi
    print(f"Faturalandırma kriteri: Desi ({desi:.2f})")

# Fiyatlandırma baremleri
if islem_degeri < 5:
    toplam_ucret = 50.0
elif islem_degeri >= 5 and islem_degeri <= 20:
    toplam_ucret = islem_degeri * 10
else:
    toplam_ucret = islem_degeri * 8

print(f"Toplam Kargo Gönderim Ücreti: {toplam_ucret:.2f} TL")

# ==============================================================================
# DOSYA SONU
# ==============================================================================