from PyQt5 import QtCore, QtGui, QtWidgets
from PIL import Image

class TranslasiDialog(QtWidgets.QDialog):
    # Signal to send the translated image back to main
    imageTranslated = QtCore.pyqtSignal(object)

    def __init__(self, parent=None):
        if parent is not None and not isinstance(parent, QtWidgets.QWidget):
            raise TypeError("Parent must be of type QWidget or None")
        super().__init__(parent)
        self.setupUi()
        self.imagefile = None

    def setupUi(self):
        self.setObjectName("TranslasiDialog")
        self.resize(300, 200)

        self.label_x = QtWidgets.QLabel(self)
        self.label_x.setGeometry(QtCore.QRect(30, 30, 50, 20))
        self.label_x.setText("X:")

        self.lineEdit_x = QtWidgets.QLineEdit(self)
        self.lineEdit_x.setGeometry(QtCore.QRect(80, 30, 100, 25))

        self.label_y = QtWidgets.QLabel(self)
        self.label_y.setGeometry(QtCore.QRect(30, 70, 50, 20))
        self.label_y.setText("Y:")

        self.lineEdit_y = QtWidgets.QLineEdit(self)
        self.lineEdit_y.setGeometry(QtCore.QRect(80, 70, 100, 25))

        self.pushButton_ok = QtWidgets.QPushButton(self)
        self.pushButton_ok.setGeometry(QtCore.QRect(80, 120, 100, 30))
        self.pushButton_ok.setText("OK")
        self.pushButton_ok.clicked.connect(self.translasi_image)

    def set_image(self, imagefile):
        self.imagefile = imagefile

    def translasi_image(self):
        if self.imagefile is None:
            QtWidgets.QMessageBox.warning(self, "No Image", "Please set an image first.")
            return

        try:
            # Get translation values from input fields
            x_shift = int(self.lineEdit_x.text())
            y_shift = int(self.lineEdit_y.text())

            # Perform translation
            translated_image = self.imagefile.transform(
                self.imagefile.size, 
                Image.AFFINE, 
                (1, 0, x_shift, 0, 1, y_shift)
            )

            # Emit the translated image
            self.imageTranslated.emit(translated_image)
            self.close()

        except ValueError:
            QtWidgets.QMessageBox.warning(self, "Invalid Input", "Please enter valid integer values for translation.")
