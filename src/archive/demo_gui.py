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

import time
from functools import partial

from presenter.evolution import Evolution

from presenter.generation import Generation
from view.QMovieLabel import QMovieLabel


class DemoGUI(QMainWindow):
    def __init__(self, evolution):
        super(DemoGUI, self).__init__()

        self.generation = Generation.getInstance()

        self.evolution = evolution

        self.window_width = 1000
        window_height = 1000

        self.image_size = 128

        self.setGeometry(360, 50, self.window_width, window_height)
        self.setFixedSize(self.window_width, window_height)

        self.parent_image_path = "../../imgs/parent/iteration{}_main.png"
        self.candidate_image_path = "../../imgs/candidate/iteration{}_candidate{}.png"
        self.animation_image_path = "../../imgs/interpolations/iteration{}_main.gif"

        self.candidate_box = QGroupBox()
        self.candidate_layout = QHBoxLayout()
        self.candidate_buttons = [None] * self.evolution.n_children

        for child_index in range(self.evolution.n_children):
            self.candidate_buttons[child_index] = QPushButton("", self)
            self.candidate_buttons[child_index].clicked.connect(partial(self.visualize_generation, child_index))
            self.candidate_layout.addWidget(self.candidate_buttons[child_index])
            self.candidate_buttons[child_index].setIconSize(QtCore.QSize(self.image_size, self.image_size))

        self.candidate_box.setLayout(self.candidate_layout)

        self.parent = QLabel(self)

        self.main_layout = QVBoxLayout()
        self.main_layout.addWidget(self.candidate_box)
        self.main_layout.addWidget(self.parent)

        self.animation = QMovieLabel('', self)
        self.animation.adjustSize()
        self.animation.show()
        self.main_layout.addWidget(self.animation)

        self.widget = QWidget()
        self.widget.setLayout(self.main_layout)

        self.widget.show()

        self.visualize_generation()

    def visualize_generation(self, index=None):
        if index is not None:
            self.evolution.process_generation(index)
            self.generation.index += 1

        parent_path = self.parent_image_path.format(self.generation.index)
        parent_image = QPixmap(parent_path)
        self.parent.setPixmap(parent_image)

        for child_index in range(self.evolution.n_children):
            candidate_path = self.candidate_image_path.format(self.generation.index, child_index)
            self.candidate_buttons[child_index].setIcon(QtGui.QIcon(candidate_path))

        self.animation.initialize(self.animation_image_path.format(self.generation.index))
        self.animation.adjustSize()
        self.animation.show()


if __name__ == '__main__':
    is_demo = True

    n_children = 5
    batch_size = 5
    interpolation_frames = 5
    evolution = Evolution(interpolation_frames, n_children, batch_size, resolution=128)

    #evolution = Evolution(interpolation_frames, n_children, batch_size, resolution=128, logger=logger)
    app = QApplication(sys.argv)
    w = DemoGUI(evolution)
    sys.exit(app.exec_())