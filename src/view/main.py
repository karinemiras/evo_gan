
import sys, sched, time
import asyncio
import threading
from threading import Lock

from PySide2.QtWidgets import *

from view.evolution_combined_gui import Ui_MainWindow

from view.manager.candidate_manager import CandidateManager
from presenter.generation import Generation

from view.manager.evolution_tree_manager import EvolutionTreeManager

from presenter.evolution import Evolution
from view.manager.history_manager import HistoryManager


class EvolutionView(QMainWindow):

    def __init__(self, demo=False):
        super(EvolutionView, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.generation = Generation.getInstance()

        self.display_lock = Lock()

        self.display_state = "candidates"

        if demo is False:
            n_population = 10
            n_candidates = 3
            batch_size = 1
            interpolation_frames = 25
            self.evolution = Evolution(interpolation_frames, n_population, n_candidates, batch_size, resolution=128)
        else:
            self.evolution = None

        self.image_size = 128

        self.ui.centralwidget.setStyleSheet('background:rgb(230,238,241);')

        candidate_buttons = [self.ui.candidate_1_button, self.ui.candidate_2_button, self.ui.candidate_3_button]
        self.candidate_manager = CandidateManager(self.ui.parent_image, candidate_buttons, self.ui.parent_label,
                                                  self.ui.mate_label, self.ui.loading_animation, self.ui.centralwidget, self.visualize_generation)

        self.candidate_manager.update()

        parent_images = [self.ui.parent_1_image, self.ui.parent_2_image]
        self.evolution_tree_manager = EvolutionTreeManager(parent_images, self.ui.child_image, self.ui.parent_arrows,
                                                           self.ui.parent_1_label, self.ui.parent_2_label, self.ui.centralwidget)

        #history_images = [self.ui.history_image_1, self.ui.history_image_2, self.ui.history_image_3]
        #self.history_manager = HistoryManager(history_images, self.ui.centralwidget)

    def visualize_generation(self, index=None):
        if index is not None:
            self.display_state = "tree"

            self.candidate_manager.loading()

            if self.evolution is not None:
                x = threading.Thread(target=self.evolution.process_generation, args=(index, ))
                x.start()
                self.candidate_manager.update()
                x.join()
            else:
                self.generation.index += 1

            y = threading.Thread(target=self._transition_scheduler, args=())
            y.start()

            #asyncio.run(self._transition_scheduler())

        self.evolution_tree_manager.update()
        #self.history_manager.update()

    def _transition_scheduler(self):
        time.sleep(10)
        self.candidate_manager.update()
        self.display_state = "candidates"

    def paintEvent(self, event):
        if self.display_state == "candidates":
            self.candidate_manager.visible(True)
            self.evolution_tree_manager.visible(False)

        elif self.display_state == "tree":
            self.candidate_manager.visible(False)
            self.evolution_tree_manager.visible(True)


if __name__ == '__main__':
    is_demo = False
    app = QApplication(sys.argv)
    w = EvolutionView(is_demo)
    w.show()
    sys.exit(app.exec_())
