
import sys, sched, time
import asyncio
import threading
from threading import Lock

from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtCore import *

from view.evolution_combined_gui import Ui_breeding_pictures

from view.manager.candidate_manager import CandidateManager
from presenter.generation import Generation

from view.manager.evolution_tree_manager import EvolutionTreeManager
from view.manager.loading_manager import LoadingManager


from presenter.evolution import Evolution
from view.manager.history_manager import HistoryManager

from view.multithreading_helper import Worker


class EvolutionView(QMainWindow):

    def __init__(self, demo=False):
        super(EvolutionView, self).__init__()

        if demo is False:
            n_population = 10
            n_candidates = 4
            batch_size = 1
            interpolation_frames = 25
            self.evolution = Evolution(interpolation_frames, n_population, n_candidates, batch_size, resolution=128)
        else:
            self.evolution = None

        self.ui = Ui_breeding_pictures()
        self.ui.setupUi(self)

        background_path = "../resources/tree_abstract_blurred.png"
        self.ui.background_image.setPixmap(QPixmap(background_path))

        self.threadpool = QThreadPool()
        print("Multithreading with maximum %d threads" % self.threadpool.maxThreadCount())

        self.generation = Generation.getInstance()

        self.display_lock = Lock()

        self.image_size = 128

        #self.ui.centralwidget.setStyleSheet('background:rgb(230,238,241);')

        candidate_buttons = [self.ui.candidate_1_button, self.ui.candidate_2_button, self.ui.candidate_3_button, self.ui.candidate_4_button]
        candidate_frames = [self.ui.candidate_1_frame, self.ui.candidate_2_frame, self.ui.candidate_3_frame, self.ui.candidate_4_frame]
        self.candidate_manager = CandidateManager(self.ui.parent_image, self.ui.parent_frame, candidate_buttons, candidate_frames, self.ui.parent_label,
                                                  self.ui.mate_label, self.visualize_generation)

        self.loading_manager = LoadingManager(self.ui.loading_animation, self.ui.breeding_label, self.ui.centralwidget)

        self.candidate_manager.update()

        parent_images = [self.ui.parent_1_image, self.ui.parent_2_image]
        parent_frames = [self.ui.parent_1_frame, self.ui.parent_2_frame]
        self.evolution_tree_manager = EvolutionTreeManager(parent_images, parent_frames, self.ui.child_image, self.ui.child_frame, self.ui.parent_arrows,
                                                           self.ui.parent_1_label, self.ui.parent_2_label, self.ui.centralwidget)

        self.display_state = "candidates"

        #history_images = [self.ui.history_image_1, self.ui.history_image_2, self.ui.history_image_3]
        #self.history_manager = HistoryManager(history_images, self.ui.centralwidget)

    def process_evolution(self, index):

        self.loading_manager.loading()

        self.generation.index += 1

        if self.evolution is not None:
            self.evolution.save_parents(index)
            self.display_state = "tree"

            self.evolution.process_generation(index)
        else:
            time.sleep(3)

        self.evolution_tree_manager.update()
        self.loading_manager.unloading()

        time.sleep(3) # 10

        self.display_state = "candidates"
        self.candidate_manager.prepare_choice()

    def visualize_generation(self, index=None):
        if index is not None:
            worker = Worker(self.process_evolution, index)  # Any other args, kwargs are passed to the run function
            self.threadpool.start(worker)

    def paintEvent(self, event):
        if self.display_state == "candidates":
            self.candidate_manager.update()

            self.candidate_manager.visible(True)
            self.evolution_tree_manager.visible(False)
            self.loading_manager.visible(False)

            self.display_state = ""
        elif self.display_state == "tree":
            self.evolution_tree_manager.update()

            self.candidate_manager.visible(False)
            self.evolution_tree_manager.visible(True)
            self.loading_manager.visible(True)

            self.display_state = ""


if __name__ == '__main__':
    is_demo = False
    app = QApplication(sys.argv)
    w = EvolutionView(is_demo)
    w.show()
    sys.exit(app.exec_())
