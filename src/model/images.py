import numpy as np
import cv2
import imageio

save_image_folder = "../../imgs/"
interpolation_path = save_image_folder + "interpolations/"


def process_image(image, color_change=True):
    image = np.clip((image.transpose((1, 2, 0)) + 1) / 2., 0, 1)

    if color_change:
        return cv2.cvtColor((image * 255).astype("uint8"), cv2.COLOR_BGR2RGB)
    else:
        return(image * 255).astype("uint8")


def save_image(filename, image):
    path = save_image_folder + filename

    cv2.imwrite(path, image)
    return path


def save_interpolations(images, generation_index):
    path = interpolation_path + "iteration{}_main.gif".format(generation_index)
    imageio.mimsave(path, images)
    return path
