import numpy as np
import cv2


def process_image(image):
    return np.clip((image.transpose((1, 2, 0)) + 1) / 2., 0, 1)


def save_image(path, image):
    image = process_image(image)
    image = cv2.cvtColor((image * 255).astype("uint8"), cv2.COLOR_BGR2RGB)
    cv2.imwrite(path, image)

