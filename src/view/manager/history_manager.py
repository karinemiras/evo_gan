
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


class HistoryManager:

    def __init__(self, history_images, central_widget):
        self.history_length = len(history_images)

        self.generation = Generation.getInstance()

        self.animation_image_path = "../../imgs/interpolations/iteration{}_main.gif"
        self.template_image_path = "../../../resources/template.png"

        self.history_movies = [None] * self.history_length
        for child_index in range(self.history_length):
            self.history_movies[child_index] = QMovieLabel(self.template_image_path, central_widget)
            self.history_movies[child_index].setObjectName(u"history_image_{}".format(child_index))
            self.history_movies[child_index].setGeometry(history_images[child_index].geometry())
            self.history_movies[child_index].setScaledContents(True)

    def update(self):

        for child_index in range(self.history_length):
            image_path = self.animation_image_path.format(self.generation.index - (self.history_length - child_index - 1))
            if not os.path.exists(image_path):
                image_path = self.template_image_path

            self.history_movies[child_index].initialize(image_path)
            self.history_movies[child_index].setScaledContents(True)
            self.history_movies[child_index].show()
