from PIL import Image
import numpy as np

#membuka Citra menggunakan PIL
image = Image.open('D:/KULIAH/Semester 5/Project_Python/Direktori_gambar/traktor.jpg')

#mengkonversi citra ke numpy array
image_np = np.array(image)

#implementasi metode Luminance
def rgb_to_grayscale_Luminance(image):
    return (0.2989 * image[:,:,0] + 0.5870 * image[:,:,1] + 0.1140 * image[:,:,2]).astype(np.uint8)

#mengkonversi citra ke grayscale menggunakan metode Luminance 
grayscale_image = rgb_to_grayscale_Luminance(image_np)

#menyimpan citra grayscale
Image.fromarray(grayscale_image).save('grayscale_luminance.jpg')