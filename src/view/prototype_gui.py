import sys
import os
import PyQt5.QtCore
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QMovie, QPainter, QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QGroupBox, QDialog, QVBoxLayout, QGridLayout
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import PyQt5.QtCore

from functools import partial

from presenter.generation import Generation


class UIWindow(QWidget):
    def __init__(self, parent=None):
        super(UIWindow, self).__init__(parent)


class EvolutionGUI(QMainWindow):
    def __init__(self, request_candidate=None, parent=None, is_demo=False):
        super(EvolutionGUI, self).__init__(parent)

        self.generation = Generation.getInstance()

        if is_demo:
            self.image_folder = "../../demo/"
            self.generation.index = 2
        else:
            self.image_folder = "../../imgs/"

        resources_folder = "../../resources/"

        self.arrow_filename = resources_folder + "arrow.png"

        self.candidate_configuration = 'border-radius: 10px; border-image: url({})'

        self.number_of_interations = 3
        self.number_of_candidate = 3
        self.visible_interations = self.number_of_interations - 1

        self.arrow_width = 50
        self.arrow_height = 60
        self.arrow_margin = 80

        window_width = 1000
        window_height = 900

        self.setGeometry(360, 50, window_width, window_height)
        self.setFixedSize(window_width, window_height)
        self.startUIWindow()
        p = self.palette()
        p.setColor(self.backgroundRole(), PyQt5.QtCore.Qt.white)
        self.setPalette(p)

        if request_candidate is None:
            self.request_candidate = self.candidate_choice
        else:
            self.request_candidate = request_candidate

        self.parent_size = 220

        # main parents
        self.main_parent_movies = [None] * self.number_of_interations

        self.old_generation = self.generation.index

        self.update()
        #button5.clicked.connect(self.on_click_button5)

    def candidate_choice(self, candidate_index):
        self.generation.index += 1
        print("Chosen", candidate_index)

    def update(self):
        # Parents are gif's, except the first parent
        print("update", self.generation.index)
        for iteration_index, generation_index in enumerate(
                range(max(0, self.generation.index - self.number_of_interations + 1), self.generation.index + 1)):

            path = self.image_folder + "interpolations/iteration{}_main.gif".format(generation_index)
            if not os.path.exists(path):
                path = self.image_folder + "parent/iteration{}_main.png".format(generation_index)
                if not os.path.exists(path):
                    path = self.resource_folder + "frame.jpg"

            print("parent", iteration_index, generation_index, path)
            self.main_parent_movies[iteration_index] = QMovie(path)

            self.main_parent_movies[iteration_index].frameChanged.connect(self.repaint)
            self.main_parent_movies[iteration_index].setScaledSize(PyQt5.QtCore.QSize(self.parent_size, self.parent_size))
            self.main_parent_movies[iteration_index].start()

        ######### Displaying the children candidates and sub arrows to the midline ############
        # TODO remove candidate / child ambiguity
        # I personaly like 'candidate' in the GUI setting, but for evolution 'child' could be more appropriate.

        starting_x = 340

        ref_x = starting_x
        ref_y = 75

        candidate_size = self.parent_size * 0.7

        self.interation_candidates = [[None] * self.number_of_candidate] * self.number_of_interations
        self.candidate_arrows = [[None] * self.number_of_candidate] * self.visible_interations


        for iteration_index, generation_index in enumerate(
                range(max(0, self.generation.index - self.number_of_interations + 1), self.generation.index + 1)):

            arrow_y = ref_y + candidate_size

            for candidate_index in range(self.number_of_candidate):

                arrow_x = ref_x + 55

                print("candidate", iteration_index, generation_index, candidate_index, arrow_x, arrow_y)

                path = self.image_folder + 'children/iteration{}_candidate{}.png'.format(generation_index,
                                                                                     candidate_index)
                print(path)
                """
                self.interation_candidates[iteration_index][candidate_index] = QPushButton(str(generation_index) + "_" + str(candidate_index), self)
                self.interation_candidates[iteration_index][candidate_index].setStyleSheet(
                    self.candidate_configuration.format(path))

                self.interation_candidates[iteration_index][candidate_index].move(ref_x, ref_y)
                self.interation_candidates[iteration_index][candidate_index].resize(candidate_size, candidate_size)
                """
                if iteration_index != self.visible_interations:
                    multiplier = 1 # self.generation.index
                    print("repaint candidates")
                    self.interation_candidates[iteration_index][candidate_index] = QLabel(self)
                    pixmap = QPixmap(path).scaledToWidth(candidate_size)
                    self.interation_candidates[iteration_index][candidate_index].setPixmap(pixmap)
                    self.interation_candidates[iteration_index][candidate_index].resize(multiplier*candidate_size, multiplier*candidate_size)
                    self.interation_candidates[iteration_index][candidate_index].move(multiplier*ref_x, multiplier*ref_y)

                    ref_x = ref_x + candidate_size + self.arrow_margin

                if iteration_index == self.visible_interations:

                    # Last generation does not have candidate arrows
                    #self.interation_candidates[iteration_index][candidate_index].clicked.connect(
                    #    partial(self.request_candidate, candidate_index))
                    self.interation_candidates[iteration_index][candidate_index] = QPushButton("", self)
                    self.interation_candidates[iteration_index][candidate_index].setStyleSheet(
                        self.candidate_configuration.format(path))

                    self.interation_candidates[iteration_index][candidate_index].move(ref_x, ref_y)
                    self.interation_candidates[iteration_index][candidate_index].resize(candidate_size, candidate_size)

                    # Last generation does not have candidate arrows
                    self.interation_candidates[iteration_index][candidate_index].clicked.connect(
                        partial(self.request_candidate, candidate_index))
                    ref_x = ref_x + candidate_size + self.arrow_margin
                    continue

                """
                if iteration_index is not self.visible_interations:
                    self.interation_candidates[iteration_index][candidate_index] = QLabel(self)
                    pixmap = QPixmap(path).scaledToWidth(candidate_size)
                    self.interation_candidates[iteration_index][candidate_index].setPixmap(pixmap)
                    self.interation_candidates[iteration_index][candidate_index].resize(candidate_size, candidate_size)
                    self.interation_candidates[iteration_index][candidate_index].move(arrow_x, arrow_y)

                else:
                    self.interation_candidates[iteration_index][candidate_index] = QPushButton("", self)
                    self.interation_candidates[iteration_index][candidate_index].setStyleSheet(
                        self.candidate_configuration.format(path))

                    self.interation_candidates[iteration_index][candidate_index].move(ref_x, ref_y)
                    self.interation_candidates[iteration_index][candidate_index].resize(candidate_size, candidate_size)

                    # Last generation does not have candidate arrows
                    self.interation_candidates[iteration_index][candidate_index].clicked.connect(
                        partial(self.request_candidate, candidate_index))
                    continue
                    """

                self.candidate_arrows[iteration_index][candidate_index] = QLabel(self)
                pixmap = QPixmap(self.arrow_filename)
                pixmap = pixmap.scaledToWidth(self.arrow_width)
                self.candidate_arrows[iteration_index][candidate_index].setPixmap(pixmap)
                self.candidate_arrows[iteration_index][candidate_index].resize(self.arrow_width, self.arrow_height)
                self.candidate_arrows[iteration_index][candidate_index].move(arrow_x, arrow_y)

            # Reset reference point
            ref_x = starting_x
            ref_y = ref_y + candidate_size + self.arrow_margin + self.arrow_height


    def startUIWindow(self):
        self.Window = UIWindow(self)
        self.setWindowTitle("Choose a parent to breed from the green area!")

    def paintEvent(self, event):

        if self.old_generation is not self.generation.index:
            self.old_generation = self.generation.index
            self.update()

        ref_x = 40
        ref_y = 40

        #########################################################
        parent_painters = [None] * self.number_of_interations
        arrow_painters = [None] * self.visible_interations

        arrowhead_height = 15
        arrowhead_width = 20
        # +2 for slight corrections of the arrow location
        arrow_correction = 2

        midline_width = 800

        for generation_index in range(self.number_of_interations):
            current_frame = self.main_parent_movies[generation_index].currentPixmap()
            frameRect = current_frame.rect()
            frameRect.moveCenter(self.rect().center())

            if frameRect.intersects(event.rect()):
                parent_painters[generation_index] = QPainter(self)
                parent_painters[generation_index].drawPixmap(ref_x, ref_y, current_frame)

            if generation_index == self.number_of_interations - 1:
                # Last generation has a different visualization
                break

            # Setup brush
            arrow_painters[generation_index] = QPainter()
            arrow_painters[generation_index].begin(self)
            arrow_painters[generation_index].setRenderHint(QPainter.Antialiasing)
            arrow_painters[generation_index].setPen(QPen(PyQt5.QtCore.Qt.red, 5))

            # Parent Directional arrow to the new generation

            arrow_x = ref_x + 110
            arrowhead_y_start = ref_y + self.parent_size + self.arrow_height + arrow_correction
            arrow_head_y_end = arrowhead_y_start + arrowhead_height

            arrow_painters[generation_index].drawLine(arrow_x, ref_y + self.parent_size + arrow_correction, arrow_x,
                                                      arrow_head_y_end)

            arrow_painters[generation_index].drawLine(arrow_x - arrowhead_width, arrowhead_y_start, arrow_x, arrow_head_y_end)
            arrow_painters[generation_index].drawLine(arrow_x + arrowhead_width, arrowhead_y_start, arrow_x, arrow_head_y_end)

            # Main branch connecting to the candidate arrow
            arrow_y_midline = ref_y + self.parent_size + 30
            arrow_painters[generation_index].drawLine(arrow_x, arrow_y_midline, arrow_x + midline_width, arrow_y_midline)

            ref_y = ref_y + self.parent_size + self.arrow_margin

        painter = QPainter()
        painter.begin(self)
        painter.setPen(QPen(PyQt5.QtCore.Qt.green, 5, PyQt5.QtCore.Qt.DotLine))

        painter.drawRect(320, 645, 660, 200)

if __name__ == '__main__':
    is_demo = True
    app = QApplication(sys.argv)
    w = EvolutionGUI(None, is_demo=True)
    w.show()
    sys.exit(app.exec_())