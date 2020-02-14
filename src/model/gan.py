import torch

from model.biggan import (BigGAN)


class GAN:

    def __init__(self, truncation=0.4):
        self.truncation = truncation

        self.model = BigGAN.from_pretrained("biggan-deep-512")
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

        self.model.to(self.device)

    def get_model_image(self, individual):
        noise_vector = torch.from_numpy(individual.noise_vector).to(self.device)
        class_vector = torch.from_numpy(individual.class_vector).to(self.device)
        with torch.no_grad():
            return self.model(noise_vector, class_vector, self.truncation).to('cpu').numpy().squeeze(0)

    def get_model_images(self, noise_vectors, class_vectors):
        noise_vectors = noise_vectors.to(self.device)
        class_vectors = class_vectors.to(self.device)
        with torch.no_grad():
            return self.model(noise_vectors, class_vectors, self.truncation).to('cpu').numpy()
