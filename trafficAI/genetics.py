import numpy

from typing import Callable


POPULATION = 1000
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
        self.population.sort(key=lambda x: x['stucked'])

        maximum = max(indv['stucked'] for indv in self.population)

        for index in range(len(self.population)):
            stucked = self.population[index]['stucked']
            self.population[index]['score'] = maximum - stucked

        points = numpy.array([indv['score'] for indv in self.population])
        total_points = sum(points)

        propability_per_point = 1 / total_points
        # the score is to ^20 to further the learning of the NN
        # True, it makes the algorithm more likely to stuck in local
        # minimum, but it's fine for the demo
        propability = numpy.power(points, 20) * propability_per_point

        for index in range(self.population // 2):
            selected = numpy.random.choice(self.population, 2, p=propability)
            self.copulate(selected[0], selected[1], index)

    def copulate(self, indv1, indv2, num):
        """
        Merge two individuals (their DNA) together and mutates them a bit

        Add them straight to the queue to be evaluated

        Note:
            ehm, dont mind the name... :-D

        """
        weights1, weights2, = [], []

        for layer_index in len(indv1['weights']):
            indv1_w, indv2_w = indv1['weights'], indv2['weights']
            mask = numpy.random.random(indv1_w.shape) < MERGE_RATIO

            indv1_new_layers = indv1_w.copy()
            indv2_new_layers = indv2_w.copy()

            indv1_new_layers[mask] = indv2_w[mask]
            indv2_new_layers[mask] = indv1_w[mask]

            weights1.append(indv1_new_layers)
            weights2.append(indv2_new_layers)

        self.queue.extend(
            {'stucked': 0, 'weights': self.mutate(weights1), 'number': num},
            {'stucked': 0, 'weights': self.mutate(weights2), 'number': num + 1}
        )

    def mutate(self, individual) -> None:
        """
        Change the weights of given individual
        """
        new_weights = numpy.array(())
        for layer in individual['weights']:
            mask = numpy.random.random(layer.shape) >= MUTATE_CHANCE
            randomly_created = numpy.random.random(layer.shape)
            layer[mask] = randomly_created[mask]

            new_weights.append(layer)

        individual['weights'] = new_weights
