
from model.biggan import (truncated_noise_sample)
import numpy as np
import math


class Individual:

    number_of_classes = 1000

    def __init__(self, truncation=0.4, vector_threshold=0.25, batch_size=1):

        self.truncation = truncation
        self.dim_z = 128
        # Sigma should be between 0 and 1
        self.vector_threshold = vector_threshold
        self.batch_size = batch_size

        self.class_vector = None
        self.create_random_class_vector()

        self.noise_vector = None
        self.create_random_noise_vector()

    def create_random_class_vector(self):
        self.class_vector = self._insert_random_class_vectors()

    def create_random_noise_vector(self):
        self.noise_vector = truncated_noise_sample(truncation=self.truncation, dim_z=self.dim_z,
                                                   batch_size=self.batch_size).astype('float32')

    def mutate_noise_vector(self):
        self.noise_vector = (np.random.randn(self.batch_size, self.dim_z) * self.vector_threshold
                             + self.noise_vector).astype('float32')

        lowest_value = np.min(self.noise_vector)
        highest_value = np.max(self.noise_vector)
        absolute_value = max(abs(lowest_value), abs(highest_value))
        # important to
        self.noise_vector = (self.noise_vector / absolute_value * self.truncation)

    def mutate_class_vector(self):
        active_classes = np.where(self.class_vector > 0.0)

        self.class_vector[active_classes] += self.vector_threshold * np.random.randn(len(active_classes[0]))
        # remove classes below vector threshold
        self.class_vector[self.class_vector <= self.vector_threshold] = 0

        self.class_vector = self._insert_random_class_vectors(self.class_vector)

    def _insert_random_class_vectors(self, initial_vectors=None):

        initial_random_classes = 0
        if initial_vectors is not None:
            class_vector = initial_vectors
        else:
            initial_random_classes = 1
            class_vector = np.zeros((self.batch_size, self.number_of_classes))

        # initial adds one to the number of random classes
        for index in range(self.batch_size):

            number_of_random_classes = initial_random_classes + math.floor(self._get_number_of_random_classes())
            # the ceil function is used to ensure that there is always one random class added.

            random_classes = np.random.randint(0, self.number_of_classes, size=(number_of_random_classes, ))
            class_vector[index, random_classes] = self.vector_threshold + \
                                                     (1 - self.vector_threshold) * np.random.rand(number_of_random_classes)

        return class_vector.astype('float32')

    def _get_number_of_random_classes(self):
        # use an logarithmic formula to calculate the number of successive random changes of adding a new random class
        # https://www.wolframalpha.com/input/?i=log_0.25%28x%29
        #
        # This construction replaces the need for the weird while loops
        # while True:
        #    if np.random.rand() > 1 - self.sigma:
        #        random_class = np.random.randint(0, self.number_of_classes)
        #        class_vector[0, random_class] = self.sigma + (1-self.sigma) * np.random.rand()
        #    else:
        #        break
        #
        # The closer the random number generator is to 0, it assumes that this is indicative of a small chance of
        # succeeding an game of multiple random consecutive chances.

        return math.log(np.random.rand(), self.vector_threshold)