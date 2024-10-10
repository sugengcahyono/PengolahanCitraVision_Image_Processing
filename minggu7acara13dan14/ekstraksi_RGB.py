import os
from PIL import Image
import pandas as pd

# fungsi untuk ekstraksi RGB dari gambar
def extract_rgb(image_path):
    # membuka gambar 
    img = Image.open(image_path)
    # mengkonversi gambar ke RGB (jika tidak dalam mode RGB)
    img = img.convert('RGB')

    # mendapatkan ukuran gambar 
    width, height = img.size
    rgb_data = []

    # mengakses tiap pixel gambar 
    for y in range(height):
        for x in range(width):
            r, g, b = img.getpixel((x,y))
            rgb_data.append([r, g, b])

    return rgb_data

# fungsi untuk memproses semua gambar dalam  folder dan menyimpan hasilnya ke excel
def process_images_in_folder(folder_path, output_excel_path):
    # memuat list untuk menyimpan data RGB dari semua gambar
    all_rgb_data = []

    # menjelajahi folder untuk menemukan file gambar
    for filename in os.listdir(folder_path):
        if filename.endswith(('.png', '.jpg', '.jpeg', '.bmp')): # memilih format gambar
            image_path = os.path.join(folder_path, filename)
            print(f"Memproses gambar: {filename}")
            rgb_data = extract_rgb(image_path)

            # menambahkan informasi gambar dan RGB ke list 
            for r, g, b in rgb_data:
                all_rgb_data.append({'Image': filename, 'R': r,'G': g, 'B': b})

    # membuat DataFrame dari data RGB
    df = pd.DataFrame(all_rgb_data)

    # menyimpan DataFrame ke file Excel
    df.to_excel(output_excel_path, index=False)
    print(f"Data RGB berhasil disimpan ke {output_excel_path}")

#D:\KULIAH\Semester 5\KULIAH\Workshop Pengolahan Citra dan Vision\Image_processing\PengolahanCitraVision_Image_Processing\Direktori_gambar\tomate.jpg
# Path folder bersisi gambar
folder_path = 'D:/KULIAH/Semester 5/KULIAH/Workshop Pengolahan Citra dan Vision/Image_processing/PengolahanCitraVision_Image_Processing/Direktori_gambar'
#path file Excel Output
output_excel_path = 'output.xlsx'

# Memproses gambar dan mengekstrak RGB
process_images_in_folder(folder_path, output_excel_path)

