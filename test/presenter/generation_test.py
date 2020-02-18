import unittest

from presenter.generation import Generation


class TestGenerationMethods(unittest.TestCase):

    def test_instances(self):
        generation_object = Generation()
        generation_instance = Generation.getInstance()

        generation_object.index = 1

        self.assertEqual(generation_object, generation_instance)
        self.assertEqual(generation_object.index, generation_instance.index)

    def test_instance(self):
        generation_instance = Generation.getInstance()
        self.assertRaises(Generation())

    def test_instance(self):
        generation_instance1 = Generation.getInstance()
        generation_instance1.index = 1

        generation_instance2 = Generation.getInstance()
        generation_instance2.index = 2

        self.assertEqual(generation_instance1, generation_instance2)
        self.assertEqual(generation_instance1.index, generation_instance2.index)


if __name__ == '__main__':
    unittest.main()