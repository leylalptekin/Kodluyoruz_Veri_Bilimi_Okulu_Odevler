import math

#########################################
# Soru 1:  Kullanıcıdan pi değeri ve yarıçap bilgisi alarak
# dairenin alanını hesaplayan bir fonksiyon oluşturulur.
#########################################

def daire_alani(pi_degeri, yaricap):
    alan = pi_degeri * (yaricap ** 2)
    return "Dairenin alanı: " + str(round(alan, 2))

# Kullanıcıdan pi ve yarıçap bilgisi al
pi = float(input("Pi değeri: "))
yaricap = float(input("Yarıçap: "))
print(daire_alani(pi, yaricap))


#########################################
# Soru 2:  Faktöriyel adında fonksiyon oluşturulur.
# Döngü kullanarak parametre olarak girilen sayının faktöriyeli hesaplanır.
# Format metodunu kullanılarak ekrana yazdırılır.
#########################################
def faktoriyel(sayi):
    sonuc = 1
    for i in range(1, sayi + 1):
        sonuc *= i
    print(f"{sayi}! = {sonuc}")

# Kullanıcıdan sayı al
sayi = int(input("Faktöriyelini almak istediğiniz sayı: "))
faktoriyel(sayi)

#########################################
# Soru 3:Kişinin fonksiyona doğum yılını vererek kaç yaşında olduğunu hesaplayan bir fonksiyon oluşturun.
#########################################

def yas_hesapla(dogum_yili):
    mevcut_yil = 2024  # Yaş hesabı için mevcut yıl
    yas = mevcut_yil - dogum_yili
    return yas

# Kullanıcıdan doğum yılı al
dogum_yili = int(input("Doğum yılınız: "))
print(f"Yaşınız: {yas_hesapla(dogum_yili)}")



#########################################
# Soru 4: Doğum yılı ve isim bilgisi verilen fonksiyon kişinin emekli olup olmadığını söylesin.
# (Kişi 65 yaşında ise emekli olur.) Burada yaş hesabını yukarıdaki örnekteki fonksiyonu kullanarak yapsın.
# (Yani fonksiyon içinde fonksiyon kullanmanızı istiyorum :)) Kişi 65 yaşında ya da daha fazlaysa "Emekli oldunuz" yanıtını,
# 65 yaşından küçükse emekliliğine kaç yıl kaldığını da hesaplayarak "(isim) emekliliğine (yıl) kaldı." yanıtını versin.
#########################################

def yas_hesapla(dogum_yili):
    mevcut_yil = 2024
    yas = mevcut_yil - dogum_yili
    return yas

def emeklilik_sorgula(isim, dogum_yili):
    yas = yas_hesapla(dogum_yili)
    if yas >= 65:
        print(f"{isim}, emekli oldunuz.")
    else:
        emeklilik_yili = 65 - yas
        print(f"{isim}, emekliliğinize {emeklilik_yili} yıl kaldı.")

# Kullanıcıdan isim ve doğum yılı al
isim = input("İsminiz: ")
dogum_yili = int(input("Doğum yılınız: "))
emeklilik_sorgula(isim, dogum_yili)
