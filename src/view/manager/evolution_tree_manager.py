
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

    def __init__(self, parent_images, child_image, parent_arrow, parent_1_label, parent_2_label, central_widget):
        self.number_of_parents = len(parent_images)

        self.generation = Generation.getInstance()

        self.parent_image_path = "../../imgs/parent/iteration{}_{}.png"
        self.animation_image_path = "../../imgs/interpolations/iteration{}_main.gif"
        self.template_image_path = "../../resources/template.png"

        self.parent_images = parent_images

        #self.child_image = child_image

        self.child_image = QMovieLabel(self.template_image_path, central_widget)
        self.child_image.setObjectName(u"history_image")
        self.child_image.setGeometry(child_image.geometry())
        self.child_image.setScaledContents(True)

        self.elements = parent_images
        self.elements.extend([self.child_image, child_image, parent_arrow, parent_1_label, parent_2_label])

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
        for parent_index in range(self.number_of_parents):
            parent_path = self.parent_image_path.format(self.generation.index, parent_index)
            if not os.path.exists(parent_path):
                parent_path = self.template_image_path
            parent_image = QPixmap(parent_path)
            self.parent_images[parent_index].setPixmap(parent_image)
            self.parent_images[parent_index].setScaledContents(True)

        child_path = self.animation_image_path.format(self.generation.index)
        if not os.path.exists(child_path):
            child_path = self.template_image_path

        """
        child_image = QPixmap(child_path)

        self.child_image.setPixmap(child_image)
        self.child_image.setScaledContents(True)
        """

        self.child_image.initialize(child_path)
        self.child_image.setScaledContents(True)

