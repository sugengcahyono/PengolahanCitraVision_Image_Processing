from PIL import Image

#Buka gambar
img = Image.open('D:/KULIAH/Semester 5/Project_Python/Direktori_gambar/traktor.jpg')

# Mengubah ukuran gambar menjadi 800x600 piksel dengan metode resampling LANCZOS
img_resized = img.resize((800, 600), Image.Resampling.LANCZOS)

# #ubah ukuran gambar
# img_resized = img.resize(800, 600) #mengubah ukuran menjadi 800x600 piksel

#simpan gambar yang diubah ukurannya
img_resized.save('D:/KULIAH/Semester 5/Project_Python/Hasil_gambar/Resized/resized_image1.jpg')

print("Gambar berhasil diubah ukurannya dan disimpan.")