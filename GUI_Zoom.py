from PyQt5 import QtCore, QtGui, QtWidgets
from PIL import Image

class ZoomDialog(QtWidgets.QDialog):
    imageZoomed = QtCore.pyqtSignal(object)

    def __init__(self, parent=None):
        if parent is not None and not isinstance(parent, QtWidgets.QWidget):
            raise TypeError("Parent must be of type QWidget or None")
        super().__init__(parent)
        self.setupUi()
        self.imagefile = None

    def setupUi(self):
        self.setObjectName("ZoomDialog")
        self.resize(278, 161)

        self.label_5 = QtWidgets.QLabel(self)
        self.label_5.setGeometry(QtCore.QRect(40, 40, 81, 19))
        self.label_5.setText("Skala:")

        self.lineEdit_3 = QtWidgets.QLineEdit(self)
        self.lineEdit_3.setGeometry(QtCore.QRect(110, 40, 113, 25))

        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(110, 90, 112, 34))
        self.pushButton.setText("OK")
        self.pushButton.clicked.connect(self.zoom_image)

    def set_image(self, imagefile):
        if isinstance(imagefile, Image.Image):
            self.imagefile = imagefile
        else:
            QtWidgets.QMessageBox.warning(self, "Invalid Image", "The provided image is not valid.")

    def zoom_image(self):
        if self.imagefile is None:
            QtWidgets.QMessageBox.warning(self, "No Image", "Please set an image first.")
            return

        try:
            zoom_factor = float(self.lineEdit_3.text())
            if zoom_factor <= 0:
                raise ValueError("Zoom factor must be positive")

            # Calculate new dimensions
            width, height = self.imagefile.size
            new_width = int(width * zoom_factor)
            new_height = int(height * zoom_factor)

            # Resize image
            zoomed_image = self.imagefile.resize((new_width, new_height), Image.Resampling.LANCZOS)
            
            # Emit signal with zoomed image
            self.imageZoomed.emit(zoomed_image)
            self.close()
        except ValueError as e:
            QtWidgets.QMessageBox.warning(self, "Invalid Input", f"Error: {e}")
