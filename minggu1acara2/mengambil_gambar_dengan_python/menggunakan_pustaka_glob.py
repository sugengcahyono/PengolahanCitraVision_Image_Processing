import glob

#ambil semua file .jpg didalam direktori
images = glob.glob('C:/Users/LENOVO/Downloads/*.jpg')

for image in images:
    print(image)

    #lakukan sesuatu dengan gambar 