import cv2
import matplotlib.pyplot as plt
import numpy as np

# Tentukan path citra
image1_path = 'D:/KULIAH/Semester 5/Project_Python/Direktori_gambar/binary_image.png' 
image2_path = 'D:/KULIAH/Semester 5/Project_Python/Direktori_gambar/tomate.jpg'

# Membaca citra dari path dengan format berwarna
image1 = cv2.imread(image1_path, cv2.IMREAD_COLOR)
image2 = cv2.imread(image2_path, cv2.IMREAD_COLOR)

# Menyamakan ukuran citra (resize citra kedua sesuai ukuran citra pertama)
image2 = cv2.resize(image2, (image1.shape[1], image1.shape[0]))

# Fungsi untuk melakukan operasi pada setiap channel warna
def apply_operation_per_channel(image1, image2, operation):
    result = np.zeros_like(image1)
    for c in range(3):  # Untuk setiap channel (B, G, R)
        result[:, :, c] = operation(image1[:, :, c], image2[:, :, c])
    return result

# Penjumlahan citra
addition_result = apply_operation_per_channel(image1, image2, cv2.add)

# Pengurangan citra
subtraction_result = apply_operation_per_channel(image1, image2, cv2.subtract)

# Perkalian citra
multiplication_result = apply_operation_per_channel(image1, image2, cv2.multiply)

# Pembagian citra (menghindari pembagian dengan nol)
def safe_divide(img1, img2):
    with np.errstate(divide='ignore', invalid='ignore'):
        division = cv2.divide(img1.astype('float32'), img2.astype('float32'))
        return np.nan_to_num(division).astype('uint8')

division_result = apply_operation_per_channel(image1, image2, safe_divide)

# Operasi OR
or_result = apply_operation_per_channel(image1, image2, cv2.bitwise_or)

# Operasi AND
and_result = apply_operation_per_channel(image1, image2, cv2.bitwise_and)

# Operasi XOR
xor_result = apply_operation_per_channel(image1, image2, cv2.bitwise_xor)

# Menampilkan hasil menggunakan matplotlib
plt.figure(figsize=(14, 7))

# Menampilkan citra pertama 
plt.subplot(2, 4, 1)
plt.title("Citra 1")
plt.imshow(cv2.cvtColor(image1, cv2.COLOR_BGR2RGB))
plt.axis('off')

# Menampilkan citra kedua 
plt.subplot(2, 4, 2)
plt.title("Citra 2")
plt.imshow(cv2.cvtColor(image2, cv2.COLOR_BGR2RGB))
plt.axis('off')

# Menampilkan hasil penjumlahan 
plt.subplot(2, 4, 3)
plt.title("Penjumlahan")
plt.imshow(cv2.cvtColor(addition_result, cv2.COLOR_BGR2RGB))
plt.axis('off')

# Menampilkan hasil Pengurangan  
plt.subplot(2, 4, 4)
plt.title("Pengurangan")
plt.imshow(cv2.cvtColor(subtraction_result, cv2.COLOR_BGR2RGB))
plt.axis('off')

# Menampilkan hasil perkalian  
plt.subplot(2, 4, 5)
plt.title("Perkalian")
plt.imshow(cv2.cvtColor(multiplication_result, cv2.COLOR_BGR2RGB))
plt.axis('off')

# Menampilkan hasil pembagian 
plt.subplot(2, 4, 6)
plt.title("Pembagian")
plt.imshow(cv2.cvtColor(division_result, cv2.COLOR_BGR2RGB))
plt.axis('off')

# Menampilkan hasil OR 
plt.subplot(2, 4, 7)
plt.title("OR")
plt.imshow(cv2.cvtColor(or_result, cv2.COLOR_BGR2RGB))
plt.axis('off')

# Menampilkan hasil AND 
plt.subplot(2, 4, 8)
plt.title("AND")
plt.imshow(cv2.cvtColor(and_result, cv2.COLOR_BGR2RGB))
plt.axis('off')

# Menampilkan hasil XOR 
plt.figure(figsize=(7,7))
plt.title("XOR")
plt.imshow(cv2.cvtColor(xor_result, cv2.COLOR_BGR2RGB))
plt.axis('off')

plt.show()
