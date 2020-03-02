# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'evolution_candidates_ui.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1280, 720)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.parent_image = QLabel(self.centralwidget)
        self.parent_image.setObjectName(u"parent_image")
        self.parent_image.setGeometry(QRect(270, 225, 250, 250))
        self.parent_image.setPixmap(QPixmap(u"../../resources/question_mark.png"))
        self.parent_image.setScaledContents(True)
        self.candidate_button_1 = QPushButton(self.centralwidget)
        self.candidate_button_1.setObjectName(u"candidate_button_1")
        self.candidate_button_1.setGeometry(QRect(800, 75, 150, 150))
        self.candidate_button_1.setAutoFillBackground(False)
        icon = QIcon()
        icon.addFile(u"../../resources/question_mark.png", QSize(), QIcon.Normal, QIcon.Off)
        self.candidate_button_1.setIcon(icon)
        self.candidate_button_1.setIconSize(QSize(150, 150))
        self.candidate_button_2 = QPushButton(self.centralwidget)
        self.candidate_button_2.setObjectName(u"candidate_button_2")
        self.candidate_button_2.setGeometry(QRect(800, 275, 150, 150))
        self.candidate_button_2.setIcon(icon)
        self.candidate_button_2.setIconSize(QSize(150, 150))
        self.candidate_button_3 = QPushButton(self.centralwidget)
        self.candidate_button_3.setObjectName(u"candidate_button_3")
        self.candidate_button_3.setGeometry(QRect(800, 475, 150, 150))
        self.candidate_button_3.setIcon(icon)
        self.candidate_button_3.setIconSize(QSize(150, 150))
        self.parent_label = QLabel(self.centralwidget)
        self.parent_label.setObjectName(u"parent_label")
        self.parent_label.setGeometry(QRect(268, 164, 251, 51))
        font = QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.parent_label.setFont(font)
        self.parent_label.setAlignment(Qt.AlignCenter)
        self.mate_label = QLabel(self.centralwidget)
        self.mate_label.setObjectName(u"mate_label")
        self.mate_label.setGeometry(QRect(750, 10, 251, 51))
        font1 = QFont()
        font1.setPointSize(24)
        font1.setBold(False)
        font1.setWeight(50)
        self.mate_label.setFont(font1)
        self.mate_label.setAlignment(Qt.AlignCenter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1280, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.parent_image.setText("")
        self.candidate_button_1.setText("")
        self.candidate_button_2.setText("")
        self.candidate_button_3.setText("")
        self.parent_label.setText(QCoreApplication.translate("MainWindow", u"Current parent", None))
        self.mate_label.setText(QCoreApplication.translate("MainWindow", u"Choose a mate", None))
    # retranslateUi

