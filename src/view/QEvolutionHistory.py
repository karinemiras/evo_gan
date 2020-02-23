
import sys
import asyncio
import os
from PyQt5 import QtGui, QtCore
import PyQt5.QtCore
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QMovie, QPainter, QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QPushButton, QHBoxLayout, QGroupBox, QDialog, QVBoxLayout, QGridLayout
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import PyQt5.QtCore


from presenter.generation import Generation

from view.QMovieLabel import QMovieLabel


class QEvolutionHistory(QWidget):

    def __init__(self, parent=None):
        super(QEvolutionHistory, self).__init__(parent)
        self.number_of_children = 3

        self.generation = Generation.getInstance()
        self.animation_image_path = "../../imgs/interpolations/iteration{}_main.gif"
        self.template_image_path = "../../resources/template.png"

        self.historical_layout = QGridLayout()

        self.animations = [None] * self.number_of_children
        for child_index in range(self.number_of_children):
            self.animations[child_index] = QMovieLabel('', parent)
            self.animations[child_index].adjustSize()
            self.animations[child_index].show()

            self.historical_layout.addWidget(self.animations[child_index], child_index, 0)

        super(QEvolutionHistory, self).setLayout(self.historical_layout)

    def update(self):
        for child_index in range(self.number_of_children):
            image_path = self.animation_image_path.format(self.generation.index - (self.number_of_children - child_index - 1))
            if not os.path.exists(image_path):
                image_path = self.template_image_path
            self.animations[child_index].initialize(image_path)
            self.animations[child_index].adjustSize()
            self.animations[child_index].show()


