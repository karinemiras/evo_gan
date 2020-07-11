
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

class LoadingManager:
    def __init__(self, loading_label, breeding_label, central_widget):

        self.loading_image_path = "../resources/yellow_loading.gif"
        self.template_image_path = "../resources/template.png"

        self.loading_label = QMovieLabel(self.template_image_path, central_widget)
        self.loading_label.setObjectName(u"history_image")
        self.loading_label.setGeometry(loading_label.geometry())
        self.loading_label.setScaledContents(True)
        self.loading_elements = [loading_label, self.loading_label, breeding_label]

        self.generation = Generation.getInstance()

        loading_path = self.loading_image_path.format(self.generation.index)
        if not os.path.exists(loading_path):
            loading_path = self.template_image_path
        self.loading_label.initialize(loading_path)
        self.loading_label.setScaledContents(True)

        self.visibility = True

        self.visible(False)

    def visible(self, state):
        if state != self.visibility:
            if state:
                for loading_element in self.loading_elements:
                    loading_element.hide()
            else:
                for loading_element in self.loading_elements:
                    loading_element.hide()

            self.visibility = state

    def loading(self):
        for loading_element in self.loading_elements:
            loading_element.show()

        self.loading_label.setText("Please Hold – Breeding Taking Place.")

    def unloading(self):
        for loading_element in self.loading_elements:
            loading_element.hide()

        self.loading_label.show()
        self.loading_label.setText("Child")

    def update(self):
        self.loading_label.movie.start()