import cv2
import numpy as np

# contoh citra 5x5
image = np.array([
    [100, 120, 130, 140, 150],
    [110, 130, 150, 170, 160],
    [120, 140, 160, 180, 170],
    [130, 150, 170, 190, 180],
    [140, 160, 180, 200, 190]
], dtype=np.float32)

# Kernel rata rata (Average filter) 3x3
kernel = np.ones((3, 3), np.float32) / 9

# Lakukan konvolusi menggunakan openCV
output_image = cv2.filter2D(image, -1, kernel)

print("Citra Asli:")
print(image)
print("\nHasil konvolusi dengan openCV:")
print(output_image)