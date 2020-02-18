import unittest
import time

from model.gan import GAN
from model.individual import Individual
from model.biggan.model import BigGAN


class TestGANMethods(unittest.TestCase):

    gan = GAN()

    color_image_dim = 3

    def test_initialization(self):
        self.assertTrue(GAN.resolution in [128, 256, 512])

        self.assertIsInstance(self.gan.model, BigGAN)

    def test_individual(self):
        individual = Individual()

        self.gan.resolution = 512

        start_time = time.time()
        image = self.gan.get_model_image(individual)
        elapsed_time = time.time() - start_time
        print(elapsed_time)

        self.assertEqual(image.shape[0], self.gan.resolution)
        self.assertEqual(image.shape[1], self.gan.resolution)
        self.assertEqual(image.shape[2], self.color_image_dim)


if __name__ == '__main__':
    unittest.main()