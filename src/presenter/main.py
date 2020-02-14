
from model.evolution import Evolution
from presenter.logger import Logger


evolution: Evolution = None
logger: Logger = None

def request_child(child_index: int):
    global evolution, logger

    parent_filename, child_filename, interpolation_filename = \
        evolution.process_generation(generation_index=logger.generation_index, child_index=child_index)

    logger.create_log(parent_filename=parent_filename, child_filename=child_filename,
                      interpolation_filename=interpolation_filename)

    return parent_filename, child_filename, interpolation_filename


def main():
    global evolution, logger

    logger = Logger()

    logger.open_log(template=True)

    n_children = 3
    batch_size = 5
    interpolation_frames = 3

    evolution = Evolution(interpolation_frames, n_children, batch_size=batch_size)

    evolution.initialize(logger.generation_index)

    request_child(0)

    #logger.write_log()




if __name__=="__main__":
    main()
