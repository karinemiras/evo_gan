import unittest

from model.individual import Individual


class TestIndividualMethods(unittest.TestCase):

    def test_individual_vectors(self):
        individual = Individual()

        self.assertEqual(individual.noise_vector.shape[0], individual.batch_size)
        self.assertEqual(individual.noise_vector.shape[1], 128) # not sure why this should be 128 (dim_z)

        self.assertEqual(individual.class_vector.shape[0], individual.batch_size)
        self.assertEqual(individual.class_vector.shape[1], individual.number_of_classes)

    def test_individual_vectors_batch_size(self):
        individual = Individual(batch_size=3)

        self.assertEqual(individual.noise_vector.shape[0], individual.batch_size)
        self.assertEqual(individual.noise_vector.shape[1], 128) # not sure why this should be 128 (dim_z)

        self.assertEqual(individual.class_vector.shape[0], individual.batch_size)
        self.assertEqual(individual.class_vector.shape[1], individual.number_of_classes)

    def test_individual_mutated_noise_vectors(self):
        individual = Individual(batch_size=3)

        individual.mutate_noise_vector()

        self.assertEqual(individual.noise_vector.shape[0], individual.batch_size)
        self.assertEqual(individual.noise_vector.shape[1], 128)  # not sure why this should be 128 (dim_z)

    def test_individual_mutated_class_vectors(self):
        individual = Individual(batch_size=3)

        individual.mutate_class_vector()
        print(individual.class_vector)

        self.assertEqual(individual.class_vector.shape[0], individual.batch_size)
        self.assertEqual(individual.class_vector.shape[1], individual.number_of_classes)

if __name__ == '__main__':
    unittest.main()