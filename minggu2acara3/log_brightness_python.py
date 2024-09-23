import numpy as np
import cv2
import matplotlib.pyplot as plt

#membaca gambar dari direktori
image = cv2.imread('D:/KULIAH/Semester 5/Project_Python/Direktori_gambar/traktor.jpg', cv2.IMREAD_GRAYSCALE)

#tentukan konstanta c berdasarkan rumus 
c = 255 / np.log(1 + np.max(image))

#terapkan transformasi log brightness
log_transformed = c * np.log(1 + image)

#konversi hasil ke format uint8 (gambar 8 bit)
log_transformed = np.array(log_transformed, dtype=np.uint8)

#tampilkan gambar asli dan gambar setelah log brightness
plt.figure(figsize=(10, 4))

plt.subplot(1, 2, 1)
plt.title("Gambar Asli")
plt.imshow(image, cmap='gray', vmin=0, vmax=255)
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title("Setelah Log Brightness")
plt.imshow(log_transformed, cmap='gray', vmin=0, vmax=255)
plt.axis('off')

plt.show()