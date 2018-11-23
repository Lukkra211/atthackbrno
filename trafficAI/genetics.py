import numpy

from typing import Callable


POPULATION = 100
MUTATE_CHANCE = 0.9
MERGE_RATIO = 0.95


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

        self.best_fit = None

    def __compute_layers(self):

        pass

    def __generate_queue(self):
        return [{'number': i, 'stucked': 0, 'weights': self.__generate_dna()}
                for i in range(POPULATION)]

    def rated(self, individual, stucked):
        individual['stucked'] = stucked
        self.population.append(individual)

    def __generate_dna(self):
        weights = []

        for index in range(len(self.layers) - 1):
            size = (self.layers[index + 1], self.layers[index])
            weights.append(numpy.random.random(size) * 2 - 1)

        return numpy.array(weights)

    def get_nn(self, weights, normalize=default_normalize) -> Callable:
        """
        Create the neural networks which works like a function that only
        takes the inputs, other params are defined by the `Evolution`
        """
        def nn(inputs):
            return neural_network(inputs, weights, normalize, self.layers)
        return nn

    def breed(self):
        """
        Create new population out of the old one which should have been already
        evaluated

        Score of each individual is calculated by subtracting the number of
        stucked cars from the maximum of stucked car of the worst neural
        network. The scores then determine the propability that it will be
        merged with other NN.
        """
        self.queue = []
        self.population.sort(key=lambda x: x['stucked'])

        maximum = self.population[-1]['stucked']

        stucked_list = [float(indv['stucked']) for indv in self.population]
        propability = numpy.array(stucked_list)
        propability = numpy.power(maximum + 1 - propability, 20)

        total_points = sum(propability)
        propability_per_point = 1 / total_points
        propability = propability * propability_per_point

        for index in range(len(self.population) // 2):
            selected = numpy.random.choice(self.population, 2, p=propability)
            self.copulate(selected[0], selected[1], index)

        self.population = []

    def copulate(self, indv1, indv2, num):
        """
        Merge two individuals (their DNA) together and mutates them a bit

        Add them straight to the queue to be evaluated

        Note:
            ehm, dont mind the name... :-D

        """
        weights1, weights2, = [], []

        for l1, l2 in zip(indv1['weights'], indv2['weights']):
            mask = numpy.random.random(l1.shape) >= MERGE_RATIO

            new_l1 = l1.copy()
            new_l2 = l2.copy()

            new_l1[mask] = l2[mask]
            new_l2[mask] = l1[mask]

            self.mutate(new_l1)
            self.mutate(new_l2)

            weights1.append(new_l1)
            weights2.append(new_l2)

        self.queue.extend([
            {'stucked': 0, 'weights': weights1, 'number': num},
            {'stucked': 0, 'weights': weights2, 'number': num + 1}
        ])

    def mutate(self, weights) -> None:
        """
        Change the weights of given individual
        """
        for layer in weights:
            mask = numpy.random.random(layer.shape) >= MUTATE_CHANCE
            randomly_created = numpy.random.random(layer.shape)
            layer[mask] = randomly_created[mask]
