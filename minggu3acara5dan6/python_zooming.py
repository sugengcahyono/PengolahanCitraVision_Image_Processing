from PIL import Image

# Load image
image_path = 'D:/KULIAH/Semester 5/Project_Python/Direktori_gambar/tomate.jpg'
image = Image.open(image_path)

# Fungsi zooming  
def zoom_image(image, zoom_factor):
    width, height = image.size
    zoomed_image = image.resize((int(width * zoom_factor), int(height * zoom_factor)))
    return zoomed_image

# Melakukan zoom gambar dg skala faktor 1.5
zoomed = zoom_image(image, 100)

# Menyimpan hasil
zoomed.save('zoomed_image.jpg')
