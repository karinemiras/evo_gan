import sys

from PyQt5.QtWidgets import QApplication

from model.evolution import Evolution
from presenter.logger import Logger
from view.evolution_gui import EvolutionGUI


evolution: Evolution = None
logger: Logger = None


def request_candidate(child_index: int):
    global evolution, logger

    evolution.process_generation(child_index=child_index)

    logger.create_log(parent=evolution.parent)
    logger.write_log()

    evolution.generation.index += 1

#TODO Make dataset offline available.

def main():
    global evolution, logger

    logger = Logger()

    logger.open_log(template=True)

    n_children = 3
    batch_size = 5
    interpolation_frames = 5

    evolution = Evolution(interpolation_frames, n_children, batch_size, logger)

    request_candidate(0)
    request_candidate(1)

    app = QApplication(sys.argv)
    w = EvolutionGUI(request_candidate)
    w.show()

    sys.exit(app.exec_())


if __name__=="__main__":
    main()