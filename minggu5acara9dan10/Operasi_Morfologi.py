import cv2
import numpy as np
from skimage.morphology import skeletonize, thin
import matplotlib.pyplot as plt


# Baca gambar biner
img = cv2.imread('D:/KULIAH/Semester 5/Project_Python/Direktori_gambar/binary_image.png', 0) #pastikan gambar sudah biner 
_, binary_img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

binary_img = binary_img.astype(np.uint8)  # Pastikan tipe data biner sesuai

# kernel morfologi
kernel = np.ones((3,3), np.uint8)

# 1. Erosi
erosion = cv2.erode(binary_img, kernel, iterations=1)

# 2. Dilasi
dilation = cv2.dilate(binary_img, kernel, iterations=1)

# 3. Opening (erosi kemudian dilasi)
opening = cv2.morphologyEx(binary_img, cv2.MORPH_OPEN, kernel)

# 4. closing (dilasi kemudian erosi)
closing = cv2.morphologyEx(binary_img, cv2.MORPH_OPEN, kernel)

# 5. Hit-or-Miss
#Membuat kernel hit-or-miss (ada berbagai variasi)
kernel_hitmiss = np.array([[1, 1, 1],
                          [0, 1, 0],
                          [-1, -1, -1]])

hit_or_miss = cv2.morphologyEx(binary_img, cv2.MORPH_HITMISS, kernel_hitmiss)

# 6. Thinning (Penipisan)
thinned_img = thin(binary_img // 255) * 255 #menggunakan skimage

# 7. Thickening (Penebalan - tidak ada langsung di OpenCV, bisa dikombinasikan dengan operasi lain)
thickpening = cv2.dilate(binary_img, kernel, iterations=1) - erosion

# 8. Skeletonization (Kerangka)
skeleton = skeletonize(binary_img // 255) * 255 #menggunakan skimage

# 9. Pruning ( Pemangkasan - biasanya dilakukan pada krangka untuk menghilangkan cabang kecil)
# Pruning tidak ada  di OpenCv secara langsung, harus diimplementasikan menggunakan pendekatan sendiri.
# Berikut adalah langkah dasar untuk melakukan Prunning setelah skeletonization:

def prune_skeleton(skeleton_img, iterations=1):
    pruned_img = skeleton_img.copy().astype(np.uint8)  # Pastikan tipe data biner
    for _ in range(iterations):
        pruned_img = cv2.morphologyEx(pruned_img, cv2.MORPH_HITMISS, kernel_hitmiss)
    return pruned_img

pruned_skeleton = prune_skeleton(skeleton, iterations=2)

#Menampilkan hasil
# cv2.imshow('Original', binary_img)
# cv2.imshow('Erosion', erosion)
# cv2.imshow('Dilation', dilation)
# cv2.imshow('Opening', opening)
# cv2.imshow('Closing', closing)
# cv2.imshow('Hit-or-Miss', hit_or_miss)
# cv2.imshow('Thinning', thinned_img.astype(np.uint8))
# cv2.imshow('Skeleton', skeleton.astype(np.uint8))
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# Fungsi untuk menampilkan gambar menggunakan matplotlib
def show_image(title, img):
    plt.imshow(img, cmap='gray')
    plt.title(title)
    plt.axis('off')
    plt.show()

# Menampilkan gambar hasil menggunakan matplotlib
show_image('Original', binary_img)
show_image('Erosion', erosion)
show_image('Dilation', dilation)
show_image('Opening', opening)
show_image('Closing', closing)
show_image('Hit-or-Miss', hit_or_miss)
show_image('Thinning', thinned_img.astype(np.uint8))
show_image('Skeleton', skeleton.astype(np.uint8))