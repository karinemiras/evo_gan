import torch
import nltk
from pytorch_pretrained_biggan import (BigGAN, one_hot_from_names, one_hot_from_int, truncated_noise_sample,
                                       save_as_images, display_in_terminal)
from PIL import Image
import time
import numpy as np
import copy
import cv2
from threading import Thread
import queue
import sys

class Individual():
    def __init__(self, device, truncation=0.4, batch_size=1, sigma=0.1):
        self.device = device
        self.truncation = truncation
        self.batch_size = 1
        self.sigma = 1.0

        self.class_vector = None
        self.create_random_class_vector()

        self.noise_vector = None
        self.create_random_noise_vector()

    def create_random_class_vector(self):
        random_class = np.random.randint(0, 1000)
        class_vector = np.zeros((1,1000)).astype('float32')
        class_vector[0, random_class] = 1*np.random.rand()

        while True:
            if np.random.rand()>0.5:
                class_vector = np.zeros((1,1000)).astype('float32')
                class_vector[0, random_class] = 1*np.random.rand()
            else:
                break
        self.class_vector = class_vector

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

class Evolution():
    def __init__(self, interpolation_frames, n_children, truncation=0.4, batch_size=1):
        self.model = BigGAN.from_pretrained("biggan-deep-512")
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.batch_size = batch_size
        self.truncation = truncation
        self.model.to(self.device)

        self.generation = 0
        self.parent = Individual(self.device)
        self.n_children = n_children
        self.children = [None]*self.n_children
        self.make_children()

        self.interpolation_frames = interpolation_frames
        self.main_interpolation = [None]*self.interpolation_frames
        self.child_interpolations = [[None]*self.interpolation_frames]*n_children
        self.children_ready = False
        self.interpolating = False
        self.chosen = True

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

    def interpolate_children(self):
        self.interpolating = True
        for idx in range(self.n_children):
            self.interpolate(self.parent, self.children[idx], main=False, child_index=idx)
        self.interpolating = False

    def start(self):
        input_thread = Thread(target=self.add_input, daemon=True)
        input_thread.start()

        # Interpolate frames main visualisation
        self.interpolate(self.parent, self.children[np.random.randint(self.n_children)], main=True)

        child_thread = Thread(target=self.interpolate_children)
        child_thread.start()

        # # Open full screen window
        cv2.namedWindow("BigGAN", cv2.WINDOW_NORMAL)
        # cv2.setWindowProperty("BigGAN", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

        interpolation_index = 0
        forward = True

        next_interpolation_ready = False

        t = time.time()
        while True:
            frame = cv2.cvtColor(self.main_interpolation[interpolation_index],cv2.COLOR_BGR2RGB)
            cv2.imshow("BigGAN", frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

            if interpolation_index==0:
                forward = True

            if interpolation_index==self.interpolation_frames-1:
                if next_interpolation_ready:
                    print("Interpolation ready")
                    next_interpolation_ready = False
                    self.main_interpolation = self.main_interpolation_tmp
                    if self.save_images:
                        for image in self.main_interpolation:
                            image = cv2.cvtColor((image*255).astype("uint8"), cv2.COLOR_BGR2RGB)
                            cv2.imwrite("{0}{1:06d}.png".format(self.save_image_folder, self.save_image_index), image)
                            self.save_image_index += 1
                    interpolation_index = 0
                else:
                    forward = False

            if forward:
                interpolation_index += 1
            else:
                interpolation_index -= 1

            print(self.chosen)
            if time.time()-t > 20.0 and not self.interpolating and self.chosen:
                print("Interpolating")
                #if not self.input_queue.empty():
                child_idx = 0 #self.input_queue.get()
                self.chosen = False

                print("Chosen value: {}".format(child_idx))

                self.main_interpolation_tmp = copy.deepcopy(self.child_interpolations[child_idx])

                self.parent = copy.deepcopy(self.children[child_idx])

                self.make_children()

                child_thread = Thread(target=self.interpolate_children)
                child_thread.start()

                t = time.time()
                next_interpolation_ready = True


            time.sleep(1/30.)

    def interpolate(self, individual1, individual2, main=False, child_index=None):
        noise_interpolation = np.linspace(individual1.noise_vector.squeeze(0), individual2.noise_vector.squeeze(0), num=self.interpolation_frames)
        class_interpolation = np.linspace(individual1.class_vector.squeeze(0), individual2.class_vector.squeeze(0), num=self.interpolation_frames)

        for idx in range(0, len(noise_interpolation), self.batch_size):
            noise_vectors = torch.from_numpy(noise_interpolation[idx:idx+self.batch_size]).to(self.device)
            class_vectors = torch.from_numpy(class_interpolation[idx:idx+self.batch_size]).to(self.device)

            with torch.no_grad():
                if main:
                    self.main_interpolation[idx:idx+self.batch_size] = self.model(noise_vectors, class_vectors, self.truncation).to('cpu').numpy()
                    self.main_interpolation[idx:idx+self.batch_size] = [np.clip((interpolation.transpose((1,2,0)) + 1)/2., 0, 1) for interpolation in self.main_interpolation[idx:idx+self.batch_size]]
                else:
                    self.child_interpolations[child_index][idx:idx+self.batch_size] = self.model(noise_vectors, class_vectors, self.truncation).to('cpu').numpy()
                    self.child_interpolations[child_index][idx:idx+self.batch_size] = [np.clip((interpolation.transpose((1,2,0)) + 1)/2., 0, 1) for interpolation in self.child_interpolations[child_index][idx:idx+self.batch_size]]

            torch.cuda.empty_cache()

    def make_children(self):
        for i in range(self.n_children - 1):
            self.children[i] = Individual(self.device)
            self.children[i].noise_vector = copy.deepcopy(self.parent.noise_vector)
            self.children[i].class_vector = copy.deepcopy(self.parent.class_vector)
            self.children[i].mutate_noise_vector()

        self.children[self.n_children - 1] = Individual(self.device)


        for idx, child in enumerate(self.children):
            noise_vector = torch.from_numpy(child.noise_vector).to(self.device)
            class_vector = torch.from_numpy(child.class_vector).to(self.device)
            with torch.no_grad():
                image = self.model(noise_vector, class_vector, self.truncation).to('cpu').numpy().squeeze(0)
                image = np.clip((image.transpose((1,2,0)) + 1)/2., 0, 1)
                image = cv2.cvtColor((image*255).astype("uint8"), cv2.COLOR_BGR2RGB)
                cv2.imwrite("{0}{1:06d}-{2}.png".format("children/", self.generation, idx), image)

        self.generation += 1

def main():
    n_children = 4
    batch_size = 4
    interpolation_frames = 60
    evolution = Evolution(interpolation_frames, n_children, batch_size=batch_size)

if __name__=="__main__":
    main()
