from PIL import Image

#Buka gambar 
img = Image.open("D:/KULIAH/Semester 5/Project_Python/Direktori_gambar/traktor.jpg")

# Konversi gambar ke grayscale dan simpan
img_gray = img.convert("L")
img_gray.save("D:/KULIAH/Semester 5/Project_Python/Hasil_gambar/Gray_Image/Gray_image.png")

#simpan gambar dengan kompresi maksimal (khusus untuk format png)
img.save("D:/KULIAH/Semester 5/Project_Python/Compressed/Gray_Image/Compressed_image.png", optimize=True)