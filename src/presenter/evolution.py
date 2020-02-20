import time
import copy
import numpy as np
import random

from model.individual import Individual
from model.images import save_image, save_interpolations
from model.interpolation import Interpolation
from model.gan import GAN

from presenter.logger import Logger
from presenter.helper import extract_parent_from_logger
from presenter.generation import Generation


class Evolution:

    def __init__(self, interpolation_frames, n_children, batch_size, resolution=128, logger: Logger = None):
        self.batch_size = batch_size

        self.gan = GAN(resolution)

        self.interpolation = Interpolation(interpolation_frames)

        self.generation = Generation.getInstance()

        save = True
        if logger is None:
            self.parent = Individual()
        else:
            self.parent, save = extract_parent_from_logger(logger)

        if save:
            self._save_parent_image(self.generation.index, generate=True)

        self.n_children = n_children
        self.children = [Individual] * self.n_children

        self._make_children(self.generation.index)

    def _make_children(self, generation_index):
        last_child_index = self.n_children - 1

        for child_index in range(last_child_index):
            self.children[child_index] = copy.deepcopy(self.parent)

            self.children[child_index].mutate()
            self._generate_child_image(generation_index, child_index)

        # Add a random child to the candidate pool
        self.children[last_child_index] = Individual()
        self._generate_child_image(generation_index, last_child_index)

        #random.shuffle(self.children)

    def _save_parent_image(self, generation_index, generate=False):
        if generate:
            self.parent.image = self.gan.get_model_image(self.parent)
        filename = "parent/iteration{}_main.png".format(generation_index)
        save_image(filename, self.parent.image)

        return filename

    def _generate_child_image(self, generation_index, child_index, save=True):
        self.children[child_index].image = self.gan.get_model_image(self.children[child_index])

        filename = "children/iteration{}_candidate{}.png".format(generation_index, child_index)

        if save:
            save_image(filename, self.children[child_index].image)

    # THREAD
    def _interpolate_child(self, child_index):
        t = time.time()
        print("Interpolating children")
        child_interpolations = self.interpolation.interpolate(self.gan, self.parent, self.children[child_index])
        print("Interpolated_children in {} seconds".format(time.time()-t))
        return save_interpolations(child_interpolations, self.generation.index + 1)

    def process_generation(self, child_index):

        _ = self._interpolate_child(child_index)

        self.parent = copy.deepcopy(self.children[child_index])

        self._save_parent_image(self.generation.index + 1)
        self._make_children(self.generation.index + 1)


def main():
    n_children = 3
    batch_size = 1
    interpolation_frames = 10 #60
    evolution = Evolution(interpolation_frames, n_children, resolution=128, batch_size=batch_size)

    evolution.process_generation(1)

if __name__=="__main__":
    main()
