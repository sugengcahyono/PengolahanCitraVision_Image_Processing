from PIL import Image

# Load image
image_path = 'D:/KULIAH/Semester 5/Project_Python/Direktori_gambar/tomate.jpg'
image = Image.open(image_path)

# Fungsi rotasi 
def rotate_image(image, angle):
    rotated_image = image.rotate(angle, expand=True)
    return rotated_image

# Melakukan rotasi gambar 90 derajat 
rotated = rotate_image(image, 90)

# Menyimpan hasil
rotated.save('rotated_image.jpg')
