import torch
import os
import numpy as np

from model.biggan import (BigGAN)


class GAN:

    root_dir = os.path.dirname(os.path.abspath(__file__))

    def __init__(self, resolution=128, truncation=0.4):
        self.resolution = resolution

        self.truncation = truncation

        self.model = BigGAN.from_pretrained("biggan-deep-" + str(self.resolution), cache_dir=self.root_dir + "/../../biggan/")
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

        self.model.to(self.device)

    def get_model_image(self, individual):
        noise_vector = torch.from_numpy(individual.noise_vector).to(self.device)
        class_vector = torch.from_numpy(individual.class_vector).to(self.device)

        with torch.no_grad():
            return process_image(self.model(noise_vector, class_vector, self.truncation).to('cpu').numpy().squeeze(0))

    def get_model_images(self, noise_vectors, class_vectors):
        noise_vectors = noise_vectors.to(self.device)
        class_vectors = class_vectors.to(self.device)

        with torch.no_grad():
            images = self.model(noise_vectors, class_vectors, self.truncation).to('cpu').numpy()
            return [process_image(image) for image in images]


def process_image(image):
    image = np.clip((image.transpose((1, 2, 0)) + 1) / 2., 0, 1)

    return (image * 255).astype("uint8")


if __name__ == "__main__":
    gan = GAN()

    print(gan.model)