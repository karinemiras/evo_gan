import numpy as np
import cv2
import imageio

from presenter.generation import Generation

save_image_folder = "../imgs/"

generation = Generation.getInstance()


def save_image(filename, image):
    path = save_image_folder + filename
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    cv2.imwrite(path, image)
    return path


def save_interpolations(images):
    global generation
    path = save_image_folder + "interpolations/iteration{}_main.gif".format(generation.index + 1)
    imageio.mimsave(path, images)
    return path


def save_parent_image(gan, parent, generate=False):
    global generation
    index = generation.index + 1
    if generate:
        parent.image = gan.get_model_image(parent)
        index = index - 1

    filename = "parent/iteration{}_0.png".format(index)
    save_image(filename, parent.image)

    return filename, parent


def save_chosen_parent_image(individual):
    global generation
    filename = "parent/iteration{}_1.png".format(generation.index)
    save_image(filename, individual.image)

    return filename


def generate_population_image(gan, individual, child_index):
    global generation
    individual.image = gan.get_model_image(individual)

    filename = "population/iteration{}_{}.png".format(generation.index, child_index)

    save_image(filename, individual.image)

    return individual


def save_candidate_image(image, child_index):
    global generation
    filename = "candidate/iteration{}_{}.png".format(generation.index, child_index)

    save_image(filename, image)

