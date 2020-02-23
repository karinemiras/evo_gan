
from model.biggan import (truncated_noise_sample)
import numpy as np
import math


class Individual:

    number_of_classes = 1000

    def __init__(self, truncation=0.4, vector_threshold=0.25):

        self.truncation = truncation
        self.dim_z = 128
        # Sigma should be between 0 and 1
        self.vector_threshold = vector_threshold
        self.batch_size = 1
        self.max_classes = 2

        self.image = None

        self.class_vector = None
        self.noise_vector = None

        self.initialize()

    def initialize(self, log_dict=None):
        if log_dict is None:
            self._create_random_class_vector()
            self._create_random_noise_vector()
        else:
            self.class_vector = np.array(log_dict["class"]).astype('float32')
            self.noise_vector = np.array(log_dict["noise"]).astype('float32')

    def _create_random_class_vector(self):
        self.class_vector = self._insert_random_class_vectors()

    def _create_random_noise_vector(self):
        self.noise_vector = truncated_noise_sample(truncation=self.truncation, dim_z=self.dim_z,
                                                   batch_size=self.batch_size).astype('float32')

    def mutate(self, noise=None):
        self._mutate_class_vector()

        if noise is None:
            self._mutate_noise_vector()
        else:
            self.noise_vector = noise.reshape(1, self.dim_z).astype('float32')

    def _mutate_noise_vector(self):
        self.noise_vector = (np.random.randn(self.batch_size, self.dim_z) * self.vector_threshold
                             + self.noise_vector).astype('float32')

        lowest_value = np.min(self.noise_vector)
        highest_value = np.max(self.noise_vector)
        absolute_value = max(abs(lowest_value), abs(highest_value))
        # important to
        self.noise_vector = (self.noise_vector / absolute_value * self.truncation)

    def _mutate_class_vector(self):
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

        # TODO allow for batch size
        nonzero_values = np.flatnonzero(class_vector[0])
        np.sort(nonzero_values)

        nonzero_index = min(len(nonzero_values), self.max_classes) - 1
        if nonzero_index >= 0:
            nonzero_value = nonzero_values[nonzero_index]
            threshold = class_vector[0, nonzero_value]

            # Permit batch index
            class_vector[class_vector < threshold] = 0


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
