from PyQt5 import QtCore, QtGui, QtWidgets
from PIL import Image

class RotasiDialog(QtWidgets.QDialog):
    imageRotated = QtCore.pyqtSignal(object)

    def __init__(self, parent=None):
        if parent is not None and not isinstance(parent, QtWidgets.QWidget):
            raise TypeError("Parent must be of type QWidget or None")
        super().__init__(parent)
        self.setupUi()
        self.imagefile = None

    def setupUi(self):
        self.setObjectName("RotasiDialog")
        self.resize(305, 180)

        self.label_5 = QtWidgets.QLabel(self)
        self.label_5.setGeometry(QtCore.QRect(40, 40, 81, 19))
        self.label_5.setText("Derajat:")

        self.lineEdit_3 = QtWidgets.QLineEdit(self)
        self.lineEdit_3.setGeometry(QtCore.QRect(130, 40, 113, 25))

        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(130, 100, 112, 34))
        self.pushButton.setText("OK")
        self.pushButton.clicked.connect(self.rotate_image)

    def set_image(self, imagefile):
        self.imagefile = imagefile

    def rotate_image(self):
        if self.imagefile is None:
            QtWidgets.QMessageBox.warning(self, "No Image", "Please set an image first.")
            return

        try:
            angle = float(self.lineEdit_3.text())
            rotated_image = self.imagefile.rotate(angle, expand=True)

            self.imageRotated.emit(rotated_image)
            self.close()
        except ValueError:
            QtWidgets.QMessageBox.warning(self, "Invalid Input", "Please enter a valid number for the rotation angle.")
