#########################################################
# Soru 1 :  Değişkenlere atanmış değerlerin veri tipleri arasında dönüşüm yapılır.
#########################################################

# Değişkenlere atanmış değerler
x = 98  # int
y = 19.03  # float
z = "100"  # string

# Tip dönüşümleri
x_float = float(x)  # int to float
y_int = int(y)  # float to int
z_int = int(z)  # string to int

# Sonuçları yazdır
print(x_float)
print(y_int)
print(z_int)

#########################################################
# Soru 2 : İsimlerden oluşan üç değişkene yaş değerleri atanır.
# Belirlenen üç değişken birbiriyle karşılaştırma operatörleri ile karşılaştırılır.
# Bu karşılaştırmalara mantıksal operatörler de eklenir.
#########################################################

# İsimler ve yaşları
leyla_yas = 26
melek_yas = 24
mutlu_yas = 28


sonuc_1 = leyla_yas > melek_yas  # Leyla'nın yaşı Melek'in yaşından büyük mü?
sonuc_2 = mutlu_yas > leyla_yas  # Mutlu'nun yaşı Leyla'nın yaşından büyük mü?


sonuc_3 = (leyla_yas > melek_yas) and (mutlu_yas > leyla_yas)
sonuc_4 = (melek_yas < mutlu_yas) or (leyla_yas == mutlu_yas)

# Sonuçları yazdır
print(sonuc_1)
print(sonuc_2)
print(sonuc_3)
print(sonuc_4)


#########################################################
# Soru 3 : Kullanıcıdan iki değer girmesini istenir.
# Girilen değerlerin toplama, çıkarma, çarpma, bölme sonuçlarını yazdırılır.
#########################################################

# Kullanıcıdan iki değer al
deger1 = float(input("Birinci sayıyı girin: "))
deger2 = float(input("İkinci sayıyı girin: "))


toplam = deger1 + deger2
cikarma = deger1 - deger2
carpma = deger1 * deger2
bolme = deger1 / deger2


print("Toplama:", toplam)
print("Çıkarma:", cikarma)
print("Çarpma:", carpma)
print("Bölme:", bolme)




#########################################################
# Soru 4 : Kullanıcıdan isim, yaş, şehir ve meslek bilgilerini istenir ve cevaplarını yazdırılır.
#########################################################

# Kullanıcıdan bilgileri al
isim = input("Lütfen isminizi giriniz: ")
yas = input("Yaşınızı yazın: ")
sehir = input("Şehrinizi yazın: ")
meslek = input("Mesleğinizi yazın: ")

# Bilgileri ekrana yazdır
print("İsim: " + isim)
print("Yaş: " + yas)
print("Şehir: " + sehir)
print("Meslek: " + meslek)

#########################################################
# Soru 5 :"Hi-Kod Veri Bilimi Atölyesi" ifadesini bir değişkene tanımlanır.
#
# İfadedeki her bir kelimeyi ("Gelecek Hayalim: W-Code", "Veri", "Bilimi", "Atölyesi") değişken içinden seçilir.
#
# İfadeyi hepsini büyük harf olacak hale çevrilir. ("GELECEK HAYALİM: W-CODE VERİ BİLİMİ ATÖLYESİ")
#
# İfadeyi hepsini büyük harf olacak hale çevrilir.("gelecek hayalim: w-code veri bilimi atölyesi")
#
# "0123456789" ifadesindeki yalnızca çift sayıları ve yalnızca tek sayıları seçilir. ("02468", "13579")
#########################################################

# İfade değişkeni tanımlama
ifade = "Hi-Kod Veri Bilimi Atölyesi"

# İfadeden kelimeleri seçme
kelime1 = ifade.split()[0]  # "Hi-Kod"
kelime2 = ifade.split()[1]  # "Veri"
kelime3 = ifade.split()[2]  # "Bilimi"
kelime4 = ifade.split()[3]  # "Atölyesi"

#tek çıktı ile ifade etme (virgülle ayırma)
kelime5 = ifade.split()
print("Virgülle ayır: ", kelime5)
# İfadeyi tamamen büyük harflere çevirme
buyuk_harf = ifade.upper()

# İfadeyi tamamen küçük harflere çevirme
kucuk_harf = ifade.lower()

# Sonuçları yazdırma
print("Birinci kelime:", kelime1)
print("İkinci kelime:", kelime2)
print("Üçüncü kelime:", kelime3)
print("Dördüncü kelime:", kelime4)
print("Büyük harfli ifade:", buyuk_harf)
print("Küçük harfli ifade:", kucuk_harf)

#########################################################
# Soru 6 : "0123456789" ifadesindeki yalnızca çift sayıları ve yalnızca tek sayıları seçilir. ("02468", "13579")
#########################################################
# İfade tanımlama
sayi_dizisi = "0123456789"

# Çift sayılar
cift_sayilar = sayi_dizisi[0::2]  # 0'dan başlayıp iki atlayarak çift sayılar seçilir

# Tek sayılar
tek_sayilar = sayi_dizisi[1::2]  # 1'den başlayıp iki atlayarak tek sayılar seçilir

# Sonuçları yazdırma
print("Çift sayılar:", cift_sayilar)
print("Tek sayılar:", tek_sayilar)
