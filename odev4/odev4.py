##################################3
# Soru 1:Aşağıdaki işlemleri indexing ve slicing kullanarak liste üzerinde uygulayın.
#
# liste = ["Python",True,9,"3",8.4,"Hi-Kod","False",4.7]
#
# 1.1) "3" değerine ulaşmak için indexleme yapın.
#
# 1.2) "Hi-Kod" değerine ulaşmak için indexleme yapın.
#
# 1.3) 4.7 değerine ulaşmak için indexleme yapın.
#
# 1.4) 9,"3",8.4,"Hi-Kod" değerlerine ulaşmak için slicing yapın.
#
# 1.5) 8.4,"Hi-Kod","False",4.7 değerlerine ulaşmak için slicing yapın.
###################################

liste = ["Python", True, 9, "3", 8.4, "Hi-Kod", "False", 4.7]
#1.1
print(liste[3])  # "3"
#1.2
print(liste[5])  # "Hi-Kod"

#1.3
print(liste[7])  # 4.7

#1.4
print(liste[2:6])  # [9, "3", 8.4, "Hi-Kod"]

#1.5
print(liste[4:])  # [8.4, "Hi-Kod", "False", 4.7]

##################################3
# Soru 2: Verilen listede bulunan string veri tipindeki öğeleri yeni_liste isimli listeye eklenir.
#
# liste = ["Python",True,9,"3",8.4,"Hi-Kod","False",4.7]
###################################
yeni_liste = []

# String veri tipindeki öğeleri yeni_listeye ekleyelim
for eleman in liste:
    if isinstance(eleman, str):  # Eğer eleman bir string ise
        yeni_liste.append(eleman)

print(yeni_liste)



##################################3
# Soru 3:Enumerate methodunu araştırın ve aşağıdaki örneği enumerate methodu ile yapın.
#
# for index in range(len(meyveler)):
#
#     print("{}. indexte bulunan meyve: {}".format(index,meyveler[index])
###################################

meyveler = ["elma", "armut", "kiraz", "muz"]

for index, meyve in enumerate(meyveler):
    print("{}. indexte bulunan meyve: {}".format(index, meyve))
