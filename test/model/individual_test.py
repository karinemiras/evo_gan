import unittest

from model.individual import Individual


class TestIndividualMethods(unittest.TestCase):

    def test_individual_vectors(self):
        individual = Individual()

        self.assertEqual(individual.noise_vector.shape[0], individual.batch_size)
        self.assertEqual(individual.noise_vector.shape[1], individual.dim_z) # not sure why this should be 128 (dim_z)

        self.assertEqual(individual.class_vector.shape[0], individual.batch_size)
        self.assertEqual(individual.class_vector.shape[1], individual.number_of_classes)

    def test_individual_mutated_vectors(self):
        individual = Individual()

        individual.mutate()

        self.assertEqual(individual.noise_vector.shape[0], individual.batch_size)
        self.assertEqual(individual.noise_vector.shape[1], individual.dim_z)  # not sure why this should be 128 (dim_z)

        self.assertEqual(individual.class_vector.shape[0], individual.batch_size)
        self.assertEqual(individual.class_vector.shape[1], individual.number_of_classes)


if __name__ == '__main__':
    unittest.main()