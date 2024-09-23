import cv2
import numpy as np
import matplotlib.pyplot as plt

#membaca citra dari path
image_path = 'D:/KULIAH/Semester 5/Project_Python/Direktori_gambar/tomate.jpg'
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)# membaca gambar grayscale

# 1. Region Growing
def region_growing(img,seed_point, threshold):
    h, w = img.shape
    segmented = np.zeros((h,w), dtype=np.uint8)
    segmented[seed_point] = 255
    region_intensity = img[seed_point]

    to_check = [seed_point]

    while to_check :
        current_point = to_check.pop(0)
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                x,y = current_point[0]+ dx,current_point[1]+dy
                if 0 <= x < h and 0 <= y <w and segmented[x, y] == 0:
                    if abs(int(img[x,y]) - int(region_intensity)) <= threshold:
                        segmented[x, y] = 255
                        to_check.append((x,y))
    return segmented

seed = (10, 10)
threshold_value = 20
segmented_image = region_growing(image, seed, threshold_value)

# 2. K-Means Clustering (K =2)
def kmeans_clustering(image, k):
    pixel_values = image.reshape((-1, 1))
    pixel_values = np.float32(pixel_values)

    # definisikan kriteria untuk algoritma K-Means
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.2)
    _, labels, (centers) =  cv2.kmeans(pixel_values, k, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)

    #ubah label menjadi citra hasil klaster
    centers = np.uint8(centers)
    segmented_image = centers[labels.flatten()]
    segmented_image = segmented_image.reshape(image.shape)

    return segmented_image
segmented_image_kmeans = kmeans_clustering(image, 2)

# 3. watershed segmnetation
def watershed_segmentation(image):
    #meenggunakan thresholding untuk binerisasi
    _, thresh = cv2.threshold(image, 0, 255, cv2. THRESH_BINARY_INV + cv2.THRESH_OTSU)

    #menggunakan morfologi untuk menggunakan noise
    kernel = np.ones((3, 3), np.uint8)
    opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=2)

    #tentukan sre background dan sure foreground
    sure_bg = cv2.dilate(opening, kernel, iterations=3)
    dist_transform = cv2.distanceTransform(opening, cv2.DIST_L2, 5)
    _, sure_fg = cv2.threshold(dist_transform, 0.7 * dist_transform.max(), 255, 0)

    #label unknow region 
    sure_fg = np.uint8(sure_fg)
    unknown = cv2.subtract(sure_bg, sure_fg)

    #label marker
    _, markers = cv2.connectedComponents(sure_fg)
    markers = markers + 1
    markers[unknown == 255] = 0

    #watershed
    markers = cv2.watershed(cv2.cvtColor(image, cv2.COLOR_GRAY2BGR), markers)
    image[markers == -1] = [255] # garis watershed

    return image

watershed_image = watershed_segmentation(image)

#4. grolbal thresholding (T = 100)
def global_thresholding(image, threshold_value):
    _, binary_image = cv2.threshold(image, threshold_value, 255, cv2.THRESH_BINARY)
    return binary_image

global_threshold_image = global_thresholding(image, 100)


# 5. adaptive Thresholding
def adaptive_thesholding(image):
    adaptive_thresh_mean = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
    adaptive_thresh_gaussian = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
    
    return adaptive_thresh_mean, adaptive_thresh_gaussian

adaptive_thresh_mean, adaptive_thresh_gaussian = adaptive_thesholding(image)

#plot semua hasil secara bersamaan
plt.figure(figsize=(15, 10))

#original image
plt.subplot(3, 2, 1)
plt.imshow(image, cmap='gray')
plt.title('Original Image')

#Region Growing result
plt.subplot(3, 2, 2)
plt.imshow(segmented_image, cmap='gray')
plt.title('Region Growing')

#K-Means Clustering Result
plt.subplot(3, 2, 3)
plt.imshow(segmented_image_kmeans, cmap='gray')
plt.title('K-Means Clustering')

# watershed result
plt.subplot(3, 2, 4)
plt.imshow(watershed_image, cmap='gray')
plt.title('Watershed Segmentation')

# Global Tresholding result
plt.subplot(3, 2, 5)
plt.imshow(global_threshold_image, cmap='gray')
plt.title('Global Thresholding')

#adaptive Threshoding result
plt.subplot(3, 2, 6)
plt.imshow(adaptive_thresh_mean, cmap='gray')
plt.title('Adaptive Thresholding (Mean)')

plt.tight_layout()
plt.show()
