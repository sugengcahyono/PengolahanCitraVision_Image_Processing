import os

# Tentukan path direktori
directori = 'C:/Users/LENOVO/Downloads' 

#List semua file dalam direktori
for filename in os.listdir(directori):
    if filename.endswith(".jpg") or filename.endswith(".png"):
        print(os.path.join(directori, filename))

        # Lakukan sesuatu dengan file gambar, seperti membukanya 

from PIL import Image

img = Image.open(os.path.join(directori, filename))
img.show()