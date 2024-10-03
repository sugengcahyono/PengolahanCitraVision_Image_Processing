import numpy as np
import cv2
import matplotlib.pyplot as plt

# Mengambil gambar dari path dengan warna asli (BGR)
image_path = 'D:/KULIAH/Semester 5/Project_Python/Direktori_gambar/tomate.jpg'  # Ganti dengan path gambar Anda
image_example = cv2.imread(image_path, cv2.IMREAD_COLOR)

# Konversi dari BGR (OpenCV) ke RGB (untuk tampilan yang benar di Matplotlib)
image_example_rgb = cv2.cvtColor(image_example, cv2.COLOR_BGR2RGB)

# Fungsi untuk menerapkan kernel pada gambar
def apply_kernel(image, kernel):
    return cv2.filter2D(image, -1, kernel)

# Kernel predefined (dapat diganti secara manual)
kernels = {
    'identity': np.array([[0, 0, 0], [0, 1, 0], [0, 0, 0]]),
    'edge_detection_1': np.array([[1, 0, -1], [0, 0, 0], [-1, 0, 1]]),
    'edge_detection_2': np.array([[0, 1, 0], [1, -4, 1], [0, 1, 0]]),
    'edge_detection_3': np.array([[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]]),
    'sharpen': np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]]),
    'gaussian_blur_3x3': np.array([[1, 2, 1], [2, 4, 2], [1, 2, 1]]) / 16,
    'gaussian_blur_5x5': np.array([[1, 4, 6, 4, 1],
                                   [4, 16, 24, 16, 4],
                                   [6, 24, 36, 24, 6],
                                   [4, 16, 24, 16, 4],
                                   [1, 4, 6, 4, 1]]) / 256,
    'unsharp_masking': (-1/256) * np.array([[1, 4, 6, 4, 1],
                                 [4, 16, 24, 16, 4],
                                 [6, 24, -476, 24, 6],
                                 [4, 16, 24, 16, 4],
                                 [1, 4, 6, 4, 1]]),
    # Average Filter
    'average': np.ones((5, 5), np.float32) / 25,
    
    # Low Pass Filter (sama seperti average tapi bisa digunakan sebagai low-pass sederhana)
    'low_pass': np.ones((3, 3), np.float32) / 9,
    
    # Bandstop filter sederhana (kombinasi dari low-pass dan high-pass)
    'bandstop': np.array([[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]]) + np.ones((3, 3)) / 9
}

# Terapkan kernel pada gambar
identity_result = apply_kernel(image_example, kernels['identity'])
edge_result_1 = apply_kernel(image_example, kernels['edge_detection_1'])
edge_result_2 = apply_kernel(image_example, kernels['edge_detection_2'])
edge_result_3 = apply_kernel(image_example, kernels['edge_detection_3'])
sharpen_result = apply_kernel(image_example, kernels['sharpen'])
gaussian_blur3 = apply_kernel(image_example, kernels['gaussian_blur_3x3'])
gaussian_blur5 = apply_kernel(image_example, kernels['gaussian_blur_5x5'])
unsharp_masking = apply_kernel(image_example, kernels['unsharp_masking'])

# Filter baru
average_result = apply_kernel(image_example, kernels['average'])
low_pass_result = apply_kernel(image_example, kernels['low_pass'])
bandstop_result = apply_kernel(image_example, kernels['bandstop'])

# Visualisasi hasil dari kernel yang diterapkan
plt.figure(figsize=(15, 10))

# Tampilkan gambar asli 
plt.subplot(3, 4, 1)
plt.title("Gambar Asli")
plt.imshow(image_example_rgb)
plt.axis('off')

# Tampilkan hasil identity
plt.subplot(3, 4, 2)
plt.title("Identity")
plt.imshow(cv2.cvtColor(identity_result, cv2.COLOR_BGR2RGB))
plt.axis('off')

# Tampilkan hasil edge detection 1
plt.subplot(3, 4, 3)
plt.title("Edge Detection 1")
plt.imshow(cv2.cvtColor(edge_result_1, cv2.COLOR_BGR2RGB))
plt.axis('off')

# Tampilkan hasil edge detection 2
plt.subplot(3, 4, 4)
plt.title("Edge Detection 2")
plt.imshow(cv2.cvtColor(edge_result_2, cv2.COLOR_BGR2RGB))
plt.axis('off')

# Tampilkan hasil edge detection 3
plt.subplot(3, 4, 5)
plt.title("Edge Detection 3")
plt.imshow(cv2.cvtColor(edge_result_3, cv2.COLOR_BGR2RGB))
plt.axis('off')

# Tampilkan hasil sharpen
plt.subplot(3, 4, 6)
plt.title("Sharpen")
plt.imshow(cv2.cvtColor(sharpen_result, cv2.COLOR_BGR2RGB))
plt.axis('off')

# Tampilkan hasil gaussian blur 3x3
plt.subplot(3, 4, 7)
plt.title("Gaussian Blur 3x3")
plt.imshow(cv2.cvtColor(gaussian_blur3, cv2.COLOR_BGR2RGB))
plt.axis('off')

# Tampilkan hasil gaussian blur 5x5
plt.subplot(3, 4, 8)
plt.title("Gaussian Blur 5x5")
plt.imshow(cv2.cvtColor(gaussian_blur5, cv2.COLOR_BGR2RGB))
plt.axis('off')

# Tampilkan hasil unsharp masking
plt.subplot(3, 4, 9)
plt.title("Unsharp Masking")
plt.imshow(cv2.cvtColor(unsharp_masking, cv2.COLOR_BGR2RGB))
plt.axis('off')

# Tampilkan hasil average filter
plt.subplot(3, 4, 10)
plt.title("Average Filter")
plt.imshow(cv2.cvtColor(average_result, cv2.COLOR_BGR2RGB))
plt.axis('off')

# Tampilkan hasil low pass filter
plt.subplot(3, 4, 11)
plt.title("Low Pass Filter")
plt.imshow(cv2.cvtColor(low_pass_result, cv2.COLOR_BGR2RGB))
plt.axis('off')

# Tampilkan hasil bandstop filter
plt.subplot(3, 4, 12)
plt.title("Bandstop Filter")
plt.imshow(cv2.cvtColor(bandstop_result, cv2.COLOR_BGR2RGB))
plt.axis('off')

plt.show()
