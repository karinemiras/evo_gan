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
from view.QEvolutionHistory import QEvolutionHistory
from view.QFamilyTree import QFamilyTree
from view.QCandidatesView import QCandidatesView

class EvolutionGUI(QMainWindow):
    def __init__(self, demo = False):
        super(EvolutionGUI, self).__init__()

        self.generation = Generation.getInstance()

        if demo is False:
            n_children = 5
            batch_size = 5
            interpolation_frames = 5
            self.evolution = Evolution(interpolation_frames, n_children, batch_size, resolution=128)
        else:
            self.evolution = None

        self.window_width = 1000
        window_height = 1000

        self.image_size = 128

        self.setGeometry(360, 50, self.window_width, window_height)
        self.setFixedSize(self.window_width, window_height)

        self.parent_image_path = "../../imgs/parent/iteration{}_main.png"
        self.candidate_image_path = "../../imgs/children/iteration{}_candidate{}.png"
        self.animation_image_path = "../../imgs/interpolations/iteration{}_main.gif"


        self.family_tree = QFamilyTree(self)

        self.candidates = QCandidatesView(self.visualize_generation, self)

        self.history = QEvolutionHistory(self)

        self.main_layout = QGridLayout()
        self.main_layout.addWidget(self.family_tree, 0, 0)
        self.main_layout.addWidget(self.candidates, 0, 1)
        self.main_layout.addWidget(self.history, 0, 2)

        self.widget = QWidget()
        self.widget.setLayout(self.main_layout)
        self.widget.show()

        self.visualize_generation()

    def visualize_generation(self, index=None):
        if index is not None:
            if self.evolution is not None:
                self.evolution.process_generation(index)
            self.generation.index += 1

        self.family_tree.update()

        self.candidates.update()

        self.history.update()


if __name__ == '__main__':
    is_demo = True

    #evolution = Evolution(interpolation_frames, n_children, batch_size, resolution=128, logger=logger)
    app = QApplication(sys.argv)
    w = EvolutionGUI(True)
    sys.exit(app.exec_())