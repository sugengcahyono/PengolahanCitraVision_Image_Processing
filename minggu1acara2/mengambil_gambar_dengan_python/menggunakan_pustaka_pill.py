from PIL import Image

# buka gambar dan tampilkan 
image_path = 'C:/Users/LENOVO/Downloads/downloadsd.jpg'
img = Image.open(image_path)
img.show()

# anda juga bisa memproses gambar disini,misal mengubah ukuran atau mengkonversi format 
img_resized = img.resize((100, 100))
img_resized.show()