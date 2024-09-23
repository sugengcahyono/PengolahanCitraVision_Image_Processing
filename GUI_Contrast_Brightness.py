from PyQt5 import QtCore, QtGui, QtWidgets
from PIL import Image
import numpy as np

class LinearContrastBrightnessDialog(QtWidgets.QDialog):
    # Tambahkan sinyal untuk mengirim gambar hasil transformasi ke `main.py`
    imageProcessed = QtCore.pyqtSignal(object)

    def __init__(self, parent=None):
        if parent is not None and not isinstance(parent, QtWidgets.QWidget):
            raise TypeError("Parent must be of type QWidget or None")
        super().__init__(parent)
        self.setupUi()
        self.imagefile = None
        self.imageResult = None

    def setupUi(self):
        self.setObjectName("LinearContrastBrightnessDialog")
        self.resize(800, 300)
        
        # Label dan slider untuk kontras
        self.label_contrast = QtWidgets.QLabel(self)
        self.label_contrast.setGeometry(QtCore.QRect(30, 70, 151, 41))
        self.label_contrast.setText("Linear Contrast")

        self.horizontalSlider_contrast = QtWidgets.QSlider(self)
        self.horizontalSlider_contrast.setGeometry(QtCore.QRect(190, 80, 461, 22))
        self.horizontalSlider_contrast.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_contrast.setMinimum(-100)
        self.horizontalSlider_contrast.setMaximum(100)
        self.horizontalSlider_contrast.setValue(0)
        self.horizontalSlider_contrast.valueChanged.connect(self.update_line_edit_contrast)
        
        self.lineEdit_contrast = QtWidgets.QLineEdit(self)
        self.lineEdit_contrast.setGeometry(QtCore.QRect(670, 80, 113, 25))
        self.lineEdit_contrast.setText(str(self.horizontalSlider_contrast.value()))

        # Label dan slider untuk brightness
        self.label_brightness = QtWidgets.QLabel(self)
        self.label_brightness.setGeometry(QtCore.QRect(30, 120, 151, 41))
        self.label_brightness.setText("Linear Brightness")

        self.horizontalSlider_brightness = QtWidgets.QSlider(self)
        self.horizontalSlider_brightness.setGeometry(QtCore.QRect(190, 130, 461, 22))
        self.horizontalSlider_brightness.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_brightness.setMinimum(-255)
        self.horizontalSlider_brightness.setMaximum(255)
        self.horizontalSlider_brightness.setValue(0)
        self.horizontalSlider_brightness.valueChanged.connect(self.update_line_edit_brightness)
        
        self.lineEdit_brightness = QtWidgets.QLineEdit(self)
        self.lineEdit_brightness.setGeometry(QtCore.QRect(670, 130, 113, 25))
        self.lineEdit_brightness.setText(str(self.horizontalSlider_brightness.value()))

        # Tombol OK
        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(190, 190, 112, 34))
        self.pushButton.setText("OK")
        self.pushButton.clicked.connect(self.apply_contrast_brightness)

    def update_line_edit_contrast(self):
        self.lineEdit_contrast.setText(str(self.horizontalSlider_contrast.value()))

    def update_line_edit_brightness(self):
        self.lineEdit_brightness.setText(str(self.horizontalSlider_brightness.value()))

    def set_image(self, imagefile):
        self.imagefile = imagefile

    def apply_contrast_brightness(self):
        # Memastikan citra telah diatur
        if self.imagefile is None:
            QtWidgets.QMessageBox.warning(self, "No Image", "Please set an image first.")
            return
        
        # Membuka citra menggunakan PIL
        image = self.imagefile.convert('RGB')  # Konversi ke RGB (atau format asli yang diinginkan)

        # Dapatkan nilai dari slider untuk menyesuaikan kontras dan brightness
        contrast_value = self.horizontalSlider_contrast.value()
        brightness_value = self.horizontalSlider_brightness.value()

        # Terapkan transformasi linier kontras
        contrast_factor = 1 + (contrast_value / 100.0)
        img_np = np.array(image, dtype=np.float32)
        img_np = img_np * contrast_factor
        img_np = np.clip(img_np, 0, 255).astype(np.uint8)

        # Terapkan transformasi linier brightness
        img_np = img_np + brightness_value
        img_np = np.clip(img_np, 0, 255).astype(np.uint8)

        # Mengonversi array yang sudah diproses kembali menjadi gambar RGB
        linear_contrast_brightness_image = Image.fromarray(img_np)

        # Simpan hasil untuk keperluan save
        self.imageResult = linear_contrast_brightness_image

        # Emit sinyal dengan gambar hasil transformasi
        self.imageProcessed.emit(linear_contrast_brightness_image)

        # Tutup dialog setelah pemrosesan selesai
        self.close()
