import os
import cv2
import pandas as pd
import mahotas as mt


#path ke folder gambar 
folder_path = 'D:/KULIAH/Semester 5/KULIAH/Workshop Pengolahan Citra dan Vision/Image_processing/PengolahanCitraVision_Image_Processing/Direktori_gambar'

# buat list untuk menyimpan hasil 
data = []

# fungsi untuk menghitung fitur GLCM dengan mahotas 
def extract_glcm_features(image_gray):
    glcm = mt.features.haralick(image_gray).mean(axis=0) # bisa diganti derajat
    contrast = glcm[1] # contrast
    homogeneity = glcm[4] # homogeneity
    energy = glcm[8] # Energy
    correlation = glcm[2] #correlation 
    return contrast, homogeneity, energy, correlation

# iterasi melalui semua file dalam folder 
for index, filename in enumerate(os.listdir(folder_path)):
    if filename.endswith(('.png', '.jpg', '.jpeg')): # cek apakah file dalam gambar 
        img_path = os.path.join(folder_path, filename)
        img = cv2.imread(img_path)

        # konversi gambar ke grayscale 
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # ektraksi fitur glcm
        contrast, homogeneity, energy, correlation = extract_glcm_features(img_gray)

        #tambahkan data ke list 
        data.append([index +1, filename, contrast, homogeneity, energy, correlation])

# buat dataframe menggunakan pandas 
df = pd.DataFrame(data, columns=['No', 'Nama Gambar', 'Contrast', 'Homogenitas', 'Energi', 'Korelasi'])

# simpan hasil ke file excel 
output_path = 'output_Texture=45.xlsx'
df.to_excel(output_path, index=False)
print(f'hasil ekstraski fitur GLCM telah disimpan di {output_path}')
