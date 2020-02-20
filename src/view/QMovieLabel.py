
from PyQt5 import QtGui, QtCore
import PyQt5.QtCore
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QMovie, QPainter, QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QPushButton, QHBoxLayout, QGroupBox, QDialog, QVBoxLayout, QGridLayout
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import PyQt5.QtCore

class QMovieLabel(QLabel):

    def __init__(self, fileName, parent=None):
        super(QMovieLabel, self).__init__(parent)
        self.initialize(fileName)

    def initialize(self, fileName):
        m = QtGui.QMovie(fileName)
        self.setMovie(m)
        m.start()

    def setMovie(self, movie):
        super(QMovieLabel, self).setMovie(movie)
        s=movie.currentImage().size()
        self._movieWidth = s.width()
        self._movieHeight = s.height()