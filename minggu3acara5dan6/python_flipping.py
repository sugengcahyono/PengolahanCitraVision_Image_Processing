from PIL import Image, ImageOps

# Load image
image_path = 'D:/KULIAH/Semester 5/Project_Python/Direktori_gambar/tomate.jpg'
image = Image.open(image_path)

# Fungsi flipping 
def flip_image(image, mode='horizontal'):
    if mode == 'horizontal':
        flipped_image = ImageOps.mirror(image)
    elif mode == 'vertical':
        flipped_image = ImageOps.flip(image)
    return flipped_image

# Melakukan rotasi gambar 90 derajat 
flipped_horizontal = flip_image(image, 'vertical')

# Menyimpan hasil
flipped_horizontal.save('flipped_horizontal.jpg')
