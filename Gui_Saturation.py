from PyQt5 import QtCore, QtGui, QtWidgets
from PIL import Image
import numpy as np

class LinearSaturationDialog(QtWidgets.QDialog):
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
        self.setObjectName("LinearSaturationDialog")
        self.resize(800, 300)
        
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(30, 70, 151, 41))
        self.label.setText("Linear Saturation")

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
        self.pushButton.clicked.connect(self.linear_saturation)

    def update_line_edit(self):
        self.lineEdit.setText(str(self.horizontalSlider.value()))

    def set_image(self, imagefile):
        self.imagefile = imagefile

    def linear_saturation(self):
        # Memastikan citra telah diatur
        if self.imagefile is None:
            QtWidgets.QMessageBox.warning(self, "No Image", "Please set an image first.")
            return
        
        # Membuka citra menggunakan PIL
        image = self.imagefile.convert('RGB')  # Konversi ke RGB (atau format asli yang diinginkan)

        # Mengonversi citra ke numpy array dan mengubah ke ruang warna HSV
        img_np = np.array(image)
        img_hsv = Image.fromarray(img_np, 'RGB').convert('HSV')
        img_hsv_np = np.array(img_hsv, dtype=np.float32)

        # Dapatkan nilai dari slider untuk menyesuaikan saturasi linier
        saturation_value = self.horizontalSlider.value()

        # Terapkan transformasi linier saturasi dengan menyesuaikan berdasarkan slider
        saturation_factor = 1 + (saturation_value / 100.0)
        img_hsv_np[..., 1] *= saturation_factor

        # Memastikan nilai piksel tetap dalam rentang [0, 255]
        img_hsv_np[..., 1] = np.clip(img_hsv_np[..., 1], 0, 255)

        # Mengonversi array yang sudah diproses kembali menjadi gambar RGB
        linear_saturation_image = Image.fromarray(img_hsv_np.astype(np.uint8), 'HSV').convert('RGB')

        # Simpan hasil untuk keperluan save
        self.imageResult = linear_saturation_image

        # Emit sinyal dengan gambar hasil transformasi
        self.imageProcessed.emit(linear_saturation_image)

        # Tutup dialog setelah pemrosesan selesai
        self.close()
