import numpy as np
import cv2
import matplotlib.pyplot as plt
from skimage import data

#mengambil gambar contoh dari skimage
image_example = data.camera()

#Terapkan deteksi tepi sobel 
sobel_x = cv2.Sobel(image_example, cv2.CV_64F, 1, 0, ksize=3) # Gradien Horizontal
sobel_y = cv2.Sobel(image_example, cv2.CV_64F, 0, 1, ksize=3) #Gradien vertikal
sobel_combined = cv2.magnitude(sobel_x, sobel_y)

#terapkan deteksi tepi Prewitt secar manual 
prewitt_x = cv2.filter2D(image_example, -1, np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]]))
prewitt_y = cv2.filter2D(image_example, -1, np.array([[1, 1, 1,], [0, 0, 0], [-1, -1, -1]]))
prewitt_combined = np.sqrt(np.square(prewitt_x) + np.square(prewitt_y))

# Terapkan deteksi tepi canny
canny_edges = cv2.Canny(image_example, 100, 200)

#visualisasi hasil dari sobel, Prewitt dan Canny
plt.figure(figsize=(15, 10))

# tampilkan gambar asli 
plt.subplot(2, 2, 1)
plt.title("Gambar asli")
plt.imshow(image_example, cmap='gray')
plt.axis('off')

#Tampilkan hasil deteksi tepi sobel 
plt.subplot(2, 2, 2)
plt.title("Deteksi Tepi (Sobel)")
plt.imshow(sobel_combined, cmap='gray')
plt.axis('off')

#Tampilkan hasil deteksi tepi prewitt 
plt.subplot(2, 2, 3)
plt.title("Deteksi Tepi (prewitt)")
plt.imshow(prewitt_combined, cmap='gray')
plt.axis('off')

#tampilkan hasil deteksi tepi canny
plt.subplot(2, 2, 4)
plt.title("Deteksi Tepi (Canny)")
plt.imshow(canny_edges, cmap='gray')
plt.axis('off')

plt.show()