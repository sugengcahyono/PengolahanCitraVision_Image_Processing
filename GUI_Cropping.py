from PyQt5 import QtCore, QtGui, QtWidgets
from PIL import Image

class CropsDialog(QtWidgets.QDialog):
    # Signal to send the cropped image back to main
    imageCropped = QtCore.pyqtSignal(object)

    def __init__(self, parent=None):
        if parent is not None and not isinstance(parent, QtWidgets.QWidget):
            raise TypeError("Parent must be of type QWidget or None")
        super().__init__(parent)
        self.setupUi()
        self.imagefile = None

    def setupUi(self):
        self.setObjectName("CropsDialog")
        self.resize(535, 226)

        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(30, 30, 68, 19))
        self.label_2.setText("Left:")

        self.label_3 = QtWidgets.QLabel(self)
        self.label_3.setGeometry(QtCore.QRect(30, 80, 68, 19))
        self.label_3.setText("Top:")

        self.label_4 = QtWidgets.QLabel(self)
        self.label_4.setGeometry(QtCore.QRect(280, 80, 91, 19))
        self.label_4.setText("Bottom:")

        self.label_5 = QtWidgets.QLabel(self)
        self.label_5.setGeometry(QtCore.QRect(280, 30, 68, 19))
        self.label_5.setText("Right:")

        # Bounding box input fields
        self.lineEdit = QtWidgets.QLineEdit(self)
        self.lineEdit.setGeometry(QtCore.QRect(90, 30, 113, 25))

        self.lineEdit_2 = QtWidgets.QLineEdit(self)
        self.lineEdit_2.setGeometry(QtCore.QRect(90, 80, 113, 25))

        self.lineEdit_3 = QtWidgets.QLineEdit(self)
        self.lineEdit_3.setGeometry(QtCore.QRect(370, 30, 113, 25))

        self.lineEdit_4 = QtWidgets.QLineEdit(self)
        self.lineEdit_4.setGeometry(QtCore.QRect(370, 80, 113, 25))

        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(370, 150, 112, 34))
        self.pushButton.setText("OK")
        self.pushButton.clicked.connect(self.crop_image)

    def set_image(self, imagefile):
        self.imagefile = imagefile

    def crop_image(self):
        # Ensure image is set
        if self.imagefile is None:
            QtWidgets.QMessageBox.warning(self, "No Image", "Please set an image first.")
            return

        try:
            # Get bounding box values from user input
            left = int(self.lineEdit.text())
            top = int(self.lineEdit_2.text())
            right = int(self.lineEdit_3.text())
            bottom = int(self.lineEdit_4.text())

            print(f"Cropping image with box: {(left, top, right, bottom)}")  # Debugging statement

            # Perform cropping
            cropped_image = self.imagefile.crop((left, top, right, bottom))

            # Emit the cropped image
            self.imageCropped.emit(cropped_image)

            print("Cropped image emitted.")  # Debugging statement

            # Close the dialog
            self.close()

        except ValueError as e:
            print(f"ValueError: {e}")  # Debugging statement
            QtWidgets.QMessageBox.warning(self, "Invalid Input", "Please enter valid integer values for bounding box.")
        except Exception as e:
            print(f"Exception: {e}")  # Debugging statement
            QtWidgets.QMessageBox.warning(self, "Error", "An error occurred while cropping the image.")

