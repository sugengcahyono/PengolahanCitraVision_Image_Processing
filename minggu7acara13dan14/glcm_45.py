import os
import cv2
import pandas as pd
import mahotas as mt

# Path ke folder gambar 
folder_path = 'D:/KULIAH/Semester 5/KULIAH/Workshop Pengolahan Citra dan Vision/Image_processing/PengolahanCitraVision_Image_Processing/Direktori_gambar'

# Buat list untuk menyimpan hasil 
data = []

# Fungsi untuk menghitung fitur GLCM dengan mahotas pada sudut tertentu (45 derajat)
def extract_glcm_features(image_gray):
    # Menghitung GLCM untuk empat sudut (0, 45, 90, 135 derajat) dan pilih sudut ke-45 (index ke-1)
    glcm = mt.features.haralick(image_gray)  # menghasilkan array fitur dari keempat sudut

    # Mengambil hasil dari sudut 45 derajat (index 1)
    glcm_at_45 = glcm[2]  # index ke-1 untuk sudut 45 derajat

    # Ekstraksi fitur yang kita perlukan dari GLCM sudut 45 derajat
    contrast = glcm_at_45[1]  # contrast
    homogeneity = glcm_at_45[4]  # homogeneity
    energy = glcm_at_45[8]  # energy
    correlation = glcm_at_45[2]  # correlation 

    return contrast, homogeneity, energy, correlation

# Iterasi melalui semua file dalam folder 
for index, filename in enumerate(os.listdir(folder_path)):
    if filename.endswith(('.png', '.jpg', '.jpeg')):  # Cek apakah file adalah gambar 
        img_path = os.path.join(folder_path, filename)
        img = cv2.imread(img_path)

        # Konversi gambar ke grayscale 
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Ekstraksi fitur GLCM pada sudut 45 derajat
        contrast, homogeneity, energy, correlation = extract_glcm_features(img_gray)

        # Tambahkan data ke list 
        data.append([index + 1, filename, contrast, homogeneity, energy, correlation])

# Buat DataFrame menggunakan pandas 
df = pd.DataFrame(data, columns=['No', 'Nama Gambar', 'Contrast', 'Homogenitas', 'Energi', 'Korelasi'])

# Simpan hasil ke file Excel 
output_path = 'output_Texture_Sudut_90.xlsx'
df.to_excel(output_path, index=False)
print(f'Hasil ekstraksi fitur GLCM untuk sudut 90 derajat telah disimpan di {output_path}')

