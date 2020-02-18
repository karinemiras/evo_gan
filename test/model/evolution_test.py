import copy
import numpy as np
import unittest

from model.evolution import Evolution
from model.individual import Individual


class TestEvolutionMethods(unittest.TestCase):
    n_children = 3
    batch_size = 1
    interpolation_frames = 3

    evolution = Evolution(interpolation_frames=interpolation_frames, n_children=n_children,
                          batch_size=batch_size)

    def test_initialization(self):

        self.assertIsInstance(self.evolution.parent, Individual)
        self.assertEqual(len(self.evolution.children), self.n_children)

        for child in self.evolution.children:
            self.assertIsInstance(child, Individual)

    def test_progress_generation(self):
        child_index = 0

        old_child = self.evolution.children[child_index]

        self.evolution.process_generation(child_index)

        # Recheck parent and child
        self.test_initialization()

        self.assertTrue(np.allclose(self.evolution.parent.noise_vector, old_child.noise_vector))
        self.assertTrue(np.allclose(self.evolution.parent.class_vector, old_child.class_vector))


if __name__ == '__main__':
    unittest.main()