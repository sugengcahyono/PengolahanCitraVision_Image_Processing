import cv2
import matplotlib.pyplot as plt
import numpy as np

# Tentukan path citra
image1_path = 'D:/KULIAH/Semester 5/Project_Python/Direktori_gambar/traktor.jpg' 
image2_path = 'D:/KULIAH/Semester 5/Project_Python/Direktori_gambar/tomate.jpg'

# Membaca citra dari path (dalam format BGR)
image1 = cv2.imread(image1_path)
image2 = cv2.imread(image2_path)

# Menyamakan ukuran citra (resize citra kedua sesuai ukuran citra pertama)
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

# Operasi NAND (NOT AND)
nand_result = cv2.bitwise_not(and_result)

# Operasi NOT (Negasi citra 1)
not_image1 = cv2.bitwise_not(image1)

# Operasi NOR (NOT OR)
nor_result = cv2.bitwise_not(or_result)

# Operasi XNOR (NOT XOR)
xnor_result = cv2.bitwise_not(xor_result)

# Konversi hasil dari BGR ke RGB untuk ditampilkan dengan matplotlib
image1_rgb = cv2.cvtColor(image1, cv2.COLOR_BGR2RGB)
image2_rgb = cv2.cvtColor(image2, cv2.COLOR_BGR2RGB)
addition_result_rgb = cv2.cvtColor(addition_result, cv2.COLOR_BGR2RGB)
subtraction_result_rgb = cv2.cvtColor(subtraction_result, cv2.COLOR_BGR2RGB)
multiplication_result_rgb = cv2.cvtColor(multiplication_result, cv2.COLOR_BGR2RGB)
division_result_rgb = cv2.cvtColor(division_result, cv2.COLOR_BGR2RGB)
or_result_rgb = cv2.cvtColor(or_result, cv2.COLOR_BGR2RGB)
and_result_rgb = cv2.cvtColor(and_result, cv2.COLOR_BGR2RGB)
xor_result_rgb = cv2.cvtColor(xor_result, cv2.COLOR_BGR2RGB)
nand_result_rgb = cv2.cvtColor(nand_result, cv2.COLOR_BGR2RGB)
not_image1_rgb = cv2.cvtColor(not_image1, cv2.COLOR_BGR2RGB)
nor_result_rgb = cv2.cvtColor(nor_result, cv2.COLOR_BGR2RGB)
xnor_result_rgb = cv2.cvtColor(xnor_result, cv2.COLOR_BGR2RGB)

# Menampilkan hasil menggunakan matplotlib
plt.figure(figsize=(18, 10))

# Menampilkan citra pertama
plt.subplot(3, 4, 1)
plt.title("Citra 1")
plt.imshow(image1_rgb)
plt.axis('off')

# Menampilkan citra kedua
plt.subplot(3, 4, 2)
plt.title("Citra 2")
plt.imshow(image2_rgb)
plt.axis('off')

# Menampilkan hasil penjumlahan
plt.subplot(3, 4, 3)
plt.title("Penjumlahan")
plt.imshow(addition_result_rgb)
plt.axis('off')

# Menampilkan hasil Pengurangan
plt.subplot(3, 4, 4)
plt.title("Pengurangan")
plt.imshow(subtraction_result_rgb)
plt.axis('off')

# Menampilkan hasil perkalian
plt.subplot(3, 4, 5)
plt.title("Perkalian")
plt.imshow(multiplication_result_rgb)
plt.axis('off')

# Menampilkan hasil pembagian
plt.subplot(3, 4, 6)
plt.title("Pembagian")
plt.imshow(division_result_rgb)
plt.axis('off')

# Menampilkan hasil OR
plt.subplot(3, 4, 7)
plt.title("OR")
plt.imshow(or_result_rgb)
plt.axis('off')

# Menampilkan hasil AND
plt.subplot(3, 4, 8)
plt.title("AND")
plt.imshow(and_result_rgb)
plt.axis('off')

# Menampilkan hasil XOR
plt.subplot(3, 4, 9)
plt.title("XOR")
plt.imshow(xor_result_rgb)
plt.axis('off')

# Menampilkan hasil NAND
plt.subplot(3, 4, 10)
plt.title("NAND")
plt.imshow(nand_result_rgb)
plt.axis('off')

# Menampilkan hasil NOT
plt.subplot(3, 4, 11)
plt.title("NOT (Citra 1)")
plt.imshow(not_image1_rgb)
plt.axis('off')

# Menampilkan hasil NOR
plt.subplot(3, 4, 12)
plt.title("NOR")
plt.imshow(nor_result_rgb)
plt.axis('off')

# Menampilkan hasil XNOR
plt.figure(figsize=(7, 7))
plt.title("XNOR")
plt.imshow(xnor_result_rgb)
plt.axis('off')

plt.show()
