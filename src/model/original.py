import torch
import nltk
from model.biggan import (BigGAN, one_hot_from_names, one_hot_from_int, truncated_noise_sample,
                                       save_as_images, display_in_terminal)
from PIL import Image
import time
import numpy as np
import copy
import cv2
from threading import Thread, Lock
import queue
import sys

class Individual():
    def __init__(self, device, truncation=0.4, batch_size=1, sigma=0.25):
        self.device = device
        self.truncation = truncation
        self.batch_size = 1

        # Sigma should be between 0 and 1
        self.sigma = sigma

        self.class_vector = None
        self.create_random_class_vector()

        self.noise_vector = None
        self.create_random_noise_vector()

    def create_random_class_vector(self):
        random_class = np.random.randint(0, 1000)
        class_vector = np.zeros((1,1000)).astype('float32')
        class_vector[0, random_class] = self.sigma + (1-self.sigma)*np.random.rand()

        while True:
            if np.random.rand()>1-self.sigma:
                random_class = np.random.randint(0, 1000)
                class_vector[0, random_class] = self.sigma + (1-self.sigma)*np.random.rand()
            else:
                break
        self.class_vector = class_vector
        threshold_indices = self.class_vector[0] <= self.sigma
        self.class_vector[0, threshold_indices] = 0

    def create_random_noise_vector(self):
        noise_vector = truncated_noise_sample(truncation=self.truncation, batch_size=self.batch_size).astype('float32')
        self.noise_vector = noise_vector

    def mutate_noise_vector(self):
        # Resample genes that fall outside the truncation
        accepted = np.zeros(self.noise_vector.shape).astype(self.noise_vector.dtype)
        for idx, value in enumerate(self.noise_vector[0]):
            flag = False
            while not flag:
                new_value = value + np.random.randn()*self.sigma
                if new_value <= self.truncation and new_value >= -self.truncation:
                    accepted[0, idx] = new_value
                    flag = True
        self.noise_vector = accepted

    def mutate_class_vector(self):
        active_classes = np.where(self.class_vector[0]>0.0)

        for idx in active_classes:
            self.class_vector[0, idx] += self.sigma - 2*self.sigma*np.random.rand()

        while True:
            if np.random.rand()>1-self.sigma:
                random_class = np.random.randint(0, 1000)
                self.class_vector[0, random_class] = self.sigma + (1-self.sigma)*np.random.rand()
            else:
                break

        threshold_indices = self.class_vector[0] <= self.sigma
        self.class_vector[0, threshold_indices] = 0

class Evolution():
    def __init__(self, interpolation_frames, n_children, truncation=0.4, batch_size=1):
        self.model = BigGAN.from_pretrained("biggan-deep-512")
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.batch_size = batch_size
        self.truncation = truncation
        self.model.to(self.device)

        self.generation = 0
        self.parent = None
        self.next_parent = None
        self.next_parent_idx = None
        self.n_children = n_children
        self.children = [None]*self.n_children

        self.interpolation_frames = interpolation_frames
        self.main_interpolation = [None]*self.interpolation_frames
        self.main_interpolation_tmp = [None]*self.interpolation_frames
        self.child_interpolations = [[None]*self.interpolation_frames]*n_children
        self.children_ready = False
        self.interpolating = False

        self.save_images = True
        self.save_image_index = 0
        self.save_image_folder = "./interpolations/"

        self.input_queue = queue.Queue()
        self.start()

    def add_input(self):
        while True:
            child_idx = sys.stdin.read(1)
            try:
                self.input_queue.put(int(child_idx))
            except:
                pass

    def make_children(self):
        for i in range(self.n_children - 1):
            self.children[i] = Individual(self.device)
            self.children[i].noise_vector = np.copy(self.parent.noise_vector)
            self.children[i].class_vector = np.copy(self.parent.class_vector)
            self.children[i].mutate_noise_vector()
            self.children[i].mutate_class_vector()

            self.save_individual("children/child_{}.png".format(i), self.children[i])

        self.children[self.n_children - 1] = Individual(self.device)

        self.save_individual("children/child_{}.png".format(self.n_children - 1), self.children[self.n_children - 1])

        self.generation += 1

    def interpolate(self, individual1, individual2, child_index=None):
        cop = None
        if child_index==2:
            cop = np.copy(self.child_interpolations[0][-1])
        noise_interpolation = np.linspace(individual1.noise_vector.squeeze(0), individual2.noise_vector.squeeze(0), num=self.interpolation_frames)
        class_interpolation = np.linspace(individual1.class_vector.squeeze(0), individual2.class_vector.squeeze(0), num=self.interpolation_frames)

        specific_child = copy.deepcopy(self.child_interpolations[child_index])
        for idx in range(0, len(noise_interpolation), self.batch_size):

            with Lock():

                noise_vectors = torch.from_numpy(noise_interpolation[idx:idx+self.batch_size]).to(self.device)
                class_vectors = torch.from_numpy(class_interpolation[idx:idx+self.batch_size]).to(self.device)

                with torch.no_grad():
                    tmp_interpolation = self.model(noise_vectors, class_vectors, self.truncation).to('cpu').numpy()
                    specific_child[idx:idx+self.batch_size] = np.copy([np.clip((interpolation.transpose((1,2,0)) + 1)/2., 0, 1) for interpolation in tmp_interpolation])


        self.child_interpolations[child_index] = specific_child
                # torch.cuda.empty_cache()

    def save_numpy(self, path, image):
        image = cv2.cvtColor((image*255).astype("uint8"), cv2.COLOR_BGR2RGB)
        cv2.imwrite(path, image)

    def save_individual(self, path, individual):
        noise_vector = torch.from_numpy(individual.noise_vector).to(self.device)
        class_vector = torch.from_numpy(individual.class_vector).to(self.device)
        with torch.no_grad():
            image = self.model(noise_vector, class_vector, self.truncation).to('cpu').numpy().squeeze(0)
            image = np.clip((image.transpose((1,2,0)) + 1)/2., 0, 1)
            image = cv2.cvtColor((image*255).astype("uint8"), cv2.COLOR_BGR2RGB)
            cv2.imwrite(path, image)

    def interpolate_children(self):
        t = time.time()
        print("Interpolating children")
        self.interpolating = True
        for idx in range(self.n_children):
            self.interpolate(self.parent, self.children[idx], child_index=idx)
        self.interpolating = False
        print("Interpolated_children in {} seconds".format(time.time()-t))

    def start(self):
        input_thread = Thread(target=self.add_input, daemon=True)
        input_thread.start()

        self.parent = Individual(self.device)
        self.make_children()

        self.next_parent_idx = np.random.randint(4)
        self.interpolate(self.parent, self.children[self.next_parent_idx], child_index=self.next_parent_idx)

        self.main_interpolation = np.copy(self.child_interpolations[self.next_parent_idx])

        self.parent = self.children[self.next_parent_idx]
        self.make_children()

        child_thread = Thread(target=self.interpolate_children)
        child_thread.start()

        time.sleep(20)

        cv2.namedWindow("BigGAN", cv2.WINDOW_NORMAL)
        # cv2.setWindowProperty("BigGAN", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

        interpolation_index = 0
        forward = True

        next_interpolation_ready = False

        t = time.time()

        indexes_saved = []

        while True:
            frame = cv2.cvtColor(self.main_interpolation[interpolation_index],cv2.COLOR_BGR2RGB)

            if self.save_images and interpolation_index not in indexes_saved and len(indexes_saved)<self.interpolation_frames - 1:
                indexes_saved.append(interpolation_index)
                image = (frame*255).astype("uint8")
                cv2.imwrite("{0}{1:06d}.png".format(self.save_image_folder, self.save_image_index), image)
                self.save_image_index += 1

            cv2.imshow("BigGAN", frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

            if interpolation_index==0:
                forward = True

            if interpolation_index==self.interpolation_frames-1:
                if next_interpolation_ready:
                    print("Interpolation ready")
                    next_interpolation_ready = False

                    self.main_interpolation = np.copy(self.main_interpolation_tmp)
                    indexes_saved = []
                    interpolation_index = 0
                else:
                    forward = False

            if forward:
                interpolation_index += 1
            else:
                interpolation_index -= 1

            if time.time()-t > 30.0 and not self.interpolating:
                if not self.input_queue.empty():
                    self.next_parent_idx = self.input_queue.get()
                    if self.next_parent_idx not in [i for i in range(self.n_children)]:
                        self.next_parent_idx = np.random.randint(4)
                else:
                    self.next_parent_idx = np.random.randint(4)

                print("Chosen: {}".format(self.next_parent_idx))

                self.main_interpolation_tmp = np.copy(self.child_interpolations[self.next_parent_idx])

                self.parent = self.children[self.next_parent_idx]

                self.make_children()

                child_thread = Thread(target=self.interpolate_children)
                child_thread.start()

                t = time.time()
                next_interpolation_ready = True

            time.sleep(1/30.)

def main():
    n_children = 4
    batch_size = 4
    interpolation_frames = 60
    evolution = Evolution(interpolation_frames, n_children, batch_size=batch_size)

if __name__=="__main__":
    main()
