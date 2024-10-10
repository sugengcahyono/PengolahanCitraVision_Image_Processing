import os
import numpy as np
import pandas as pd
from skimage import io, color
from skimage.feature import graycomatrix, graycoprops

# fungsi untuk ekstraksi fitur tekstur dari gambar menggunakan GLCM
def extract_glcm_features(image_path):
    # membaca gambar
    img = io.imread(image_path)

    # mengkonversi gambar ke grayscale (karena GLCM hanya bekerja pada gambar grayscale)
    if len(img.shape) == 3: # jika gambar berwara, konversi ke grayscale
        img_gray = color.rgb2gray(img)
        img_gray = (img_gray * 255).astype('uint8') # mengubah dari float [0,1] ke int [0,255]
    else:
        img_gray = img
    
    # menghitung GLCM ( Gray Level Co-occurence Matrix)
    # glcm = greycomatrix(img_gray, distances=[1], angles=[0, np.pi/4, np.pi/2, 3*np.pi/4], levels=256, symmetric=True, normed=True)
    glcm = graycomatrix(img_gray, distances=[1], angles=[0, np.pi/4, np.pi/2, 3*np.pi/4], levels=256, symmetric=True, normed=True)


    # Ekstraksi fitur teksture dari GLCM (contrast, dissimilarity, homogeneity, energy, correlation)
    features = {
        'contrast': graycomatrix(glcm, 'contrast').mean(),
        'dissimilarity': graycomatrix(glcm, 'dissimilarity').mean(),
        'homogeneity': graycomatrix(glcm, 'homogeneity').mean(),
        'energy': graycomatrix(glcm, 'energy').mean(),
        'correlation': graycomatrix(glcm, 'correlation').mean()
    }

    return features

# fungsi untuk memproses semua gambar dalam folder dan menyimpan hassilnya ke Excel
def process_images_for_glcm(folder_path, output_excel_path):
    all_texture_features = []

    # menjelajahi folder untuk menemukan file gambar 
    for filename in os.listdir(folder_path):
        if filename.endswith(('.png', '.jpg', '.jpeg', '.bmp')): # memilih format gambar
            image_path = os.path.join(folder_path, filename)
            print(f"Memproses gambar: {filename}")

            # ekstraksi fitur GLCM dari gambar
            features = extract_glcm_features(image_path)

            # menambah informasi gambar dan fitur tekstur ke list
            features['images'] = filename
            all_texture_features.append(features)

    # membuat DataFrame dari data teksture
    df = pd.DataFrame(all_texture_features)

    # menyimpan DataFrame ke file excel
    df.to_excel(output_excel_path,  index=False)
    print(f"Fitur teksture berhasil disimpan ke {output_excel_path}")


# path folder berisi gambar 
folder_path = 'D:/KULIAH/Semester 5/KULIAH/Workshop Pengolahan Citra dan Vision/Image_processing/PengolahanCitraVision_Image_Processing/Direktori_gambar'
#path excel output
output_excel_path = 'output_glcm_features.xlsx'

# memprose gambar dan mengekstrak fitur tekstur menggunakan GLCM
process_images_for_glcm(folder_path, output_excel_path)