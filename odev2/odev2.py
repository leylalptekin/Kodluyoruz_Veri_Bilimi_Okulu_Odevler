##########################################
# Soru 1:Ödev-1: Kullanıcıdan maaş bilgisini istenir ve bu bilgiye göre maaşından ne kadar vergi kesileceğini hesaplanır. Kullanıcının geliri;
#
#
#  10000 ve altındaysa maaşından %5 kesinti olur.
#  25000 ve altındaysa maaşından %10 kesinti olur.
#  45000 ve altındaysa maaşından %25 kesinti olur.
#  Diğer koşullarda %30 kesinti olur.
#
# Bu durumlara göre kullanıcının yeni maaşı yazdırılır.
##########################################


maas = float(input("Maaşınızı girin: "))

# Vergi kesintisini hesaplama
if maas <= 10000:
    kesinti = maas * 0.05
elif maas <= 25000:
    kesinti = maas * 0.10
elif maas <= 45000:
    kesinti = maas * 0.25
else:
    kesinti = maas * 0.30

# Yeni maaşı hesaplama
yeni_maas = maas - kesinti

# Sonuçları yazdırma
print("Kesilen vergi miktarı:", kesinti)
print("Yeni maaşınız:", yeni_maas)

##########################################
# Soru 2:  Kullanıcıdan kullanıcı adı ve şifre oluşturmasını istenir.
# Şifrenin uzunluğu altı haneye ulaşmışsa hesabınız oluşturuldu mesajı alınır,
# altı haneden azsa altı haneli şifre oluşturması gerektiğinin mesajı alınır. (Sadece koşul kullanılması yeterli.)
##########################################

# Kullanıcıdan şifre alma
sifre = input("Şifrenizi oluşturun (en az 6 karakter): ")

# Şifre uzunluğunu kontrol etme
if len(sifre) >= 6:
    print("Hesabınız oluşturuldu.")
else:
    print("Şifreniz en az 6 haneli olmalıdır.")


##########################################
# Soru 3: Bir önceki örnek geliştirilir.
#
#  Kullanıcı girdiği şifre 5 ve 10 hane arasında olmak zorunda.
#  Eğer bu koşula uyuyorsa "Hesabınız oluşturuldu." mesajı alır.
#  Koşulu sağlamıyorsa "Lütfen girdiniz şifre 5 haneden az 10 haneden fazla olmasın!" uyarısı alır.
#  Bunu oluştururken kullanıcı istediğimiz şartlarda şifre oluşturana kadar sormaya devam eder
##########################################


while True:

    sifre = input("Şifrenizi oluşturun (5-10 karakter arasında): ")


    if 5 <= len(sifre) <= 10:
        print("Hesabınız oluşturuldu.")
        break  # Döngüden çık
    else:
        print("Lütfen şifreniz 5 haneden az 10 haneden fazla olmasın!")


##########################################
# Soru 4:  Kullanıcıdan isim ve şifre isteyeceğiz ve şifre girişi için üç hak verilir.
#
#
#  Eğer önceden tanımlı şifre ile kullanıcıdan gelen şifre aynıysa "Giriş yapıldı." yazar.
#  Şifre girişi yanlışsa "Yanlış şifre girildi!" uyarısı verilsin ve üç yanlış denemede program biter.
#  Tercihe göre kalan hak bilgisi verilir. 
##########################################

# Önceden tanımlı şifre
dogru_sifre = "ruhucenet1234"


isim = input("İsminizi girin: ")
deneme_hakki = 3


while deneme_hakki > 0:
    kullanici_sifre = input("Şifrenizi girin: ")

    if kullanici_sifre == dogru_sifre:
        print("Giriş yapıldı.")
        break
    else:
        deneme_hakki -= 1  # Kalan deneme hakkını azalt
        print("Yanlış şifre girildi!")
        print("Kalan deneme hakkınız:", deneme_hakki)

# Tüm denemeler bittiğinde
if deneme_hakki == 0:
    print("Üç yanlış deneme yapıldı, program sonlandırılıyor.")
