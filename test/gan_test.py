import unittest

from model.gan import GAN

from model.individual import Individual


class TestGANMethods(unittest.TestCase):

    def test_gan(self):
        gan = GAN()

        individual = Individual()

        image = gan.get_model_image(individual)

        self.assertEqual(image.shape[0], gan.resolution)
        self.assertEqual(image.shape[1], gan.resolution)
        self.assertEqual(image.shape[2], 3)

if __name__ == '__main__':
    unittest.main()