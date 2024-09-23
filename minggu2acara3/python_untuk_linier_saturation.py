from PIL import Image  
import numpy as np

# Definisikan fungsi linear_saturation
def linear_saturation(input_image_path, output_image_path, saturation_factor):
    # Membuka gambar
    img = Image.open(input_image_path).convert('RGB')

    # Mengubah gambar menjadi array numpy dan mengubah ke ruang warna HSV
    img_np = np.array(img)
    img_hsv = Image.fromarray(img_np, 'RGB').convert('HSV')
    img_hsv_np = np.array(img_hsv, dtype=np.float32)

    # Meningkatkan komponen saturasi (channel S)
    img_hsv_np[..., 1] *= saturation_factor

    # Memastikan nilai piksel tetap dalam rentang [0, 255]
    img_hsv_np[..., 1] = np.clip(img_hsv_np[..., 1], 0, 255)

    # Mengubah array kembali ke gambar RGB 
    img_out = Image.fromarray(img_hsv_np.astype(np.uint8), 'HSV').convert('RGB')

    # Menyimpan gambar hasil 
    img_out.save(output_image_path)

# Contoh penggunaan
linear_saturation('traktor.jpg', 'output_saturation.jpg', 1.5)