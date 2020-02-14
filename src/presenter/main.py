
import time
import numpy as np

from threading import Thread

from model.individual import Individual
from model.evolution import Evolution


self.generation = 0

self.generation += 1




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
