
from model.evolution import Evolution
from presenter.logger import Logger


evolution: Evolution = None
logger: Logger = None

def request_child(child_index: int):
    global evolution, logger
    print(logger.generation_index)
    evolution.process_generation(generation_index=logger.generation_index, child_index=child_index)

    logger.create_log(parent=evolution.parent)


def main():
    global evolution, logger

    logger = Logger()

    logger.open_log(template=True)

    n_children = 3
    batch_size = 5
    interpolation_frames = 60

    evolution = Evolution(interpolation_frames, n_children, batch_size, logger)

    request_child(2)
    request_child(1)
    request_child(0)

    logger.write_log()


if __name__=="__main__":
    main()
