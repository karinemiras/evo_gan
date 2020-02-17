

class Generation:

    __instance = None

    @staticmethod
    def getInstance():
        """ Static access method. """
        if Generation.__instance == None:
            Generation()
        return Generation.__instance

    index = 0

    def __init__(self, index=0):
        """ Virtually private constructor. """
        if Generation.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            Generation.__instance = self

        self.index = index


if __name__ == "__main__":
    gen = Generation(1)
    print(gen.index)
    generation = Generation.getInstance()
    generation.index = 3
    print(gen.index, generation.index)
