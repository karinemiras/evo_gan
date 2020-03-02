import torch

import numpy as np
from model.individual import Individual


class Interpolation:

    def __init__(self, interpolation_frames):

        self.interpolation_frames = interpolation_frames

    def interpolate(self, gan, parent, child, batch_size=1):
        noise_interpolation = np.linspace(parent.noise_vector.squeeze(0), child.noise_vector.squeeze(0),
                                          num=self.interpolation_frames * 2)
        class_interpolation = np.linspace(parent.class_vector.squeeze(0), child.class_vector.squeeze(0),
                                          num=self.interpolation_frames * 2)

        child_interpolations = [None] * self.interpolation_frames
        # not sure why having a batch size is necessary
        for index in range(0, self.interpolation_frames, batch_size):

            #with Lock(): # TODO remove
            noise_vectors = torch.from_numpy(noise_interpolation[index:index+batch_size])
            class_vectors = torch.from_numpy(class_interpolation[index:index+batch_size])

            child_interpolations[index:index+batch_size] = gan.get_model_images(noise_vectors, class_vectors)

        child = Individual()
        # Todo make more practical for batch sizes larger than 1
        child.set_values(np.expand_dims(class_interpolation[-1], 0),
                         np.expand_dims(noise_interpolation[-1], 0), child_interpolations[-1])

        return child_interpolations, child