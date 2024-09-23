from PIL import Image
import numpy as np

#membuka Citra menggunakan PIL
image = Image.open('D:/KULIAH/Semester 5/Project_Python/Direktori_gambar/traktor.jpg')

#mengkonversi citra ke numpy array
image_np = np.array(image)

#implementasi metode Average
def rgb_to_grayscale_average(image):
    return np.mean(image, axis=2).astype(np.uint8)

#mengkonversi citra ke grayscale menggunakan metode average 
grayscale_image = rgb_to_grayscale_average(image_np)

#menyimpan citra grayscale
Image.fromarray(grayscale_image).save('grayscale_average.jpg')