# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'evolution_tree_ui.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 720)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.child_image = QtWidgets.QLabel(self.centralwidget)
        self.child_image.setGeometry(QtCore.QRect(575, 400, 250, 250))
        self.child_image.setText("")
        self.child_image.setPixmap(QtGui.QPixmap("../../resources/question_mark.png"))
        self.child_image.setScaledContents(True)
        self.child_image.setObjectName("child_image")
        self.parent_image_2 = QtWidgets.QLabel(self.centralwidget)
        self.parent_image_2.setGeometry(QtCore.QRect(800, 100, 250, 250))
        self.parent_image_2.setText("")
        self.parent_image_2.setPixmap(QtGui.QPixmap("../../resources/question_mark.png"))
        self.parent_image_2.setScaledContents(True)
        self.parent_image_2.setObjectName("parent_image_2")
        self.parent_image_1 = QtWidgets.QLabel(self.centralwidget)
        self.parent_image_1.setGeometry(QtCore.QRect(350, 100, 250, 250))
        self.parent_image_1.setText("")
        self.parent_image_1.setPixmap(QtGui.QPixmap("../../resources/question_mark.png"))
        self.parent_image_1.setScaledContents(True)
        self.parent_image_1.setObjectName("parent_image_1")
        self.parent_arrows = QtWidgets.QLabel(self.centralwidget)
        self.parent_arrows.setGeometry(QtCore.QRect(460, 110, 481, 381))
        self.parent_arrows.setText("")
        self.parent_arrows.setPixmap(QtGui.QPixmap("../../resources/arrows_merging.png"))
        self.parent_arrows.setScaledContents(True)
        self.parent_arrows.setObjectName("parent_arrows")
        self.parent_1_label = QtWidgets.QLabel(self.centralwidget)
        self.parent_1_label.setGeometry(QtCore.QRect(350, 50, 251, 51))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(False)
        font.setWeight(50)
        self.parent_1_label.setFont(font)
        self.parent_1_label.setAlignment(QtCore.Qt.AlignCenter)
        self.parent_1_label.setObjectName("parent_1_label")
        self.parent_2_label = QtWidgets.QLabel(self.centralwidget)
        self.parent_2_label.setGeometry(QtCore.QRect(800, 50, 251, 51))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(False)
        font.setWeight(50)
        self.parent_2_label.setFont(font)
        self.parent_2_label.setAlignment(QtCore.Qt.AlignCenter)
        self.parent_2_label.setObjectName("parent_2_label")
        self.parent_arrows.raise_()
        self.child_image.raise_()
        self.parent_image_2.raise_()
        self.parent_image_1.raise_()
        self.parent_1_label.raise_()
        self.parent_2_label.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1280, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.parent_1_label.setText(_translate("MainWindow", "Current parent"))
        self.parent_2_label.setText(_translate("MainWindow", "Choosen mate"))
