
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

    def __init__(self, parent_image, parent_frame, candidate_buttons, candidate_frames, parent_label, candidate_label, function):

        self.number_of_candidates = len(candidate_buttons)
        print("number of candidates", self.number_of_candidates)

        self.icon_size = 225

        self.generation = Generation.getInstance()

        self.parent_image_path = "../imgs/parent/iteration{}_0.png"
        self.candidate_image_path = "../imgs/candidate/iteration{}_{}.png"
        self.template_image_path = "../resources/template.png"

        self.parent_frame_path = "../resources/image_frame_parent.png"
        self.candidate_frame_path = "../resources/image_frame.png"

        self.parent_image = parent_image
        self.parent_frame = parent_frame

        self.candidate_buttons = candidate_buttons
        self.candidate_frames = candidate_frames

        self.function = function

        self.prepare_choice()

        self.elements = [self.parent_image]
        self.elements.extend(self.candidate_buttons)
        self.elements.extend(self.candidate_frames)
        self.elements.extend([parent_label, self.parent_frame, candidate_label, ])

        self.wait = False

        self.visibility = False
        self.visible(True)

    def nothing(self, candidate):
        pass

    def reconnect(self, signal, newhandler=None, oldhandler=None):
        while True:
            try:
                if oldhandler is not None:
                    signal.disconnect(oldhandler)
                else:
                    signal.disconnect()
            except TypeError:
                break
        if newhandler is not None:
            signal.connect(newhandler)

    def nothing(self):
        pass

    def process_choice(self, candidate_index):
        if not self.wait:
            self.wait = True

            for index in range(self.number_of_candidates):
                self.candidate_buttons[index].setEnabled(False)

            self.candidate_frames[candidate_index].setEnabled(True)
            self.candidate_buttons[candidate_index].setEnabled(True)

            self.function(candidate_index)

    def prepare_choice(self):
        self.wait = False

        for candidate_index in range(self.number_of_candidates):
            self.candidate_buttons[candidate_index].clicked.connect(partial(self.process_choice, candidate_index))
            self.candidate_frames[candidate_index].setEnabled(False)
            self.candidate_buttons[candidate_index].setEnabled(True)

    def visible(self, state):
        if state != self.visibility:
            if state:
                for element in self.elements:
                    element.show()
            else:
                for element in self.elements:
                    element.hide()

            self.visibility = state

    def update(self):
        parent_path = self.parent_image_path.format(self.generation.index)
        if not os.path.exists(parent_path):
            parent_path = self.template_image_path
        child_image = QPixmap(parent_path)

        self.parent_frame.setPixmap(QPixmap(self.parent_frame_path))
        self.parent_frame.setScaledContents(True)

        self.parent_image.setPixmap(child_image)
        self.parent_image.setScaledContents(True)

        for candidate_index in range(self.number_of_candidates):

            candidate_path = self.candidate_image_path.format(self.generation.index, candidate_index)
            if not os.path.exists(candidate_path):
                candidate_path = self.template_image_path

            candidate_image = QPixmap(candidate_path)
            icon = QIcon(candidate_image.scaled(self.icon_size, self.icon_size))
            self.candidate_buttons[candidate_index].setIcon(icon)

            self.candidate_frames[candidate_index].setPixmap(QPixmap(self.candidate_frame_path))


