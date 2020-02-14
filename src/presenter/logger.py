import json
from typing import List


class Logger:

    log_folder = "../../logs/"
    regular_filename = "generation_log.json"
    template_filename = "template_log.json"

    def __init__(self):
        self.generation_index = 0
        self.generations_data = []

    def _open_json(self, filename):
        with open(self.log_folder + filename) as json_file:
            return json.load(json_file)

    def open_log(self, template=False):

        if not template:
            try:
                # open default log file
                self.generations_data = self._open_json(self.regular_filename)
            except:
                # use backup
                self.generations_data = self._open_json(self.template_filename)
        else:
            self.generations_data = self._open_json(self.template_filename)

        self.generation_index = len(self.generations_data['generations'])

    def write_log(self):

        with open(self.log_folder + self.regular_filename, 'w') as json_file:
            json.dump(self.generations_data, json_file)

    def create_log(self, parent_filename, child_filename, interpolation_filename):

        generation_dictionary = {"generation_index": self.generation_index,
                                 "parent_filename": parent_filename,
                                 "child_filename": child_filename,
                                 "interpolation_filename": interpolation_filename}
        self.generations_data['generations'].append(generation_dictionary)

        self.generation_index += 1


if __name__ == "__main__":
    logger = Logger()

    logger.open_log(template=True)

    generation_index = len(logger.generations_data["generations"])
    logger.create_log("parent_" + str(generation_index),
                    "child" + str(generation_index), "morph_" + str(generation_index))

    logger.write_log()

    print("generations", logger.generations_data)
