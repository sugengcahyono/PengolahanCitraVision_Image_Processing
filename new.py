
import time
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox, QInputDialog
from PyQt5.QtGui import QImage, QPixmap, QColor
import sys  # Import modul sys
import math
import cv2
import numpy as np
import matplotlib.pyplot as plt
from rembg import remove
from PIL import Image
import pandas as pd
# from latihan1 import Ui_MainWindow as latihan1
# from basic_aritmatika import Ui_MainWindow as latihan


class BrightnessContrastForm(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Brightness and Contrast")
        self.resize(300, 150)

        layout = QtWidgets.QVBoxLayout()

        # Tambahkan slider untuk brightness
        brightness_label = QtWidgets.QLabel("Brightness:")
        self.hscBrightness = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        self.hscBrightness.setRange(-127, 127)
        self.hscBrightness.setValue(0)
        self.tbBrightness = QtWidgets.QLineEdit("0")

        # Tambahkan slider untuk contrast
        contrast_label = QtWidgets.QLabel("Contrast:")
        self.hscContrast = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        self.hscContrast.setRange(-127, 127)
        self.hscContrast.setValue(0)
        self.tbContrast = QtWidgets.QLineEdit("0")

        # Tambahkan tombol "OK"
        tbOK = QtWidgets.QPushButton("OK")
        tbOK.clicked.connect(self.accept)

        layout.addWidget(brightness_label)
        layout.addWidget(self.hscBrightness)
        layout.addWidget(self.tbBrightness)
        layout.addWidget(contrast_label)
        layout.addWidget(self.hscContrast)
        layout.addWidget(self.tbContrast)
        layout.addWidget(tbOK)

        self.setLayout(layout)

        # Menghubungkan fungsi-fungsi dengan sinyal-sinyal
        self.hscBrightness.valueChanged.connect(self.updateBrightnessTextbox)
        self.hscContrast.valueChanged.connect(self.updateContrastTextbox)
        self.tbBrightness.textChanged.connect(self.updateBrightnessSlider)
        self.tbContrast.textChanged.connect(self.updateContrastSlider)

        self.tbBrightness.setText("0")
        self.tbContrast.setText("0")

    def updateBrightnessTextbox(self, value):
        self.tbBrightness.setText(str(value))

    def updateContrastTextbox(self, value):
        self.tbContrast.setText(str(value))

    def updateBrightnessSlider(self):
        text = self.tbBrightness.text()
        if text == "" or text == "-":
            self.hscBrightness.setValue(0)
            self.tbBrightness.setText("0")
        elif -127 <= int(text) <= 127:
            self.hscBrightness.setValue(int(text))
        else:
            QtWidgets.QMessageBox.warning(self, "Error", "Input nilai Error")
            self.tbBrightness.setText("0")

    def updateContrastSlider(self):
        text = self.tbContrast.text()
        if text == "" or text == "-":
            self.hscContrast.setValue(0)
            self.tbContrast.setText("0")
        elif -127 <= int(text) <= 127:
            self.hscContrast.setValue(int(text))
        else:
            QtWidgets.QMessageBox.warning(self, "Error", "Input nilai Error")
            self.tbContrast.setText("0")
            

class LogBrightness(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
    
    def setupUi(self, LogBrightness):
        LogBrightness.setObjectName("LogBrightness")
        LogBrightness.resize(300, 150)
        
        self.tbLogBrightness = QtWidgets.QLineEdit(LogBrightness)
        self.tbLogBrightness.setGeometry(QtCore.QRect(140, 30, 113, 20))
        self.tbLogBrightness.setObjectName("tbLogBrightness")
        self.tbLogBrightness.textChanged.connect(self.onTextChanged)
        
        self.hscLogBrightness = QtWidgets.QSlider(LogBrightness)
        self.hscLogBrightness.setGeometry(QtCore.QRect(10, 60, 271, 22))
        self.hscLogBrightness.setOrientation(QtCore.Qt.Horizontal)
        self.hscLogBrightness.setObjectName("hscLogBrightness")
        self.hscLogBrightness.valueChanged.connect(self.onSliderChanged)
        
        self.buttonOK = QtWidgets.QPushButton(LogBrightness)
        self.buttonOK.setGeometry(QtCore.QRect(120, 100, 75, 23))
        self.buttonOK.setObjectName("buttonOK")
        self.buttonOK.setText("OK")
        self.buttonOK.clicked.connect(self.accept)
        
        self.setWindowTitle("Log Brightness")
        
        self.hscLogBrightness.setValue(0)
        self.tbLogBrightness.setText("0")
    
    def onTextChanged(self):
        text = self.tbLogBrightness.text()
        if not text.isdigit() or not 0 <= int(text) <= 105:
            QtWidgets.QMessageBox.critical(self, "Input Error", "Input nilai Error")
            self.tbLogBrightness.setText("0")
        else:
            self.hscLogBrightness.setValue(int(text))
    
    def onSliderChanged(self):
        value = self.hscLogBrightness.value()
        self.tbLogBrightness.setText(str(value))
        
class GammaTransform(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.setWindowTitle("Gamma Correction")
        self.resize(300, 120)

        self.hscGamma = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        self.tbGamma = QtWidgets.QLineEdit()
        self.btnOKGamma = QtWidgets.QPushButton("OK")

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.hscGamma)
        layout.addWidget(self.tbGamma)
        layout.addWidget(self.btnOKGamma)

        self.setLayout(layout)

        # Set range and single step for the slider to match 0-791
        self.hscGamma.setRange(0, 791)
        self.hscGamma.setSingleStep(1)

        self.hscGamma.valueChanged.connect(self.hsc_gamma_changed)
        self.tbGamma.textChanged.connect(self.tb_gamma_changed)
        self.btnOKGamma.clicked.connect(self.accept)

        self.hscGamma.setValue(0)
        self.tbGamma.setText("0")

    def hsc_gamma_changed(self, value):
        formatted_value = "{:.2f}".format(value * 0.01)
        self.tbGamma.setText(formatted_value)

    def tb_gamma_changed(self, text):
        pass

            
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(865, 430)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 20, 411, 361))
        self.label.setFrameShape(QtWidgets.QFrame.Box)
        self.label.setLineWidth(2)
        self.label.setMidLineWidth(0)
        self.label.setText("")
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(440, 20, 411, 361))
        self.label_2.setFrameShape(QtWidgets.QFrame.Box)
        self.label_2.setLineWidth(2)
        self.label_2.setMidLineWidth(0)
        self.label_2.setText("")
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 865, 21))
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
        self.menuBrightness = QtWidgets.QMenu(self.menuColors)
        self.menuBrightness.setObjectName("menuBrightness")
        self.menuBit_Depth = QtWidgets.QMenu(self.menuColors)
        self.menuBit_Depth.setObjectName("menuBit_Depth")
        
        #Tentang
        self.menuTentang = QtWidgets.QMenu(self.menubar)
        self.menuTentang.setObjectName("menuTentang")

        self.menuImage_Processing = QtWidgets.QMenu(self.menubar)
        self.menuImage_Processing.setObjectName("menuImage_Processing")
        self.menuAritmetical_Operation = QtWidgets.QMenu(self.menubar)
        self.menuAritmetical_Operation.setObjectName("menuAritmetical_Operation")
        self.menuGeometric_Operation = QtWidgets.QMenu(self.menubar)
        self.menuGeometric_Operation.setObjectName("menuGeometric_Operation")
        self.menuClear = QtWidgets.QMenu(self.menubar)
        self.menuClear.setObjectName("menuClear")
        self.menuFilter = QtWidgets.QMenu(self.menubar)
        self.menuFilter.setObjectName("menuFilter")
        self.menuEdge_Detection_2 = QtWidgets.QMenu(self.menuFilter)
        self.menuEdge_Detection_2.setObjectName("menuEdge_Detection_2")
        self.menuGaussian_Blur = QtWidgets.QMenu(self.menuFilter)
        self.menuGaussian_Blur.setObjectName("menuGaussian_Blur")
        self.menuEdge_Detection = QtWidgets.QMenu(self.menubar)
        self.menuEdge_Detection.setObjectName("menuEdge_Detection")
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
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
        #open
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionOpen.triggered.connect(self.openFile)
        
        #Tentang
        self.actionTentang = QtWidgets.QAction(MainWindow)
        self.actionTentang.setObjectName("actionTentang")
        self.actionTentang.triggered.connect(self.frameTentang)
        
        #save
        self.actionSave_As = QtWidgets.QAction(MainWindow)
        self.actionSave_As.setObjectName("actionSave_As")
        self.actionSave_As.triggered.connect(self.saveImage)
        
        #exit
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionExit.triggered.connect(self.exitApplication)
        
        #Histogram Input
        self.actionInput = QtWidgets.QAction(MainWindow)
        self.actionInput.setObjectName("actionInput")
        self.actionInput.triggered.connect(self.input_histogram)
        
        #Histogram output
        self.actionOutput = QtWidgets.QAction(MainWindow)
        self.actionOutput.setObjectName("actionOutput")
        self.actionOutput.triggered.connect(self.Output_histogram)
        
        #Histogram input output
        self.actionInput_Output = QtWidgets.QAction(MainWindow)
        self.actionInput_Output.setObjectName("actionInput_Output")
        self.actionInput_Output.triggered.connect(self.input_histogram)
        self.actionInput_Output.triggered.connect(self.Output_histogram)
        
        #Brightness & Contrast
        self.actionBrightnessness_contras = QtWidgets.QAction(MainWindow)
        self.actionBrightnessness_contras.setObjectName("actionBrightnessness_contras")
        self.actionBrightnessness_contras.triggered.connect(self.showBrightnessContrastForm)
        
        #Invers
        self.actionInvers = QtWidgets.QAction(MainWindow)
        self.actionInvers.setObjectName("actionInvers")
        self.actionInvers.triggered.connect(self.convertToInvers)
        
        #Log Brightness
        self.actionLog_Brightness = QtWidgets.QAction(MainWindow)
        self.actionLog_Brightness.setObjectName("actionLog_Brightness")
        self.actionLog_Brightness.triggered.connect(self.log_brightness)
        
        #Gamma Correction
        self.actionGamma_Correction = QtWidgets.QAction(MainWindow)
        self.actionGamma_Correction.setObjectName("actionGamma_Correction")
        self.actionGamma_Correction.triggered.connect(self.gamma_correction_triggered)
        
        #RGB_Kuning
        self.actionKuning = QtWidgets.QAction(MainWindow)
        self.actionKuning.setObjectName("actionKuning")
        self.actionKuning.triggered.connect(self.convertToYellowRGB)
        
        #RGB_Orange
        self.actionOrange = QtWidgets.QAction(MainWindow)
        self.actionOrange.setObjectName("actionOrange")
        self.actionOrange.triggered.connect(self.convertToOrangeRGB)
        
        #RGB_Cyan
        self.actionCyan = QtWidgets.QAction(MainWindow)
        self.actionCyan.setObjectName("actionCyan")
        self.actionCyan.triggered.connect(self.convertToCyanRGB)
        
        #RGB_Purple
        self.actionPurple = QtWidgets.QAction(MainWindow)
        self.actionPurple.setObjectName("actionPurple")
        self.actionPurple.triggered.connect(self.convertToPurpleRGB)
        
        #RGB_Grey
        self.actionGrey = QtWidgets.QAction(MainWindow)
        self.actionGrey.setObjectName("actionGrey")
        self.actionGrey.triggered.connect(self.convertToGreyRGB)
        
        #RGB_Coklat
        self.actionCoklat = QtWidgets.QAction(MainWindow)
        self.actionCoklat.setObjectName("actionCoklat")
        self.actionCoklat.triggered.connect(self.convertToBrownRGB)
        
        #RGB_Merah
        self.actionMerah = QtWidgets.QAction(MainWindow)
        self.actionMerah.setObjectName("actionMerah")
        self.actionMerah.triggered.connect(self.convertToRedRGB)
        
        #RGB to RGB
        self.actionRGB_toRGB = QtWidgets.QAction(MainWindow)
        self.actionRGB_toRGB.setObjectName("actionRGB_toRGB")
        self.actionRGB_toRGB.triggered.connect(self.useRGB)
        self.actionRGB_toRGB.triggered.connect(self.ekstrakRgb)
        
        #RGB to HSV
        self.actionRGB_toHSV = QtWidgets.QAction(MainWindow)
        self.actionRGB_toHSV.setObjectName("actionRGB_toHSV")
        self.actionRGB_toHSV.triggered.connect(self.useHsv)
        self.actionRGB_toHSV.triggered.connect(self.ekstrakHsv)
        
        #RGB to YcRcB
        self.actionRGB_toYCrCb = QtWidgets.QAction(MainWindow)
        self.actionRGB_toYCrCb.setObjectName("actionRGB_toYCrCb")
        self.actionRGB_toYCrCb.triggered.connect(self.useYrcb)
        self.actionRGB_toYCrCb.triggered.connect(self.ekstrakYrcb)
        
        #average
        self.actionAverage = QtWidgets.QAction(MainWindow)
        self.actionAverage.setObjectName("actionAverage")
        self.actionAverage.triggered.connect(self.convertToGreyscaleAverage)
        
        #lightness
        self.actionLightness = QtWidgets.QAction(MainWindow)
        self.actionLightness.setObjectName("actionLightness")
        self.actionLightness.triggered.connect(self.convertToGreyscaleLightness)
        
        #luminance
        self.actionLuminance = QtWidgets.QAction(MainWindow)
        self.actionLuminance.setObjectName("actionLuminance")
        self.actionLuminance.triggered.connect(self.convertToGreyscaleLuminance)
        
        #Contrast
        self.actionContras = QtWidgets.QAction(MainWindow)
        self.actionContras.setObjectName("actionContras")
        self.actionContras.triggered.connect(self.ConvertToContrast)
        
        #Bit1
        self.action1_Bit = QtWidgets.QAction(MainWindow)
        self.action1_Bit.setObjectName("action1_Bit")
        self.action1_Bit.triggered.connect(lambda: self.bitdepth(1))
        
        #Bit2
        self.action2_Bit = QtWidgets.QAction(MainWindow)
        self.action2_Bit.setObjectName("action2_Bit")
        self.action2_Bit.triggered.connect(lambda: self.bitdepth(2))
        
        #Bit3
        self.action3_Bit = QtWidgets.QAction(MainWindow)
        self.action3_Bit.setObjectName("action3_Bit")
        self.action3_Bit.triggered.connect(lambda: self.bitdepth(3))
        
        #Bit4
        self.action_Bit = QtWidgets.QAction(MainWindow)
        self.action_Bit.setObjectName("action_Bit")
        self.action_Bit.triggered.connect(lambda: self.bitdepth(4))
        
        #Bit5
        self.action5_Bit = QtWidgets.QAction(MainWindow)
        self.action5_Bit.setObjectName("action5_Bit")
        self.action5_Bit.triggered.connect(lambda: self.bitdepth(5))
        
        #Bit6
        self.action6_Bit = QtWidgets.QAction(MainWindow)
        self.action6_Bit.setObjectName("action6_Bit")
        self.action6_Bit.triggered.connect(lambda: self.bitdepth(6))
        
        #Bit7
        self.action7_Bit = QtWidgets.QAction(MainWindow)
        self.action7_Bit.setObjectName("action7_Bit")
        self.action7_Bit.triggered.connect(lambda: self.bitdepth(7))
        
        #Histogram Equalization
        self.actionHistogram_Equalization = QtWidgets.QAction(MainWindow)
        self.actionHistogram_Equalization.setObjectName("actionHistogram_Equalization")
        self.actionHistogram_Equalization.triggered.connect(self.applyHistogramEqualization)
        
        #Fuzzy HE RGB
        self.actionFuzzy_HE_RGB = QtWidgets.QAction(MainWindow)
        self.actionFuzzy_HE_RGB.setObjectName("actionFuzzy_HE_RGB")
        self.actionFuzzy_HE_RGB.triggered.connect(self.fuzzy_he_rgb)
        
        #Fuzzy Grayscale
        self.actionFuzzy_Grayscale = QtWidgets.QAction(MainWindow)
        self.actionFuzzy_Grayscale.setObjectName("actionFuzzy_Grayscale")
        self.actionFuzzy_Grayscale.triggered.connect(self.fuzzy_greyscale)
        
        #Segmen Citra
        self.actionSegmen_Citra = QtWidgets.QAction(MainWindow)
        self.actionSegmen_Citra.setObjectName("actionSegmen_Citra")
        self.actionSegmen_Citra.triggered.connect(self.segmentImage)
        
        #Tresholding
        self.actionTresholding = QtWidgets.QAction(MainWindow)
        self.actionTresholding.setObjectName("actionTresholding")
        self.actionTresholding.triggered.connect(self.Thresholding)
        
        #Aritmatika
        self.actionAritmatika = QtWidgets.QAction(MainWindow)
        self.actionAritmatika.setObjectName("actionAritmatika")
        self.actionAritmatika.triggered.connect(self.frameArimatika)
        
        #Flip Horizontal
        self.actionFlipHorizontal = QtWidgets.QAction(MainWindow)
        self.actionFlipHorizontal.setObjectName("actionFlipHorizontal")
        self.actionFlipHorizontal.triggered.connect((self.fliphorizontal))
        
        #Flip Vertical
        self.actionFlipVertical = QtWidgets.QAction(MainWindow)
        self.actionFlipVertical.setObjectName("actionFlipVertical")
        self.actionFlipVertical.triggered.connect(self.flipvertikal)
        
        #Rotate
        self.actionRotate = QtWidgets.QAction(MainWindow)
        self.actionRotate.setObjectName("actionRotate")
        self.actionRotate.triggered.connect(self.rotateImage)
        
        #Uniform Scale
        self.actionUniform_Scale = QtWidgets.QAction(MainWindow)
        self.actionUniform_Scale.setObjectName("actionUniform_Scale")
        self.actionUniform_Scale.triggered.connect(self.UniformScale)
        
        #Non Uniform Scale
        self.actionNonUniform_Scale = QtWidgets.QAction(MainWindow)
        self.actionNonUniform_Scale.setObjectName("actionNonUniform_Scale")
        self.actionNonUniform_Scale.triggered.connect(self.NonUnishowScaleDialog)
        
        #Tranlasi
        self.actionTranlasi = QtWidgets.QAction(MainWindow)
        self.actionTranlasi.setObjectName("actionTranlasi")
        self.actionTranlasi.triggered.connect(self.tranlasi)
        
        #ROI
        self.actionROI = QtWidgets.QAction(MainWindow)
        self.actionROI.setObjectName("actionROI")
        self.actionROI.triggered.connect(self.select_roi)
        
        #Background removal
        self.actionBackground_Removal = QtWidgets.QAction(MainWindow)
        self.actionBackground_Removal.setObjectName("actionBackground_Removal")
        self.actionBackground_Removal.triggered.connect(self.removeBackground)
        
        #Cropping
        self.actionCropping = QtWidgets.QAction(MainWindow)
        self.actionCropping.setObjectName("actionCropping")
        self.actionCropping.triggered.connect(self.Cropping)
        
        #Filter Identitas
        self.actionIdentity = QtWidgets.QAction(MainWindow)
        self.actionIdentity.setObjectName("actionIdentity")
        self.actionIdentity.triggered.connect(self.identity_filter)
        
        #Sharpen
        self.actionSharpen = QtWidgets.QAction(MainWindow)
        self.actionSharpen.setObjectName("actionSharpen")
        self.actionSharpen.triggered.connect(self.apply_sharpen_filter)
        
        #Unsharp Masking
        self.actionUnsharp_Masking = QtWidgets.QAction(MainWindow)
        self.actionUnsharp_Masking.setObjectName("actionUnsharp_Masking")
        self.actionUnsharp_Masking.triggered.connect(self.apply_unsharp_masking_filter)
        
        #Average Filter
        self.actionAverage_Filter = QtWidgets.QAction(MainWindow)
        self.actionAverage_Filter.setObjectName("actionAverage_Filter")
        self.actionAverage_Filter.triggered.connect(self.average_filter)
        
        #Low Pass Filter
        self.actionLow_Pass_Filter = QtWidgets.QAction(MainWindow)
        self.actionLow_Pass_Filter.setObjectName("actionLow_Pass_Filter")
        self.actionLow_Pass_Filter.triggered.connect(self.low_pass_filter)
        
        #High Pass Filter
        self.actionHigh_Pass_Filter = QtWidgets.QAction(MainWindow)
        self.actionHigh_Pass_Filter.setObjectName("actionHigh_Pass_Filter")
        self.actionHigh_Pass_Filter.triggered.connect(self.apply_high_pass_filter)
        
        #Bandstop Filter
        self.actionBandstop_Filter = QtWidgets.QAction(MainWindow)
        self.actionBandstop_Filter.setObjectName("actionBandstop_Filter")
        self.actionBandstop_Filter.triggered.connect(self.apply_bandstop_filter)
        
        #Prewit
        self.actionPrewitt = QtWidgets.QAction(MainWindow)
        self.actionPrewitt.setObjectName("actionPrewitt")
        self.actionPrewitt.triggered.connect(self.prewittEdgeDetection)
        
        #Sobel
        self.actionSobel = QtWidgets.QAction(MainWindow)
        self.actionSobel.setObjectName("actionSobel")
        self.actionSobel.triggered.connect(self.sobelEdgeDetection)
        
        #Robert
        self.actionRobert = QtWidgets.QAction(MainWindow)
        self.actionRobert.setObjectName("actionRobert")
        self.actionRobert.triggered.connect(self.applyRobertFilter)
        
        #Erosion Square3
        self.actionSquare_3 = QtWidgets.QAction(MainWindow)
        self.actionSquare_3.setObjectName("actionSquare_3")
        self.actionSquare_3.triggered.connect(self.erodeSquare3)
        
        #Erosion Square5
        self.actionSquare_5 = QtWidgets.QAction(MainWindow)
        self.actionSquare_5.setObjectName("actionSquare_5")
        self.actionSquare_5.triggered.connect(self.erodeSquare5)
        
        #Erosion Cross3
        self.actionCross_3 = QtWidgets.QAction(MainWindow)
        self.actionCross_3.setObjectName("actionCross_3")
        self.actionCross_3.triggered.connect(self.erodeCross3)
        
        #Dilation Square3
        self.actionSquare_4 = QtWidgets.QAction(MainWindow)
        self.actionSquare_4.setObjectName("actionSquare_4")
        self.actionSquare_4.triggered.connect(self.dilateSquare3)
        
        #Dilation Square5
        self.actionSquare_6 = QtWidgets.QAction(MainWindow)
        self.actionSquare_6.setObjectName("actionSquare_6")
        self.actionSquare_6.triggered.connect(self.dilateSquare5)
        
        #Dilation Cross3
        self.actionCross_4 = QtWidgets.QAction(MainWindow)
        self.actionCross_4.setObjectName("actionCross_4")
        self.actionCross_4.triggered.connect(self.dilateCross3)
        
        #Opening
        self.actionSquare_9 = QtWidgets.QAction(MainWindow)
        self.actionSquare_9.setObjectName("actionSquare_9")
        self.actionSquare_9.triggered.connect(self.applyOpening9)
        
        #Closing
        self.actionSquare_10 = QtWidgets.QAction(MainWindow)
        self.actionSquare_10.setObjectName("actionSquare_10")
        self.actionSquare_10.triggered.connect(self.applyClosingOperation9)
        
        #Edge Detection1
        self.actionEdge_Detection_1 = QtWidgets.QAction(MainWindow)
        self.actionEdge_Detection_1.setObjectName("actionEdge_Detection_1")
        self.actionEdge_Detection_1.triggered.connect(self.apply_edge_detection_filter)
        
        
        #Edge Detection2
        self.actionEdge_Detection_2 = QtWidgets.QAction(MainWindow)
        self.actionEdge_Detection_2.setObjectName("actionEdge_Detection_2")
        self.actionEdge_Detection_2.triggered.connect(self.apply_edge_detection2_filter)
        
        
        #Edge Detection3
        self.actionEdge_Detection_3 = QtWidgets.QAction(MainWindow)
        self.actionEdge_Detection_3.setObjectName("actionEdge_Detection_3")
        self.actionEdge_Detection_3.triggered.connect(self.apply_edge_detection3_filter)
        
        #Gassuan Blur3
        self.actionGaussian_Blur_3x3 = QtWidgets.QAction(MainWindow)
        self.actionGaussian_Blur_3x3.setObjectName("actionGaussian_Blur_3x3")
        self.actionGaussian_Blur_3x3.triggered.connect(self.applyGaussianBlur3)
        
        #Gaussian Blur5
        self.actionGaussian_Blur_5x5 = QtWidgets.QAction(MainWindow)
        self.actionGaussian_Blur_5x5.setObjectName("actionGaussian_Blur_5x5")
        self.actionGaussian_Blur_5x5.triggered.connect(self.applyGaussianBlur5)
        
        #Clear
        self.actionClear = QtWidgets.QAction(MainWindow)
        self.actionClear.setObjectName("actionClear")
        # self.actionClear.triggered.connect(self.clear)
        
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave_As)
        self.menuFile.addAction(self.actionExit)
        self.menuHistogram.addAction(self.actionInput)
        self.menuHistogram.addSeparator()
        self.menuHistogram.addAction(self.actionOutput)
        self.menuHistogram.addAction(self.actionInput_Output)
        self.menuView.addAction(self.menuHistogram.menuAction())
        self.menuRGB.addAction(self.actionKuning)
        self.menuRGB.addAction(self.actionOrange)
        self.menuRGB.addAction(self.actionCyan)
        self.menuRGB.addAction(self.actionPurple)
        self.menuRGB.addAction(self.actionGrey)
        self.menuRGB.addAction(self.actionCoklat)
        self.menuRGB.addAction(self.actionMerah)
        self.menuRGB.addAction(self.actionRGB_toRGB)
        self.menuRGB.addAction(self.actionRGB_toHSV)
        self.menuRGB.addAction(self.actionRGB_toYCrCb)
        self.menuRGB_to_Grayscale.addAction(self.actionAverage)
        self.menuRGB_to_Grayscale.addAction(self.actionLightness)
        self.menuRGB_to_Grayscale.addAction(self.actionLuminance)
        self.menuBrightness.addAction(self.actionContras)
        self.menuBit_Depth.addAction(self.action1_Bit)
        self.menuBit_Depth.addAction(self.action2_Bit)
        self.menuBit_Depth.addAction(self.action3_Bit)
        self.menuBit_Depth.addAction(self.action_Bit)
        self.menuBit_Depth.addAction(self.action5_Bit)
        self.menuBit_Depth.addAction(self.action6_Bit)
        self.menuBit_Depth.addAction(self.action7_Bit)
        self.menuColors.addAction(self.menuRGB.menuAction())
        self.menuColors.addAction(self.menuRGB_to_Grayscale.menuAction())
        self.menuColors.addAction(self.menuBrightness.menuAction())
        self.menuColors.addAction(self.actionBrightnessness_contras)
        self.menuColors.addAction(self.actionInvers)
        self.menuColors.addAction(self.actionLog_Brightness)
        self.menuColors.addAction(self.menuBit_Depth.menuAction())
        self.menuColors.addAction(self.actionGamma_Correction)
        self.menuTentang.addAction(self.actionTentang)
        self.menuImage_Processing.addAction(self.actionHistogram_Equalization)
        self.menuImage_Processing.addAction(self.actionFuzzy_HE_RGB)
        self.menuImage_Processing.addAction(self.actionFuzzy_Grayscale)
        self.menuImage_Processing.addAction(self.actionSegmen_Citra)
        self.menuImage_Processing.addAction(self.actionTresholding)
        self.menuAritmetical_Operation.addAction(self.actionAritmatika)
        self.menuGeometric_Operation.addAction(self.actionFlipHorizontal)
        self.menuGeometric_Operation.addAction(self.actionFlipVertical)
        self.menuGeometric_Operation.addAction(self.actionRotate)
        self.menuGeometric_Operation.addAction(self.actionUniform_Scale)
        self.menuGeometric_Operation.addAction(self.actionNonUniform_Scale)
        self.menuGeometric_Operation.addAction(self.actionTranlasi)
        self.menuGeometric_Operation.addAction(self.actionCropping)
        self.menuGeometric_Operation.addAction(self.actionROI)
        self.menuGeometric_Operation.addAction(self.actionBackground_Removal)
        self.menuEdge_Detection_2.addAction(self.actionEdge_Detection_1)
        self.menuEdge_Detection_2.addAction(self.actionEdge_Detection_2)
        self.menuEdge_Detection_2.addAction(self.actionEdge_Detection_3)
        self.menuGaussian_Blur.addAction(self.actionGaussian_Blur_3x3)
        self.menuGaussian_Blur.addAction(self.actionGaussian_Blur_5x5)
        self.menuFilter.addAction(self.actionIdentity)
        self.menuFilter.addAction(self.menuEdge_Detection_2.menuAction())
        self.menuFilter.addAction(self.actionSharpen)
        self.menuFilter.addAction(self.menuGaussian_Blur.menuAction())
        self.menuFilter.addAction(self.actionUnsharp_Masking)
        self.menuFilter.addAction(self.actionAverage_Filter)
        self.menuFilter.addAction(self.actionLow_Pass_Filter)
        self.menuFilter.addAction(self.actionHigh_Pass_Filter)
        self.menuFilter.addAction(self.actionBandstop_Filter)
        self.menuEdge_Detection.addAction(self.actionPrewitt)
        self.menuEdge_Detection.addAction(self.actionSobel)
        self.menuEdge_Detection.addAction(self.actionRobert)
        self.menuErosion.addAction(self.actionSquare_3)
        self.menuErosion.addAction(self.actionSquare_5)
        self.menuErosion.addAction(self.actionCross_3)
        self.menuDilation.addAction(self.actionSquare_4)
        self.menuDilation.addAction(self.actionSquare_6)
        self.menuDilation.addAction(self.actionCross_4)
        self.menuOpening.addAction(self.actionSquare_9)
        self.menuClosing.addAction(self.actionSquare_10)
        self.menuClear.addAction(self.actionClear)
        self.menuMorfologi.addAction(self.menuErosion.menuAction())
        self.menuMorfologi.addAction(self.menuDilation.menuAction())
        self.menuMorfologi.addAction(self.menuOpening.menuAction())
        self.menuMorfologi.addAction(self.menuClosing.menuAction())
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuColors.menuAction())
        self.menubar.addAction(self.menuTentang.menuAction())
        self.menubar.addAction(self.menuImage_Processing.menuAction())
        self.menubar.addAction(self.menuAritmetical_Operation.menuAction())
        self.menubar.addAction(self.menuGeometric_Operation.menuAction())
        self.menubar.addAction(self.menuFilter.menuAction())
        self.menubar.addAction(self.menuEdge_Detection.menuAction())
        self.menubar.addAction(self.menuMorfologi.menuAction())
        self.menubar.addAction(self.menuClear.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Form1"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.menuHistogram.setTitle(_translate("MainWindow", "Histogram"))
        self.menuColors.setTitle(_translate("MainWindow", "Colors"))
        self.menuRGB.setTitle(_translate("MainWindow", "RGB"))
        self.menuRGB_to_Grayscale.setTitle(_translate("MainWindow", "RGB to Grayscale"))
        self.menuBrightness.setTitle(_translate("MainWindow", "Brightness"))
        self.menuBit_Depth.setTitle(_translate("MainWindow", "Bit Depth"))
        self.menuTentang.setTitle(_translate("MainWindow", "Tentang"))
        self.menuImage_Processing.setTitle(_translate("MainWindow", "Image Processing"))
        self.menuAritmetical_Operation.setTitle(_translate("MainWindow", "Aritmetical Operation"))
        self.menuGeometric_Operation.setTitle(_translate("MainWindow", "Geometric Operation"))
        self.menuFilter.setTitle(_translate("MainWindow", "Filter"))
        self.menuEdge_Detection_2.setTitle(_translate("MainWindow", "Edge Detection"))
        self.menuGaussian_Blur.setTitle(_translate("MainWindow", "Gaussian Blur"))
        self.menuEdge_Detection.setTitle(_translate("MainWindow", "Edge Detection"))
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
        self.actionInput_Output.setText(_translate("MainWindow", "Input Output"))
        self.actionBrightnessness_contras.setText(_translate("MainWindow", "Brightnessness - Contrast"))
        self.actionInvers.setText(_translate("MainWindow", "Invers"))
        self.actionLog_Brightness.setText(_translate("MainWindow", "Log Brightness"))
        self.actionGamma_Correction.setText(_translate("MainWindow", "Gamma Correction"))
        self.actionKuning.setText(_translate("MainWindow", "Kuning"))
        self.actionOrange.setText(_translate("MainWindow", "Orange"))
        self.actionCyan.setText(_translate("MainWindow", "Cyan"))
        self.actionPurple.setText(_translate("MainWindow", "Purple"))
        self.actionGrey.setText(_translate("MainWindow", "Grey"))
        self.actionCoklat.setText(_translate("MainWindow", "Coklat"))
        self.actionMerah.setText(_translate("MainWindow", "Merah"))
        self.actionRGB_toRGB.setText(_translate("MainWindow", "RGB to RGB"))
        self.actionRGB_toHSV.setText(_translate("MainWindow", "RGB to HSV"))
        self.actionRGB_toYCrCb.setText(_translate("MainWindow", "RGB to YCrCb"))
        self.actionAverage.setText(_translate("MainWindow", "Average"))
        self.actionLightness.setText(_translate("MainWindow", "Lightness"))
        self.actionLuminance.setText(_translate("MainWindow", "Luminance"))
        self.actionContras.setText(_translate("MainWindow", "Contrast"))
        self.action1_Bit.setText(_translate("MainWindow", "1 Bit"))
        self.action2_Bit.setText(_translate("MainWindow", "2 Bit"))
        self.action3_Bit.setText(_translate("MainWindow", "3 Bit"))
        self.action_Bit.setText(_translate("MainWindow", "4 Bit"))
        self.action5_Bit.setText(_translate("MainWindow", "5 Bit"))
        self.action6_Bit.setText(_translate("MainWindow", "6 Bit"))
        self.action7_Bit.setText(_translate("MainWindow", "7 Bit"))
        self.actionTentang.setText(_translate("MainWindow", "Tentang"))
        self.actionHistogram_Equalization.setText(_translate("MainWindow", "Histogram Equalization"))
        self.actionFuzzy_HE_RGB.setText(_translate("MainWindow", "Fuzzy HE RGB"))
        self.actionFuzzy_Grayscale.setText(_translate("MainWindow", "Fuzzy Grayscale"))
        self.actionSegmen_Citra.setText(_translate("MainWindow", "Segmen Citra"))
        self.actionTresholding.setText(_translate("MainWindow", "Tresholding"))
        self.actionAritmatika.setText(_translate("MainWindow", "Aritmatika"))
        self.actionFlipHorizontal.setText(_translate("MainWindow", "Flip Horizontal"))
        self.actionFlipVertical.setText(_translate("MainWindow", "Flip Vertical"))
        self.actionRotate.setText(_translate("MainWindow", "Rotate"))
        self.actionUniform_Scale.setText(_translate("MainWindow", "Uniform Scale"))
        self.actionNonUniform_Scale.setText(_translate("MainWindow", "Non Unifrom Scale"))
        self.actionTranlasi.setText(_translate("MainWindow", "Translasi"))
        self.actionCropping.setText(_translate("MainWindow", "Crop Image"))
        self.actionROI.setText(_translate("MainWindow", "ROI"))
        self.actionBackground_Removal.setText(_translate("MainWindow", "Background Removal"))
        self.actionIdentity.setText(_translate("MainWindow", "Identity"))
        self.actionSharpen.setText(_translate("MainWindow", "Sharpen"))
        self.actionUnsharp_Masking.setText(_translate("MainWindow", "Unsharp Masking"))
        self.actionAverage_Filter.setText(_translate("MainWindow", "Average Filter"))
        self.actionLow_Pass_Filter.setText(_translate("MainWindow", "Low Pass Filter"))
        self.actionHigh_Pass_Filter.setText(_translate("MainWindow", "High Pass Filter"))
        self.actionBandstop_Filter.setText(_translate("MainWindow", "Bandstop Filter"))
        self.actionPrewitt.setText(_translate("MainWindow", "Prewitt"))
        self.actionSobel.setText(_translate("MainWindow", "Sobel"))
        self.actionRobert.setText(_translate("MainWindow", "Robert"))
        self.actionSquare_3.setText(_translate("MainWindow", "Square 3"))
        self.actionSquare_5.setText(_translate("MainWindow", "Square 5"))
        self.actionCross_3.setText(_translate("MainWindow", "Cross 3"))
        self.actionSquare_4.setText(_translate("MainWindow", "Square 3"))
        self.actionSquare_6.setText(_translate("MainWindow", "Square 5"))
        self.actionCross_4.setText(_translate("MainWindow", "Cross 3"))
        self.actionSquare_9.setText(_translate("MainWindow", "Square 9"))
        self.actionSquare_10.setText(_translate("MainWindow", "Square 9"))
        self.actionClear.setText(_translate("MainWindow", "Clear"))
        self.actionEdge_Detection_1.setText(_translate("MainWindow", "Edge Detection 1"))
        self.actionEdge_Detection_2.setText(_translate("MainWindow", "Edge Detection 2"))
        self.actionEdge_Detection_3.setText(_translate("MainWindow", "Edge Detection 3"))
        self.actionGaussian_Blur_3x3.setText(_translate("MainWindow", "Gaussian Blur 3x3"))
        self.actionGaussian_Blur_5x5.setText(_translate("MainWindow", "Gaussian Blur 5x5"))
        
        # Membuat instance BrightnessContrastForm sebagai atribut
        self.brightness_contrast_form = BrightnessContrastForm()

        # Menghubungkan tombol Brightness & Contrast dengan method showBrightnessContrastForm
        self.actionBrightnessness_contras.triggered.connect(self.showBrightnessContrastForm)

    
    #Fungsi buka GUI tentang
    def frameTentang(self): 
        # Definisi fungsi frameArimatika yang merupakan metode dari suatu kelas. Fungsi ini mungkin digunakan untuk membuat dan menampilkan sebuah jendela Qt.
        self.window = QtWidgets.QMainWindow() # Membuat sebuah objek jendela utama dari Qt.
        self.ui = latihan1() # Membuat sebuah objek dari kelas latihan.
        self.ui.setupUi(self.window) # Memanggil metode setupUi dari objek ui untuk menginisialisasi tampilan antarmuka.
        self.window.show()  # Menampilkan jendela utama.
    
    #Fungsi buka GUI Aritmatika    
    def frameArimatika(self): 
        # Definisi fungsi frameArimatika yang merupakan metode dari suatu kelas. Fungsi ini mungkin digunakan untuk membuat dan menampilkan sebuah jendela Qt.
        self.window = QtWidgets.QMainWindow() # Membuat sebuah objek jendela utama dari Qt.
        self.ui = latihan() # Membuat sebuah objek dari kelas latihan.
        self.ui.setupUi(self.window) # Memanggil metode setupUi dari objek ui untuk menginisialisasi tampilan antarmuka.
        self.window.show()  # Menampilkan jendela utama.
    
    #Fungsi flip horizontal 
    def fliphorizontal(self):
            toImg = self.label.pixmap()
            img = toImg.toImage()
            width = img.width()
            height = img.height()

            # Create a numpy array to store the flipped image
            flipped_image = QtGui.QImage(width, height, QtGui.QImage.Format_RGBA8888)

            for y in range(height):
                for x in range(width):
                    pixel_color = QtGui.QColor(img.pixel(x, y))
                    flipped_image.setPixelColor(width - 1 - x, y, pixel_color)       

            flipped_pixmap = QtGui.QPixmap.fromImage(flipped_image)
            self.label_2.setPixmap(flipped_pixmap)
            self.label_2.setAlignment(QtCore.Qt.AlignCenter)
    
    #flip vertikal
    def flipvertikal(self):
            toImg = self.label.pixmap()
            img = toImg.toImage()
            width = img.width()
            height = img.height()

            # Create a numpy array to store the flipped image
            flipped_image = QtGui.QImage(width, height, QtGui.QImage.Format_RGBA8888)

            for y in range(height):
                for x in range(width):
                    pixel_color = QtGui.QColor(img.pixel(x, y))
                    flipped_image.setPixelColor(x, height - 1 - y, pixel_color) 

            flipped_pixmap = QtGui.QPixmap.fromImage(flipped_image)
            self.label_2.setPixmap(flipped_pixmap)
            self.label_2.setAlignment(QtCore.Qt.AlignCenter)

    #Fungsi rotate image
    def rotateImage(self):
        rotation , ok = QtWidgets.QInputDialog.getInt(None , "Rotate Image","Enter rotation angle (degress):",0,-360,360)
        if ok:
            current_pixmap = self.label.pixmap()
            second_pixmap = self.label_2.pixmap()
            
            if self.label_2.pixmap() is None:
                    rotated_image = current_pixmap.transformed(QtGui.QTransform().rotate(rotation))
                    # rotated_pixmap = QtGui.QPixmap.fromImage(rotated_image)
                    self.label_2.setPixmap(rotated_image)
                    self.label_2.setAlignment(QtCore.Qt.AlignCenter)
                    self.label_2.setScaledContents(True)
                    
            else:    
                    rotated_image = second_pixmap.transformed(QtGui.QTransform().rotate(rotation))
                    # rotated_pixmap = QtGui.QPixmap.fromImage(rotated_image)
                    self.label_2.setPixmap(rotated_image)
                    self.label_2.setAlignment(QtCore.Qt.AlignCenter)
                    self.label_2.setScaledContents(True)
                    
    def UniformScale(self):
        scale_factor, ok = QInputDialog.getDouble(None, 'Uniform Scaling', 'Enter scale factor:')
        
        if ok:
            self.scaleImage(scale_factor)
            
    #Fungsi tresholding
    def Thresholding(self):
        if self.label:
            # Convert QPixmap to QImage for image processing
            input_qimage = self.label.pixmap().toImage()
            width = input_qimage.width()
            height = input_qimage.height()

            # Create a new QImage for the processed image
            output_qimage = QtGui.QImage(width, height, QtGui.QImage.Format_RGB32)

            # Set threshold value (adjust as needed)
            threshold_value = 128

            # Apply Thresholding
            for x in range(width):
                for y in range(height):
                    pixel_color = QtGui.QColor(input_qimage.pixel(x, y))
                    # Calculate grayscale value (average of R, G, B)
                    grayscale_value = (pixel_color.red() + pixel_color.green() + pixel_color.blue()) // 3

                    # Apply thresholding
                    if grayscale_value < threshold_value:
                        output_qimage.setPixelColor(x, y, QtGui.QColor(0, 0, 0))  # Set pixel to black
                    else:
                        output_qimage.setPixelColor(x, y, QtGui.QColor(255, 255, 255))  # Set pixel to white

            # Convert QImage to QPixmap for display
            self.output_image = QtGui.QPixmap.fromImage(output_qimage)
            self.label_2.setPixmap(self.output_image)
            self.label_2.setScaledContents(True)
            self.simpan=output_qimage
        
        
    def scaleImage(self, scale_factor):
        transform = QtGui.QTransform()
        transform.scale(scale_factor, scale_factor)
        input_image = self.label.pixmap()
        p = input_image.transformed(transform)
        self.label_2.setPixmap(p)
        self.label_2.setScaledContents(False)
        
    def NonUnishowScaleDialog(self):
        scaleX, ok1 = QInputDialog.getDouble(None, 'Non-Uniform Scaling', 'Enter scale factor for X-axis:')
        scaleY, ok2 = QInputDialog.getDouble(None, 'Non-Uniform Scaling', 'Enter scale factor for Y-axis:')
        
        if ok1 and ok2:
            self.NonUniscaleImage(scaleX, scaleY)

    def NonUniscaleImage(self, scaleX, scaleY):
        transform = QtGui.QTransform()
        transform.scale(scaleX, scaleY)
        input_image = self.label.pixmap()
        p = input_image.transformed(transform)
        self.label_2.setPixmap(p)
        self.label_2.setScaledContents(False)
        
    def identity_filter(self):
        if self.label.pixmap() is None:
            QtWidgets.QMessageBox.information(self, "Information", "Tidak ada citra yang akan diolah")
        else:
            pixmap = self.label.pixmap()
            image = pixmap.toImage()

            identityFilter = [
                [0, 0, 0],
                [0, 1, 0],
                [0, 0, 0]
            ]

            for i in range(image.width()):
                for j in range(image.height()):
                    c1 = QtGui.QColor(image.pixel(i, j))
                    c1r = 0
                    c1g = 0
                    c1b = 0

                    for k in range(-1, 2):
                        for l in range(-1, 2):
                            posX = i + k
                            posY = j + l

                            if 0 <= posX < image.width() and 0 <= posY < image.height():
                                c2 = QtGui.QColor(image.pixel(posX, posY))
                                c1r += identityFilter[k + 1][l + 1] * c2.red()
                                c1g += identityFilter[k + 1][l + 1] * c2.green()
                                c1b += identityFilter[k + 1][l + 1] * c2.blue()

                    image.setPixel(i, j, QtGui.qRgb(c1r, c1g, c1b))
            self.label_2.setPixmap(QtGui.QPixmap.fromImage(image))
            
    def apply_edge_detection_filter(self):
        if self.label.pixmap() is not None:
            image = self.label.pixmap().toImage()
            result_image = self.apply_edge_detection_filter_to_image(image)
            pixmap = QtGui.QPixmap.fromImage(result_image)
            self.label_2.setPixmap(pixmap)
            self.label_2.setScaledContents(True)

    def apply_edge_detection_filter_to_image(self, image):
        img_data = QtGui.QImage(image)
        img_width = img_data.width()
        img_height = img_data.height()

        kernel = np.array([[1, 0, -1], [0, 0, 0], [-1, 0, 1]])

        for i in range(img_width - 2):
            for j in range(img_height - 2):
                c1r = 0
                c1g = 0
                c1b = 0

                for k in range(3):
                    for l in range(3):
                        pixel = QtGui.QColor(img_data.pixel(i + k, j + l))
                        c1r += kernel[k, l] * pixel.red()
                        c1g += kernel[k, l] * pixel.green()
                        c1b += kernel[k, l] * pixel.blue()

                c1r = max(0, min(255, c1r))
                c1g = max(0, min(255, c1g))
                c1b = max(0, min(255, c1b))

                img_data.setPixel(i, j, QtGui.qRgb(c1r, c1g, c1b))

        return img_data
    
    def apply_edge_detection2_filter(self):
        if self.label.pixmap() is not None:
            image = self.label.pixmap().toImage()
            result_image = self.apply_edge_detection2_filter_to_image(image)
            pixmap = QtGui.QPixmap.fromImage(result_image)
            self.label_2.setPixmap(pixmap)
            self.label_2.setScaledContents(True)
            
    def apply_edge_detection2_filter_to_image(self, image):
        img_data = QtGui.QImage(image)
        img_width = img_data.width()
        img_height = img_data.height()

        kernel = np.array([[0, 1, 0], [1, -4, 1], [0, 1, 0]])

        for i in range(img_width):
            for j in range(img_height):
                c1r = 0
                c1g = 0
                c1b = 0

                for k in range(3):
                    for l in range(3):
                        posX = i + k
                        posY = j + l

                        if 0 <= posX < img_width and 0 <= posY < img_height:
                            pixel = QtGui.QColor(img_data.pixel(posX, posY))
                            c1r += kernel[k, l] * pixel.red()
                            c1g += kernel[k, l] * pixel.green()
                            c1b += kernel[k, l] * pixel.blue()

                c1r = max(0, min(255, c1r))
                c1g = max(0, min(255, c1g))
                c1b = max(0, min(255, c1b))

                img_data.setPixel(i, j, QtGui.qRgb(c1r, c1g, c1b))

        return img_data
    
    def apply_edge_detection3_filter(self):
        if self.label.pixmap() is not None:
            image = self.label.pixmap().toImage()
            result_image = self.apply_edge_detection3_filter_to_image(image)
            pixmap = QtGui.QPixmap.fromImage(result_image)
            self.label_2.setPixmap(pixmap)
            self.label_2.setScaledContents(True)

    def apply_edge_detection3_filter_to_image(self, image):
        img_data = QtGui.QImage(image)
        img_width = img_data.width()
        img_height = img_data.height()

        kernel = np.array([[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]])

        for i in range(img_width):
            for j in range(img_height):
                c1r = 0
                c1g = 0
                c1b = 0

                for k in range(3):
                    for l in range(3):
                        posX = i + k
                        posY = j + l

                        if 0 <= posX < img_width and 0 <= posY < img_height:
                            pixel = QtGui.QColor(img_data.pixel(posX, posY))
                            c1r += kernel[k, l] * pixel.red()
                            c1g += kernel[k, l] * pixel.green()
                            c1b += kernel[k, l] * pixel.blue()

                c1r = max(0, min(255, c1r))
                c1g = max(0, min(255, c1g))
                c1b = max(0, min(255, c1b))

                img_data.setPixel(i, j, QtGui.qRgb(c1r, c1g, c1b))

        return img_data
            
    def apply_sharpen_filter(self):
        if self.label:
            # Convert QPixmap to QImage for image processing
            input_qimage = self.label.pixmap().toImage()
            width = input_qimage.width()
            height = input_qimage.height()

            # Create a new QImage for the processed image
            output_qimage = QtGui.QImage(width, height, QtGui.QImage.Format_RGB32)

            # Create a sharpening kernel (you can adjust the kernel values) 
            kernel = np.array([[-1, -1, -1],
                               [-1,  9, -1],
                               [-1, -1, -1]])

            # Apply the convolution operation to sharpen the image
            for x in range(1, width - 1):
                for y in range(1, height - 1):
                    new_color = [0, 0, 0]

                    for dx in range(3):
                        for dy in range(3):
                            pixel_color = QtGui.QColor(input_qimage.pixel(x + dx - 1, y + dy - 1))
                            new_color[0] += pixel_color.red() * kernel[dx][dy]
                            new_color[1] += pixel_color.green() * kernel[dx][dy]
                            new_color[2] += pixel_color.blue() * kernel[dx][dy]

                    for i in range(3):
                        new_color[i] = min(max(new_color[i], 0), 255)

                    output_qimage.setPixelColor(x, y, QtGui.QColor(new_color[0], new_color[1], new_color[2]))

            # Convert QImage to QPixmap for display
            self.output_image = QtGui.QPixmap.fromImage(output_qimage)
            self.label_2.setPixmap(self.output_image)
            self.label_2.setScaledContents(True)
            
    # def applyGaussianBlur3(self):
    #     if self.label:
    #         # Convert QPixmap to QImage for image processing
    #         input_qimage = self.label.pixmap().toImage()
    #         width = input_qimage.width()
    #         height = input_qimage.height()

    #         # Create a new QImage for the processed image
    #         output_qimage = QtGui.QImage(width, height, QtGui.QImage.Format_RGB32)

    #         # Gaussian kernel
    #         kernel = np.array([[1, 2, 1],
    #                            [2, 4, 2],
    #                            [1, 2, 1]])

    #         kernel = kernel / 16.0  # Normalize the kernel

    #         for x in range(1, width - 1):
    #             for y in range(1, height - 1):
    #                 r, g, b, _ = input_qimage.pixelColor(x, y).getRgb()

    #                 r_sum = 0
    #                 g_sum = 0
    #                 b_sum = 0

    #                 for i in range(-1, 2):
    #                     for j in range(-1, 2):
    #                         neighbor_color = input_qimage.pixelColor(x + i, y + j)
    #                         neighbor_r, neighbor_g, neighbor_b, _ = neighbor_color.getRgb()

    #                         r_sum += neighbor_r * kernel[i + 1][j + 1]
    #                         g_sum += neighbor_g * kernel[i + 1][j + 1]
    #                         b_sum += neighbor_b * kernel[i + 1][j + 1]

    #                 # Set the new pixel color
    #                 output_qimage.setPixelColor(x, y, QtGui.QColor(int(r_sum), int(g_sum), int(b_sum)))

    #         self.output_image = QtGui.QPixmap.fromImage(output_qimage)
    #         self.label_2.setPixmap(self.output_image)
    #         self.label_2.setScaledContents(True)
    
    def applyGaussianBlur3(self):
        if self.label:
            # Convert QPixmap to QImage for image processing
            input_qimage = self.label.pixmap().toImage()
            width = input_qimage.width()
            height = input_qimage.height()

            # Convert QImage to a numpy array
            input_image = input_qimage.bits().asstring(width * height * 4)
            input_image = np.frombuffer(input_image, dtype=np.uint8).reshape((height, width, 4))

            # Convert RGBA to RGB (drop the alpha channel)
            input_image_rgb = cv2.cvtColor(input_image, cv2.COLOR_RGBA2RGB)

            # Apply Gaussian Blur using OpenCV
            kernel_size = (3, 3)  # Kernel size as per the provided manual kernel
            sigma = 1.0  # Standard deviation for Gaussian kernel, adjust as needed
            blurred_image = cv2.GaussianBlur(input_image_rgb, kernel_size, sigma)

            # Convert back to QImage
            output_qimage = QtGui.QImage(blurred_image.data, blurred_image.shape[1], blurred_image.shape[0], blurred_image.strides[0], QtGui.QImage.Format_RGB888)

            # Convert QImage to QPixmap and set it to the label
            self.output_image = QtGui.QPixmap.fromImage(output_qimage)
            self.label_2.setPixmap(self.output_image)
            self.label_2.setScaledContents(True)


    def applyGaussianBlur5(self):
        if self.label:
            # Convert QPixmap to QImage for image processing
            input_qimage = self.label.pixmap().toImage()
            width = input_qimage.width()
            height = input_qimage.height()

            # Create a new QImage for the processed image
            output_qimage = QtGui.QImage(width, height, QtGui.QImage.Format_RGB32)

            # Define Gaussian Kernel (5x5)
            kernel = np.array([
                [1, 4, 6, 4, 1],
                [4, 16, 24, 16, 4],
                [6, 24, 36, 24, 6],
                [4, 16, 24, 16, 4],
                [1, 4, 6, 4, 1]
            ]) / 256.0  # Normalize the kernel

            # Apply Gaussian Blur
            for x in range(2, width - 2):
                for y in range(2, height - 2):
                    r, g, b = 0, 0, 0
                    for i in range(-2, 3):
                        for j in range(-2, 3):
                            pixel_color = QtGui.QColor(input_qimage.pixel(x + i, y + j))
                            r += pixel_color.red() * kernel[i + 2][j + 2]
                            g += pixel_color.green() * kernel[i + 2][j + 2]
                            b += pixel_color.blue() * kernel[i + 2][j + 2]

                    # Set the new pixel color
                    output_qimage.setPixelColor(x, y, QtGui.QColor(int(r), int(g), int(b)))

            # Convert QImage to QPixmap for display
            self.output_image = QtGui.QPixmap.fromImage(output_qimage)
            self.label_2.setPixmap(self.output_image)
            self.label_2.setScaledContents(True)
            self.simpan=output_qimage
    
    def apply_high_pass_filter(self):
        if self.label.pixmap() is not None:
            image = self.label.pixmap().toImage()
            result_image = self.apply_filter(image)  # Memanggil metode filter High-Pass
            pixmap = QtGui.QPixmap.fromImage(result_image)
            self.label_2.setPixmap(pixmap)
            self.label_2.setScaledContents(True)
            
    def apply_filter(self, image):
        avg_filter = [
            [-1, 0, 1],
            [-1, 0, 3],
            [-3, 0, 1]
        ]

        for i in range(image.width()):
            for j in range(image.height()):
                c1 = QtGui.QColor(image.pixel(i, j))
                c1r = 0
                c1g = 0
                c1b = 0

                for k in range(3):
                    posX = i
                    posX += k

                    for l in range(3):
                        posY = j
                        posY += l

                        if 0 <= posX < image.width() and 0 <= posY < image.height():
                            c1r += ((avg_filter[k][l]) * QtGui.QColor(image.pixel(i + k, j + l)).red())
                            c1g += ((avg_filter[k][l]) * QtGui.QColor(image.pixel(i + k, j + l)).green())
                            c1b += ((avg_filter[k][l]) * QtGui.QColor(image.pixel(i + k, j + l)).blue())

                image.setPixel(i, j, QtGui.QColor(self.truncate(int(c1r)), self.truncate(int(c1g)), self.truncate(int(c1b))).rgb())

        return image

    def truncate(self, x):
        if x > 255:
            return 255
        elif x < 0:
            return 0
        return x
            
    def apply_unsharp_masking_filter(self):
        if self.label.pixmap() is not None:
            image = self.label.pixmap().toImage()
            result_image = self.apply_unsharp_mask_to_image(image)
            pixmap = QtGui.QPixmap.fromImage(result_image)
            self.label_2.setPixmap(pixmap)
            self.label_2.setScaledContents(True)
            self.simpan=pixmap

    def apply_unsharp_mask_to_image(self, image):
        unsharp_mask_filter = np.array([[1, 4, 6, 4, 1],
                                        [4, 16, 24, 16, 4],
                                        [6, 24, -476, 24, 6],
                                        [4, 16, 24, 16, 4],
                                        [1, 4, 6, 4, 1]])

        img_data = QtGui.QImage(image)
        img_width = img_data.width()
        img_height = img_data.height()

        result_image = QtGui.QImage(img_width, img_height, QtGui.QImage.Format_RGB32)

        for i in range(img_width):
            for j in range(img_height):
                c1 = img_data.pixelColor(i, j)
                c1r = 0
                c1g = 0
                c1b = 0

                posX = 0
                posY = 0

                for k in range(5):
                    posX = i
                    posX += k

                    for l in range(5):
                        posY = j
                        posY += l

                        if posX < 0 or posY < 0 or posX >= img_width or posY >= img_height:
                            c1r += 0
                            c1g += 0
                            c1b += 0
                        else:
                            c1r += ((-1 * unsharp_mask_filter[k, l] / 256) * img_data.pixelColor(i + k, j + l).red())
                            c1g += ((-1 * unsharp_mask_filter[k, l] / 256) * img_data.pixelColor(i + k, j + l).green())
                            c1b += ((-1 * unsharp_mask_filter[k, l] / 256) * img_data.pixelColor(i + k, j + l).blue())

                result_image.setPixel(i, j, QtGui.qRgb(self.truncate(int(c1r)), self.truncate(int(c1g)), self.truncate(int(c1b))))

        return result_image
            
    def apply_bandstop_filter(self):
        if self.label.pixmap() is not None:
            image = self.label.pixmap().toImage()
            result_image = self.apply_bandstop_filter_to_image(image)
            pixmap = QtGui.QPixmap.fromImage(result_image)
            self.label_2.setPixmap(pixmap)
            self.label_2.setScaledContents(True)

    def apply_bandstop_filter_to_image(self, image):
        avg_filter = np.array([[1, -1, 1], [-1, 0.5, -1], [1, -1, 1]])

        img_data = QtGui.QImage(image)
        img_width = img_data.width()
        img_height = img_data.height()

        result_image = QtGui.QImage(img_width, img_height, QtGui.QImage.Format_RGB32)

        for i in range(img_width):
            for j in range(img_height):
                c1 = QtGui.QColor(img_data.pixel(i, j))
                c1r = 0
                c1g = 0
                c1b = 0

                for k in range(3):
                    for l in range(3):
                        pos_x = i + k - 1
                        pos_y = j + l - 1

                        if pos_x < 0 or pos_y < 0 or pos_x >= img_width or pos_y >= img_height:
                            c1r += 0
                            c1g += 0
                            c1b += 0
                        else:
                            c1r += avg_filter[k, l] * QtGui.QColor(img_data.pixel(pos_x, pos_y)).red()
                            c1g += avg_filter[k, l] * QtGui.QColor(img_data.pixel(pos_x, pos_y)).green()
                            c1b += avg_filter[k, l] * QtGui.QColor(img_data.pixel(pos_x, pos_y)).blue()

                result_image.setPixel(i, j, QtGui.qRgb(int(self.truncate(c1r)), int(self.truncate(c1g)), int(self.truncate(c1b))))

        return result_image

    def truncate(self, x):
        if x > 255:
            return 255
        elif x < 0:
            return 0
        return x

    def prewittEdgeDetection(self):
        if self.label.pixmap() is not None:
            image = self.label.pixmap().toImage()
            result_image = self.apply_prewitt_filter_to_image(image)
            pixmap = QtGui.QPixmap.fromImage(result_image)
            self.label_2.setPixmap(pixmap)
            self.label_2.setScaledContents(True)
            self.simpan=pixmap
            
            
    def apply_prewitt_filter_to_image(self, image):
        prewitt_filter = np.array([[0, 1, 1], [-1, 0, 1], [-1, -1, 0]])

        img_data = QtGui.QImage(image)
        img_width = img_data.width()
        img_height = img_data.height()

        result_image = QtGui.QImage(img_width, img_height, QtGui.QImage.Format_RGB32)

        for i in range(img_width):
            for j in range(img_height):
                c1 = QtGui.QColor(img_data.pixel(i, j))
                c1r = 0
                c1g = 0
                c1b = 0

                for k in range(3):
                    for l in range(3):
                        pos_x = i + k - 1
                        pos_y = j + l - 1

                        if pos_x < 0 or pos_y < 0 or pos_x >= img_width or pos_y >= img_height:
                            c1r += 0
                            c1g += 0
                            c1b += 0
                        else:
                            c1r += prewitt_filter[k, l] * QtGui.QColor(img_data.pixel(pos_x, pos_y)).red()
                            c1g += prewitt_filter[k, l] * QtGui.QColor(img_data.pixel(pos_x, pos_y)).green()
                            c1b += prewitt_filter[k, l] * QtGui.QColor(img_data.pixel(pos_x, pos_y)).blue()

                result_image.setPixel(i, j, QtGui.qRgb(int(self.truncate(c1r)), int(self.truncate(c1g)), int(self.truncate(c1b))))

        return result_image

    def truncate(self, x):
        if x > 255:
            return 255
        elif x < 0:
            return 0
        return x
    


    # def prewittEdgeDetection(self):
    #     if self.label.pixmap() is not None:
    #         pixmap = self.label.pixmap()
    #         image = pixmap.toImage()
    #         result_image = self.apply_prewitt_filter_to_image(image)
    #         self.label_2.setPixmap(QtGui.QPixmap.fromImage(result_image))
    #         self.label_2.setScaledContents(True)

    # def apply_prewitt_filter_to_image(self, image):
    #     # Convert QPixmap to numpy array
    #     img_data = np.array(image.convertToFormat(QtGui.QImage.Format_RGB888))

    #     # Convert image data to format supported by OpenCV
    #     img_data_cv = cv2.cvtColor(img_data, cv2.COLOR_RGB2BGR)

    #     # Convert to grayscale
    #     gray = cv2.cvtColor(img_data_cv, cv2.COLOR_BGR2GRAY)

    #     # Define Prewitt kernels
    #     kernelx = np.array([[1, 0, -1], [1, 0, -1], [1, 0, -1]])
    #     kernely = np.array([[1, 1, 1], [0, 0, 0], [-1, -1, -1]])

    #     # Apply Prewitt filter
    #     img_prewittx = cv2.filter2D(gray, -1, kernelx)
    #     img_prewitty = cv2.filter2D(gray, -1, kernely)

    #     # Combine both directions
    #     img_prewitt = cv2.bitwise_or(img_prewittx, img_prewitty)

    #     # Convert to QImage
    #     height, width = img_prewitt.shape
    #     bytesPerLine = width
    #     result_image = QtGui.QImage(img_prewitt.data, width, height, bytesPerLine, QtGui.QImage.Format_Grayscale8)
        
    #     return result_image



    def sobelEdgeDetection(self):
        if self.label.pixmap() is not None:
            image = self.label.pixmap().toImage()
            result_image = self.apply_sobel_filter_to_image(image)
            pixmap = QtGui.QPixmap.fromImage(result_image)
            self.label_2.setPixmap(pixmap)
            self.label_2.setScaledContents(True)
            
    def apply_sobel_filter_to_image(self, image):
        sobel_filter = np.array([[0, -1, -2], [1, 0, -1], [2, 1, 0]])

        img_data = QtGui.QImage(image)
        img_width = img_data.width()
        img_height = img_data.height()

        result_image = QtGui.QImage(img_width, img_height, QtGui.QImage.Format_RGB32)

        for i in range(img_width):
            for j in range(img_height):
                c1 = QtGui.QColor(img_data.pixel(i, j))
                c1r = 0
                c1g = 0
                c1b = 0

                for k in range(3):
                    for l in range(3):
                        pos_x = i + k - 1
                        pos_y = j + l - 1

                        if pos_x < 0 or pos_y < 0 or pos_x >= img_width or pos_y >= img_height:
                            c1r += 0
                            c1g += 0
                            c1b += 0
                        else:
                            c1r += sobel_filter[k, l] * QtGui.QColor(img_data.pixel(pos_x, pos_y)).red()
                            c1g += sobel_filter[k, l] * QtGui.QColor(img_data.pixel(pos_x, pos_y)).green()
                            c1b += sobel_filter[k, l] * QtGui.QColor(img_data.pixel(pos_x, pos_y)).blue()

                result_image.setPixel(i, j, QtGui.qRgb(int(self.truncate(c1r)), int(self.truncate(c1g)), int(self.truncate(c1b))))

        return result_image
    
    def applyRobertFilter(self):
        if self.label.pixmap() is not None:
            # Convert QPixmap to QImage for image processing
            input_qimage = self.label.pixmap().toImage()
            width = input_qimage.width()
            height = input_qimage.height()

             # Create a new QImage for the processed image
            output_qimage = QtGui.QImage(width, height, QtGui.QImage.Format_RGB32)

            # Define Robert Filter kernels for two directions
            kernel_x = np.array([[-1, 0], [0, 1]])
            kernel_y = np.array([[0, -1], [1, 0]])

            for x in range(1, width - 1):
                for y in range(1, height - 1):
                    sum_x = sum_y = 0

                    for i in range(2):
                        for j in range(2):
                            pixel_color = QtGui.QColor(input_qimage.pixel(x - 1 + i, y - 1 + j))
                            gray = pixel_color.red()  # Assuming it's a grayscale image

                            sum_x += gray * kernel_x[i][j]
                            sum_y += gray * kernel_y[i][j]

             # Calculate the gradient magnitude
                    magnitude = int(np.sqrt(sum_x**2 + sum_y**2))
                    output_qimage.setPixelColor(x, y, QtGui.QColor(magnitude, magnitude, magnitude))

            # Convert QImage to QPixmap for display
            self.output_image = QtGui.QPixmap.fromImage(output_qimage)
            self.label_2.setPixmap(self.output_image)
            self.label_2.setScaledContents(True)

    def average_filter(self):
        if self.label.pixmap() is not None:
            image = self.label.pixmap().toImage()
            result_image = self.apply_average_filter_to_image(image)
            pixmap = QtGui.QPixmap.fromImage(result_image)
            self.label_2.setPixmap(pixmap)
            self.label_2.setScaledContents(True)
            
    def apply_average_filter_to_image(self, image):
        avg_filter = np.array([[1, 1, 1],
                               [1, 1, 1],
                               [1, 1, 1]])

        img_data = QtGui.QImage(image)
        img_width = img_data.width()
        img_height = img_data.height()

        result_image = QtGui.QImage(img_width, img_height, QtGui.QImage.Format_RGB32)

        for i in range(img_width):
            for j in range(img_height):
                c1 = img_data.pixelColor(i, j)
                c1r = 0
                c1g = 0
                c1b = 0

                posX = 0
                posY = 0

                for k in range(3):
                    posX = i
                    posX += k

                    for l in range(3):
                        posY = j
                        posY += l

                        if posX < 0 or posY < 0 or posX >= img_width or posY >= img_height:
                            c1r += 0
                            c1g += 0
                            c1b += 0
                        else:
                            c1r += ((avg_filter[k, l] / 9) * img_data.pixelColor(i + k, j + l).red())
                            c1g += ((avg_filter[k, l] / 9) * img_data.pixelColor(i + k, j + l).green())
                            c1b += ((avg_filter[k, l] / 9) * img_data.pixelColor(i + k, j + l).blue())

                result_image.setPixel(i, j, QtGui.qRgb(self.truncate(int(c1r)), self.truncate(int(c1g)), self.truncate(int(c1b))))

        return result_image

    def low_pass_filter(self):
        if self.label.pixmap() is not None:

            kernel = [[1, 2, 1],
                    [2, 4, 2],
                    [1, 2, 1]]
            kernel_size = 16

            for i in range(1, self.image.width() - 1):
                for j in range(1, self.image.height() - 1):
                    r, g, b = 0, 0, 0
                    for x in range(-1, 2):
                        for y in range(-1, 2):
                            color = QColor(self.image.pixel(i + x, j + y))
                            r += color.red() * kernel[x + 1][y + 1]
                            g += color.green() * kernel[x + 1][y + 1]
                            b += color.blue() * kernel[x + 1][y + 1]

                    r //= kernel_size
                    g //= kernel_size
                    b //= kernel_size
                    self.image.setPixel(i, j, QColor(r, g, b).rgb())
            self.label_2.setPixmap(QPixmap.fromImage(self.image))

    def erodeSquare(self, size):
        if self.label:
            # Convert QPixmap to QImage for image processing
            input_qimage = self.label.pixmap().toImage()
            width = input_qimage.width()
            height = input_qimage.height()

            # Create a new QImage for the processed image
            output_qimage = QtGui.QImage(width, height, QtGui.QImage.Format_RGB32)

            # Define the erosion element (square or cross)
            element = np.ones((size, size), dtype=np.uint8)

            for x in range(width):
                for y in range(height):
                    pixel_color = QtGui.QColor(input_qimage.pixel(x, y))
                    r, g, b, _ = pixel_color.getRgb()

                    # Apply erosion operation
                    if r == 0 and g == 0 and b == 0:
                        neighborhood = np.zeros((size, size), dtype=np.uint8)

                        # Check if the neighborhood matches the element
                        if np.array_equal(neighborhood, element):
                            r = 255
                            g = 255
                            b = 255

                    # Set the new pixel color
                    output_qimage.setPixel(x, y, QtGui.qRgb(r, g, b))

            # Convert QImage to QPixmap for display
            self.output_image = QtGui.QPixmap.fromImage(output_qimage)
            self.label_2.setPixmap(self.output_image)
            self.label_2.setScaledContents(True)

    def erodeSquare3(self):
        self.erodeSquare(3)

    def erodeSquare5(self):
        self.erodeSquare(5)

    def erodeCross3(self):
        if self.label:
            # Convert QPixmap to QImage for image processing
            input_qimage = self.label.pixmap().toImage()
            width = input_qimage.width()
            height = input_qimage.height()

            # Create a new QImage for the processed image
            output_qimage = QtGui.QImage(width, height, QtGui.QImage.Format_RGB32)

            # Define the 3x3 cross element
            element = np.array([[0, 1, 0], [1, 1, 1], [0, 1, 0]], dtype=np.uint8)

            for x in range(width):
                for y in range(height):
                    pixel_color = QtGui.QColor(input_qimage.pixel(x, y))
                    r, g, b, _ = pixel_color.getRgb()

                    # Apply erosion operation
                    if r == 0 and g == 0 and b == 0:
                        neighborhood = np.zeros((3, 3), dtype=np.uint8)

                        for i in range(-1, 2):
                            for j in range(-1, 2):
                                if 0 <= x + i < width and 0 <= y + j < height:
                                    if element[i + 1][j + 1] == 1:
                                        neighbor_color = QtGui.QColor(input_qimage.pixel(x + i, y + j))
                                        neighbor_r, neighbor_g, neighbor_b, _ = neighbor_color.getRgb()

                                        if neighbor_r == 0 and neighbor_g == 0 and neighbor_b == 0:
                                            neighborhood[i + 1][j + 1] = 1

                        # Check if the neighborhood matches the element
                        if np.array_equal(neighborhood, element):
                            r = 255
                            g = 255
                            b = 255

                    # Set the new pixel color
                    output_qimage.setPixel(x, y, QtGui.qRgb(r, g, b))

            # Convert QImage to QPixmap for display
            self.output_image = QtGui.QPixmap.fromImage(output_qimage)
            self.label_2.setPixmap(self.output_image)
            self.label_2.setScaledContents(True)

    def dilateSquare(self, size):
        if self.label:
            # Convert QPixmap to QImage for image processing
            input_qimage = self.label.pixmap().toImage()
            width = input_qimage.width()
            height = input_qimage.height()

            # Create a new QImage for the processed image
            output_qimage = QtGui.QImage(width, height, QtGui.QImage.Format_RGB32)

            # Define the dilation element (square or cross)
            element = np.ones((size, size), dtype=np.uint8)

            for x in range(width):
                for y in range(height):
                    pixel_color = QtGui.QColor(input_qimage.pixel(x, y))
                    r, g, b, _ = pixel_color.getRgb()

                    # Apply dilation operation
                    if r == 255 and g == 255 and b == 255:
                        neighborhood = np.ones((size, size), dtype=np.uint8)

                        # Set the new pixel color if any element in the neighborhood matches
                        if np.any(np.logical_and(neighborhood, element)):
                            r = 0
                            g = 0
                            b = 0

                    # Set the new pixel color
                    output_qimage.setPixel(x, y, QtGui.qRgb(r, g, b))

            # Convert QImage to QPixmap for display
            self.output_image = QtGui.QPixmap.fromImage(output_qimage)
            self.label_2.setPixmap(self.output_image)
            self.label_2.setScaledContents(True)

    def dilateSquare3(self):
        self.dilateSquare(3)

    def dilateSquare5(self):
        self.dilateSquare(5)

    def dilateCross3(self):
        if self.label:
            # Convert QPixmap to QImage for image processing
            input_qimage = self.label.pixmap().toImage()
            width = input_qimage.width()
            height = input_qimage.height()

            # Create a new QImage for the processed image
            output_qimage = QtGui.QImage(width, height, QtGui.QImage.Format_RGB32)

            # Define the 3x3 cross element
            element = np.array([[0, 1, 0], [1, 1, 1], [0, 1, 0]], dtype=np.uint8)

            for x in range(width):
                for y in range(height):
                    pixel_color = QtGui.QColor(input_qimage.pixel(x, y))
                    r, g, b, _ = pixel_color.getRgb()

                    # Apply dilation operation
                    if r == 255 and g == 255 and b == 255:
                        neighborhood = np.zeros((3, 3), dtype=np.uint8)

                        for i in range(-1, 2):
                            for j in range(-1, 2):
                                if 0 <= x + i < width and 0 <= y + j < height:
                                    if element[i + 1][j + 1] == 1:
                                        neighbor_color = QtGui.QColor(input_qimage.pixel(x + i, y + j))
                                        neighbor_r, neighbor_g, neighbor_b, _ = neighbor_color.getRgb()

                                        if neighbor_r == 255 and neighbor_g == 255 and neighbor_b == 255:
                                            neighborhood[i + 1][j + 1] = 1

                        # Set the new pixel color if any element in the neighborhood matches
                        if np.any(np.logical_and(neighborhood, element)):
                            r = 0
                            g = 0
                            b = 0

                    # Set the new pixel color
                    output_qimage.setPixel(x, y, QtGui.qRgb(r, g, b))

            # Convert QImage to QPixmap for display
            self.output_image = QtGui.QPixmap.fromImage(output_qimage)
            self.label_2.setPixmap(self.output_image)
            self.label_2.setScaledContents(True)
            
    def segmentImage(self):
        if self.label:
            # Convert QPixmap to QImage for image processing
            input_qimage = self.label.pixmap().toImage()
            width = input_qimage.width()
            height = input_qimage.height()

            # Create a new QImage for the processed image
            output_qimage = QtGui.QImage(width, height, QtGui.QImage.Format_RGB32)

            for x in range(1, width - 1):
                for y in range(1, height - 1):
                    gx = 0
                    gy = 0

                    for dx in [-1, 0, 1]:
                        for dy in [-1, 0, 1]:
                            pixel_color = QtGui.QColor(input_qimage.pixel(x + dx, y + dy))
                            intensity = pixel_color.red()  # Using red channel for grayscale

                            # Sobel masks
                            if dx == -1:
                                gx -= intensity
                            elif dx == 1:
                                gx += intensity
                            if dy == -1:
                                gy -= intensity
                            elif dy == 1:
                                gy += intensity

                    edge_intensity = min(int(abs(gx) + abs(gy)), 255)
                    output_qimage.setPixelColor(x, y, QtGui.QColor(edge_intensity, edge_intensity, edge_intensity))

            # Convert QImage to QPixmap for display
            self.output_image = QtGui.QPixmap.fromImage(output_qimage)
            self.label_2.setPixmap(self.output_image)
            self.label_2.setScaledContents(True)
            
    def applyClosingOperation9(self):
        if self.label:
            # Convert QPixmap to QImage for image processing
            input_qimage = self.label.pixmap().toImage()
            width = input_qimage.width()
            height = input_qimage.height()

            # Create a new QImage for the processed image
            output_qimage = QtGui.QImage(width, height, QtGui.QImage.Format_RGB32)

            # Define a 9x9 square kernel for Closing Operation
            kernel = [[1] * 9 for _ in range(9)]

            # Apply Closing Operation
            for x in range(width):
                for y in range(height):
                    r_sum, g_sum, b_sum = 0, 0, 0
                    for i in range(9):
                        for j in range(9):
                            xi, yj = x + i - 4, y + j - 4
                            if 0 <= xi < width and 0 <= yj < height:
                                pixel_color = QtGui.QColor(input_qimage.pixel(xi, yj))
                                r_sum += pixel_color.red() * kernel[i][j]
                                g_sum += pixel_color.green() * kernel[i][j]
                                b_sum += pixel_color.blue() * kernel[i][j]

                    # Set the new pixel color
                    output_qimage.setPixelColor(x, y, QtGui.QColor(min(r_sum, 255), min(g_sum, 255), min(b_sum, 255)))

            # Convert QImage to QPixmap for display
            self.output_image = QtGui.QPixmap.fromImage(output_qimage)
            self.label_2.setPixmap(self.output_image)
            self.label_2.setScaledContents(True)
                    
    def applyOpening9(self):
        if self.label:
            # Convert QPixmap to QImage for image processing
            input_qimage = self.label.pixmap().toImage()
            width = input_qimage.width()
            height = input_qimage.height()

            # Create a new QImage for the processed image
            output_qimage = QtGui.QImage(width, height, QtGui.QImage.Format_RGB32)

            # Define the square kernel (9x9)
            kernel_size = 9
            kernel_radius = kernel_size // 2

            # Apply Opening Operation
            for x in range(kernel_radius, width - kernel_radius):
                for y in range(kernel_radius, height - kernel_radius):
                    min_r, min_g, min_b = 255, 255, 255
                    max_r, max_g, max_b = 0, 0, 0

                    for i in range(-kernel_radius, kernel_radius + 1):
                        for j in range(-kernel_radius, kernel_radius + 1):
                            pixel_color = QtGui.QColor(input_qimage.pixel(x + i, y + j))
                            min_r = min(min_r, pixel_color.red())
                            min_g = min(min_g, pixel_color.green())
                            min_b = min(min_b, pixel_color.blue())
                            max_r = max(max_r, pixel_color.red())
                            max_g = max(max_g, pixel_color.green())
                            max_b = max(max_b, pixel_color.blue())

                    # Set the new pixel color
                    output_qimage.setPixelColor(x, y, QtGui.QColor(max_r, max_g, max_b))

            # Convert QImage to QPixmap for display
            self.output_image = QtGui.QPixmap.fromImage(output_qimage)
            self.label_2.setPixmap(self.output_image)
            self.label_2.setScaledContents(True)

            
    def showBrightnessContrastForm(self):
        if self.label.pixmap() is not None:
            frm2 = BrightnessContrastForm(self.centralwidget)
            if frm2.exec_() == QtWidgets.QDialog.Accepted:
                self.progressBar.setVisible(True)
                pixmap = self.label.pixmap()
                image = pixmap.toImage()
                b = QtGui.QImage(image)

                nilaiBrightness = frm2.tbBrightness.text()
                nilaiContrast = frm2.tbContrast.text()
                f = (259 * (int(nilaiContrast) + 255)) / (255 * (259 - int(nilaiContrast)))

                for i in range(b.width()):
                    for j in range(b.height()):
                        color = QtGui.QColor(b.pixel(i, j))
                        r1 = self.truncate(color.red() + int(nilaiBrightness) + (int(f) * (color.red() - 128) + 128))
                        g1 = self.truncate(color.green() + int(nilaiBrightness) + (int(f) * (color.green() - 128) + 128))
                        b1 = self.truncate(color.blue() + int(nilaiBrightness) + (int(f) * (color.blue() - 128) + 128))
                        b.setPixel(i, j, QtGui.qRgb(r1, g1, b1))
                    self.progressBar.setValue(int(100 * (i + 1) / b.width()))

                self.progressBar.setVisible(False)
                self.label_2.setPixmap(QtGui.QPixmap.fromImage(b))

    def truncate(self, value):
        return max(0, min(255, value))
    
    def log_brightness(self):
        if self.label.pixmap() is not None:
            frm3 = LogBrightness()
            if frm3.exec_() == QtWidgets.QDialog.Accepted:
                pixmap = self.label.pixmap()
                image = pixmap.toImage()
                nilaiBrightness = float(frm3.tbLogBrightness.text())

                for i in range(image.width()):
                    for j in range(image.height()):
                        color = QtGui.QColor(image.pixel(i, j))
                        r1 = nilaiBrightness * math.log10(1 + color.red())
                        g1 = nilaiBrightness * math.log10(1 + color.green())
                        b1 = nilaiBrightness * math.log10(1 + color.blue())
                        image.setPixel(i, j, QtGui.QColor(int(r1), int(g1), int(b1)).rgb())

                self.label_2.setPixmap(QtGui.QPixmap.fromImage(image))
                
    def gamma_correction_triggered(self):
        if self.label.pixmap() is not None:
            frm4 = GammaTransform()
            if frm4.exec_() == QtWidgets.QDialog.Accepted:
                pixmap = self.label.pixmap()
                image = pixmap.toImage()
                nilaiGamma = float(frm4.tbGamma.text())

                for i in range(image.width()):
                    for j in range(image.height()):
                        color = QtGui.QColor(image.pixel(i, j))
                        merah = color.redF()
                        hijau = color.greenF()
                        biru = color.blueF()
                        r1 = int(255 * pow(merah, nilaiGamma))
                        g1 = int(255 * pow(hijau, nilaiGamma))
                        b1 = int(255 * pow(biru, nilaiGamma))
                        image.setPixelColor(i, j, QtGui.QColor(r1, g1, b1))

                self.label_2.setPixmap(QtGui.QPixmap.fromImage(image))
                
    def bitdepth(self, bit):
        if self.label.pixmap() is not None:
            pixmap = self.label.pixmap()
            image = pixmap.toImage()
            level = 255 / (2**bit - 1)

            for i in range(image.width()):
                for j in range(image.height()):
                    color = QtGui.QColor(image.pixel(i, j))
                    R = int(round(color.red() / level) * level)
                    G = int(round(color.green() / level) * level)
                    B = int(round(color.blue() / level) * level)
                    image.setPixel(i, j, QtGui.qRgb(R, G, B))

            self.label_2.setPixmap(QtGui.QPixmap.fromImage(image))

        # Membuat fungsi grayscale Average
    def convertToGreyscaleAverage(self):
        input_pixmap = self.label.pixmap()
        if input_pixmap:
            input_image = input_pixmap.toImage()
            width = input_image.width()
            height = input_image.height()
            
            # Buat gambar abu-abu dengan ukuran yang sama
            grey_image = QtGui.QImage(width, height, QtGui.QImage.Format_Grayscale8)
            
            for y in range(height):
                for x in range(width):
                    pixel = input_image.pixel(x, y)
                    color = QtGui.QColor(pixel)
                    # Ambil nilai merah, hijau, dan biru dari warna pixel
                    red = color.red()
                    green = color.green()
                    blue = color.blue()
                    # Hitung nilai rata-rata komponen warna dan atur ke nilai abu-abu
                    grey_value = (red + green + blue) // 3
                    
                    grey_pixel = QtGui.qRgb(grey_value, grey_value, grey_value)
                    grey_image.setPixel(x, y, grey_pixel)
            
            self.label_2.setPixmap(QtGui.QPixmap.fromImage(grey_image))
            self.label_2.setScaledContents(True)
            self.simpan=grey_image

    # Membuat fungsi grayscale Lightness
    def convertToGreyscaleLightness(self):
        input_pixmap = self.label.pixmap()
        if input_pixmap:
            input_image = input_pixmap.toImage()
            width = input_image.width()
            height = input_image.height()
            
            # Buat gambar abu-abu dengan ukuran yang sama
            grey_image = QtGui.QImage(width, height, QtGui.QImage.Format_Grayscale8)
            
            for y in range(height):
                for x in range(width):
                    pixel = input_image.pixel(x, y)
                    color = QtGui.QColor(pixel)
                    # Ambil nilai merah, hijau, dan biru dari warna pixel
                    red = color.red()
                    green = color.green()
                    blue = color.blue()
                    # Hitung nilai kecerahan menggunakan metode Lightness
                    max_value = max(red, green, blue)
                    min_value = min(red, green, blue)
                    lightness = (max_value + min_value) // 2
                    grey_pixel = QtGui.qRgb(lightness, lightness, lightness)
                    grey_image.setPixel(x, y, grey_pixel)
            
            self.label_2.setPixmap(QtGui.QPixmap.fromImage(grey_image))
            self.label_2.setScaledContents(True)
            self.simpan=grey_image
            
    #RGB - KUNING
    def convertToYellowRGB(self):
        if self.label.pixmap() is not None:
            image = self.label.pixmap().toImage()
            result_image = self.apply_kuning_filter_to_image(image)
            pixmap = QtGui.QPixmap.fromImage(result_image)
            self.label_2.setPixmap(pixmap)
            self.label_2.setScaledContents(True)
            
    def apply_kuning_filter_to_image(self, image):
        img_data = QtGui.QImage(image)
        img_width = img_data.width()
        img_height = img_data.height()

        for i in range(img_width):
            for j in range(img_height):
                c1 = img_data.pixelColor(i, j)
                r1 = min(c1.red() + 255, 255)
                g1 = min(c1.green() + 255, 255)
                b1 = c1.blue()
                img_data.setPixel(i, j, QtGui.qRgb(r1, g1, b1))

        return img_data
     
    #RGB - ORANGE    
    def convertToOrangeRGB(self):
        if self.label.pixmap() is not None:
            image = self.label.pixmap().toImage()
            result_image = self.apply_orange_filter_to_image(image)
            pixmap = QtGui.QPixmap.fromImage(result_image)
            self.label_2.setPixmap(pixmap)
            self.label_2.setScaledContents(True)
            
    def apply_orange_filter_to_image(self, image):
        img_data = QtGui.QImage(image)
        img_width = img_data.width()
        img_height = img_data.height()

        for i in range(img_width):
            for j in range(img_height):
                c1 = img_data.pixelColor(i, j)
                r1 = min(c1.red() + 255, 255)
                g1 = min(c1.green() + 120, 255)
                b1 = min(c1.blue() + 20, 255)
                img_data.setPixel(i, j, QtGui.qRgb(r1, g1, b1))

        return img_data
      
    #RGB - CYAN  
    def convertToCyanRGB(self):
        if self.label.pixmap() is not None:
            image = self.label.pixmap().toImage()
            result_image = self.apply_cyan_filter_to_image(image)
            pixmap = QtGui.QPixmap.fromImage(result_image)
            self.label_2.setPixmap(pixmap)
            self.label_2.setScaledContents(True)
            
    def apply_cyan_filter_to_image(self, image):
        img_data = QtGui.QImage(image)
        img_width = img_data.width()
        img_height = img_data.height()

        for i in range(img_width):
            for j in range(img_height):
                c1 = img_data.pixelColor(i, j)
                r1 = min(c1.red() + 0, 255)
                g1 = min(c1.green() + 255, 255)
                b1 = min(c1.blue() + 255, 255)
                img_data.setPixel(i, j, QtGui.qRgb(r1, g1, b1))

        return img_data
     
    #RGB - PURPLE    
    def convertToPurpleRGB(self):
        if self.label.pixmap() is not None:
            image = self.label.pixmap().toImage()
            result_image = self.apply_purple_filter_to_image(image)
            pixmap = QtGui.QPixmap.fromImage(result_image)
            self.label_2.setPixmap(pixmap)
            self.label_2.setScaledContents(True)
            
    def apply_purple_filter_to_image(self, image):
        img_data = QtGui.QImage(image)
        img_width = img_data.width()
        img_height = img_data.height()

        for i in range(img_width):
            for j in range(img_height):
                c1 = img_data.pixelColor(i, j)
                r1 = min(c1.red() + 110, 255)
                g1 = min(c1.green() + 20, 255)
                b1 = min(c1.blue() + 100, 255)
                img_data.setPixel(i, j, QtGui.qRgb(r1, g1, b1))

        return img_data

    def convertToGreyRGB(self):
        if self.label.pixmap() is not None:
            image = self.label.pixmap().toImage()
            result_image = self.apply_grey_filter_to_image(image)
            pixmap = QtGui.QPixmap.fromImage(result_image)
            self.label_2.setPixmap(pixmap)
            self.label_2.setScaledContents(True)

    def apply_grey_filter_to_image(self, image):
        img_data = QtGui.QImage(image)
        img_width = img_data.width()
        img_height = img_data.height()

        for i in range(img_width):
            for j in range(img_height):
                c1 = img_data.pixelColor(i, j)
                r1 = min(c1.red() + 128, 255)
                g1 = min(c1.green() + 128, 255)
                b1 = min(c1.blue() + 128, 255)
                avg = (r1 + g1 + b1) // 3
                img_data.setPixel(i, j, QtGui.qRgb(avg, avg, avg))

        return img_data

      
    #RGB - BROWN    
    def convertToBrownRGB(self):
        if self.label.pixmap() is not None:
            image = self.label.pixmap().toImage()
            result_image = self.apply_coklat_filter_to_image(image)
            pixmap = QtGui.QPixmap.fromImage(result_image)
            self.label_2.setPixmap(pixmap)
            self.label_2.setScaledContents(True)
            
    def apply_coklat_filter_to_image(self, image):
        img_data = QtGui.QImage(image)
        img_width = img_data.width()
        img_height = img_data.height()

        for i in range(img_width):
            for j in range(img_height):
                c1 = img_data.pixelColor(i, j)
                r1 = min(c1.red() + 170, 255)
                g1 = min(c1.green() + 121, 255)
                b1 = min(c1.blue() + 60, 255)
                img_data.setPixel(i, j, QtGui.qRgb(r1, g1, b1))

        return img_data
        
    #RGB - RED
    def convertToRedRGB(self):
        if self.label.pixmap() is not None:
            image = self.label.pixmap().toImage()
            result_image = self.apply_merah_filter_to_image(image)
            pixmap = QtGui.QPixmap.fromImage(result_image)
            self.label_2.setPixmap(pixmap)
            self.label_2.setScaledContents(True)

    def apply_merah_filter_to_image(self, image):
        img_data = QtGui.QImage(image)
        img_width = img_data.width()
        img_height = img_data.height()

        for i in range(img_width):
            for j in range(img_height):
                c1 = img_data.pixelColor(i, j)
                r1 = min(c1.red() + 255, 255)
                g1 = min(c1.green() + 0, 255)
                b1 = min(c1.blue() + 0, 255)
                img_data.setPixel(i, j, QtGui.qRgb(r1, g1, b1))

        return img_data
    
    def tranlasi(self):
            if not self.label.pixmap():
                return
            # Menampilkan dialog untuk memasukkan nilai translasi (geser)
            getimage = self.label.pixmap().toImage()
            width = getimage.width()
            height = getimage.height()
            tx, ok1 = QtWidgets.QInputDialog.getInt(None, "Translasi Image", "Enter translation in X direction (pixels):", 0, -width, width)
            ty, ok2 = QtWidgets.QInputDialog.getInt(None, "Translasi Image", "Enter translation in Y direction (pixels):", 0, -height, height)

            if ok1 and ok2:
                # Mendapatkan pixmap yang akan di-translasi
                pixmap = self.label.pixmap()

                # Mendapatkan ukuran asli pixmap
                original_size = pixmap.size()
                width = original_size.width()
                height = original_size.height()

                new_image = QtGui.QImage(original_size, QtGui.QImage.Format_RGB32)
                new_image.fill(QtCore.Qt.white)

                for y in range(height):
                    for x in range(width):
                        # Mendapatkan warna piksel asli
                        color = QtGui.QColor(pixmap.toImage().pixel(x, y))

                        # Menghitung koordinat baru setelah translasi
                        new_x = x + tx
                        new_y = y + ty

                        # Pastikan koordinat baru berada dalam batas gambar
                        if 0 <= new_x < width and 0 <= new_y < height:
                            new_image.setPixel(new_x, new_y, color.rgb())

                # Menampilkan hasil translasi di label_2
                p = QtGui.QPixmap.fromImage(new_image)
                self.label_2.setPixmap(p)
                self.label_2.setScaledContents(True)

    def select_roi(self):
        if self.label.pixmap() is not None:
            
                qImg = self.label.pixmap().toImage()
                # Mengonversi QImage menjadi citra NumPy
                width, height = qImg.width(), qImg.height()
                ptr = qImg.constBits()
                ptr.setsize(qImg.byteCount())
                image_data = np.array(ptr).reshape(height, width, 4)  # 4 channel (RGBA)
                
                # Mengonversi citra RGBA menjadi citra BGR
                image_bgr = cv2.cvtColor(image_data, cv2.COLOR_RGBA2RGB)
                roiSelected = cv2.selectROI("pilih area", image_bgr)
                croppedImage = image_bgr[int(roiSelected[1]):int(roiSelected[1]+roiSelected[3]),int(roiSelected[0]):int(roiSelected[0]+roiSelected[2])]
                croppedImage_rgb = cv2.cvtColor(croppedImage, cv2.COLOR_BGR2RGB)
                
                # Dapatkan ukuran dan tipe data citra
                height, width, channel = croppedImage_rgb.shape
                bytesPerLine = 3 * width
                
                # Buat QImage dari citra NumPy
                qImg = QtGui.QImage(croppedImage_rgb.data, width, height, bytesPerLine, QtGui.QImage.Format_RGB888)
                # Konversi QImage menjadi QPixmap
                pixmap = QtGui.QPixmap.fromImage(qImg)
                # Tampilkan QPixmap di QLabel
                self.label_2.setPixmap(pixmap)
                # Untuk memastikan label mengukur ukuran citra yang ditampilkan
                self.label_2.setScaledContents(True)
                cv2.destroyAllWindows()

    def removeBackground(self):
        if self.label.pixmap() is not None:
            # Simpan input sementara dengan nama unik berdasarkan timestamp
            timestamp = int(time.time())
            input_file_path = f"removebg/input/temp_input_{timestamp}.png"
            output_file_path = f"removebg/output/output_{timestamp}.png"

            input_pixmap = self.label.pixmap()
            input_pixmap.save(input_file_path)

            with open(input_file_path, "rb") as input_file:
                output_data = remove(input_file.read())
                with open(output_file_path, "wb") as output_file:
                    output_file.write(output_data)

            output_pixmap = QtGui.QPixmap(output_file_path)
            self.label_2.setPixmap(output_pixmap)
            
    def Cropping(self):
            if not self.label.pixmap():
                return

            getimage = self.label.pixmap().toImage()
            width = getimage.width()
            height = getimage.height()
            # Menampilkan dialog untuk memasukkan koordinat crop
            x1, ok1 = QtWidgets.QInputDialog.getInt(None, "Crop Image", "Enter x-coordinate of top-left corner:", 0, 0, width - 1)
            y1, ok2 = QtWidgets.QInputDialog.getInt(None, "Crop Image", "Enter y-coordinate of top-left corner:", 0, 0, height- 1)
            x2, ok3 = QtWidgets.QInputDialog.getInt(None, "Crop Image", "Enter x-coordinate of bottom-right corner:", width - 1, 0, width - 1)
            y2, ok4 = QtWidgets.QInputDialog.getInt(None, "Crop Image", "Enter y-coordinate of bottom-right corner:", height- 1, 0, height- 1)

            if ok1 and ok2 and ok3 and ok4:
                # Menyusun batas crop
                left = min(x1, x2)
                right = max(x1, x2)
                top = min(y1, y2)
                bottom = max(y1, y2)

                # Mendapatkan pixmap yang akan di-crop
                pixmap = self.label.pixmap()

                # Mendapatkan bagian yang di-crop dari pixmap
                cropped_pixmap = pixmap.copy(left, top, right - left, bottom - top)

                # Menampilkan hasil crop di label_2
                self.label_2.setPixmap(cropped_pixmap)
                self.label_2.setAlignment(QtCore.Qt.AlignCenter)
                
    def useHsv(self):
        pixmap = self.label.pixmap()
        if pixmap:
            image = pixmap.toImage()
            width = image.width()
            height = image.height()

            processed_image = QtGui.QImage(width, height, QtGui.QImage.Format_RGB888)

            for y in range(height):
                for x in range(width):
                    color = QtGui.QColor(image.pixel(x, y))
                    r, g, b = color.red(), color.green(), color.blue()
                    r, g, b = r / 255.0, g / 255.0, b / 255.0

                    max_val = max(r, g, b)
                    min_val = min(r, g, b)
                    delta = max_val - min_val

                    h = 0.0
                    s = 0.0
                    v = max_val

                    if delta != 0:
                        if max_val == r:
                            h = 60.0 * (((g - b) / delta) % 6)
                        elif max_val == g:
                            h = 60.0 * (((b - r) / delta) + 2)
                        elif max_val == b:
                            h = 60.0 * (((r - g) / delta) + 4)

                        s = delta / max_val

                    h = (h / 360) * 255
                    s = s * 255
                    v = v * 255

                    processed_image.setPixel(x, y, QtGui.QColor(int(h), int(s), int(v)).rgb())

            pixmap = QtGui.QPixmap.fromImage(processed_image)
            self.label_2.setPixmap(pixmap)
            
    def ekstrakHsv(self):
        if self.label.pixmap() is not None:
            input_image = self.label.pixmap().toImage()
            
            # Mengubah QImage ke format RGB888
            input_image = input_image.convertToFormat(QtGui.QImage.Format_RGB888)
            
            width = input_image.width()
            height = input_image.height()
            
            # Mengambil data piksel dari QImage
            ptr = input_image.constBits()
            ptr.setsize(height * width * 3)  # 3 bytes per piksel untuk RGB
            
            # Mengonversi data piksel ke array numpy
            image = np.array(ptr).reshape(height, width, 3)
            
            # Normalisasi nilai piksel
            image = image.astype(float) / 255.0

            r, g, b = cv2.split(image)

            max_v = np.max([r, g, b], axis=0)
            min_v = np.min([r, g, b], axis=0)

            v = max_v

            s = np.where(max_v == 0, 0, (max_v - min_v) / max_v)

            h = np.zeros_like(max_v)
            h[max_v == r] = np.where(max_v[max_v == r] == min_v[max_v == r], 0, 60 * (0 + (g - b) / (max_v - min_v))[max_v == r])
            h[max_v == g] = np.where(max_v[max_v == g] == min_v[max_v == g], 0, 60 * (2 + (b - r) / (max_v - min_v))[max_v == g])
            h[max_v == b] = np.where(max_v[max_v == b] == min_v[max_v == b], 0, 60 * (4 + (r - g) / (max_v - min_v))[max_v == b])

            h[h < 0] += 360

            # Hitung rata-rata H, S, V
            avg_h = np.mean(h)
            avg_s = np.mean(s)
            avg_v = np.mean(v)

            # Tampilkan dalam dataframe
            data = pd.DataFrame([[avg_h, avg_s, avg_v]], columns=['Average H', 'Average S', 'Average V'])

            export_path, _ = QFileDialog.getSaveFileName(None, "Save HSV Data", "", "Excel Files (*.xlsx)")
            if export_path:
                data.to_excel(export_path, index=False)
                            
    def useYrcb(self):
        pixmap = self.label.pixmap()
        if pixmap:
            image = pixmap.toImage()
            width = image.width()
            height = image.height()

            processed_image = QtGui.QImage(width, height,QtGui.QImage.Format_RGB888)

            for y in range(height):
                for x in range(width):
                    color = QtGui.QColor(image.pixel(x, y))
                    r, g, b = color.red(), color.green(), color.blue()

                    # Konversi RGB ke YCrCb
                    y_value = int(0.299 * r + 0.587 * g + 0.114 * b)
                    cr_value = int(128 + 0.5 * r - 0.418688 * g - 0.081312 * b)
                    cb_value = int(128 - 0.168736 * r - 0.331264 * g + 0.5 * b)

                    # Pastikan nilai-nilai berada dalam rentang 0-255
                    y_value = max(0, min(255, y_value))
                    cr_value = max(0, min(255, cr_value))
                    cb_value = max(0, min(255, cb_value))

                    processed_image.setPixel(x, y, QtGui.QColor(y_value, cr_value, cb_value).rgb())

            pixmap = QtGui.QPixmap.fromImage(processed_image)
            self.label_2.setPixmap(pixmap)
                
    def ekstrakYrcb(self):
        if self.label.pixmap() is not None:
            input_image = self.label.pixmap().toImage()
            width = input_image.width()
            height = input_image.height()

            # Mengambil data piksel dari QImage
            ptr = input_image.constBits()
            ptr.setsize(height * width * 4)  # 4 bytes per piksel untuk RGBA
            
            # Mengonversi data piksel ke array numpy dan ubah ukuran ke (height, width, 4)
            image = np.array(ptr).reshape(height, width, 4)
            
            # Ambil komponen RGB (R,G,B) dan normalisasikan
            r, g, b = image[:,:,0], image[:,:,1], image[:,:,2]
            r, g, b = r / 255.0, g / 255.0, b / 255.0

            Y = 0 + 0.299*r + 0.587*g + 0.114 *b
            Cb = 128 + (-0.169 * r -0.331 * g + 0.500 *b)
            Cr = 128 + 0.500 * r -0.419* g - 0.081 * b

            avg_Y = np.mean(Y)
            avg_Cb = np.mean(Cb)
            avg_Cr = np.mean(Cr)

            # Tampilkan dalam dataframe
            data = pd.DataFrame([[avg_Y, avg_Cb, avg_Cr]], columns=['Average Y', 'Average Cb', 'Average Cr'])

            export_path, _ = QFileDialog.getSaveFileName(None, "Save YCrCb Data", "", "Excel Files (*.xlsx)")
            if export_path:
                data.to_excel(export_path, index=False)
                    
    def useRGB(self):
        pixmap = self.label.pixmap()
        if pixmap:
            image = pixmap.toImage()
            pixmap_2 = QtGui.QPixmap.fromImage(image)
            self.label_2.setPixmap(pixmap_2)    
    def ekstrakRgb(self):
        if self.label.pixmap() is not None:
            input_image = self.label.pixmap().toImage()
            width = input_image.width()
            height = input_image.height()

            # Mengambil data piksel dari QImage
            ptr = input_image.constBits()
            ptr.setsize(height * width * 4)  # 4 bytes per piksel untuk RGBA
            
            # Mengonversi data piksel ke array numpy dan ubah ukuran ke (height, width, 4)
            image = np.array(ptr).reshape(height, width, 4)
            
            # Ambil komponen RGB (R,G,B) dan normalisasikan
            r, g, b = image[:,:,0], image[:,:,1], image[:,:,2]
            r, g, b = r / 255.0, g / 255.0, b / 255.0

            avg_r = np.mean(r)
            avg_g = np.mean(g)
            avg_b = np.mean(b)

            # Tampilkan dalam dataframe
            data = pd.DataFrame([[avg_r, avg_g, avg_b]], columns=['Average R', 'Average G', 'Average B'])

            export_path, _ = QFileDialog.getSaveFileName(None, "Save RGB Data", "", "Excel Files (*.xlsx)")
            if export_path:
                data.to_excel(export_path, index=False)
    
    #INVERS
    def convertToInvers(self):
        # Ambil pixmap dari label
        pixmap = self.label.pixmap()
        if pixmap:
            img = pixmap.toImage()
            width, height = img.width(), img.height()

            for y in range(height):
                for x in range(width):
                    pixel = img.pixel(x, y)
                    # Dapatkan nilai merah (red), hijau (green), dan biru (blue) dari pixel
                    red = QtGui.qRed(pixel)
                    green = QtGui.qGreen(pixel)
                    blue = QtGui.qBlue(pixel)
                    # Inversi warna
                    inverted_color = QtGui.QColor(255 - red, 255 - green, 255 - blue)
                    # Set pixel ke warna invers pada gambar
                    img.setPixel(x, y, inverted_color.rgb())

            # Terapkan gambar invers padf
            pixmap = QtGui.QPixmap.fromImage(img)
            self.label_2.setPixmap(pixmap)
            self.label_2.setScaledContents(True)
            
    #Contrast
    def ConvertToContrast(self):
        input_pixmap = self.label.pixmap()
        if input_pixmap:
        # Konversi QPixmap ke QImage
            input_image = input_pixmap.toImage()

        # Dapatkan ukuran gambar
            width = input_image.width()
            height = input_image.height()

            # Membuat salinan gambar untuk diubah
            output_image = QtGui.QImage(width, height, QtGui.QImage.Format_RGB32)

            # Faktor kontras (misalnya, 1.5 untuk meningkatkan kontras)
            contrast_factor = 1.5

            for x in range(width):
                for y in range(height):
                    pixel_color = QtGui.QColor(*input_image.pixelColor(x, y).getRgb())

                    # Mengubah nilai warna pixel dengan faktor kontras
                    new_red = self.applyContrastToColor(pixel_color.red(), contrast_factor)
                    new_green = self.applyContrastToColor(pixel_color.green(), contrast_factor)
                    new_blue = self.applyContrastToColor(pixel_color.blue(), contrast_factor)

                    # Menetapkan warna baru untuk pixel
                    output_image.setPixelColor(x, y, QtGui.QColor(new_red, new_green, new_blue))

            # Mengubah QPixmap hasil ke dalam QLabel
            output_pixmap = QtGui.QPixmap.fromImage(output_image)
            self.label_2.setPixmap(output_pixmap)
        
    def applyContrastToColor(self, color_value, contrast_factor):
        # Mengaplikasikan kontras pada nilai warna individual
        new_color_value = (color_value - 128) * contrast_factor + 128
        return max(0, min(255, int(new_color_value)))

     
    def showBrightnessContrastForm(self):
        if self.label.pixmap() is not None:
            if self.brightness_contrast_form.exec_() == QtWidgets.QDialog.Accepted:
                pixmap = self.label.pixmap()
                image = pixmap.toImage()
                b = QtGui.QImage(image)

                nilaiBrightness = self.brightness_contrast_form.tbBrightness.text()
                nilaiContrast = self.brightness_contrast_form.tbContrast.text()
                f = (259 * (int(nilaiContrast) + 255)) / (255 * (259 - int(nilaiContrast)))

                for i in range(b.width()):
                    for j in range(b.height()):
                        color = QtGui.QColor(b.pixel(i, j))
                        r1 = self.truncate(color.red() + int(nilaiBrightness) + (int(f) * (color.red() - 128) + 128))
                        g1 = self.truncate(color.green() + int(nilaiBrightness) + (int(f) * (color.green() - 128) + 128))
                        b1 = self.truncate(color.blue() + int(nilaiBrightness) + (int(f) * (color.blue() - 128) + 128))
                        b.setPixel(i, j, QtGui.qRgb(r1, g1, b1))

                self.label_2.setPixmap(QtGui.QPixmap.fromImage(b))

    def truncate(self, value):
        return max(0, min(255, value))
            
    def input_histogram(self):
        if self.label.pixmap() is not None:
            # Mendapatkan citra dari label dan mengonversinya ke objek QImage.
            inputan = self.label.pixmap()
            input_image = inputan.toImage()
            # Mengambil lebar dan tinggi gambar input
            width = input_image.width()
            height = input_image.height()

            # Membuat matriks kosong dengan ukuran yang sesuai untuk data piksel gambar input.
            input_data = np.zeros((height, width), dtype=np.uint8)
             # Loop melalui setiap piksel gambar input dan mengubahnya menjadi citra grayscale.
            for y in range(height):
                for x in range(width):
                    color = QtGui.QColor(input_image.pixel(x, y))
                    # Menghitung nilai grayscale menggunakan formula luminance.
                    val = int(0.3 * color.red() + 0.59 * color.green() + 0.11 * color.blue())
                    input_data[y, x] = val

            # Menghitung histogram dari citra grayscale.
            histogram, bins = np.histogram(input_data, bins=256, range=(0, 256))

            # Menampilkan grafik histogram
            plt.figure(figsize=(8, 6))
            plt.bar(bins[:-1], histogram, width=1, color='blue')
            plt.title('Histogram Input')
            plt.xlabel('Intensitas Piksel')
            plt.ylabel('Frekuensi')
            plt.show()

    def Output_histogram(self):
            # Mendapatkan citra dari label dan mengonversinya ke objek QImage.
         if self.label_2.pixmap() is not None:
            inputan = self.label_2.pixmap()
            input_image = inputan.toImage()
            # Mengambil lebar dan tinggi gambar input
            width = input_image.width()
            height = input_image.height()

            # Membuat matriks kosong dengan ukuran yang sesuai untuk data piksel gambar input.
            input_data = np.zeros((height, width), dtype=np.uint8)
             # Loop melalui setiap piksel gambar input dan mengubahnya menjadi citra grayscale.
            for y in range(height):
                for x in range(width):
                    color = QtGui.QColor(input_image.pixel(x, y))
                    # Menghitung nilai grayscale menggunakan formula luminance.
                    val = int(0.3 * color.red() + 0.59 * color.green() + 0.11 * color.blue())
                    input_data[y, x] = val

            # Menghitung histogram dari citra grayscale.
            histogram, bins = np.histogram(input_data, bins=256, range=(0, 256))

            # Menampilkan grafik histogram
            plt.figure(figsize=(8, 6))
            plt.bar(bins[:-1], histogram, width=1, color='blue')
            plt.title('Histogram Output')
            plt.xlabel('Intensitas Piksel')
            plt.ylabel('Frekuensi')
            plt.show()
    
            
# Membuat fungsi untuk membuka file pada python    
    # def openFile(self):
    #     options = QFileDialog.Options() # Inisialisasi opsi untuk dialog pemilihan berkas
    #     options |= QFileDialog.ReadOnly # Menambahkan opsi mode baca saja ke dalam opsi dialog
    #     # menghapus gambar dari label kedua
    #     self.label_2.clear()
    #     # menampung file path dari dialog open file dan difilter hanya format png , jpg , bmp
    #     file_name, _ = QFileDialog.getOpenFileName(None, "Open Image File", "", "Images (*.png *.jpg *.bmp *.jpeg);;All Files (*)", options=options)
    #     # check apakah terdapat path file
    #     if file_name:
    #         # untuk membuat objek QImage dari suatu berkas gambar dengan nama file_name
    #         image = QtGui.QImage(file_name)
    #         # check varibale apakah tidak kosong
    #         if not image.isNull():
    #             # simpan gambar pada variable pixmap
    #             pixmap = QtGui.QPixmap.fromImage(image)
    #             self.label.setPixmap(pixmap)  # Set gambar pada label
    #             self.label.setScaledContents(True) # set  kontennya agar sesuai dengan ukuran label.
    #             self.image = image # menetapkan objek QImage yang sudah dibuat sebelumnya (dalam contoh kode sebelumnya) ke atribut self.image dari kelas atau objek saat ini
    
    # Membuat fungsi grayscale Luminance        
    def convertToGreyscaleLuminance(self):
        # Ambil pixmap dari label
        pixmap = self.label.pixmap()
        if pixmap:
            img = pixmap.toImage()
            width, height = img.width(), img.height()

            for y in range(height):
                for x in range(width):
                    pixel = img.pixel(x, y)
                    # Dapatkan nilai merah (red), hijau (green), dan biru (blue) dari pixel
                    red = QtGui.qRed(pixel)
                    green = QtGui.qGreen(pixel)
                    blue = QtGui.qBlue(pixel)
                    # Konversi RGB ke greyscale menggunakan formula Luminance
                    luminance = int(0.299 * red + 0.587 * green + 0.114 * blue)
                    # Buat warna greyscale
                    greyscale_color = QtGui.QColor(luminance, luminance, luminance)
                    # Set pixel ke warna greyscale pada gambar
                    img.setPixel(x, y, greyscale_color.rgb())

            # Terapkan gambar greyscale padf
            pixmap = QtGui.QPixmap.fromImage(img)
            self.label_2.setPixmap(pixmap)
            self.label_2.setScaledContents(True)
            self.simpan=img
            
    #HISTOGRAM_EQUALIZATION
    def applyHistogramEqualization(self):
        if self.label is not None:
            inputan = self.label.pixmap()
            input_image = inputan.toImage()
            width = input_image.width()
            height = input_image.height()

            equalized_image = QtGui.QImage(width, height, QtGui.QImage.Format_RGB32)

            # Menghitung histogram
            histogram = [0] * 256
            total_pixels = width * height
            

            for x in range(width):
                for y in range(height):
                    pixel_color = QtGui.QColor(*input_image.pixelColor(x, y).getRgb())
                    intensity = pixel_color.red()  # Kami asumsikan gambar grayscale

                    histogram[intensity] += 1

            # Menghitung distribusi kumulatif
            cumulative_distribution = [0] * 256
            cumulative_distribution[0] = histogram[0] / total_pixels

            for i in range(1, 256):
                cumulative_distribution[i] = cumulative_distribution[i - 1] + histogram[i] / total_pixels

            # Menyesuaikan nilai pixel pada gambar hasil
            for x in range(width):
                for y in range(height):
                    pixel_color = QtGui.QColor(*input_image.pixelColor(x, y).getRgb())
                    intensity = pixel_color.red()  # Kami asumsikan gambar grayscale

                    new_intensity = int(255 * cumulative_distribution[intensity])
                    new_color = QtGui.QColor(new_intensity, new_intensity, new_intensity)
                    equalized_image.setPixelColor(x, y, new_color)
            

            output_pixmap = QtGui.QPixmap.fromImage(equalized_image)
            self.label_2.setPixmap(output_pixmap)

    #FUZZY HE RGB
    def fuzzy_he_rgb(self):
        if self.label is not None:
            inputan = self.label.pixmap()
            input_image = inputan.toImage()
            width = input_image.width()
            height = input_image.height()

            # Mengambil data piksel dari gambar input
            input_data = np.zeros((height, width, 3), dtype=np.uint8)
            for y in range(height):
                for x in range(width):
                    color = QtGui.QColor(input_image.pixel(x, y))
                    input_data[y, x, 0] = color.red()
                    input_data[y, x, 1] = color.green()
                    input_data[y, x, 2] = color.blue()

            # Menerapkan rumus Fuzzy HE RGB
            output_data = np.zeros_like(input_data)
            for i in range(3):  # Loop untuk saluran warna (R, G, B)
                for y in range(height):
                    for x in range(width):
                        val = input_data[y, x, i]
                        if val < 128:
                            output_data[y, x, i] = int(2 * val ** 2 / 255.0)
                        else:
                            output_data[y, x, i] = int(255 - 2 * (255 - val) ** 2 / 255.0)

            # Membuat gambar output dan menampilkannya df
            output_image = QtGui.QImage(output_data.data, width, height, width * 3, QtGui.QImage.Format_RGB888)
            self.label_2.setPixmap(QtGui.QPixmap.fromImage(output_image))

    #FUZZY GREYSCALE
    def fuzzy_greyscale(self):
        if self.label is not None:
            inputan = self.label.pixmap()
            input_image = inputan.toImage()
            width = input_image.width()
            height = input_image.height()

            # Mengambil data piksel dari gambar input
            input_data = np.zeros((height, width), dtype=np.uint8)
            for y in range(height):
                for x in range(width):
                    color = QtGui.QColor(input_image.pixel(x, y))
                    # Menghitung nilai greyscale menggunakan rumus Fuzzy
                    val = int(0.3 * color.red() + 0.59 * color.green() + 0.11 * color.blue())
                    input_data[y, x] = val

            # Membuat gambar output dan menampilkannya df
            output_image = QtGui.QImage(input_data.data, width, height, width, QtGui.QImage.Format_Grayscale8)
            self.label_2.setPixmap(QtGui.QPixmap.fromImage(output_image))

         
    def connectActions(self):
            self.actionOpen.triggered.connect(self.openFile)
            self.actionSave_As.triggered.connect(self.saveImage)
            self.actionExit.triggered.connect(self.exitApplication)
        
        # Membuat fungsi untuk membuka file pada python    
    def openFile(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        file_name, _ = QFileDialog.getOpenFileName(None, "Open Image File", "", "Images (*.png *.jpg *.bmp *.jpeg);;All Files (*)", options=options)
        if file_name:
            image = QtGui.QImage(file_name)
            if not image.isNull():
                pixmap = QtGui.QPixmap.fromImage(image)
                self.label.setPixmap(pixmap)
                self.label.setScaledContents(True)
                self.image = image  # Set the image to self.image
                self.simpan = None  # Clear self.simpan until a process is done



        # Membuat fungsi untuk membuka save file pada python       
    def saveImage(self):
        if self.simpan and not self.simpan.isNull():
            options = QFileDialog.Options()
            options |= QFileDialog.ReadOnly
            file_name, _ = QFileDialog.getSaveFileName(None, "Save Image File", "", "Images (*.png *.jpg *.bmp *.jpeg);;All Files (*)", options=options)
            if file_name:
                if not self.simpan.save(file_name):
                    QMessageBox.warning(None, "Save Image File", "Failed to save image.")
        else:
            QMessageBox.warning(None, "Save Image File", "No image to save.")


        # Membuat fungsi untuk exit pada python                   
    def exitApplication(self):
            QtWidgets.qApp.quit()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
