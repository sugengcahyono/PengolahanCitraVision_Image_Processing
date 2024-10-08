# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Aritmatika.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QApplication
from PyQt5.QtWidgets import QGraphicsScene
import tempfile
import os
import cv2
from PIL import Image, ImageOps
import numpy as np
import matplotlib.pyplot as plt
from Gui_LogBrightness import LogBrightnessDialog
from Gui_Brightness import LinearBrightnessDialog
from Gui_Contrast import LinearContrastDialog
from Gui_Saturation import LinearSaturationDialog
from GUI_Contrast_Brightness import LinearContrastBrightnessDialog
from GUI_Cropping import CropsDialog
from GUI_Translasi import TranslasiDialog
from GUI_Rotasi import RotasiDialog
from GUI_Zoom import ZoomDialog
from GUI_Crop_Region import CropDialog
from skimage.morphology import skeletonize, thin
from skimage import data



class Ui_MainWindow(object):

    #metode __init__ 
    def __init__(self):
        super().__init__()
       
        self.imagePath = None
        self.image_pixmap = None  # Variable to store the selected image pixmap
        self.imagefile1 = None
        self.imagefile2 = None
        self.imageResult = None

    # Membuka Gambar 
    def openImage1(self):
            # Show file dialog to select an image file
            options = QFileDialog.Options()
            fileName, _ = QFileDialog.getOpenFileName(None, "Open Image", "", "Image Files (*.png *.jpg *.bmp *.jpeg)", options=options)
            
            if fileName:
                self.imagePath1 = fileName
                image_path = fileName
                img = Image.open(image_path)
                self.imagefile1 = img
                # img.show()

                # Load the image and display it in the QGraphicsView
                self.image_pixmap = QtGui.QPixmap(fileName)

                # Get the size of the QGraphicsView
                view_width = self.graphicsView_2.width()
                view_height = self.graphicsView_2.height()

                # Scale the pixmap to fit the QGraphicsView, preserving the aspect ratio
                scaled_pixmap = self.image_pixmap.scaled(view_width, view_height, QtCore.Qt.KeepAspectRatio)

                self.scene.clear()  # Clear any previous content in the scene
                self.scene.addPixmap(scaled_pixmap)
                # self.graphicsView.fitInView(self.scene.itemsBoundingRect(), QtCore.Qt.KeepAspectRatio)
                self.graphicsView_2.setSceneRect(self.scene.itemsBoundingRect())

    def openImage2(self):
            # Show file dialog to select an image file
            options = QFileDialog.Options()
            fileName, _ = QFileDialog.getOpenFileName(None, "Open Image", "", "Image Files (*.png *.jpg *.bmp *.jpeg)", options=options)
            
            if fileName:
                self.imagePath = fileName
                image_path = fileName
                img = Image.open(image_path)
                self.imagefile2 = img
                # img.show()

                # Load the image and display it in the QGraphicsView
                self.image_pixmap = QtGui.QPixmap(fileName)

                # Get the size of the QGraphicsView
                view_width = self.graphicsView_4.width()
                view_height = self.graphicsView_4.height()

                # Scale the pixmap to fit the QGraphicsView, preserving the aspect ratio
                scaled_pixmap = self.image_pixmap.scaled(view_width, view_height, QtCore.Qt.KeepAspectRatio)

                self.scene1.clear()  # Clear any previous content in the scene
                self.scene1.addPixmap(scaled_pixmap)
                # self.graphicsView.fitInView(self.scene.itemsBoundingRect(), QtCore.Qt.KeepAspectRatio)
                self.graphicsView_4.setSceneRect(self.scene.itemsBoundingRect())

    # Menampilkan gambar
    def show_image(self):
            self.imagefile.show()

    def clear_images(self):
        """Menghapus gambar dari graphicsView_2, graphicsView_3, dan graphicsView_4 serta membersihkan scene."""
        print("Button clicked, clearing images...")

        # Hapus konten dari kotak 2 (graphicsView_2)
        if hasattr(self, 'scene'):
            self.scene.clear()  # Clear the custom scene set in graphicsView_2
        else:
            self.graphicsView_2.scene().clear()  # Clear directly if no custom scene

        # Hapus konten dari kotak 3 (graphicsView_3)
        if hasattr(self, 'sceneOutput'):
            self.sceneOutput.clear()  # Clear the custom scene set in graphicsView_3 (Output)
        else:
            self.graphicsView_3.scene().clear()  # Clear directly if no custom scene

        # Hapus konten dari kotak 4 (graphicsView_4)
        if hasattr(self, 'scene1'):
            self.scene1.clear()  # Clear the custom scene set in graphicsView_4
        else:
            self.graphicsView_4.scene().clear()  # Clear directly if no custom scene

        print("Images cleared from graphicsView_2, graphicsView_3, and graphicsView_4.")

    def close_window(self):
        """Menutup halaman saat ini tanpa menutup seluruh aplikasi."""
        self.close()  # Close the current window only



    def saveAs(self):
            if hasattr(self, 'imageResult') and self.imageResult is not None:
                # Buka dialog untuk memilih lokasi dan memberi nama file
                options = QFileDialog.Options()
                fileName, _ = QFileDialog.getSaveFileName(None, "Save Image As", "", "PNG Files (*.png);;JPEG Files (*.jpg);;BMP Files (*.bmp)", options=options)
                
                if fileName:
                    # Simpan gambar ke lokasi yang dipilih dengan nama file baru
                    self.imageResult.save(fileName)
                    print(f"Gambar disimpan di: {fileName}")
                else:
                    print("Penyimpanan dibatalkan.")
            else:
                print("Tidak ada gambar untuk disimpan.")  


    def addition(self):
        # Membuka citra menggunakan PIL
        image1 = self.imagefile1  # Citra pertama
        image2 = self.imagefile2  # Citra kedua (misalnya, citra lain yang Anda pilih)

        # Mengonversi citra ke numpy array
        image1_np = np.array(image1)
        image2_np = np.array(image2)

        # Menyamakan ukuran citra kedua sesuai ukuran citra pertama (jika berbeda)
        if image1_np.shape != image2_np.shape:
            image2_np = cv2.resize(image2_np, (image1_np.shape[1], image1_np.shape[0]))

        # Melakukan penjumlahan citra
        added_image_np = cv2.add(image1_np, image2_np)

        # Mengubah array kembali ke gambar
        added_image = Image.fromarray(added_image_np.astype(np.uint8))
        self.imageResult = added_image  # Simpan hasil untuk keperluan save

        # Menyimpan citra penjumlahan sebagai Image object
        added_image.save("output_addition_temp.jpg")  # Simpan sementara

        # Menampilkan gambar penjumlahan di kotak output (Kotak2)
        pixmap = QtGui.QPixmap("output_addition_temp.jpg")
        scaled_pixmap = pixmap.scaled(self.graphicsView_3.width(), self.graphicsView_3.height(), QtCore.Qt.KeepAspectRatio)

        self.sceneOutput.clear()  # Hapus konten sebelumnya di output scene
        self.sceneOutput.addPixmap(scaled_pixmap)
        self.graphicsView_3.setSceneRect(self.sceneOutput.itemsBoundingRect())


    def subtraction(self):
        # Membuka citra menggunakan PIL
        image1 = self.imagefile1  # Citra pertama
        image2 = self.imagefile2  # Citra kedua

        # Mengonversi citra ke numpy array
        image1_np = np.array(image1)
        image2_np = np.array(image2)

        # Menyamakan ukuran citra kedua sesuai ukuran citra pertama (jika berbeda)
        if image1_np.shape != image2_np.shape:
            image2_np = cv2.resize(image2_np, (image1_np.shape[1], image1_np.shape[0]))

        # Melakukan pengurangan citra
        subtracted_image_np = cv2.subtract(image1_np, image2_np)

        # Mengubah array kembali ke gambar
        subtracted_image = Image.fromarray(subtracted_image_np.astype(np.uint8))
        self.imageResult = subtracted_image  # Simpan hasil untuk keperluan save

        # Menyimpan citra pengurangan sebagai Image object
        subtracted_image.save("output_subtraction_temp.jpg")  # Simpan sementara

        # Menampilkan gambar pengurangan di kotak output (Kotak3)
        pixmap = QtGui.QPixmap("output_subtraction_temp.jpg")
        scaled_pixmap = pixmap.scaled(self.graphicsView_3.width(), self.graphicsView_3.height(), QtCore.Qt.KeepAspectRatio)

        self.sceneOutput.clear()  # Hapus konten sebelumnya di output scene
        self.sceneOutput.addPixmap(scaled_pixmap)
        self.graphicsView_3.setSceneRect(self.sceneOutput.itemsBoundingRect())

    def multiplication(self):
        # Membuka citra menggunakan PIL
        image1 = self.imagefile1  # Citra pertama
        image2 = self.imagefile2  # Citra kedua

        # Mengonversi citra ke numpy array
        image1_np = np.array(image1)
        image2_np = np.array(image2)

        # Menyamakan ukuran citra kedua sesuai ukuran citra pertama (jika berbeda)
        if image1_np.shape != image2_np.shape:
            image2_np = cv2.resize(image2_np, (image1_np.shape[1], image1_np.shape[0]))

        # Melakukan perkalian citra
        multiplied_image_np = cv2.multiply(image1_np, image2_np)

        # Mengubah array kembali ke gambar
        multiplied_image = Image.fromarray(multiplied_image_np.astype(np.uint8))
        self.imageResult = multiplied_image  # Simpan hasil untuk keperluan save

        # Menyimpan citra perkalian sebagai Image object
        multiplied_image.save("output_multiplication_temp.jpg")  # Simpan sementara

        # Menampilkan gambar perkalian di kotak output (Kotak3)
        pixmap = QtGui.QPixmap("output_multiplication_temp.jpg")
        scaled_pixmap = pixmap.scaled(self.graphicsView_3.width(), self.graphicsView_3.height(), QtCore.Qt.KeepAspectRatio)

        self.sceneOutput.clear()  # Hapus konten sebelumnya di output scene
        self.sceneOutput.addPixmap(scaled_pixmap)
        self.graphicsView_3.setSceneRect(self.sceneOutput.itemsBoundingRect())


    def division(self):
        # Membuka citra menggunakan PIL
        image1 = self.imagefile1  # Citra pertama
        image2 = self.imagefile2  # Citra kedua

        # Mengonversi citra ke numpy array
        image1_np = np.array(image1)
        image2_np = np.array(image2)

        # Menyamakan ukuran citra kedua sesuai ukuran citra pertama (jika berbeda)
        if image1_np.shape != image2_np.shape:
            image2_np = cv2.resize(image2_np, (image1_np.shape[1], image1_np.shape[0]))

        # Menghindari pembagian dengan nol, menggunakan np.errstate untuk mengabaikan warning
        with np.errstate(divide='ignore', invalid='ignore'):
            divided_image_np = cv2.divide(image1_np.astype('float'), image2_np.astype('float'))
            divided_image_np = np.nan_to_num(divided_image_np).astype(np.uint8)

        # Mengubah array kembali ke gambar
        divided_image = Image.fromarray(divided_image_np)
        self.imageResult = divided_image  # Simpan hasil untuk keperluan save

        # Menyimpan citra pembagian sebagai Image object
        divided_image.save("output_division_temp.jpg")  # Simpan sementara

        # Menampilkan gambar pembagian di kotak output (Kotak3)
        pixmap = QtGui.QPixmap("output_division_temp.jpg")
        scaled_pixmap = pixmap.scaled(self.graphicsView_3.width(), self.graphicsView_3.height(), QtCore.Qt.KeepAspectRatio)

        self.sceneOutput.clear()  # Hapus konten sebelumnya di output scene
        self.sceneOutput.addPixmap(scaled_pixmap)
        self.graphicsView_3.setSceneRect(self.sceneOutput.itemsBoundingRect())


    def bitwise_not(self):
        # Membuka citra menggunakan PIL
        image1 = self.imagefile1  # Citra pertama

        # Mengonversi citra ke numpy array
        image1_np = np.array(image1)

        # Melakukan operasi NOT
        not_image_np = cv2.bitwise_not(image1_np)

        # Mengubah array kembali ke gambar
        not_image = Image.fromarray(not_image_np.astype(np.uint8))
        self.imageResult = not_image  # Simpan hasil untuk keperluan save

        # Menyimpan citra NOT sebagai Image object
        not_image.save("output_not_temp.jpg")  # Simpan sementara

        # Menampilkan gambar NOT di kotak output (Kotak3)
        pixmap = QtGui.QPixmap("output_not_temp.jpg")
        scaled_pixmap = pixmap.scaled(self.graphicsView_3.width(), self.graphicsView_3.height(), QtCore.Qt.KeepAspectRatio)

        self.sceneOutput.clear()  # Hapus konten sebelumnya di output scene
        self.sceneOutput.addPixmap(scaled_pixmap)
        self.graphicsView_3.setSceneRect(self.sceneOutput.itemsBoundingRect())


    def bitwise_or(self):
        # Membuka citra menggunakan PIL
        image1 = self.imagefile1  # Citra pertama
        image2 = self.imagefile2  # Citra kedua

        # Mengonversi citra ke numpy array
        image1_np = np.array(image1)
        image2_np = np.array(image2)

        # Menyamakan ukuran citra kedua sesuai ukuran citra pertama (jika berbeda)
        if image1_np.shape != image2_np.shape:
            image2_np = cv2.resize(image2_np, (image1_np.shape[1], image1_np.shape[0]))

        # Melakukan operasi OR
        or_image_np = cv2.bitwise_or(image1_np, image2_np)

        # Mengubah array kembali ke gambar
        or_image = Image.fromarray(or_image_np.astype(np.uint8))
        self.imageResult = or_image  # Simpan hasil untuk keperluan save

        # Menyimpan citra OR sebagai Image object
        or_image.save("output_or_temp.jpg")  # Simpan sementara

        # Menampilkan gambar OR di kotak output
        pixmap = QtGui.QPixmap("output_or_temp.jpg")
        scaled_pixmap = pixmap.scaled(self.graphicsView_3.width(), self.graphicsView_3.height(), QtCore.Qt.KeepAspectRatio)

        self.sceneOutput.clear()
        self.sceneOutput.addPixmap(scaled_pixmap)
        self.graphicsView_3.setSceneRect(self.sceneOutput.itemsBoundingRect())


    def bitwise_and(self):
        # Membuka citra menggunakan PIL
        image1 = self.imagefile1  # Citra pertama
        image2 = self.imagefile2  # Citra kedua

        # Mengonversi citra ke numpy array
        image1_np = np.array(image1)
        image2_np = np.array(image2)

        # Menyamakan ukuran citra kedua sesuai ukuran citra pertama (jika berbeda)
        if image1_np.shape != image2_np.shape:
            image2_np = cv2.resize(image2_np, (image1_np.shape[1], image1_np.shape[0]))

        # Melakukan operasi AND
        and_image_np = cv2.bitwise_and(image1_np, image2_np)

        # Mengubah array kembali ke gambar
        and_image = Image.fromarray(and_image_np.astype(np.uint8))
        self.imageResult = and_image  # Simpan hasil untuk keperluan save

        # Menyimpan citra AND sebagai Image object
        and_image.save("output_and_temp.jpg")  # Simpan sementara

        # Menampilkan gambar AND di kotak output
        pixmap = QtGui.QPixmap("output_and_temp.jpg")
        scaled_pixmap = pixmap.scaled(self.graphicsView_3.width(), self.graphicsView_3.height(), QtCore.Qt.KeepAspectRatio)

        self.sceneOutput.clear()
        self.sceneOutput.addPixmap(scaled_pixmap)
        self.graphicsView_3.setSceneRect(self.sceneOutput.itemsBoundingRect())


    def bitwise_xor(self):
        # Membuka citra menggunakan PIL
        image1 = self.imagefile1  # Citra pertama
        image2 = self.imagefile2  # Citra kedua

        # Mengonversi citra ke numpy array
        image1_np = np.array(image1)
        image2_np = np.array(image2)

        # Menyamakan ukuran citra kedua sesuai ukuran citra pertama (jika berbeda)
        if image1_np.shape != image2_np.shape:
            image2_np = cv2.resize(image2_np, (image1_np.shape[1], image1_np.shape[0]))

        # Melakukan operasi XOR
        xor_image_np = cv2.bitwise_xor(image1_np, image2_np)

        # Mengubah array kembali ke gambar
        xor_image = Image.fromarray(xor_image_np.astype(np.uint8))
        self.imageResult = xor_image  # Simpan hasil untuk keperluan save

        # Menyimpan citra XOR sebagai Image object
        xor_image.save("output_xor_temp.jpg")  # Simpan sementara

        # Menampilkan gambar XOR di kotak output
        pixmap = QtGui.QPixmap("output_xor_temp.jpg")
        scaled_pixmap = pixmap.scaled(self.graphicsView_3.width(), self.graphicsView_3.height(), QtCore.Qt.KeepAspectRatio)

        self.sceneOutput.clear()
        self.sceneOutput.addPixmap(scaled_pixmap)
        self.graphicsView_3.setSceneRect(self.sceneOutput.itemsBoundingRect())


    def bitwise_nand(self):
        # Membuka citra menggunakan PIL
        image1 = self.imagefile1  # Citra pertama
        image2 = self.imagefile2  # Citra kedua

        # Mengonversi citra ke numpy array
        image1_np = np.array(image1)
        image2_np = np.array(image2)

        # Menyamakan ukuran citra kedua sesuai ukuran citra pertama (jika berbeda)
        if image1_np.shape != image2_np.shape:
            image2_np = cv2.resize(image2_np, (image1_np.shape[1], image1_np.shape[0]))

        # Melakukan operasi AND dan kemudian NOT (NAND)
        nand_image_np = cv2.bitwise_not(cv2.bitwise_and(image1_np, image2_np))

        # Mengubah array kembali ke gambar
        nand_image = Image.fromarray(nand_image_np.astype(np.uint8))
        self.imageResult = nand_image  # Simpan hasil untuk keperluan save

        # Menyimpan citra NAND sebagai Image object
        nand_image.save("output_nand_temp.jpg")  # Simpan sementara

        # Menampilkan gambar NAND di kotak output
        pixmap = QtGui.QPixmap("output_nand_temp.jpg")
        scaled_pixmap = pixmap.scaled(self.graphicsView_3.width(), self.graphicsView_3.height(), QtCore.Qt.KeepAspectRatio)

        self.sceneOutput.clear()
        self.sceneOutput.addPixmap(scaled_pixmap)
        self.graphicsView_3.setSceneRect(self.sceneOutput.itemsBoundingRect())


    def bitwise_nor(self):
        # Membuka citra menggunakan PIL
        image1 = self.imagefile1  # Citra pertama
        image2 = self.imagefile2  # Citra kedua

        # Mengonversi citra ke numpy array
        image1_np = np.array(image1)
        image2_np = np.array(image2)

        # Menyamakan ukuran citra kedua sesuai ukuran citra pertama (jika berbeda)
        if image1_np.shape != image2_np.shape:
            image2_np = cv2.resize(image2_np, (image1_np.shape[1], image1_np.shape[0]))

        # Melakukan operasi OR dan kemudian NOT (NOR)
        nor_image_np = cv2.bitwise_not(cv2.bitwise_or(image1_np, image2_np))

        # Mengubah array kembali ke gambar
        nor_image = Image.fromarray(nor_image_np.astype(np.uint8))
        self.imageResult = nor_image  # Simpan hasil untuk keperluan save

        # Menyimpan citra NOR sebagai Image object
        nor_image.save("output_nor_temp.jpg")  # Simpan sementara

        # Menampilkan gambar NOR di kotak output
        pixmap = QtGui.QPixmap("output_nor_temp.jpg")
        scaled_pixmap = pixmap.scaled(self.graphicsView_3.width(), self.graphicsView_3.height(), QtCore.Qt.KeepAspectRatio)

        self.sceneOutput.clear()
        self.sceneOutput.addPixmap(scaled_pixmap)
        self.graphicsView_3.setSceneRect(self.sceneOutput.itemsBoundingRect())


    def bitwise_xnor(self):
        # Membuka citra menggunakan PIL
        image1 = self.imagefile1  # Citra pertama
        image2 = self.imagefile2  # Citra kedua

        # Mengonversi citra ke numpy array
        image1_np = np.array(image1)
        image2_np = np.array(image2)

        # Menyamakan ukuran citra kedua sesuai ukuran citra pertama (jika berbeda)
        if image1_np.shape != image2_np.shape:
            image2_np = cv2.resize(image2_np, (image1_np.shape[1], image1_np.shape[0]))

        # Melakukan operasi XOR dan kemudian NOT (XNOR)
        xnor_image_np = cv2.bitwise_not(cv2.bitwise_xor(image1_np, image2_np))

        # Mengubah array kembali ke gambar
        xnor_image = Image.fromarray(xnor_image_np.astype(np.uint8))
        self.imageResult = xnor_image  # Simpan hasil untuk keperluan save

        # Menyimpan citra XNOR sebagai Image object
        xnor_image.save("output_xnor_temp.jpg")  # Simpan sementara

        # Menampilkan gambar XNOR di kotak output
        pixmap = QtGui.QPixmap("output_xnor_temp.jpg")
        scaled_pixmap = pixmap.scaled(self.graphicsView_3.width(), self.graphicsView_3.height(), QtCore.Qt.KeepAspectRatio)

        self.sceneOutput.clear()
        self.sceneOutput.addPixmap(scaled_pixmap)
        self.graphicsView_3.setSceneRect(self.sceneOutput.itemsBoundingRect())



#######################################################################################
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1092, 776)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.graphicsView_2 = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView_2.setGeometry(QtCore.QRect(40, 60, 321, 291))
        self.graphicsView_2.setObjectName("graphicsView_2")
        self.graphicsView_3 = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView_3.setGeometry(QtCore.QRect(410, 60, 641, 641))
        self.graphicsView_3.setObjectName("graphicsView_3")
        self.graphicsView_4 = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView_4.setGeometry(QtCore.QRect(40, 410, 321, 291))
        self.graphicsView_4.setObjectName("graphicsView_4")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 10, 101, 51))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 360, 101, 51))
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
       
        # Set fungsi "Pilih gambar 1"       
        self.pushButton.setGeometry(QtCore.QRect(250, 20, 112, 34))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.openImage1)

        # menampilkan gambar di Input1 menggunakan grapich
        self.scene = QGraphicsScene()
        self.graphicsView_2.setScene(self.scene)

        # menampilkan gambar di Input2 menggunakan grapich
        self.scene1 = QGraphicsScene()
        self.graphicsView_4.setScene(self.scene1)

        # menampilkan gambar di Output menggunakan grapich
        self.sceneOutput = QGraphicsScene()
        self.graphicsView_3.setScene(self.sceneOutput)

        # Set Fungsi "Pilih gambar2"
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(250, 370, 112, 34))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.openImage2)

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(700, 30, 101, 51))
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1092, 31))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuAritmatical_Operations = QtWidgets.QMenu(self.menubar)
        self.menuAritmatical_Operations.setObjectName("menuAritmatical_Operations")
        self.menuLogical_Operations = QtWidgets.QMenu(self.menubar)
        self.menuLogical_Operations.setObjectName("menuLogical_Operations")
        self.menuClear = QtWidgets.QMenu(self.menubar)
        self.menuClear.setObjectName("menuClear")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        # set Fungsi Penjumlahan
        self.actionAddition = QtWidgets.QAction(MainWindow)
        self.actionAddition.setObjectName("actionAddition")
        self.actionAddition.triggered.connect(self.addition)
        
        # set fungsi Pengurangan 
        self.actionSubtract = QtWidgets.QAction(MainWindow)
        self.actionSubtract.setObjectName("actionSubtract")
        self.actionSubtract.triggered.connect(self.subtraction)

        # set fungsi Perkalian 
        self.actionMultiplication = QtWidgets.QAction(MainWindow)
        self.actionMultiplication.setObjectName("actionMultiplication")
        self.actionMultiplication.triggered.connect(self.multiplication)

        # set fungsi Pembagian 
        self.actionDistribution = QtWidgets.QAction(MainWindow)
        self.actionDistribution.setObjectName("actionDistribution")
        self.actionDistribution.triggered.connect(self.division)

        # set Fungsi NOT
        self.actionNOT = QtWidgets.QAction(MainWindow)
        self.actionNOT.setObjectName("actionNOT")
        self.actionNOT.triggered.connect(self.bitwise_not)

        # set fungsi AND
        self.actionAND = QtWidgets.QAction(MainWindow)
        self.actionAND.setObjectName("actionOR")
        self.actionAND.triggered.connect(self.bitwise_and)

        # set fungsi NAND
        self.actionNAND = QtWidgets.QAction(MainWindow)
        self.actionNAND.setObjectName("actionNAND")
        self.actionNAND.triggered.connect(self.bitwise_nand)

        #set fungsi OR
        self.actionOR_2 = QtWidgets.QAction(MainWindow)
        self.actionOR_2.setObjectName("actionOR_2")
        self.actionOR_2.triggered.connect(self.bitwise_or)

        # set fungsi NOR
        self.actionNOR = QtWidgets.QAction(MainWindow)
        self.actionNOR.setObjectName("actionNOR")
        self.actionNOR.triggered.connect(self.bitwise_nor)

        # set fungsi XOR
        self.actionXOR = QtWidgets.QAction(MainWindow)
        self.actionXOR.setObjectName("actionXOR")
        self.actionXOR.triggered.connect(self.bitwise_xor)

        # set fungsi XNOR
        self.actionXNOR = QtWidgets.QAction(MainWindow)
        self.actionXNOR.setObjectName("actionXNOR")
        self.actionXNOR.triggered.connect(self.bitwise_xnor)

        # set fungsi Save
        self.actionSave_As = QtWidgets.QAction(MainWindow)
        self.actionSave_As.setObjectName("actionSave_As")
        self.actionSave_As.triggered.connect(self.saveAs)


        # set fungsi Close
        self.actionExit_and_Back = QtWidgets.QAction(MainWindow)
        self.actionExit_and_Back.setObjectName("actionExit_and_Back")
        self.actionExit_and_Back.triggered.connect(MainWindow.close)
        
        
        # set fungsi Clear
        self.actionClear = QtWidgets.QAction(MainWindow)
        self.actionClear.setObjectName("actionClear")
        self.actionClear.triggered.connect(self.clear_images)


        self.menuFile.addAction(self.actionSave_As)
        self.menuFile.addAction(self.actionExit_and_Back)
        self.menuAritmatical_Operations.addAction(self.actionAddition)
        self.menuAritmatical_Operations.addAction(self.actionSubtract)
        self.menuAritmatical_Operations.addAction(self.actionMultiplication)
        self.menuAritmatical_Operations.addAction(self.actionDistribution)
        self.menuLogical_Operations.addAction(self.actionNOT)
        self.menuLogical_Operations.addAction(self.actionAND)
        self.menuLogical_Operations.addAction(self.actionNAND)
        self.menuLogical_Operations.addAction(self.actionOR_2)
        self.menuLogical_Operations.addAction(self.actionNOR)
        self.menuLogical_Operations.addAction(self.actionXOR)
        self.menuLogical_Operations.addAction(self.actionXNOR)
        self.menuClear.addAction(self.actionClear)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAritmatical_Operations.menuAction())
        self.menubar.addAction(self.menuLogical_Operations.menuAction())
        self.menubar.addAction(self.menuClear.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Aritmatical Operations"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Input 1</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Input 2</span></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "Pilih Gambar 1"))
        self.pushButton_2.setText(_translate("MainWindow", "Pilih Gambar 2"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Output</span></p><p><br/></p></body></html>"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuAritmatical_Operations.setTitle(_translate("MainWindow", "Aritmatical Operations"))
        self.menuLogical_Operations.setTitle(_translate("MainWindow", "Logical Operations"))
        self.menuClear.setTitle(_translate("MainWindow", "Clear"))
        self.actionAddition.setText(_translate("MainWindow", "Addition (+)"))
        self.actionSubtract.setText(_translate("MainWindow", "Subtract (-)"))
        self.actionMultiplication.setText(_translate("MainWindow", "Multiplication (*)"))
        self.actionDistribution.setText(_translate("MainWindow", "Distribution (/)"))
        self.actionNOT.setText(_translate("MainWindow", "NOT"))
        self.actionAND.setText(_translate("MainWindow", "AND"))
        self.actionNAND.setText(_translate("MainWindow", "NAND"))
        self.actionOR_2.setText(_translate("MainWindow", "OR"))
        self.actionNOR.setText(_translate("MainWindow", "NOR"))
        self.actionXOR.setText(_translate("MainWindow", "XOR"))
        self.actionXNOR.setText(_translate("MainWindow", "XNOR"))
        self.actionSave_As.setText(_translate("MainWindow", "Save As"))
        self.actionExit_and_Back.setText(_translate("MainWindow", "Exit and Back"))
        self.actionClear.setText(_translate("MainWindow", "Clear"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
