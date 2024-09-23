

from PIL import Image

#Buka gambar yang ada 
img = Image.open('D:/KULIAH/Semester 5/Project_Python/Direktori_gambar/traktor.jpg')

#simpan gambar ke format lain, misalnya PNG
img.save('D:/KULIAH/Semester 5/Project_Python/Hasil_gambar/format_PNG/image.png')

#simpan gambar ke lokasi berbeda dengan nama yang sama 
img.save('D:/KULIAH/Semester 5/Project_Python/Hasil_gambar/formatsama(jpg)/new_image.jpg')

#simpan gambar dengan kualitas yang berbeda (khusus untuk format JPEG)
img.save("D:/KULIAH/Semester 5/Project_Python/Hasil_gambar/kualitasbeda/image_quality1.jpg", quality=85)