from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QLabel, QMainWindow, QApplication
from PyQt5.QtGui import QPixmap
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Image Viewer")
        self.setGeometry(100, 100, 931, 600)

        # Central widget
        self.centralwidget = QtWidgets.QWidget(self)
        self.setCentralWidget(self.centralwidget)
        
        # QLabel to display the image
        self.imageLabel = QLabel(self.centralwidget)
        self.imageLabel.setGeometry(QtCore.QRect(40, 40, 411, 321))
        self.imageLabel.setScaledContents(True)  # Allow image to scale
        
        # QListView (Placeholder for other functionalities)
        self.listView_2 = QtWidgets.QListView(self.centralwidget)
        self.listView_2.setGeometry(QtCore.QRect(460, 40, 411, 321))

        # Menu bar
        self.menubar = self.menuBar()
        
        # Create menus
        self.menuMenu = self.menubar.addMenu('Menu')
        self.menuHistogram = self.menubar.addMenu('Histogram')
        self.menuColors = self.menubar.addMenu('Colors')
        self.menuRGB = self.menuColors.addMenu('RGB')
        self.menuRBG_to_Grayscale = self.menuColors.addMenu('RBG to Grayscale')
        self.menuBit_Depth = self.menuColors.addMenu('Bit Depth')
        self.menuImage_Processing = self.menubar.addMenu('Image Processing')
        self.menuAritmetical_Operation = self.menubar.addMenu('Aritmetical Operation')
        self.menuFilter = self.menubar.addMenu('Filter')
        self.menuEdge_Detection_2 = self.menuFilter.addMenu('Edge Detection 2')
        self.menuUnsharp_Masking = self.menubar.addMenu('Unsharp Masking')
        self.menuEdge_Detection = self.menubar.addMenu('Edge Detection')
        self.menuMorfologi = self.menubar.addMenu('Morfologi')
        self.menuErosion = self.menuMorfologi.addMenu('Erosion')
        self.menuDilation = self.menuMorfologi.addMenu('Dilation')
        self.menuOpening = self.menuMorfologi.addMenu('Opening')
        self.menuClosing = self.menuMorfologi.addMenu('Closing')
        self.menuTentang = self.menubar.addMenu('Tentang')

        # Create actions
        self.actionOpen = QtWidgets.QAction('Open', self)
        self.actionOpen.triggered.connect(self.openFileDialog)
        self.menuMenu.addAction(self.actionOpen)
        
        self.actionSave_As = QtWidgets.QAction('Save As', self)
        self.actionSave_As.triggered.connect(self.saveFileDialog)
        self.menuMenu.addAction(self.actionSave_As)
        
        self.actionExit = QtWidgets.QAction('Exit', self)
        self.actionExit.triggered.connect(self.close)
        self.menuMenu.addAction(self.actionExit)  # Added Exit to the Menu

        # Additional actions
        self.actionHistrogram_Equalization = QtWidgets.QAction('Histogram Equalization', self)
        self.menuHistogram.addAction(self.actionHistrogram_Equalization)

        # Add more actions to the menus as needed
        # For simplicity, only a few additional actions are added here
        self.actionBrightness = QtWidgets.QAction('Brightness', self)
        self.menuColors.addAction(self.actionBrightness)
        
        self.actionGamma_Correction = QtWidgets.QAction('Gamma Correction', self)
        self.menuImage_Processing.addAction(self.actionGamma_Correction)

        # Status bar
        self.statusbar = self.statusBar()
        
        self.currentPixmap = None  # To store the current image

    def openFileDialog(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(self, "Open Image File", "", "Images (*.png *.jpg *.bmp)", options=options)
        if fileName:
            self.currentPixmap = QPixmap(fileName)
            self.imageLabel.setPixmap(self.currentPixmap)

    def saveFileDialog(self):
        if self.currentPixmap:
            options = QFileDialog.Options()
            fileName, _ = QFileDialog.getSaveFileName(self, "Save Image As", "", "Images (*.png *.jpg *.bmp)", options=options)
            if fileName:
                self.currentPixmap.save(fileName)
        else:
            QtWidgets.QMessageBox.warning(self, "Warning", "No image to save!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())
