import pandas as pd

#############################################
# Soru1:
#   sozluk = {"Kategori": ["Giyim","Giyim", "Ayakkabı","Aksesuar","Ayakkabı","Giyim","Aksesuar","Aksesuar","Ayakkabı","Giyim"],
#
#
#   "Ürün" : ["Kazak","T-shirt","Sandalet","Küpe","Spor Ayakkabı","Pantolon","Kolye","Yüzük","Çizme","Ceket"],
#
#
# "Fiyat" : [300,180,450,50,700,400,150,80,850,900]}
#
#
#  Yukarıdaki sözlük DataFrame’e dönüştürülür.
#  Yukarıdaki DataFrame için
#
#  2.indexte bulunan kategori bulunur. (Sadece kategori bilgisi)
#  2. indexte bulunan ürün bulunur. (Sadece ürün bilgisi)
#  4.indexten 9.indexe kadar olan veriler bulunur. (Kategori,ürün,fiyat bilgisi beraber)
#  1.indexten 6.indexe kadar olan ürünler bulunur. (Sadece ürün bilgisi)
#
#  Yukarıdaki DataFrame için
#
#  Giyim kategorisinde bulunan ürünler gösterilir.
#  Ayakkabı kategorisinde bulunan ürünler gösterilir.
#  Aksesuar kategorisinde bulunan ürünler gösterilir.
#
#  Yukarıdaki DataFrame için
#
#  Giyim kategorisinde fiyatı 300'den fazla olan ürünler gösterilir.
#  Ayakkabı kategorisinde fiyatı 600'den az olan ürünler gösterilir.
#  Aksesuar kategorisinde fiyatı 100'den fazla olan aksesuar gösterilir.
#############################################


# Sözlüğü pandas DataFrame'e dönüştür
sozluk = {"Kategori": ["Giyim","Giyim", "Ayakkabı","Aksesuar","Ayakkabı","Giyim","Aksesuar","Aksesuar","Ayakkabı","Giyim"],
          "Ürün" : ["Kazak","T-shirt","Sandalet","Küpe","Spor Ayakkabı","Pantolon","Kolye","Yüzük","Çizme","Ceket"],
          "Fiyat" : [300,180,450,50,700,400,150,80,850,900]}

df = pd.DataFrame(sozluk)
print(df)

#  2.indexte bulunan kategori bulunur. (Sadece kategori bilgisi)

kategori_2 = df.loc[2, 'Kategori']
print(kategori_2)

#  2. indexte bulunan ürün bulunur. (Sadece ürün bilgisi)

urun_2 = df.loc[2, 'Ürün']
print(urun_2)

#  4.indexten 9.indexe kadar olan veriler bulunur. (Kategori,ürün,fiyat bilgisi beraber)

veriler_4_9 = df.loc[4:9, ['Kategori', 'Ürün', 'Fiyat']]
print(veriler_4_9)

#  1.indexten 6.indexe kadar olan ürünler bulunur. (Sadece ürün bilgisi)

urunler_1_6 = df.loc[1:6, 'Ürün']
print(urunler_1_6)

#  Giyim kategorisinde bulunan ürünler gösterilir.

giyim_urunler = df[df['Kategori'] == 'Giyim']
print(giyim_urunler)

#  Ayakkabı kategorisinde bulunan ürünler gösterilir.

ayakkabi_urunler = df[df['Kategori'] == 'Ayakkabı']
print(ayakkabi_urunler)

#  Aksesuar kategorisinde bulunan ürünler gösterilir.

aksesuar_urunler = df[df['Kategori'] == 'Aksesuar']
print(aksesuar_urunler)

#  Giyim kategorisinde fiyatı 300'den fazla olan ürünler gösterilir.

giyim_300_fazla = df[(df['Kategori'] == 'Giyim') & (df['Fiyat'] > 300)]
print(giyim_300_fazla)

#  Ayakkabı kategorisinde fiyatı 600'den az olan ürünler gösterilir.

ayakkabi_600_az = df[(df['Kategori'] == 'Ayakkabı') & (df['Fiyat'] < 600)]
print(ayakkabi_600_az)

#  Aksesuar kategorisinde fiyatı 100'den fazla olan aksesuar gösterilir.

aksesuar_100_fazla = df[(df['Kategori'] == 'Aksesuar') & (df['Fiyat'] > 100)]
print(aksesuar_100_fazla)
