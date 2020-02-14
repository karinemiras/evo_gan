import time
import numpy as np
import copy

from model.individual import Individual
from model.image import save_image
from model.interpolation import Interpolation
from model.gan import GAN


class Evolution:

    def __init__(self, interpolation_frames, n_children, batch_size):
        self.batch_size = batch_size

        self.gan = GAN()
        self.interpolation = Interpolation(interpolation_frames, n_children)

        self.parent = Individual(batch_size=self.batch_size)
        self.n_children = n_children
        self.children = [Individual] * self.n_children
        self.make_children()

    def make_children(self):
        for i in range(self.n_children):
            self.children[i] = copy.deepcopy(self.parent)

            self.children[i].mutate_noise_vector()
            self.children[i].mutate_class_vector()

            self.save_child("children/child_{}.png".format(i), self.children[i])

        # TODO: Why is this one not mutated?
        #self.children[self.n_children - 1] = Individual(batch_size=self.batch_size)

        #self.save_individual("children/child_{}.png".format(self.n_children - 1), self.children[self.n_children - 1])

    def save_child(self, path, individual):
        image = self.gan.get_model_image(individual)
        save_image(path, image)

    # THREAD
    def interpolate_children(self):
        t = time.time()
        print("Interpolating children")
        for index in range(self.n_children):
            self.interpolation.interpolate(self.gan, self.parent, self.children[index], child_index=index)
        print("Interpolated_children in {} seconds".format(time.time()-t))


def main():
    n_children = 3
    batch_size = 1
    interpolation_frames = 60
    evolution = Evolution(interpolation_frames, n_children, batch_size=batch_size)

if __name__=="__main__":
    main()
