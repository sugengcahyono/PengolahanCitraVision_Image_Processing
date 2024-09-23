from PyQt5 import QtCore, QtGui, QtWidgets
from PIL import Image
import numpy as np

class LogBrightnessDialog(QtWidgets.QDialog):
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
        self.setObjectName("LogBrightnessDialog")
        self.resize(800, 300)
        
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(30, 70, 151, 41))
        self.label.setText("Log Brightness")

        self.horizontalSlider = QtWidgets.QSlider(self)
        self.horizontalSlider.setGeometry(QtCore.QRect(190, 80, 461, 22))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setMinimum(-100)
        self.horizontalSlider.setMaximum(100)
        self.horizontalSlider.setValue(0)
        self.horizontalSlider.valueChanged.connect(self.update_line_edit)
        
        self.lineEdit = QtWidgets.QLineEdit(self)
        self.lineEdit.setGeometry(QtCore.QRect(670, 80, 113, 25))
        self.lineEdit.setText(str(self.horizontalSlider.value()))

        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(190, 130, 112, 34))
        self.pushButton.setText("OK")
        self.pushButton.clicked.connect(self.log_brightness)

    def update_line_edit(self):
        self.lineEdit.setText(str(self.horizontalSlider.value()))

    def set_image(self, imagefile):
        self.imagefile = imagefile

    def log_brightness(self):
        # Memastikan citra telah diatur
        if self.imagefile is None:
            QtWidgets.QMessageBox.warning(self, "No Image", "Please set an image first.")
            return
        
        # Membuka citra menggunakan PIL
        image = self.imagefile.convert('L')  # Konversi ke grayscale

        # Mengonversi citra ke numpy array
        image_np = np.array(image)

        # Tentukan konstanta c berdasarkan rumus
        c = 255 / np.log(1 + np.max(image_np))

        # Dapatkan nilai dari slider untuk menyesuaikan log brightness
        brightness_value = self.horizontalSlider.value()

        # Terapkan transformasi log brightness dengan menyesuaikan berdasarkan slider
        log_transformed = c * np.log(1 + image_np) * (1 + brightness_value / 100.0)  # Sesuaikan berdasarkan slider

        # Konversi hasil ke format uint8 (gambar 8 bit)
        log_transformed_np = np.array(log_transformed, dtype=np.uint8)

        # Mengonversi array yang sudah diproses kembali menjadi gambar
        log_transformed_image = Image.fromarray(log_transformed_np)

        # Simpan hasil untuk keperluan save
        self.imageResult = log_transformed_image

        # Emit sinyal dengan gambar hasil transformasi
        self.imageProcessed.emit(log_transformed_image)

        # Tutup dialog setelah pemrosesan selesai
        self.close()


