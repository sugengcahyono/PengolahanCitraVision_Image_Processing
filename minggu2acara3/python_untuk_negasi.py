from PIL import Image
import numpy as np

def inverse(input_gambar_path, output_gambar_path):
    # Membuka gambar
    img = Image.open(input_gambar_path)

    # Mengubah gambar ke array numpy
    img_np = np.array(img)

    # Melakukan invers pada nilai piksel
    img_np = 255 - img_np

    # Mengubah array kembali ke gambar
    img_out = Image.fromarray(img_np.astype(np.uint8))

    # Menyimpan gambar hasil
    img_out.save(output_gambar_path)

# Contoh penggunaan
inverse('traktor.jpg', 'output_inverse.jpg')