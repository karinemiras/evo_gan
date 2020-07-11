from PIL import Image
import numpy as np
import copy

from model.individual import Individual
from model.orthogonal import find_orthogonal_basis

from presenter.images import generate_population_image, save_candidate_image
from presenter.generation import Generation


class Population:

    def __init__(self, n_population=10, n_candidates=3, n_replacements=3):
        self.n_population = n_population
        self.n_candidates = n_candidates
        self.n_replacements = n_replacements

        self.individuals = np.array([None] * self.n_population)
        self.candidates = np.array([None] * self.n_candidates)

        self.orthogonal_noise_basis = find_orthogonal_basis(self.n_population)

    def generate_candidates(self, gan):

        for individual_index in range(self.n_population):
            self.individuals[individual_index] = Individual()  # copy.deepcopy(self.parent)

            self.individuals[individual_index].mutate(self.orthogonal_noise_basis[:, individual_index])

    def cycle(self, gan):
        for individual_index in range(self.n_population):
            # fitness
            self.individuals[individual_index] = generate_population_image(gan, self.individuals[individual_index],
                                                                           individual_index)
            self.individuals[individual_index].fitness = self.fitness(individual_index)

        # Selection
        self.selection()

        self.replacement()

    def fitness(self, individual_index):
        pix = self.individuals[individual_index].image

        meanbright = np.mean(pix)

        #brightness = 0
        #for i in range(pix.shape[0]):
        #    for j in range(pix.shape[1]):
        #        brightness += pix[i, j][0] + pix[i, j][1] + pix[i, j][2]

        # meanbright = brightness/(3*512*512) # original
        #meanbright = brightness / (3 * 512 * 512 * 255)

        # normalise (max 1 for all white picture)

        return meanbright
        # return meanbright, # IF ONLY EVALUATING ONE CHARACTERISTIC

    def selection(self):
        # negative fitness to sort descending with argsort
        individuals_fitness = np.array([-individual.fitness for individual in self.individuals])
        sorted_indexes = np.argsort(individuals_fitness)
        self.individuals = self.individuals[sorted_indexes]

        self.orthogonal_noise_basis = self.orthogonal_noise_basis[:, sorted_indexes]

        self.candidates = copy.deepcopy(self.individuals[:self.n_candidates])
        for candidate_index, candidate in enumerate(self.candidates):
            save_candidate_image(candidate.image, candidate_index)

    def replacement(self):
        # prepare replaced last n candidates
        self.orthogonal_noise_basis[:, -self.n_replacements:] = 0

        self.orthogonal_noise_basis = find_orthogonal_basis(self.n_population, self.orthogonal_noise_basis)

        for individual_index in range(self.n_replacements):
            negative_index = -(individual_index+1)
            self.individuals[negative_index] = Individual()

            self.individuals[individual_index].mutate(self.orthogonal_noise_basis[:, negative_index])