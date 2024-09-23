from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox
import sys


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1070, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.listView = QtWidgets.QListView(self.centralwidget)
        self.listView.setGeometry(QtCore.QRect(10, 20, 481, 351))
        self.listView.setObjectName("listView")
        self.listView_2 = QtWidgets.QListView(self.centralwidget)
        self.listView_2.setGeometry(QtCore.QRect(500, 20, 481, 351))
        self.listView_2.setObjectName("listView_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1070, 31))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        self.menuHistogram = QtWidgets.QMenu(self.menuView)
        self.menuHistogram.setObjectName("menuHistogram")
        self.menuColors = QtWidgets.QMenu(self.menubar)
        self.menuColors.setObjectName("menuColors")
        self.menuRGB = QtWidgets.QMenu(self.menuColors)
        self.menuRGB.setObjectName("menuRGB")
        self.menuRGB_to_Grayscale = QtWidgets.QMenu(self.menuColors)
        self.menuRGB_to_Grayscale.setObjectName("menuRGB_to_Grayscale")
        self.menuBit_Depth = QtWidgets.QMenu(self.menuColors)
        self.menuBit_Depth.setObjectName("menuBit_Depth")
        self.menuTentang = QtWidgets.QMenu(self.menubar)
        self.menuTentang.setObjectName("menuTentang")
        self.menuImage_Processing = QtWidgets.QMenu(self.menubar)
        self.menuImage_Processing.setObjectName("menuImage_Processing")
        self.menuAritmetical_Operation = QtWidgets.QMenu(self.menubar)
        self.menuAritmetical_Operation.setObjectName("menuAritmetical_Operation")
        self.menuFilter = QtWidgets.QMenu(self.menubar)
        self.menuFilter.setObjectName("menuFilter")
        self.menuEdge_Detection = QtWidgets.QMenu(self.menuFilter)
        self.menuEdge_Detection.setObjectName("menuEdge_Detection")
        self.menuGaussian_Blur = QtWidgets.QMenu(self.menuFilter)
        self.menuGaussian_Blur.setObjectName("menuGaussian_Blur")
        self.menuEdge_Detection_2 = QtWidgets.QMenu(self.menubar)
        self.menuEdge_Detection_2.setObjectName("menuEdge_Detection_2")
        self.menuMorfologi = QtWidgets.QMenu(self.menubar)
        self.menuMorfologi.setObjectName("menuMorfologi")
        self.menuErosion = QtWidgets.QMenu(self.menuMorfologi)
        self.menuErosion.setObjectName("menuErosion")
        self.menuDilation = QtWidgets.QMenu(self.menuMorfologi)
        self.menuDilation.setObjectName("menuDilation")
        self.menuOpening = QtWidgets.QMenu(self.menuMorfologi)
        self.menuOpening.setObjectName("menuOpening")
        self.menuClosing = QtWidgets.QMenu(self.menuMorfologi)
        self.menuClosing.setObjectName("menuClosing")
        self.menuClear = QtWidgets.QMenu(self.menubar)
        self.menuClear.setObjectName("menuClear")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave_As = QtWidgets.QAction(MainWindow)
        self.actionSave_As.setObjectName("actionSave_As")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionInput = QtWidgets.QAction(MainWindow)
        self.actionInput.setObjectName("actionInput")
        self.actionOutput = QtWidgets.QAction(MainWindow)
        self.actionOutput.setObjectName("actionOutput")
        self.actionInput_Output = QtWidgets.QAction(MainWindow)
        self.actionInput_Output.setObjectName("actionInput_Output")
        self.actionBrightness = QtWidgets.QAction(MainWindow)
        self.actionBrightness.setObjectName("actionBrightness")
        self.actionInvers = QtWidgets.QAction(MainWindow)
        self.actionInvers.setObjectName("actionInvers")
        self.actionLog_Brigthness = QtWidgets.QAction(MainWindow)
        self.actionLog_Brigthness.setObjectName("actionLog_Brigthness")
        self.actionGamma_Correstion = QtWidgets.QAction(MainWindow)
        self.actionGamma_Correstion.setObjectName("actionGamma_Correstion")
        self.actionKuning = QtWidgets.QAction(MainWindow)
        self.actionKuning.setObjectName("actionKuning")
        self.actionOrange = QtWidgets.QAction(MainWindow)
        self.actionOrange.setObjectName("actionOrange")
        self.actionCyan = QtWidgets.QAction(MainWindow)
        self.actionCyan.setObjectName("actionCyan")
        self.actionPurple = QtWidgets.QAction(MainWindow)
        self.actionPurple.setObjectName("actionPurple")
        self.actionGrey = QtWidgets.QAction(MainWindow)
        self.actionGrey.setObjectName("actionGrey")
        self.actionCoklat = QtWidgets.QAction(MainWindow)
        self.actionCoklat.setObjectName("actionCoklat")
        self.actionAverage = QtWidgets.QAction(MainWindow)
        self.actionAverage.setObjectName("actionAverage")
        self.actionLightness = QtWidgets.QAction(MainWindow)
        self.actionLightness.setObjectName("actionLightness")
        self.action1_bit = QtWidgets.QAction(MainWindow)
        self.action1_bit.setObjectName("action1_bit")
        self.action2_bit = QtWidgets.QAction(MainWindow)
        self.action2_bit.setObjectName("action2_bit")
        self.action3_bit = QtWidgets.QAction(MainWindow)
        self.action3_bit.setObjectName("action3_bit")
        self.action4_bit = QtWidgets.QAction(MainWindow)
        self.action4_bit.setObjectName("action4_bit")
        self.action5_bit = QtWidgets.QAction(MainWindow)
        self.action5_bit.setObjectName("action5_bit")
        self.action6_bit = QtWidgets.QAction(MainWindow)
        self.action6_bit.setObjectName("action6_bit")
        self.action7_bit = QtWidgets.QAction(MainWindow)
        self.action7_bit.setObjectName("action7_bit")
        self.actionHistogram_Equalization = QtWidgets.QAction(MainWindow)
        self.actionHistogram_Equalization.setObjectName("actionHistogram_Equalization")
        self.actionFuzzy_HE_RGB = QtWidgets.QAction(MainWindow)
        self.actionFuzzy_HE_RGB.setObjectName("actionFuzzy_HE_RGB")
        self.actionIdentity = QtWidgets.QAction(MainWindow)
        self.actionIdentity.setObjectName("actionIdentity")
        self.actionSharpen = QtWidgets.QAction(MainWindow)
        self.actionSharpen.setObjectName("actionSharpen")
        self.actionUnsharp_Masking = QtWidgets.QAction(MainWindow)
        self.actionUnsharp_Masking.setObjectName("actionUnsharp_Masking")
        self.actionAverage_Filter = QtWidgets.QAction(MainWindow)
        self.actionAverage_Filter.setObjectName("actionAverage_Filter")
        self.actionLow_Pass_Filter = QtWidgets.QAction(MainWindow)
        self.actionLow_Pass_Filter.setObjectName("actionLow_Pass_Filter")
        self.actionBandstop_Filter = QtWidgets.QAction(MainWindow)
        self.actionBandstop_Filter.setObjectName("actionBandstop_Filter")
        self.actionEdge_Detection_1 = QtWidgets.QAction(MainWindow)
        self.actionEdge_Detection_1.setObjectName("actionEdge_Detection_1")
        self.actionEdge_Detection_2 = QtWidgets.QAction(MainWindow)
        self.actionEdge_Detection_2.setObjectName("actionEdge_Detection_2")
        self.actionEdge_Detection_3 = QtWidgets.QAction(MainWindow)
        self.actionEdge_Detection_3.setObjectName("actionEdge_Detection_3")
        self.actionGaussian_Blur_3x3 = QtWidgets.QAction(MainWindow)
        self.actionGaussian_Blur_3x3.setObjectName("actionGaussian_Blur_3x3")
        self.actionGaussian_Blur_5x5 = QtWidgets.QAction(MainWindow)
        self.actionGaussian_Blur_5x5.setObjectName("actionGaussian_Blur_5x5")
        self.actionGaussian_Blur_7x7 = QtWidgets.QAction(MainWindow)
        self.actionGaussian_Blur_7x7.setObjectName("actionGaussian_Blur_7x7")
        self.actionDilasi = QtWidgets.QAction(MainWindow)
        self.actionDilasi.setObjectName("actionDilasi")
        self.actionErosi = QtWidgets.QAction(MainWindow)
        self.actionErosi.setObjectName("actionErosi")
        self.actionOpening = QtWidgets.QAction(MainWindow)
        self.actionOpening.setObjectName("actionOpening")
        self.actionClosing = QtWidgets.QAction(MainWindow)
        self.actionClosing.setObjectName("actionClosing")
        self.actionClear = QtWidgets.QAction(MainWindow)
        self.actionClear.setObjectName("actionClear")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")

        self.retranslateUi(MainWindow)
        self.connectActions()
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def connectActions(self):
        self.actionOpen.triggered.connect(self.openFile)
        self.actionSave_As.triggered.connect(self.saveFile)
        self.actionExit.triggered.connect(self.exitApp)
        self.actionInput.triggered.connect(self.inputImage)
        self.actionOutput.triggered.connect(self.outputImage)
        self.actionInput_Output.triggered.connect(self.inputOutputImage)
        self.actionBrightness.triggered.connect(self.adjustBrightness)
        self.actionInvers.triggered.connect(self.invertImage)
        self.actionLog_Brigthness.triggered.connect(self.logBrightness)
        self.actionGamma_Correstion.triggered.connect(self.gammaCorrection)
        self.actionKuning.triggered.connect(self.applyKuning)
        self.actionOrange.triggered.connect(self.applyOrange)
        self.actionCyan.triggered.connect(self.applyCyan)
        self.actionPurple.triggered.connect(self.applyPurple)
        self.actionGrey.triggered.connect(self.applyGrey)
        self.actionCoklat.triggered.connect(self.applyCoklat)
        self.actionAverage.triggered.connect(self.applyAverage)
        self.actionLightness.triggered.connect(self.applyLightness)
        self.action1_bit.triggered.connect(self.convertTo1Bit)
        self.action2_bit.triggered.connect(self.convertTo2Bit)
        self.action3_bit.triggered.connect(self.convertTo3Bit)
        self.action4_bit.triggered.connect(self.convertTo4Bit)
        self.action5_bit.triggered.connect(self.convertTo5Bit)
        self.action6_bit.triggered.connect(self.convertTo6Bit)
        self.action7_bit.triggered.connect(self.convertTo7Bit)
        self.actionHistogram_Equalization.triggered.connect(self.equalizeHistogram)
        self.actionFuzzy_HE_RGB.triggered.connect(self.fuzzyHE_RGB)
        self.actionIdentity.triggered.connect(self.applyIdentity)
        self.actionSharpen.triggered.connect(self.applySharpen)
        self.actionUnsharp_Masking.triggered.connect(self.unsharpMasking)
        self.actionAverage_Filter.triggered.connect(self.applyAverageFilter)
        self.actionLow_Pass_Filter.triggered.connect(self.applyLowPassFilter)
        self.actionBandstop_Filter.triggered.connect(self.applyBandstopFilter)
        self.actionEdge_Detection_1.triggered.connect(self.detectEdges1)
        self.actionEdge_Detection_2.triggered.connect(self.detectEdges2)
        self.actionEdge_Detection_3.triggered.connect(self.detectEdges3)
        self.actionGaussian_Blur_3x3.triggered.connect(self.applyGaussianBlur3x3)
        self.actionGaussian_Blur_5x5.triggered.connect(self.applyGaussianBlur5x5)
        self.actionGaussian_Blur_7x7.triggered.connect(self.applyGaussianBlur7x7)
        self.actionDilasi.triggered.connect(self.applyDilasi)
        self.actionErosi.triggered.connect(self.applyErosi)
        self.actionOpening.triggered.connect(self.applyOpening)
        self.actionClosing.triggered.connect(self.applyClosing)
        self.actionClear.triggered.connect(self.clearAll)
        self.actionAbout.triggered.connect(self.showAbout)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.menuHistogram.setTitle(_translate("MainWindow", "Histogram"))
        self.menuColors.setTitle(_translate("MainWindow", "Colors"))
        self.menuRGB.setTitle(_translate("MainWindow", "RGB"))
        self.menuRGB_to_Grayscale.setTitle(_translate("MainWindow", "RGB to Grayscale"))
        self.menuBit_Depth.setTitle(_translate("MainWindow", "Bit Depth"))
        self.menuTentang.setTitle(_translate("MainWindow", "Tentang"))
        self.menuImage_Processing.setTitle(_translate("MainWindow", "Image Processing"))
        self.menuAritmetical_Operation.setTitle(_translate("MainWindow", "Aritmetical Operation"))
        self.menuFilter.setTitle(_translate("MainWindow", "Filter"))
        self.menuEdge_Detection.setTitle(_translate("MainWindow", "Edge Detection"))
        self.menuGaussian_Blur.setTitle(_translate("MainWindow", "Gaussian Blur"))
        self.menuEdge_Detection_2.setTitle(_translate("MainWindow", "Edge Detection"))
        self.menuMorfologi.setTitle(_translate("MainWindow", "Morfologi"))
        self.menuErosion.setTitle(_translate("MainWindow", "Erosion"))
        self.menuDilation.setTitle(_translate("MainWindow", "Dilation"))
        self.menuOpening.setTitle(_translate("MainWindow", "Opening"))
        self.menuClosing.setTitle(_translate("MainWindow", "Closing"))
        self.menuClear.setTitle(_translate("MainWindow", "Clear"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionSave_As.setText(_translate("MainWindow", "Save As"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionInput.setText(_translate("MainWindow", "Input"))
        self.actionOutput.setText(_translate("MainWindow", "Output"))
        self.actionInput_Output.setText(_translate("MainWindow", "Input/Output"))
        self.actionBrightness.setText(_translate("MainWindow", "Brightness"))
        self.actionInvers.setText(_translate("MainWindow", "Invers"))
        self.actionLog_Brigthness.setText(_translate("MainWindow", "Log Brightness"))
        self.actionGamma_Correstion.setText(_translate("MainWindow", "Gamma Correction"))
        self.actionKuning.setText(_translate("MainWindow", "Kuning"))
        self.actionOrange.setText(_translate("MainWindow", "Orange"))
        self.actionCyan.setText(_translate("MainWindow", "Cyan"))
        self.actionPurple.setText(_translate("MainWindow", "Purple"))
        self.actionGrey.setText(_translate("MainWindow", "Grey"))
        self.actionCoklat.setText(_translate("MainWindow", "Coklat"))
        self.actionAverage.setText(_translate("MainWindow", "Average"))
        self.actionLightness.setText(_translate("MainWindow", "Lightness"))
        self.action1_bit.setText(_translate("MainWindow", "1 bit"))
        self.action2_bit.setText(_translate("MainWindow", "2 bit"))
        self.action3_bit.setText(_translate("MainWindow", "3 bit"))
        self.action4_bit.setText(_translate("MainWindow", "4 bit"))
        self.action5_bit.setText(_translate("MainWindow", "5 bit"))
        self.action6_bit.setText(_translate("MainWindow", "6 bit"))
        self.action7_bit.setText(_translate("MainWindow", "7 bit"))
        self.actionHistogram_Equalization.setText(_translate("MainWindow", "Histogram Equalization"))
        self.actionFuzzy_HE_RGB.setText(_translate("MainWindow", "Fuzzy HE RGB"))
        self.actionIdentity.setText(_translate("MainWindow", "Identity"))
        self.actionSharpen.setText(_translate("MainWindow", "Sharpen"))
        self.actionUnsharp_Masking.setText(_translate("MainWindow", "Unsharp Masking"))
        self.actionAverage_Filter.setText(_translate("MainWindow", "Average Filter"))
        self.actionLow_Pass_Filter.setText(_translate("MainWindow", "Low Pass Filter"))
        self.actionBandstop_Filter.setText(_translate("MainWindow", "Bandstop Filter"))
        self.actionEdge_Detection_1.setText(_translate("MainWindow", "Edge Detection 1"))
        self.actionEdge_Detection_2.setText(_translate("MainWindow", "Edge Detection 2"))
        self.actionEdge_Detection_3.setText(_translate("MainWindow", "Edge Detection 3"))
        self.actionGaussian_Blur_3x3.setText(_translate("MainWindow", "Gaussian Blur 3x3"))
        self.actionGaussian_Blur_5x5.setText(_translate("MainWindow", "Gaussian Blur 5x5"))
        self.actionGaussian_Blur_7x7.setText(_translate("MainWindow", "Gaussian Blur 7x7"))
        self.actionDilasi.setText(_translate("MainWindow", "Dilasi"))
        self.actionErosi.setText(_translate("MainWindow", "Erosi"))
        self.actionOpening.setText(_translate("MainWindow", "Opening"))
        self.actionClosing.setText(_translate("MainWindow", "Closing"))
        self.actionClear.setText(_translate("MainWindow", "Clear"))
        self.actionAbout.setText(_translate("MainWindow", "About"))

def openFile(self):
        filename, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Open File", "", "Images (*.png *.xpm *.jpg)")
        if filename:
            self.image = QtGui.QImage(filename)
            self.displayImage(self.image)

class ImageProcessor(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(ImageProcessor, self).__init__(parent)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Image Processor")
        self.setGeometry(100, 100, 800, 600)
        
        # Setup UI components like menus, toolbars, etc.
        self.setupMenus()
        self.show()

    def setupMenus(self):
        # Setup menus and actions here
        pass

    def openFile(self):
        filename, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Open File", "", "Images (*.png *.xpm *.jpg)")
        if filename:
            self.image = QtGui.QImage(filename)
            self.displayImage(self.image)

    def saveFile(self):
        filename, _ = QtWidgets.QFileDialog.getSaveFileName(self, "Save File", "", "Images (*.png *.xpm *.jpg)")
        if filename:
            self.image.save(filename)

    def exitApp(self):
        self.close()

    def inputImage(self):
        # Assuming you want to load an image into the application
        self.openFile()

    def outputImage(self):
        # Assuming you want to process and save an image
        self.saveFile()

    def inputOutputImage(self):
        self.openFile()
        # Process the image
        self.saveFile()

    def adjustBrightness(self):
        # Dummy implementation for brightness adjustment
        pass

    def invertImage(self):
        # Dummy implementation for image inversion
        pass

    def logBrightness(self):
        # Dummy implementation for log brightness correction
        pass

    def gammaCorrection(self):
        # Dummy implementation for gamma correction
        pass

    def applyKuning(self):
        # Dummy implementation for Kuning color effect
        pass

    def applyOrange(self):
        # Dummy implementation for Orange color effect
        pass

    def applyCyan(self):
        # Dummy implementation for Cyan color effect
        pass

    def applyPurple(self):
        # Dummy implementation for Purple color effect
        pass

    def applyGrey(self):
        # Dummy implementation for Grey color effect
        pass

    def applyCoklat(self):
        # Dummy implementation for Coklat color effect
        pass

    def applyAverage(self):
        # Dummy implementation for Average color effect
        pass

    def applyLightness(self):
        # Dummy implementation for Lightness color effect
        pass

    def convertTo1Bit(self):
        # Dummy implementation for 1-bit depth conversion
        pass

    def convertTo2Bit(self):
        # Dummy implementation for 2-bit depth conversion
        pass

    def convertTo3Bit(self):
        # Dummy implementation for 3-bit depth conversion
        pass

    def convertTo4Bit(self):
        # Dummy implementation for 4-bit depth conversion
        pass

    def convertTo5Bit(self):
        # Dummy implementation for 5-bit depth conversion
        pass

    def convertTo6Bit(self):
        # Dummy implementation for 6-bit depth conversion
        pass

    def convertTo7Bit(self):
        # Dummy implementation for 7-bit depth conversion
        pass

    def equalizeHistogram(self):
        # Dummy implementation for histogram equalization
        pass

    def fuzzyHE_RGB(self):
        # Dummy implementation for fuzzy histogram equalization for RGB
        pass

    def applyIdentity(self):
        # Dummy implementation for identity transformation
        pass

    def applySharpen(self):
        # Dummy implementation for sharpening filter
        pass

    def unsharpMasking(self):
        # Dummy implementation for unsharp masking filter
        pass

    def applyAverageFilter(self):
        # Dummy implementation for average filter
        pass

    def applyLowPassFilter(self):
        # Dummy implementation for low pass filter
        pass

    def applyBandstopFilter(self):
        # Dummy implementation for bandstop filter
        pass

    def detectEdges1(self):
        # Dummy implementation for edge detection method 1
        pass

    def detectEdges2(self):
        # Dummy implementation for edge detection method 2
        pass

    def detectEdges3(self):
        # Dummy implementation for edge detection method 3
        pass

    def applyGaussianBlur3x3(self):
        # Dummy implementation for Gaussian blur with 3x3 kernel
        pass

    def applyGaussianBlur5x5(self):
        # Dummy implementation for Gaussian blur with 5x5 kernel
        pass

    def applyGaussianBlur7x7(self):
        # Dummy implementation for Gaussian blur with 7x7 kernel
        pass

    def applyDilasi(self):
        # Dummy implementation for dilation operation
        pass

    def applyErosi(self):
        # Dummy
        pass



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())