from PIL import Image, ImageOps

# Load image
image_path = 'D:/KULIAH/Semester 5/Project_Python/Direktori_gambar/tomate.jpg'
image = Image.open(image_path)

# definisi bounding box (kiri, kanan, atas Bawah)
left = 50
top = 100
right = 350
bottom = 250

#crop gambar
cropped_image = image.crop((left, top, right, bottom))

cropped_image.save('cropped_image.jpg')

#tampilkan gambar
cropped_image.show()
