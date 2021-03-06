
import PySide2

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient, QMovie)
from PySide2.QtWidgets import *

class QMovieLabel(QLabel):

    def __init__(self, fileName, parent=None):
        super(QMovieLabel, self).__init__(parent)

        self.movie = None
        self._movieHeight = 0
        self._movieWidth = 0

        self.path = ""

        self.initialize(fileName)

    def initialize(self, fileName):
        if self.path is not fileName:
            self.path = fileName
            self.movie = QMovie(fileName)
            self.setMovie(self.movie)
            self.movie.start()

    def setMovie(self, movie):
        super(QMovieLabel, self).setMovie(movie)
        s = movie.currentImage().size()
        self._movieWidth = s.width()
        self._movieHeight = s.height()
