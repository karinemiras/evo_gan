import time
import copy

from model.individual import Individual
from presenter.images import save_image, save_interpolations, prepare_folders
from model.interpolation import Interpolation
from model.gan import GAN

from presenter.logger import Logger
from presenter.helper import extract_parent_from_logger
from presenter.generation import Generation
from presenter.population import Population

from presenter.images import save_parent_image, save_chosen_parent_image


class Evolution:

    def __init__(self, interpolation_frames, n_population, n_candidates, batch_size, resolution=128):
        self.batch_size = batch_size

        prepare_folders()

        self.gan = GAN(resolution)

        self.interpolation = Interpolation(interpolation_frames)

        self.generation = Generation.getInstance()

        self._initialize_parent()

        self.population = Population(n_population, n_candidates)
        self.population.generate_candidates(self.gan)
        self.population.cycle(self.gan)

    def _initialize_parent(self):
        self.parent = Individual()
        save_parent_image(self.gan, self.parent, generate=True)

    def _interpolate_candidate(self, child_index):
        t = time.time()
        print("Interpolating children")
        chosen_candidate = self.population.candidates[child_index]
        child_interpolations, child = self.interpolation.interpolate(self.gan, self.parent, chosen_candidate)
        print("Interpolated_children in {} seconds".format(time.time()-t))
        save_interpolations(child_interpolations)

        self._set_parent(child)

    def save_parents(self, child_index):
        chosen_candidate = self.population.candidates[child_index]
        save_chosen_parent_image(chosen_candidate)

    def _set_parent(self, child):
        self.parent = copy.deepcopy(child)
        save_parent_image(self.gan, self.parent, generate=False)

    def process_generation(self, child_index):
        self._interpolate_candidate(child_index)
        self.population.cycle(self.gan)




def main():
    n_population = 10
    n_children = 3
    batch_size = 1

    interpolation_frames = 10 #60
    evolution = Evolution(interpolation_frames, n_population, n_children, resolution=128, batch_size=batch_size)

    evolution.process_generation(1)

    evolution.process_generation(1)
    evolution.process_generation(1)


if __name__=="__main__":
    main()
