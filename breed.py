import sys
import PyQt5.QtCore
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QMovie, QPainter, QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QGroupBox, QDialog, QVBoxLayout, QGridLayout
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import PyQt5.QtCore

class UIWindow(QWidget):
    def __init__(self, parent=None):
        super(UIWindow, self).__init__(parent)

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setGeometry(360, 50, 1000, 900)
        self.setFixedSize(1000, 900)
        self.startUIWindow()
        p = self.palette()
        p.setColor(self.backgroundRole(), PyQt5.QtCore.Qt.white)
        self.setPalette(p)

        self.ref_size = 220

        # main parents

        self.main1 = QMovie("imgs/iteration1_main.png")
        self.main1.frameChanged.connect(self.repaint)
        self.main1.setScaledSize(PyQt5.QtCore .QSize(self.ref_size, self.ref_size))
        self.main1.start()

        self.main2 = QMovie("imgs/iteration2_main.gif")
        self.main2.frameChanged.connect(self.repaint)
        self.main2.setScaledSize(PyQt5.QtCore.QSize(self.ref_size, self.ref_size))
        self.main2.start()

        self.main3 = QMovie("imgs/iteration4_main.gif")
        self.main3.frameChanged.connect(self.repaint)
        self.main3.setScaledSize(PyQt5.QtCore .QSize(self.ref_size, self.ref_size))
        self.main3.start()


        # candidate parents

        ref_x = 340
        ref_y = 75

        self.iteration1_candidate1 = QPushButton('', self)
        self.iteration1_candidate1.setStyleSheet(' border-radius: 10px; border-image: url({})'
                                                 .format('imgs/iteration1_candidate1.png'))
        self.iteration1_candidate1.move(ref_x, ref_y)
        self.iteration1_candidate1.resize(self.ref_size*0.7, self.ref_size*0.7)

        arrow1_1 = QLabel(self)
        pixmap = QPixmap('imgs/arrow.png')
        pixmap = pixmap.scaledToWidth(50)
        arrow1_1.setPixmap(pixmap)
        arrow1_1.resize(50, 60)
        arrow1_1.move(ref_x+55, ref_y+self.ref_size*0.7)

        ref_x = ref_x + self.ref_size*0.7 + 80

        self.iteration1_candidate2 = QPushButton('', self)
        self.iteration1_candidate2.setStyleSheet('border-radius: 10px; border-image: url({})'
                                                 .format('imgs/iteration1_candidate2.png'))
        self.iteration1_candidate2.move(ref_x, ref_y)
        self.iteration1_candidate2.resize(self.ref_size*0.7, self.ref_size*0.7)

        arrow1_2 = QLabel(self)
        pixmap = QPixmap('imgs/arrow.png')
        pixmap = pixmap.scaledToWidth(50)
        arrow1_2.setPixmap(pixmap)
        arrow1_2.resize(50, 60)
        arrow1_2.move(ref_x+55, ref_y+self.ref_size*0.7)

        ref_x = ref_x + self.ref_size*0.7 + 80

        self.iteration1_candidate3 = QPushButton('', self)
        self.iteration1_candidate3.setStyleSheet('border-radius: 10px; border-image: url({})'
                                                 .format('imgs/iteration1_candidate3.png'))
        self.iteration1_candidate3.move(ref_x, ref_y)
        self.iteration1_candidate3.resize(self.ref_size*0.7, self.ref_size*0.7)

        arrow1_3 = QLabel(self)
        pixmap = QPixmap('imgs/arrow.png')
        pixmap = pixmap.scaledToWidth(50)
        arrow1_3.setPixmap(pixmap)
        arrow1_3.resize(50, 60)
        arrow1_3.move(ref_x+55, ref_y+self.ref_size*0.7)

        ref_x = 340
        ref_y = ref_y + self.ref_size*0.7 + 80 + 65

        self.iteration2_candidate1 = QPushButton('', self)
        self.iteration2_candidate1.setStyleSheet('border-radius: 10px; border-image: url({})'
                                                 .format('imgs/iteration2_candidate1.png'))
        self.iteration2_candidate1.move(ref_x, ref_y)
        self.iteration2_candidate1.resize(self.ref_size*0.7, self.ref_size*0.7)

        arrow2_1 = QLabel(self)
        pixmap = QPixmap('imgs/arrow.png')
        pixmap = pixmap.scaledToWidth(50)
        arrow2_1.setPixmap(pixmap)
        arrow2_1.resize(50, 60)
        arrow2_1.move(ref_x+55, ref_y+self.ref_size*0.7)

        ref_x = ref_x + self.ref_size*0.7 + 80

        self.iteration2_candidate2 = QPushButton('', self)
        self.iteration2_candidate2.setStyleSheet('border-radius: 10px; border-image: url({})'
                                                 .format('imgs/iteration2_candidate2.png'))
        self.iteration2_candidate2.move(ref_x, ref_y)
        self.iteration2_candidate2.resize(self.ref_size*0.7, self.ref_size*0.7)

        arrow2_2 = QLabel(self)
        pixmap = QPixmap('imgs/arrow.png')
        pixmap = pixmap.scaledToWidth(50)
        arrow2_2.setPixmap(pixmap)
        arrow2_2.resize(50, 60)
        arrow2_2.move(ref_x+55, ref_y+self.ref_size*0.7)

        ref_x = ref_x + self.ref_size*0.7 + 80

        self.iteration2_candidate3 = QPushButton('', self)
        self.iteration2_candidate3.setStyleSheet('border-radius: 10px; border-image: url({})'
                                                 .format('imgs/iteration2_candidate3.png'))
        self.iteration2_candidate3.move(ref_x, ref_y)
        self.iteration2_candidate3.resize(self.ref_size*0.7, self.ref_size*0.7)

        arrow2_3 = QLabel(self)
        pixmap = QPixmap('imgs/arrow.png')
        pixmap = pixmap.scaledToWidth(50)
        arrow2_3.setPixmap(pixmap)
        arrow2_3.resize(50, 60)
        arrow2_3.move(ref_x+55, ref_y+self.ref_size*0.7)

        ref_x = 340
        ref_y = ref_y + self.ref_size*0.7 + 80 + 60

        self.iteration3_candidate1 = QPushButton('', self)
        self.iteration3_candidate1.setStyleSheet('border-radius: 10px; border-image: url({})'
                                                 .format('imgs/iteration3_candidate1.png'))
        self.iteration3_candidate1.move(ref_x, ref_y)
        self.iteration3_candidate1.resize(self.ref_size*0.7, self.ref_size*0.7)

        ref_x = ref_x + self.ref_size*0.7 + 80

        self.iteration3_candidate2 = QPushButton('', self)
        self.iteration3_candidate2.setStyleSheet('border-radius: 10px; border-image: url({})'
                                                 .format('imgs/iteration3_candidate2.png'))
        self.iteration3_candidate2.move(ref_x, ref_y)
        self.iteration3_candidate2.resize(self.ref_size*0.7, self.ref_size*0.7)

        ref_x = ref_x + self.ref_size*0.7 + 80

        self.iteration3_candidate3 = QPushButton('', self)
        self.iteration3_candidate3.setStyleSheet('border-radius: 10px; border-image: url({})'
                                                 .format('imgs/iteration3_candidate3.png'))
        self.iteration3_candidate3.move(ref_x, ref_y)
        self.iteration3_candidate3.resize(self.ref_size*0.7, self.ref_size*0.7)





        #button5.clicked.connect(self.on_click_button5)

        self.show()

    def startUIWindow(self):
        self.Window = UIWindow(self)
        self.setWindowTitle("Choose a parent to breed from the green area!")

    def paintEvent(self, event):

        ref_x = 40
        ref_y = 40
        currentFrame = self.main1.currentPixmap()
        frameRect = currentFrame.rect()
        frameRect.moveCenter(self.rect().center())
        if frameRect.intersects(event.rect()):
            painter = QPainter(self)
            painter.drawPixmap(ref_x, ref_y, currentFrame)

        painter = QPainter()
        painter.begin(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setPen(QPen(PyQt5.QtCore.Qt.red, 5))

        painter.drawLine(ref_x+110, ref_y + self.ref_size+2, ref_x+110, ref_y + self.ref_size+75)
        painter.drawLine(ref_x+90, ref_y + self.ref_size+2+60, ref_x+110, ref_y + self.ref_size+2+75)
        painter.drawLine(ref_x+130, ref_y + self.ref_size+2+60, ref_x+110, ref_y + self.ref_size+2+75)
        painter.drawLine(ref_x+110,  ref_y + self.ref_size+30, ref_x+110+800,  ref_y + self.ref_size+30)

        ref_y = ref_y + self.ref_size+80
        currentFrame2 = self.main2.currentPixmap()
        frameRect2 = currentFrame2.rect()
        frameRect2.moveCenter(self.rect().center())
        if frameRect2.intersects(event.rect()):
            painter2 = QPainter(self)
            painter2.drawPixmap(ref_x, ref_y, currentFrame2)

        painter = QPainter()
        painter.begin(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setPen(QPen(PyQt5.QtCore.Qt.red, 5))
        #QPen(PyQt5.QtGui.QColor(102, 85, 0), 5)
        painter.setBrush(PyQt5.QtCore.Qt.white)
        painter.drawLine(ref_x+110, ref_y + self.ref_size+2, ref_x+110, ref_y + self.ref_size+75)
        painter.drawLine(ref_x+90, ref_y + self.ref_size+2+60, ref_x+110, ref_y + self.ref_size+2+75)
        painter.drawLine(ref_x+130, ref_y + self.ref_size+2+60, ref_x+110, ref_y + self.ref_size+2+75)
        painter.drawLine(ref_x + 110, ref_y + self.ref_size + 30, ref_x + 800 + 100, ref_y + self.ref_size + 30)

        ref_y = ref_y + self.ref_size+80
        currentFrame3 = self.main3.currentPixmap()
        frameRect3 = currentFrame3.rect()
        frameRect3.moveCenter(self.rect().center())
        if frameRect3.intersects(event.rect()):
            painter3 = QPainter(self)
            painter3.drawPixmap(ref_x, ref_y, currentFrame3)


        painter = QPainter()
        painter.begin(self)
        painter.setPen(QPen(PyQt5.QtCore.Qt.green, 5, PyQt5.QtCore.Qt.DotLine))

        painter.drawRect(320, 645, 660, 200)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    sys.exit(app.exec_())