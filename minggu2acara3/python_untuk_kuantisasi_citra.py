import numpy as np
import cv2
import matplotlib.pyplot as plt

# membaca gambar grayscale dari direktori
image = cv2.imread('D:/KULIAH/Semester 5/Project_Python/Direktori_gambar/traktor.jpg', cv2.IMREAD_GRAYSCALE)

# tentukan jumlah level kuantisasi
level = 4

# menentukan interval kuantisasi
interval_size = 256 // level
intervals = [i * interval_size for i in range(level)]
mid_values = [((i * interval_size) + ((i + 1) * interval_size - 1)) // 2 for i in range (level)]

# fungsi kuantisasi manual
def quantize (image, intervals, mid_values):
    quantized_image = np.zeros_like(image)
    for i in range(len(intervals)):
        lower_bound = intervals[i]
        upper_bound = lower_bound + interval_size - 1
        maks = (image >= lower_bound) & (image <= upper_bound)
        quantized_image[maks] = mid_values[i]
    return quantized_image

# terapkan kuantisasi
quantized_image = quantize(image, intervals, mid_values)

# tampilkan gambar asli 
plt.figure(figsize=(10,4))

plt.subplot(1, 2, 1)
plt.title("gambar asli")
plt.imshow(image, cmap='gray', vmin=0, vmax=255)
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title("setelah kuantisasi")
plt.imshow(quantized_image, cmap='gray', vmin=0, vmax=255)
plt.axis('off')

plt.show()