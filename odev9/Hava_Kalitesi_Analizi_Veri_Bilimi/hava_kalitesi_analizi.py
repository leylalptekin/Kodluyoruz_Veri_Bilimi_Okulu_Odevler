# Gerekli kütüphaneleri yükleme
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Rastgelelik için tohum değeri belirleme (sonuçları tekrar üretmek için)
np.random.seed(42)
# Veri setini Kaggle'dan yükleme
df = pd.read_csv('data_date.csv')

# Veri setinin ilk 5 satırına göz atalım
df.head()
# Veri setinin genel yapısı
df.info()

# Veri setindeki özet istatistikler
df.describe()

# Sütunlardaki benzersiz değerler
df.nunique()

# Eksik verileri kontrol etme
missing_values = df.isnull().sum()
print("Eksik veriler:\n", missing_values)

# Eksik verileri silme veya doldurma stratejileri
df_clean = df.dropna()  # Eksik verileri silmek

# Verinin tekrar incelenmesi
df_clean.info()

#eda
#PM10 seviyelerinin dağılımı

# PM10 seviyelerinin dağılımını inceleyelim
plt.figure(figsize=(10, 6))
sns.histplot(df_clean['AQI Value'], bins=30, kde=True)  # Value sütununu kullanıyoruz
plt.title('PM10 Seviyelerinin Dağılımı')
plt.xlabel('PM10 Değerleri')
plt.ylabel('Frekans')
plt.show()

#Ülkelere Göre AQI Değerlerinin Dağılımı

plt.figure(figsize=(12, 6))
sns.boxplot(x='Country', y='AQI Value', data=df_clean)
plt.title('Ülkelere Göre AQI Değerlerinin Dağılımı')
plt.xlabel('Ülke')
plt.ylabel('AQI Değeri')
plt.xticks(rotation=45)
plt.show()
# zaman serisi analizi
# Tarih sütununu datetime formatına çevir
df_clean['Date'] = pd.to_datetime(df_clean['Date'])

# Tarihe göre gruplama ve ortalama hesaplama
df_daily = df_clean.groupby(df_clean['Date'].dt.date)['AQI Value'].mean().reset_index()

# Zaman serisi grafiği oluşturma
plt.figure(figsize=(12, 6))
plt.plot(df_daily['Date'], df_daily['AQI Value'], marker='o', linestyle='-')
plt.title('Günlük Ortalama AQI Değerleri')
plt.xlabel('Tarih')
plt.ylabel('Ortalama AQI Değeri')
plt.xticks(rotation=45)
plt.grid()
plt.show()

#status'a göre AQI Dağılımı

plt.figure(figsize=(10, 6))
sns.histplot(df_clean, x='AQI Value', hue='Status', multiple='stack')
plt.title('AQI Değerlerinin Durumuna Göre Dağılımı')
plt.xlabel('AQI Değeri')
plt.ylabel('Frekans')
plt.show()



