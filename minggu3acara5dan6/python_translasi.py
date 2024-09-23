from PIL import Image

# Load image
image_path = 'D:/KULIAH/Semester 5/Project_Python/Direktori_gambar/tomate.jpg'
image = Image.open(image_path)

# Fungsi translasi 
def translasi_image(image, x_shift, y_shift):
    width, height = image.size
    translasi_matrix = (1, 0, x_shift, 0, 1, y_shift)
    
    translated_image = image.transform((width, height), Image.AFFINE, translasi_matrix)
    return translated_image

# Melakukan translasi gambar
translated = translasi_image(image, 50, 50)

# Menyimpan hasil
translated.save('translated_image.jpg')
