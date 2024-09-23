from PIL import Image
import numpy as np

#membuka Citra menggunakan PIL
image = Image.open('D:/KULIAH/Semester 5/Project_Python/Direktori_gambar/traktor.jpg')

#mengkonversi citra ke numpy array
image_np = np.array(image)

#implementasi metode Lightness
def rgb_to_grayscale_Lightness(image):
    max_rgb = np.max(image, axis=2)
    min_rgb = np.min(image, axis=2)
    return((max_rgb + min_rgb) / 2).astype(np.uint8)

#mengkonversi citra ke grayscale menggunakan metode Lightness 
grayscale_image = rgb_to_grayscale_Lightness(image_np)

#menyimpan citra grayscale
Image.fromarray(grayscale_image).save('grayscale_lightness.jpg')