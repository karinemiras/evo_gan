import numpy as np
import cv2
import imageio

save_image_folder = "../../imgs/"
interpolation_path = save_image_folder + "interpolations/"


def process_image(image):
    image = np.clip((image.transpose((1, 2, 0)) + 1) / 2., 0, 1)
    return cv2.cvtColor((image * 255).astype("uint8"), cv2.COLOR_BGR2RGB)


def save_image(filename, image):
    path = save_image_folder + filename

    cv2.imwrite(path, image)
    return path


def save_interpolations(images, generation_index):
    path = interpolation_path + "iteration{}_main.gif".format(generation_index + 1)
    imageio.mimsave(path, images)
    return path
