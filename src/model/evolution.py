import time
import copy

from model.individual import Individual
from model.images import save_image, save_interpolations
from model.interpolation import Interpolation
from model.gan import GAN

from presenter.logger import Logger
from presenter.helper import extract_parent_from_logger


class Evolution:

    def __init__(self, interpolation_frames, n_children, batch_size, logger: Logger = None):
        self.batch_size = batch_size

        self.gan = GAN()
        self.interpolation = Interpolation(interpolation_frames)

        # TODO who should have the generation index under its control 'Evolution' or 'Logger'
        generation_index = 0
        if logger is None:
            self.parent = Individual()
            self._generate_parent_image(self.generation_index, generate=True)
        else:
            generation_index = logger.generation_index
            self.parent = extract_parent_from_logger(logger)

        self.n_children = n_children
        self.children = [Individual] * self.n_children

        self._make_children(generation_index)

    def _make_children(self, generation_index):
        for child_index in range(self.n_children):
            self.children[child_index] = copy.deepcopy(self.parent)

            self.children[child_index].mutate()

            self._generate_child_image(generation_index, child_index)

        # TODO: Why is this one not mutated?
        #self.children[self.n_children - 1] = Individual(batch_size=self.batch_size)
        #self.save_individual("children/child_{}.png".format(self.n_children - 1), self.children[self.n_children - 1])

    def _save_parent_image(self, generation_index, generate=False):
        if generate:
            self.parent.image = self.gan.get_model_image(self.parent)

        filename = "parent/iteration{}_main.png".format(generation_index + 1)
        print("save parent image", filename, generation_index)
        save_image(filename, self.parent.image)

        return filename

    def _generate_child_image(self, generation_index, child_index, save=True):
        self.children[child_index].image = self.gan.get_model_image(self.children[child_index])

        filename = "children/iteration{}_candidate{}.png".format(generation_index, child_index + 1)

        if save:
            save_image(filename, self.children[child_index].image)

    # THREAD
    def _interpolate_child(self, generation_index, child_index):
        t = time.time()
        print("Interpolating children")
        child_interpolations = self.interpolation.interpolate(self.gan, self.parent, self.children[child_index])
        print("Interpolated_children in {} seconds".format(time.time()-t))
        return save_interpolations(child_interpolations, generation_index)

    def process_generation(self, generation_index, child_index):

        _ = self._interpolate_child(generation_index, child_index)

        self.parent = copy.deepcopy(self.children[child_index])

        self._save_parent_image(generation_index)

        self._make_children(generation_index + 1)


def main():
    n_children = 3
    batch_size = 1
    interpolation_frames = 10 #60
    evolution = Evolution(interpolation_frames, n_children, batch_size=batch_size)
    evolution.process_generation(0, 1)

if __name__=="__main__":
    main()
