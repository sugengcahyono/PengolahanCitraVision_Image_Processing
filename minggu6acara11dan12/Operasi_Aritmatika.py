import cv2
import matplotlib.pyplot as plt
import numpy as np

# Tentukan path citra
image1_path = 'D:/KULIAH/Semester 5/Project_Python/Direktori_gambar/traktor.jpg' 
image2_path = 'D:/KULIAH/Semester 5/Project_Python/Direktori_gambar/tomate.jpg'

# Membaca citra dari path
image1 = cv2.imread(image1_path, cv2.IMREAD_GRAYSCALE)
image2 = cv2.imread(image2_path, cv2.IMREAD_GRAYSCALE)

# Menyamakan ukuran citra (resize citra kedua sesuai ukuran citra pertama
image2 = cv2.resize(image2, (image1.shape[1], image1.shape[0]))

# Penjumlahan citra
addition_result = cv2.add(image1, image2)

# Pengurangan citra
subtraction_result = cv2.subtract(image1, image2)

# Perkalian citra
multiplication_result = cv2.multiply(image1, image2)

# Pembagian citra (menghindari pembagian dengan nol)
with np.errstate(divide='ignore', invalid='ignore'):
    division_result = cv2.divide(image1.astype('float'), image2.astype('float'))
    division_result = np.nan_to_num(division_result).astype('uint8')


# Operasi OR
or_result = cv2.bitwise_or(image1, image2)

# Operasi AND
and_result = cv2.bitwise_and(image1, image2)

# Operasi XOR
xor_result = cv2.bitwise_xor(image1, image2)

# Menampilkan hasil menggunakan matplotlib
plt.figure(figsize=(14, 7))

# Menampilkan citra pertama 
plt.subplot(2, 4, 1)
plt.title("Citra 1")
plt.imshow(image1, cmap='gray', vmin=0, vmax=255)
plt.axis('off')


# Menampilkan citra kedua 
plt.subplot(2, 4, 2)
plt.title("Citra 2")
plt.imshow(image2, cmap='gray', vmin=0, vmax=255)
plt.axis('off')

# Menampilkan hasil penjumlahan 
plt.subplot(2, 4, 3)
plt.title("Penjumlahan")
plt.imshow(addition_result, cmap='gray', vmin=0, vmax=255)
plt.axis('off')


# Menampilkan hasil Pengurangan  
plt.subplot(2, 4, 4)
plt.title("Pengurangan")
plt.imshow(subtraction_result, cmap='gray', vmin=0, vmax=255)
plt.axis('off')

# Menampilkan hasil perkalian  
plt.subplot(2, 4, 5)
plt.title("Perkalian")
plt.imshow(multiplication_result, cmap='gray', vmin=0, vmax=255)
plt.axis('off')

# Menampilkan hasil pembagian 
plt.subplot(2, 4, 6)
plt.title("Pembagian")
plt.imshow(division_result, cmap='gray', vmin=0, vmax=255)
plt.axis('off')


# Menampilkan hasil OR 
plt.subplot(2, 4, 7)
plt.title("OR")
plt.imshow(or_result, cmap='gray', vmin=0, vmax=255)
plt.axis('off')


# Menampilkan hasil AND 
plt.subplot(2, 4, 8)
plt.title("AND")
plt.imshow(and_result, cmap='gray', vmin=0, vmax=255)
plt.axis('off')

# Menampilkan hasil XOR 
plt.figure(figsize=(7,7))
plt.title("XOR")
plt.imshow(xor_result, cmap='gray', vmin=0, vmax=255)
plt.axis('off')

plt.show()