import os
from PIL import Image

directory = 'D:/KULIAH/Semester 5/Project_Python/Direktori_gambar'
output_directory = 'D:/KULIAH/Semester 5/Project_Python/Hasil_gambar'

if not os.path.exists(output_directory):
    os.makedirs(output_directory)

for filename in os.listdir(directory):
    if filename.endswith(".jpg") or filename.endswith(".png"):
        img_path = os.path.join(directory, filename)
        img = Image.open(img_path)
        img_resized = img.resize((200, 200)) #ubah ukuran menjadi 200x200
        img_resized.save(os.path.join(output_directory, filename))