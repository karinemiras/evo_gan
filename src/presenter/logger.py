import json

from model.individual import Individual

from presenter.generation import Generation


class Logger:

    log_folder = "../../logs/"
    regular_filename = "generation_log.json"
    template_filename = "template_log.json"

    def __init__(self):
        self.generation = Generation.getInstance()
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

        self.generation.index = len(self.generations_data['generations'])

    def write_log(self):

        with open(self.log_folder + self.regular_filename, 'w') as json_file:
            # Indent makes it more readable for humans... TODO: do not expand the arrays
            json.dump(self.generations_data, json_file, indent=4)

    def create_log(self, parent: Individual, child_index: int):

        generation_dictionary = {"generation_index": self.generation.index,
                                 "parent_class": parent.class_vector.tolist(),
                                 "parent_noise": parent.noise_vector.tolist(),
                                 "child_index": child_index}
        self.generations_data['generations'].append(generation_dictionary)


if __name__ == "__main__":
    from presenter.helper import extract_parent_from_logger
    logger = Logger()

    logger.open_log(template=True)
    parent = extract_parent_from_logger(logger)
    print(parent, Generation.getInstance().index)
    logger.create_log(parent=Individual(), child_index=0)
    logger.write_log()

