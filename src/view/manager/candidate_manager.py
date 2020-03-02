
import sys
import asyncio
import os
import PySide2

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *
from functools import partial


from presenter.generation import Generation

from view.QMovieLabel import QMovieLabel


class CandidateManager:

    def __init__(self, parent_image, candidate_buttons, parent_label, candidate_label, loading_label, central_widget, function):

        self.number_of_candidates = len(candidate_buttons)

        self.icon_size = 200

        self.generation = Generation.getInstance()

        self.parent_image_path = "../../imgs/parent/iteration{}_0.png"
        self.candidate_image_path = "../../imgs/candidate/iteration{}_{}.png"
        self.template_image_path = "../../../resources/template.png"
        self.loading_image_path = "../../resources/loading.gif"

        self.parent_image = parent_image

        self.candidate_buttons = candidate_buttons

        self.loading_label = QMovieLabel(self.template_image_path, central_widget)
        self.loading_label.setObjectName(u"history_image")
        self.loading_label.setGeometry(loading_label.geometry())
        self.loading_label.setScaledContents(True)

        for candidate_index in range(self.number_of_candidates):
            self.candidate_buttons[candidate_index].clicked.connect(partial(function, candidate_index))

        self.elements = [self.parent_image]
        self.elements.extend(self.candidate_buttons)
        self.elements.extend([parent_label, candidate_label, ])

        self.loading_elements = [loading_label, self.loading_label]

        self.visibility = False

        self.visible(True)

    def visible(self, state):
        if state != self.visibility:
            print("visible ", state)
            if state:
                for element in self.elements:
                    element.show()
                for loading_element in self.loading_elements:
                    loading_element.hide()
            else:
                for element in self.elements:
                    element.hide()
                for loading_element in self.loading_elements:
                    loading_element.hide()

            self.visibility = state

    def loading(self):
        print("loading")
        for loading_element in self.loading_elements:
            loading_element.show()

    def update(self):
        parent_path = self.parent_image_path.format(self.generation.index)
        if not os.path.exists(parent_path):
            parent_path = self.template_image_path
        child_image = QPixmap(parent_path)

        self.parent_image.setPixmap(child_image)
        self.parent_image.setScaledContents(True)

        for candidate_index in range(self.number_of_candidates):
            candidate_path = self.candidate_image_path.format(self.generation.index, candidate_index)
            if not os.path.exists(candidate_path):
                candidate_path = self.template_image_path

            candidate_image = QPixmap(candidate_path)
            icon = QIcon(candidate_image.scaled(self.icon_size, self.icon_size))
            self.candidate_buttons[candidate_index].setIcon(icon)

        loading_path = self.loading_image_path.format(self.generation.index)
        if not os.path.exists(loading_path):
            loading_path = self.template_image_path

        """
        child_image = QPixmap(child_path)

        self.child_image.setPixmap(child_image)
        self.child_image.setScaledContents(True)
        """

        self.loading_label.initialize(loading_path)
        self.loading_label.setScaledContents(True)
