import numpy as np

# Fungsi untuk melakukan konvolusi 2D
def convolve2D(image, kernel):
    # Dimensi kernel
    kernel_height, kernel_width = kernel.shape
    # Dimensi Citra
    image_height, image_width = image.shape

    # Inisialisasi output array dengan ukuran yang sama dengan citra asli
    output = np.zeros((image_height, image_width))

    # Padding : tambahkan padding untuk mengatasi piksel di tepi citra
    pad_h = kernel_height // 2
    pad_w = kernel_width // 2

    # Buat citra dengan padding
    padded_image = np.pad(image, ((pad_h, pad_h), (pad_w, pad_w)), mode='constant', constant_values=0)

    # Lakukan konvolusi 
    for i in range(image_height):
        for j in range(image_width):
            # Ambil bagian dari citra (window) yang sesuai dengan kernal
            window = padded_image[i:i + kernel_height, j:j + kernel_width]
            # Hitung produk titik antara windowdan kernel, lalu jumlahkan 
            output[i, j] = np.sum(window * kernel)

    return output

# Contoh citra 5x5
image = np.array([
    [100, 120, 130, 140, 150],
    [110, 130, 140, 150, 160],
    [120, 140, 150, 160, 170],
    [130, 150, 160, 170, 180],
    [140, 160, 170, 180, 190]
])

# Kernel rata rata (Average filter) 3x3
kernel = np.array([
    [1/9, 1/9, 1/9],
    [1/9, 1/9, 1/9],
    [1/9, 1/9, 1/9]
])

# Lakukan konvolusi 
output_image = convolve2D(image, kernel)

print("Citra Asli:")
print(image)
print("\nCitra Hasil Konvolusi:")
print(output_image)