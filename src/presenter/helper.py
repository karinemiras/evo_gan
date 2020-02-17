
from presenter.logger import Logger
from model.individual import Individual


def extract_parent_from_logger(logger: Logger):

    parent = Individual()
    save = True

    if len(logger.generations_data['generations']) > 0:
        parent_dict = {"class": logger.generations_data['generations'][-1]["parent_class"],
                       "noise": logger.generations_data['generations'][-1]["parent_noise"]}
        parent.initialize(parent_dict)
        save = False

    return parent, save