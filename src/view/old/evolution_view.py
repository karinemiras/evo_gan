
import sys
from PySide2.QtWidgets import *

from view.old.evolution_gui import Ui_EvolutionGUI

from view.manager.candidate_manager import CandidateManager
from presenter.generation import Generation

from view.manager.evolution_tree_manager import EvolutionTreeManager

from presenter.evolution import Evolution
from view.manager.history_manager import HistoryManager


class EvolutionView(QMainWindow):

    def __init__(self, demo=False):
        super(EvolutionView, self).__init__()
        self.ui = Ui_EvolutionGUI()
        self.ui.setupUi(self)

        self.generation = Generation.getInstance()

        if demo is False:
            n_population = 10
            n_children = 5
            batch_size = 5
            interpolation_frames = 20
            self.evolution = Evolution(interpolation_frames, n_population, n_children, batch_size, resolution=128)
        else:
            self.evolution = None

        self.image_size = 128

        candidate_buttons = [self.ui.candidate_button_1, self.ui.candidate_button_2, self.ui.candidate_button_3, self.ui.candidate_button_4]
        self.candidate_manager = CandidateManager(candidate_buttons, self.visualize_generation, self.ui.centralwidget)

        parent_images = [self.ui.parent_image_1, self.ui.parent_image_2]
        self.evolution_tree_manager = EvolutionTreeManager(parent_images, self.ui.child_image, self.ui.parent_arrows)

        history_images = [self.ui.history_image_1, self.ui.history_image_2, self.ui.history_image_3]
        self.history_manager = HistoryManager(history_images, self.ui.centralwidget)

        self.visualize_generation()

    def visualize_generation(self, index=None):
        if index is not None:
            if self.evolution is not None:
                self.evolution.process_generation(index)
            self.generation.index += 1

        self.evolution_tree_manager.update()
        self.candidate_manager.update()
        self.history_manager.update()


if __name__ == '__main__':
    is_demo = False
    app = QApplication(sys.argv)
    w = EvolutionView(is_demo)
    w.show()
    sys.exit(app.exec_())