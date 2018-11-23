import numpy


POPULATION = 1000


def neural_network(inputs, weights, normalize, layers):
    results = normalize(numpy.vstack(inputs))
    pass


def default_normalize(x):
    return 1 / (1 + numpy.exp(-x))


class Evolution:
    def __init__(self, layers):
        self.population = []
        self.layers = layers
        self.queue = self.__generate_queue()

    def rated(self, individual, stucked):
        self.individual['stucked'] = stucked
        self.population.append(individual)

    def __generate_queue(self):
        return [{'number': i, 'stucked': 0, 'weights': self.__generate_dna}
                for i in range(POPULATION)]

    def __generate_dna(self):
        weights = pygame.array(())

        for index in range(len(self.layers) - 1):
            size = (self.layers[index], self.layers[index + 1])
            weights.append(numpy.random.random(size))

        return weights

    def get_nn(self, weights, normalize=default_normalize):
        def nn(inputs):
            return neural_network(inputs, weights, normalize, self.layers)
        return nn

    def breed(self):
        pass
