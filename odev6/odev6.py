import numpy as np
##############################################
# Soru 1: Sayılardan oluşan bir boyutlu array oluşturulur.
# Arrayi oluştururken sayıların veri tipini integer olarak belirtilir.
# Oluşturulan arrayin boyut, eleman sayısı bilgilerine bakılır.
#############################################

# Tek boyutlu bir array oluşturma, elemanlar integer olacak şekilde
arr = np.array([1, 2, 3, 4, 5], dtype=int)

# Arrayin boyutuna ve eleman sayısına bakma
print("Array:", arr)
print("Boyut:", arr.ndim)
print("Eleman sayısı:", arr.size)

##############################################
# Soru 2: İki ve üç boyutlu arrayler oluşturulur.
# Bu arraylerin boyut, eleman sayısı, satır, sütun bilgilerine ulaşılır.
# Arrayler üzerinde indexleme ve dilimleme(slicing) işlemi yapılır.
#############################################
# İki boyutlu array oluşturma
arr2d = np.array([[1, 2, 3], [4, 5, 6]], dtype=int)
print("İki boyutlu array:")
print(arr2d)
print("Boyut:", arr2d.ndim)
print("Eleman sayısı:", arr2d.size)
print("Satır sayısı:", arr2d.shape[0])
print("Sütun sayısı:", arr2d.shape[1])

# Üç boyutlu array oluşturma
arr3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]], dtype=int)
print("\nÜç boyutlu array:")
print(arr3d)
print("Boyut:", arr3d.ndim)
print("Eleman sayısı:", arr3d.size)
print("Boyut bilgisi (satır, sütun, derinlik):", arr3d.shape)

##############################################
# Soru 3:Numpy fonksiyonu kullanarak bir, iki ve üç boyutlu arrayler oluşturulur.
# Arrayler üzerinde indexleme ve dilimleme(slicing) işlemi yapılır
#############################################
# İki boyutlu arrayde slicing
print("\nİki boyutlu array'den dilimleme (1. satır, tüm sütunlar):")
print(arr2d[1, :])  # 1. satırın tamamı

# Üç boyutlu arrayde slicing
print("\nÜç boyutlu array'den dilimleme (1. boyut, 0. satır, tüm sütunlar):")
print(arr3d[0, 0, :])  # 1. boyut, 0. satır, tüm sütunlar


##############################################
# Soru 4:Sıfırlardan oluşan ve birlerden oluşan iki tane iki boyutlu array oluşturulur.
# Bu arrayler satır ve sütun bazında birleştirilir.
#############################################

# Sıfırlardan oluşan 2 boyutlu array
zero_array = np.zeros((2, 3), dtype=int)

# Birlerden oluşan 2 boyutlu array
one_array = np.ones((2, 3), dtype=int)

# Satır bazında birleştirme
concat_row = np.vstack((zero_array, one_array))
print("\nSatır bazında birleştirilmiş array:")
print(concat_row)

# Sütun bazında birleştirme
concat_col = np.hstack((zero_array, one_array))
print("\nSütun bazında birleştirilmiş array:")
print(concat_col)
