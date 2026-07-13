# ==============================================================================
# PYTHON KOŞULLU DURUMLAR - İLERİ SEVİYE UYGULAMA SORULARI
# ==============================================================================

print("--- KOŞULLU DURUMLAR GELİŞMİŞ UYGULAMA TESTİ ---")

# ------------------------------------------------------------------------------
# SORU 1: Gelişmiş Not Hesaplama ve Harf Notu Sistemi
# Senaryo: Kullanıcıdan vize (%40) ve final (%60) notunu alıp ortalamayı hesaplayın.
# Eğer final notu 50'nin altındaysa ortalamaya bakılmaksızın "Kaldınız (Final Yetersiz)" yazdırın.
# Final 50 ve üzeriyse harf notunu şu kriterlere göre belirleyin:
# 90-100 -> AA, 80-89 -> BA, 70-79 -> BB, 50-69 -> CC, 0-49 -> FF
# ------------------------------------------------------------------------------
print("\n[Soru 1 - Harf Notu Hesaplama]")
vize = float(input("Vize notunuzu giriniz: "))
final = float(input("Final notunuzu giriniz: "))

ortalama = (vize * 0.4) + (final * 0.6)
print(f"Yıl sonu ortalamanız: {ortalama}")

if final < 50:
    print("Durum: Kaldınız (Final notunuz 50'den küçük olduğu için baraja takıldınız).")
else:
    if ortalama >= 90:
        print("Harf Notu: AA - Geçtiniz.")
    elif ortalama >= 80:
        print("Harf Notu: BA - Geçtiniz.")
    elif ortalama >= 70:
        print("Harf Notu: BB - Geçtiniz.")
    elif ortalama >= 50:
        print("Harf Notu: CC - Geçtiniz.")
    else:
        print("Harf Notu: FF - Kaldınız.")


# ------------------------------------------------------------------------------
# SORU 2: ATM Para Çekme ve Limit Kontrolü
# Senaryo: Kullanıcının hesabında 5000 TL bakiye ve günlük 3000 TL çekim limiti vardır.
# Kullanıcıdan çekmek istediği tutarı alın. Bakiye yetersizse veya günlük limit 
# aşılıyorsa uygun hata mesajını verin; şartlar uyuyorsa bakiyeyi güncelleyin.
# ------------------------------------------------------------------------------
print("\n[Soru 2 - ATM Simülasyonu]")
mevcut_bakiye = 5000.0
gunluk_limit = 3000.0

cekilecek_tutar = float(input("Çekmek istediğiniz tutarı giriniz (TL): "))

if cekilecek_tutar > mevcut_bakiye:
    print("İşlem Reddedildi: Hesabınızda yeterli bakiye bulunmamaktadır.")
elif cekilecek_tutar > gunluk_limit:
    print(f"İşlem Reddedildi: Günlük maksimum çekim limitiniz {gunluk_limit} TL'dir.")
else:
    mevcut_bakiye -= cekilecek_tutar
    print("İşlem Başarılı: Paranızı hazneden alınız.")
    print(f"Kalan Güncel Bakiyeniz: {mevcut_bakiye} TL")


# ------------------------------------------------------------------------------
# SORU 3: E-Posta ve Şifre Doğrulama (İçiçe If / Nested If Yapısı)
# Senaryo: Sistemde kayıtlı e-posta "kanka@kod.com" ve şifre "py123" olsun.
# Önce e-postayı kontrol edin. E-posta yanlışsa direkt "E-posta bulunamadı" deyin.
# E-posta doğruysa bu kez şifreyi kontrol edin. Şifre yanlışsa "Şifre hatalı" deyin.
# ------------------------------------------------------------------------------
print("\n[Soru 3 - Güvenli Giriş Sistemi]")
db_email = "kanka@kod.com"
db_password = "py123"

input_email = input("E-posta adresinizi giriniz: ")

if input_email == db_email:
    input_password = input("Şifrenizi giriniz: ")
    if input_password == db_password:
        print("Giriş Başarılı: Hoş geldiniz.")
    else:
        print("Giriş Başarısız: Şifreniz hatalı.")
else:
    print("Giriş Başarısız: Bu e-posta adresi sistemde kayıtlı değil.")


# ------------------------------------------------------------------------------
# SORU 4: Şehir Yasaklı Listesi Kontrolü (Membership + If-Else)
# Senaryo: Bir kargo firması "Adana", "Mersin" ve "Hatay" şehirlerine lojistik 
# aksaklıklar nedeniyle geçici olarak gönderim yapamamaktadır. Kullanıcının girdiği 
# şehre kargo gönderilip gönderilemeyeceğini 'in' operatörü kullanarak kontrol edin.
# ------------------------------------------------------------------------------
print("\n[Soru 4 - Kargo Dağıtım Kontrolü]")
yasakli_sehirler = ["Adana", "Mersin", "Hatay"]

hedef_sehir = input("Kargo gönderilecek şehri yazınız: ")

if hedef_sehir in yasakli_sehirler:
    print(f"Üzgünüz, {hedef_sehir} şehrine geçici olarak hizmet verilememektedir.")
else:
    print(f"Siparişiniz onaylandı, kargonuz {hedef_sehir} şehrine gönderilmek üzere hazırlanıyor.")


# ------------------------------------------------------------------------------
# SORU 5: BMI (Vücut Kitle Endeksi) Hesaplama ve Durum Analizi
# Senaryo: Kullanıcıdan kilo (kg) ve boy (metre cinsinden, örn: 1.75) bilgilerini alın.
# Formül: VKE = Kilo / (Boy * Boy)
# Sonuçlara göre kategoriyi ekrana yazdırın:
# VKE < 18.5 -> Zayıf, 18.5-24.9 -> Normal, 25-29.9 -> Fazla Kilolu, 30 ve üzeri -> Obez
# ------------------------------------------------------------------------------
print("\n[Soru 5 - Vücut Kitle Endeksi Hesaplama]")
kilo = float(input("Kilonuzu giriniz (kg): "))
boy = float(input("Boyunuzu metre cinsinden giriniz (Örn: 1.78): "))

vke = kilo / (boy ** 2)
print(f"Hesaplanan Vücut Kitle Endeksiniz (VKE): {vke:.2f}")

if vke < 18.5:
    print("Kategori: Zayıf. Sağlıklı bir şekilde kilo almanız önerilir.")
elif vke >= 18.5 and vke <= 24.9:
    print("Kategori: Normal. Tebrikler, ideal kilonuzu korumaya devam edin.")
elif vke >= 25.0 and vke <= 29.9:
    print("Kategori: Fazla Kilolu. Beslenmenize dikkat etmeniz önerilir.")
else:
    print("Kategori: Obez. Bir sağlık uzmanına danışmanız tavsiye edilir.")

# ==============================================================================
# DOSYA SONU
# ==============================================================================