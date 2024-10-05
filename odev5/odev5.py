
##############################################
# Soru 1:Bir sözlük oluşturulur ve bu sözlükte öğrencilerin isimleri ve Matematik, Fizik, Kimya notları tutulur.
# Kullanıcıdan isim ve ders ismi(Matematik, Fizik, Kimya) istenir ve bu bilgilere göre çıktı verilir.
#############################################

##############################################
# Soru 2:Sözlük üzerinde değerleri değiştirme, yeni değer ekleme, kullanıcıya ulaşmak istediği bilgileri sorma gibi uygulamalar yapın.
#############################################

# Öğrenci bilgilerini içeren sözlük
ogrenciler = {
    "Leyla": {"Matematik": 85, "Fizik": 90, "Kimya": 78},
    "Melek": {"Matematik": 72, "Fizik": 88, "Kimya": 95},
    "Mutlu": {"Matematik": 65, "Fizik": 70, "Kimya": 82}
}

# Not sorgulama fonksiyonu
def not_sorgula(isim, ders):
    isim = isim.capitalize()  # İlk harfi büyük yap
    ders = ders.capitalize()  # İlk harfi büyük yap
    if isim in ogrenciler and ders in ogrenciler[isim]:
        print(isim, "adlı öğrencinin", ders, "notu:", ogrenciler[isim][ders])
    else:
        print("Öğrenci ya da ders bulunamadı.")

# Not güncelleme fonksiyonu
def not_guncelle(isim, ders, yeni_not):
    isim = isim.capitalize()  # İlk harfi büyük yap
    ders = ders.capitalize()  # İlk harfi büyük yap
    if isim in ogrenciler and ders in ogrenciler[isim]:
        ogrenciler[isim][ders] = yeni_not
        print(isim, "adlı öğrencinin", ders, "notu", yeni_not, "olarak güncellendi.")
    else:
        print("Öğrenci ya da ders bulunamadı.")

# Yeni öğrenci ekleme fonksiyonu
def yeni_ogrenci_ekle(isim, matematik_notu, fizik_notu, kimya_notu):
    isim = isim.capitalize()  # İlk harfi büyük yap
    ogrenciler[isim] = {"Matematik": matematik_notu, "Fizik": fizik_notu, "Kimya": kimya_notu}
    print(isim, "adlı öğrenci eklendi.")

# Kullanıcıdan bilgi alma kısmı
isim = input("Öğrencinin ismi nedir? ").capitalize()  # İlk harfi büyük yap
ders = input("Hangi dersin notunu öğrenmek istiyorsunuz? (Matematik, Fizik, Kimya) ").capitalize()  # İlk harfi büyük yap

# Not sorgulama
not_sorgula(isim, ders)

# Notu güncellemek istiyor musunuz?
guncelle = input("Notu güncellemek ister misiniz? (E/H) ")
if guncelle.lower() == 'e':
    yeni_not = int(input("Yeni notu girin: "))
    not_guncelle(isim, ders, yeni_not)

# Yeni öğrenci eklemek ister misiniz?
yeni_ekle = input("Yeni öğrenci eklemek ister misiniz? (E/H) ")
if yeni_ekle.lower() == 'e':
    yeni_isim = input("Yeni öğrencinin ismi nedir? ").capitalize()
    matematik = int(input("Matematik notu: "))
    fizik = int(input("Fizik notu: "))
    kimya = int(input("Kimya notu: "))
    yeni_ogrenci_ekle(yeni_isim, matematik, fizik, kimya)

