import time
import copy

from model.individual import Individual
from model.images import save_image, save_interpolations
from model.interpolation import Interpolation
from model.gan import GAN


class Evolution:

    def __init__(self, interpolation_frames, n_children, batch_size):
        self.batch_size = batch_size

        self.gan = GAN()
        self.interpolation = Interpolation(interpolation_frames)

        self.parent = Individual()


        self.n_children = n_children
        self.children = [Individual] * self.n_children

    def initialize(self, generation_index):
        self.save_parent(generation_index)
        self._make_children(generation_index)

    def _make_children(self, generation_index):
        for child_index in range(self.n_children):
            self.children[child_index] = copy.deepcopy(self.parent)

            self.children[child_index].mutate()

            self.save_child(generation_index, child_index)

        # TODO: Why is this one not mutated?
        #self.children[self.n_children - 1] = Individual(batch_size=self.batch_size)
        #self.save_individual("children/child_{}.png".format(self.n_children - 1), self.children[self.n_children - 1])

    def save_parent(self, generation_index):
        image = self.gan.get_model_image(self.parent)
        filename = "parent/parent_{}.png".format(generation_index)
        save_image(filename, image)
        return filename

    def save_child(self, generation_index, child_index):
        image = self.gan.get_model_image(self.children[child_index])

        filename = "children/child_{}_{}.png".format(generation_index, child_index)
        save_image(filename, image)

    # THREAD
    def _interpolate_child(self, generation_index, child_index):
        t = time.time()
        print("Interpolating children")
        child_interpolations = self.interpolation.interpolate(self.gan, self.parent, self.children[child_index])
        print("Interpolated_children in {} seconds".format(time.time()-t))
        return save_interpolations(child_interpolations, generation_index)

    def process_generation(self, generation_index, child_index):

        parent_filename = "parent_{}.png".format(generation_index)
        child_filename = "child_{}_{}.png".format(generation_index, child_index)
        interpolation_filename = self._interpolate_child(generation_index, child_index)

        self.parent = copy.deepcopy(self.children[child_index])
        self._make_children(generation_index + 1)

        return parent_filename, child_filename, interpolation_filename



def main():
    n_children = 3
    batch_size = 1
    interpolation_frames = 10 #60
    evolution = Evolution(interpolation_frames, n_children, batch_size=batch_size)
    evolution.initialize(0)
    evolution.process_generation(0, 1)

if __name__=="__main__":
    main()
