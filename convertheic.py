import os
from PIL import Image
import pyheif

def convert_heic_to_jpg(input_folder, output_folder):
    # Pastikan folder output ada, jika tidak maka buat foldernya
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Loop melalui semua file di folder input
    for filename in os.listdir(input_folder):
        if filename.lower().endswith('.heic'):
            heic_file_path = os.path.join(input_folder, filename)
            
            # Baca file HEIC menggunakan pyheif
            heif_file = pyheif.read(heic_file_path)
            
            # Konversi HEIC ke format yang didukung PIL
            image = Image.frombytes(
                heif_file.mode, 
                heif_file.size, 
                heif_file.data,
                "raw", 
                heif_file.mode, 
                heif_file.stride,
            )

            # Simpan file sebagai JPG di folder output
            jpg_filename = os.path.splitext(filename)[0] + ".jpg"
            jpg_file_path = os.path.join(output_folder, jpg_filename)
            image.save(jpg_file_path, "JPEG")
            print(f"Converted: {filename} -> {jpg_filename}")

# Path folder input dan output
input_folder = "path/to/input/folder"  # Ganti dengan path folder input Anda
output_folder = "path/to/output/folder"  # Ganti dengan path folder output Anda

# Panggil fungsi untuk konversi
convert_heic_to_jpg(input_folder, output_folder)
