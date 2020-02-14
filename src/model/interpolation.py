import torch

import numpy as np
import copy
from threading import Lock
from model.image import process_image


class Interpolation:
    def __init__(self, interpolation_frames, n_children):

        self.interpolation_frames = interpolation_frames
        self.child_interpolations = [[None]*self.interpolation_frames]*n_children

        self.save_images = True
        self.save_image_index = 0
        self.save_image_folder = "../../imgs/interpolations/"

    # TODO refactor
    def interpolate(self, gan, individual1, individual2, child_index=None, batch_size=1):
        noise_interpolation = np.linspace(individual1.noise_vector.squeeze(0), individual2.noise_vector.squeeze(0),
                                          num=self.interpolation_frames)
        class_interpolation = np.linspace(individual1.class_vector.squeeze(0), individual2.class_vector.squeeze(0),
                                          num=self.interpolation_frames)

        specific_child = copy.deepcopy(self.child_interpolations[child_index])
        for idx in range(0, len(noise_interpolation), batch_size):

            # TODO remove
            with Lock():

                noise_vectors = torch.from_numpy(noise_interpolation[idx:idx+batch_size])
                class_vectors = torch.from_numpy(class_interpolation[idx:idx+batch_size])

                tmp_interpolation = gan.get_model_images(noise_vectors, class_vectors).to('cpu').numpy()
                specific_child[idx:idx+batch_size] = np.copy([process_image(interpolation) for interpolation in tmp_interpolation])

        self.child_interpolations[child_index] = specific_child

