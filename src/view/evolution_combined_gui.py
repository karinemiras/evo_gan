# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'evolution_combined_ui.ui'
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


class Ui_breeding_pictures(object):
    def setupUi(self, breeding_pictures):
        if breeding_pictures.objectName():
            breeding_pictures.setObjectName(u"breeding_pictures")
        breeding_pictures.resize(1280, 720)
        self.centralwidget = QWidget(breeding_pictures)
        self.centralwidget.setObjectName(u"centralwidget")
        self.parent_image = QLabel(self.centralwidget)
        self.parent_image.setObjectName(u"parent_image")
        self.parent_image.setGeometry(QRect(120, 200, 350, 350))
        self.parent_image.setPixmap(QPixmap(u"../../resources/question_mark.png"))
        self.parent_image.setScaledContents(True)
        self.mate_label = QLabel(self.centralwidget)
        self.mate_label.setObjectName(u"mate_label")
        self.mate_label.setGeometry(QRect(740, 30, 531, 61))
        font = QFont()
        font.setFamily(u"Tauri")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.mate_label.setFont(font)
        self.mate_label.setStyleSheet(u"color : white;")
        self.mate_label.setAlignment(Qt.AlignCenter)
        self.candidate_1_button = QPushButton(self.centralwidget)
        self.candidate_1_button.setObjectName(u"candidate_1_button")
        self.candidate_1_button.setGeometry(QRect(743, 122, 225, 225))
        self.candidate_1_button.setAutoFillBackground(False)
        icon = QIcon()
        icon.addFile(u"../../resources/question_mark.png", QSize(), QIcon.Normal, QIcon.Off)
        self.candidate_1_button.setIcon(icon)
        self.candidate_1_button.setIconSize(QSize(250, 250))
        self.candidate_1_button.setFlat(True)
        self.candidate_3_button = QPushButton(self.centralwidget)
        self.candidate_3_button.setObjectName(u"candidate_3_button")
        self.candidate_3_button.setGeometry(QRect(1023, 122, 225, 225))
        self.candidate_3_button.setIcon(icon)
        self.candidate_3_button.setIconSize(QSize(250, 250))
        self.candidate_3_button.setFlat(True)
        self.parent_label = QLabel(self.centralwidget)
        self.parent_label.setObjectName(u"parent_label")
        self.parent_label.setGeometry(QRect(60, 70, 471, 51))
        self.parent_label.setFont(font)
        self.parent_label.setStyleSheet(u"color : white;")
        self.parent_label.setAlignment(Qt.AlignCenter)
        self.candidate_2_button = QPushButton(self.centralwidget)
        self.candidate_2_button.setObjectName(u"candidate_2_button")
        self.candidate_2_button.setGeometry(QRect(743, 402, 225, 225))
        self.candidate_2_button.setIcon(icon)
        self.candidate_2_button.setIconSize(QSize(250, 250))
        self.candidate_2_button.setFlat(True)
        self.child_image = QLabel(self.centralwidget)
        self.child_image.setObjectName(u"child_image")
        self.child_image.setEnabled(True)
        self.child_image.setGeometry(QRect(515, 360, 250, 250))
        self.child_image.setPixmap(QPixmap(u"../../resources/question_mark.png"))
        self.child_image.setScaledContents(True)
        self.parent_1_image = QLabel(self.centralwidget)
        self.parent_1_image.setObjectName(u"parent_1_image")
        self.parent_1_image.setEnabled(True)
        self.parent_1_image.setGeometry(QRect(340, 82, 200, 200))
        self.parent_1_image.setPixmap(QPixmap(u"../../resources/question_mark.png"))
        self.parent_1_image.setScaledContents(True)
        self.parent_1_label = QLabel(self.centralwidget)
        self.parent_1_label.setObjectName(u"parent_1_label")
        self.parent_1_label.setEnabled(True)
        self.parent_1_label.setGeometry(QRect(330, 10, 221, 51))
        font1 = QFont()
        font1.setFamily(u"Tauri")
        font1.setPointSize(30)
        font1.setBold(True)
        font1.setWeight(75)
        self.parent_1_label.setFont(font1)
        self.parent_1_label.setStyleSheet(u"color : white;")
        self.parent_1_label.setAlignment(Qt.AlignCenter)
        self.parent_2_label = QLabel(self.centralwidget)
        self.parent_2_label.setObjectName(u"parent_2_label")
        self.parent_2_label.setEnabled(True)
        self.parent_2_label.setGeometry(QRect(727, 10, 206, 51))
        self.parent_2_label.setFont(font1)
        self.parent_2_label.setStyleSheet(u"color : white;")
        self.parent_2_label.setAlignment(Qt.AlignCenter)
        self.parent_arrows = QLabel(self.centralwidget)
        self.parent_arrows.setObjectName(u"parent_arrows")
        self.parent_arrows.setEnabled(True)
        self.parent_arrows.setGeometry(QRect(390, 150, 486, 281))
        self.parent_arrows.setStyleSheet(u"")
        self.parent_arrows.setPixmap(QPixmap(u"../../resources/arrows_merging.png"))
        self.parent_arrows.setScaledContents(True)
        self.parent_2_image = QLabel(self.centralwidget)
        self.parent_2_image.setObjectName(u"parent_2_image")
        self.parent_2_image.setEnabled(True)
        self.parent_2_image.setGeometry(QRect(729, 82, 200, 200))
        self.parent_2_image.setPixmap(QPixmap(u"../../resources/question_mark.png"))
        self.parent_2_image.setScaledContents(True)
        self.loading_animation = QLabel(self.centralwidget)
        self.loading_animation.setObjectName(u"loading_animation")
        self.loading_animation.setEnabled(True)
        self.loading_animation.setGeometry(QRect(590, 430, 100, 100))
        self.loading_animation.setPixmap(QPixmap(u"../../resources/question_mark.png"))
        self.loading_animation.setScaledContents(True)
        self.candidate_4_button = QPushButton(self.centralwidget)
        self.candidate_4_button.setObjectName(u"candidate_4_button")
        self.candidate_4_button.setGeometry(QRect(1023, 402, 225, 225))
        self.candidate_4_button.setIcon(icon)
        self.candidate_4_button.setIconSize(QSize(250, 250))
        self.candidate_4_button.setFlat(True)
        self.candidate_4_frame = QLabel(self.centralwidget)
        self.candidate_4_frame.setObjectName(u"candidate_4_frame")
        self.candidate_4_frame.setEnabled(False)
        self.candidate_4_frame.setGeometry(QRect(1000, 380, 270, 270))
        self.candidate_4_frame.setPixmap(QPixmap(u"../../resources/image_frame.png"))
        self.candidate_4_frame.setScaledContents(True)
        self.candidate_2_frame = QLabel(self.centralwidget)
        self.candidate_2_frame.setObjectName(u"candidate_2_frame")
        self.candidate_2_frame.setEnabled(False)
        self.candidate_2_frame.setGeometry(QRect(720, 380, 270, 270))
        self.candidate_2_frame.setPixmap(QPixmap(u"../../resources/image_frame.png"))
        self.candidate_2_frame.setScaledContents(True)
        self.candidate_1_frame = QLabel(self.centralwidget)
        self.candidate_1_frame.setObjectName(u"candidate_1_frame")
        self.candidate_1_frame.setEnabled(False)
        self.candidate_1_frame.setGeometry(QRect(720, 100, 270, 270))
        self.candidate_1_frame.setPixmap(QPixmap(u"../../resources/image_frame.png"))
        self.candidate_1_frame.setScaledContents(True)
        self.candidate_3_frame = QLabel(self.centralwidget)
        self.candidate_3_frame.setObjectName(u"candidate_3_frame")
        self.candidate_3_frame.setEnabled(False)
        self.candidate_3_frame.setGeometry(QRect(1000, 100, 270, 270))
        self.candidate_3_frame.setPixmap(QPixmap(u"../../resources/image_frame.png"))
        self.candidate_3_frame.setScaledContents(True)
        self.parent_frame = QLabel(self.centralwidget)
        self.parent_frame.setObjectName(u"parent_frame")
        self.parent_frame.setEnabled(True)
        self.parent_frame.setGeometry(QRect(40, 120, 510, 510))
        self.parent_frame.setPixmap(QPixmap(u"../../resources/image_frame_parent.png"))
        self.parent_frame.setScaledContents(True)
        self.background_image = QLabel(self.centralwidget)
        self.background_image.setObjectName(u"background_image")
        self.background_image.setEnabled(True)
        self.background_image.setGeometry(QRect(0, 0, 1280, 720))
        self.background_image.setPixmap(QPixmap(u"../../resources/tree_background_blurred.png"))
        self.background_image.setScaledContents(True)
        self.child_frame = QLabel(self.centralwidget)
        self.child_frame.setObjectName(u"child_frame")
        self.child_frame.setEnabled(True)
        self.child_frame.setGeometry(QRect(450, 298, 380, 375))
        self.child_frame.setPixmap(QPixmap(u"../../resources/image_frame_parent.png"))
        self.child_frame.setScaledContents(True)
        self.parent_1_frame = QLabel(self.centralwidget)
        self.parent_1_frame.setObjectName(u"parent_1_frame")
        self.parent_1_frame.setEnabled(True)
        self.parent_1_frame.setGeometry(QRect(327, 71, 225, 220))
        self.parent_1_frame.setPixmap(QPixmap(u"../../resources/image_frame.png"))
        self.parent_1_frame.setScaledContents(True)
        self.parent_2_frame = QLabel(self.centralwidget)
        self.parent_2_frame.setObjectName(u"parent_2_frame")
        self.parent_2_frame.setEnabled(True)
        self.parent_2_frame.setGeometry(QRect(717, 71, 225, 220))
        self.parent_2_frame.setPixmap(QPixmap(u"../../resources/image_frame.png"))
        self.parent_2_frame.setScaledContents(True)
        self.breeding_label = QLabel(self.centralwidget)
        self.breeding_label.setObjectName(u"breeding_label")
        self.breeding_label.setGeometry(QRect(270, 660, 771, 51))
        font2 = QFont()
        font2.setFamily(u"Tauri")
        font2.setPointSize(28)
        font2.setBold(True)
        font2.setWeight(75)
        self.breeding_label.setFont(font2)
        self.breeding_label.setStyleSheet(u"color : white;")
        self.breeding_label.setAlignment(Qt.AlignCenter)
        breeding_pictures.setCentralWidget(self.centralwidget)
        self.background_image.raise_()
        self.parent_arrows.raise_()
        self.child_image.raise_()
        self.child_frame.raise_()
        self.candidate_1_frame.raise_()
        self.candidate_3_frame.raise_()
        self.candidate_4_frame.raise_()
        self.candidate_2_frame.raise_()
        self.parent_image.raise_()
        self.mate_label.raise_()
        self.parent_label.raise_()
        self.parent_1_label.raise_()
        self.parent_2_label.raise_()
        self.loading_animation.raise_()
        self.candidate_2_button.raise_()
        self.candidate_4_button.raise_()
        self.candidate_1_button.raise_()
        self.candidate_3_button.raise_()
        self.parent_frame.raise_()
        self.parent_1_image.raise_()
        self.parent_1_frame.raise_()
        self.parent_2_image.raise_()
        self.parent_2_frame.raise_()
        self.breeding_label.raise_()

        self.retranslateUi(breeding_pictures)

        QMetaObject.connectSlotsByName(breeding_pictures)
    # setupUi

    def retranslateUi(self, breeding_pictures):
        breeding_pictures.setWindowTitle(QCoreApplication.translate("breeding_pictures", u"Breeding Pictures", None))
        self.parent_image.setText("")
        self.mate_label.setText(QCoreApplication.translate("breeding_pictures", u"Choose a Parent 2", None))
        self.candidate_1_button.setText("")
        self.candidate_3_button.setText("")
        self.parent_label.setText(QCoreApplication.translate("breeding_pictures", u"Parent 1", None))
        self.candidate_2_button.setText("")
        self.child_image.setText("")
        self.parent_1_image.setText("")
        self.parent_1_label.setText(QCoreApplication.translate("breeding_pictures", u"Parent 1", None))
        self.parent_2_label.setText(QCoreApplication.translate("breeding_pictures", u"Parent 2", None))
        self.parent_arrows.setText("")
        self.parent_2_image.setText("")
        self.loading_animation.setText("")
        self.candidate_4_button.setText("")
        self.candidate_4_frame.setText("")
        self.candidate_2_frame.setText("")
        self.candidate_1_frame.setText("")
        self.candidate_3_frame.setText("")
        self.parent_frame.setText("")
        self.background_image.setText("")
        self.child_frame.setText("")
        self.parent_1_frame.setText("")
        self.parent_2_frame.setText("")
        self.breeding_label.setText(QCoreApplication.translate("breeding_pictures", u"Please Hold \u2013 Breeding Taking Place.", None))
    # retranslateUi

