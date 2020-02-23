
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


class QFamilyTree(QWidget):

    def __init__(self, parent=None):
        super(QFamilyTree, self).__init__(parent)
        self.number_of_parents = 2

        self.generation = Generation.getInstance()

        self.parent_image_path = "../../imgs/parent/iteration{}_main.png"
        self.candidate_image_path = "../../imgs/children/iteration{}_candidate{}.png"
        self.animation_image_path = "../../imgs/interpolations/iteration{}_main.gif"
        self.template_image_path = "../../resources/template.png"

        self.tree_layout = QGridLayout()

        #self.title = QLabel(self)
        #self.title.setText("Family Tree")

        self.parents = [None] * self.number_of_parents
        for child_index in range(self.number_of_parents):
            self.parents[child_index] = QLabel(self)
            self.tree_layout.addWidget(self.parents[child_index], 1, 2 * child_index)  # [0, 2]

        self.child_label = QLabel(self)
        self.tree_layout.addWidget(self.child_label, 2, 1)

        super(QFamilyTree, self).setLayout(self.tree_layout)

    def update(self):
        for parent_index in range(self.number_of_parents):
            parent_path = self.parent_image_path.format(self.generation.index - 1)
            if not os.path.exists(parent_path):
                parent_path = self.template_image_path
            parent_image = QPixmap(parent_path)
            self.parents[parent_index].setPixmap(parent_image)

        child_path = self.parent_image_path.format(self.generation.index)
        if not os.path.exists(child_path):
            child_path = self.template_path
        child_image = QPixmap(child_path)
        self.child_label.setPixmap(child_image)
