# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tambahan.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 31))
        self.menubar.setObjectName("menubar")
        self.menuTransform = QtWidgets.QMenu(self.menubar)
        self.menuTransform.setObjectName("menuTransform")
        self.menuFlipping_2 = QtWidgets.QMenu(self.menuTransform)
        self.menuFlipping_2.setObjectName("menuFlipping_2")
        self.menuCrops = QtWidgets.QMenu(self.menubar)
        self.menuCrops.setObjectName("menuCrops")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionTranslasi = QtWidgets.QAction(MainWindow)
        self.actionTranslasi.setObjectName("actionTranslasi")
        self.actionRotasi = QtWidgets.QAction(MainWindow)
        self.actionRotasi.setObjectName("actionRotasi")
        self.actionHorizontal = QtWidgets.QAction(MainWindow)
        self.actionHorizontal.setObjectName("actionHorizontal")
        self.actionVertikal = QtWidgets.QAction(MainWindow)
        self.actionVertikal.setObjectName("actionVertikal")
        self.actionHorizontal_2 = QtWidgets.QAction(MainWindow)
        self.actionHorizontal_2.setObjectName("actionHorizontal_2")
        self.actionVertikal_2 = QtWidgets.QAction(MainWindow)
        self.actionVertikal_2.setObjectName("actionVertikal_2")
        self.actionZoom = QtWidgets.QAction(MainWindow)
        self.actionZoom.setObjectName("actionZoom")
        self.menuFlipping_2.addAction(self.actionHorizontal_2)
        self.menuFlipping_2.addAction(self.actionVertikal_2)
        self.menuTransform.addAction(self.actionTranslasi)
        self.menuTransform.addAction(self.actionRotasi)
        self.menuTransform.addAction(self.menuFlipping_2.menuAction())
        self.menuTransform.addAction(self.actionZoom)
        self.menubar.addAction(self.menuTransform.menuAction())
        self.menubar.addAction(self.menuCrops.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menuTransform.setTitle(_translate("MainWindow", "Transform"))
        self.menuFlipping_2.setTitle(_translate("MainWindow", "Flipping"))
        self.menuCrops.setTitle(_translate("MainWindow", "Crops"))
        self.actionTranslasi.setText(_translate("MainWindow", "Translasi"))
        self.actionRotasi.setText(_translate("MainWindow", "Rotasi"))
        self.actionHorizontal.setText(_translate("MainWindow", "Horizontal"))
        self.actionVertikal.setText(_translate("MainWindow", "Vertikal"))
        self.actionHorizontal_2.setText(_translate("MainWindow", "Horizontal"))
        self.actionVertikal_2.setText(_translate("MainWindow", "Vertikal"))
        self.actionZoom.setText(_translate("MainWindow", "Zoom"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
