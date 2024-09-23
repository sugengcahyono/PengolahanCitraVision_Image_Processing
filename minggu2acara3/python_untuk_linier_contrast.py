from PIL import Image
import numpy as np

def linier_contrast(input_image_path, output_image_path, contrast_factor): 
    # Membuka gambar 
    img = Image.open(input_image_path)

    # Mengubah gambar ke array numpy dengan tipe float32
    img_np = np.array(img, dtype=np.float32)

    # Mengalikan semua piksel dengan contrast_factor
    img_np = img_np * contrast_factor

    # Memastikan nilai piksel tetap dalam rentang [0, 255]
    img_np = np.clip(img_np, 0, 255).astype(np.uint8)

    # Mengubah array kembali ke gambar  
    img_out = Image.fromarray(img_np)

    # Menyimpan gambar hasil
    img_out.save(output_image_path)

# Contoh penggunaan 
linier_contrast('traktor.jpg', 'output_contrast.jpg', 1.2)
