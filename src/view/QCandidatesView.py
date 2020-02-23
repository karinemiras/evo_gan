
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
from functools import partial


from presenter.generation import Generation

from view.QMovieLabel import QMovieLabel


class QCandidatesView(QWidget):

    def __init__(self, function, parent=None):
        super(QCandidatesView, self).__init__(parent)
        self.number_of_candidates = 4

        self.image_size = 128

        self.generation = Generation.getInstance()

        self.parent_image_path = "../../imgs/parent/iteration{}_main.png"
        self.candidate_image_path = "../../imgs/children/iteration{}_candidate{}.png"
        self.animation_image_path = "../../imgs/interpolations/iteration{}_main.gif"
        self.template_image_path = "../../resources/template.png"

        self.candidate_layout = QGridLayout()

        self.candidate_buttons = [None] * self.number_of_candidates
        self.rows = 2

        for candidate_index in range(self.number_of_candidates):
            self.candidate_buttons[candidate_index] = QPushButton("", self)
            self.candidate_buttons[candidate_index].clicked.connect(partial(function, candidate_index))
            self.candidate_layout.addWidget(self.candidate_buttons[candidate_index],
                                            candidate_index / 2, candidate_index % 2)
            self.candidate_buttons[candidate_index].setIconSize(QtCore.QSize(self.image_size, self.image_size))

        super(QCandidatesView, self).setLayout(self.candidate_layout)

    def update(self):
        for child_index in range(self.number_of_candidates):
            candidate_path = self.candidate_image_path.format(self.generation.index, child_index)
            if not os.path.exists(candidate_path):
                candidate_path = self.template_image_path
            self.candidate_buttons[child_index].setIcon(QtGui.QIcon(candidate_path))
