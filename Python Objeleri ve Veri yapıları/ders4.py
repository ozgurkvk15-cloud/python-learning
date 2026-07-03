# ============================================
# PYTHON DERS 4
# Konular:
# - Değişkenlerle işlem yapma
# - String birleştirme
# - Yaş hesaplama
# - Sipariş toplamı hesaplama
# ============================================

# Müşteri bilgileri

musteriAdi = "Özgür"
musteriSoyadi = "Kavak"

musteriAdiSoyadi = musteriAdi + " " + musteriSoyadi

musteriCinsiyet = True

musteriDogumYili = 2004

musteriAdresi = "Adana / Seyhan"

musteriYasi = 2026 - musteriDogumYili

print("Ad Soyad :", musteriAdiSoyadi)
print("Yaş :", musteriYasi)

print("----------------------")

# Sipariş toplamı hesaplama

siparis1 = 110
siparis2 = 1100.50
siparis3 = 356.95

toplam = siparis1 + siparis2 + siparis3

print("Toplam Sipariş Tutarı :", toplam)