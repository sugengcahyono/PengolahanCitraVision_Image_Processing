from PIL import Image 
import numpy as np

def linier_brightness(input_image_path, output_image_path, brightness_factor):
    # Membuka gambar
    img = Image.open(input_image_path)

    # Mengubah gambar ke array numpy
    img_np = np.array(img, dtype=np.int16)

    # Menambahkan brightness_factor ke semua piksel
    img_np = img_np + brightness_factor

    # Memastikan nilai piksel tetap dalam rentan [0, 255]
    img_np = np.clip(img_np, 0, 255).astype(np.uint8)

    # Mengubah array kembali ke gambar
    img_out = Image.fromarray(img_np)

    # Menyimpan gambar hasil
    img_out.save(output_image_path)

# Contoh penggunaan
linier_brightness('traktor.jpg', 'output_brightness.jpg', -100)
