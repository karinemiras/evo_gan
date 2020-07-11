
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

from presenter.generation import Generation
from view.QMovieLabel import QMovieLabel


class EvolutionTreeManager:

    def __init__(self, parent_images, parent_frames, child_image, child_frame, parent_arrow, parent_1_label, parent_2_label, central_widget):
        self.number_of_parents = len(parent_images)

        self.generation = Generation.getInstance()

        self.parent_image_path = "../imgs/parent/iteration{}_{}.png"
        self.animation_image_path = "../imgs/interpolations/iteration{}_main.gif"
        self.template_image_path = "../resources/template.png"
        self.child_frame_path = "../resources/image_frame_parent.png"
        self.parent_frame_path = "../resources/image_frame.png"
        self.merging_arrows_path = "../resources/arrows_merging.png"

        self.central_widget = central_widget
        self.parent_images = parent_images
        self.parent_frames = parent_frames

        self.parent_arrow = parent_arrow
        self.parent_arrow.setPixmap(QPixmap(self.merging_arrows_path))

        for parent_index in range(self.number_of_parents):
            self.parent_frames[parent_index].setPixmap(QPixmap(self.parent_frame_path))

        self.child_frame = child_frame
        self.child_frame.setPixmap(QPixmap(self.child_frame_path))

        self.child_image = child_image

        self.child_movie = QMovieLabel(self.template_image_path, self.central_widget)

        self.elements = parent_images
        self.elements.extend(self.parent_frames)
        self.elements.extend([self.child_image, self.child_frame, child_image, self.child_movie,
                              parent_arrow, parent_1_label, parent_2_label])

        self.visibility = True

        self.visible(False)

    def visible(self, state):
        if state != self.visibility:
            for element in self.elements:
                if state:
                    element.show()
                else:
                    element.hide()

            self.visibility = state

    def update(self):
        print("tree update")

        for parent_index in range(self.number_of_parents):
            parent_path = self.parent_image_path.format(self.generation.index - 1, parent_index)
            print(parent_index, ": ", parent_path)
            if not os.path.exists(parent_path):
                parent_path = self.template_image_path
            print(parent_index, ": ", parent_path)
            parent_image = QPixmap(parent_path)
            self.parent_images[parent_index].setPixmap(parent_image)
            self.parent_images[parent_index].setScaledContents(True)

        child_path = self.animation_image_path.format(self.generation.index)
        if not os.path.exists(child_path):
            child_path = self.template_image_path
        print("child_path", child_path)

        self.child_movie.initialize(child_path)
        self.child_movie.setGeometry(self.child_image.geometry())
        self.child_movie.setScaledContents(True)

