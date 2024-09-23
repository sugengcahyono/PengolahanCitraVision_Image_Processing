import cv2
from matplotlib import pyplot as plt

# Fungsi untuk menampilkan histogram citra
def tampilkan_histogram_citra(image_path):
    # Membaca citra dari path direktori
    image = cv2.imread(image_path)

    # Konversi citra dari BGR ke RGB
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Memisahkan kanal warna
    colors = ('red', 'green', 'blue')

    plt.figure(figsize=(10, 5))
    plt.title('Histogram untuk setiap kanal warna')
    plt.xlabel('Intensitas pixel')
    plt.ylabel('Jumlah pixel')

    # Menghitung dan menampilkan histogram untuk setiap kanal warna
    for i, color in enumerate(colors):
        histogram = cv2.calcHist([image_rgb], [i], None, [256], [0, 256])
        plt.plot(histogram, color=color)
        plt.xlim([0, 256])

    # Menampilkan histogram
    plt.show()

# Path ke citra
path = 'D:/KULIAH/Semester 5/Project_Python/Direktori_gambar/tomate.jpg'

# Menampilkan histogram
tampilkan_histogram_citra(path)
