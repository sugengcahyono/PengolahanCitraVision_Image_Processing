import cv2
import os
import pandas as pd

# path ke folder gambar 
folder_path = 'D:/KULIAH/Semester 5/KULIAH/Workshop Pengolahan Citra dan Vision/Image_processing/PengolahanCitraVision_Image_Processing/Direktori_gambar'

# Buat list untuk menyimpan hasil
data = []

# iterasi melalui semua file dalam folder 
for index, filename in enumerate(os.listdir(folder_path)):
    if filename.endswith(('.png', '.jpg', '.jpeg')): # cek apakah file adalah gambar 
        img_path = os.path.join(folder_path, filename)
        img = cv2.imread(img_path)

        # ekstraksi nilai rata rata RGB
        avg_color_per_row = cv2.mean(img)[:3] # ambil 3 komponen pertama (R,G, B)
        R, G, B = avg_color_per_row

        # tambahkan data kelist 
        data.append([index + 1, filename, R, G, B])

#buat data Frame menggunaan pandas
df = pd.DataFrame(data, columns=['No', 'Nama', 'R', 'G', 'B'])

# simpan hasil ke file excel
output_path = 'output_ekstraksi.xlsx'
df.to_excel(output_path, index=False)

print(f'Hasil ekstraksi telah disimpan di {output_path}')