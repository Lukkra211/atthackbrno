import random
import sys

import yaml

from automata import Core
from genetics import Evolution
from graphic import Presenter

TEST_STEPS = 500
GENERATIONS = 100


class Controller:
    """
    Class which glues the project components together
    """
    def __init__(self):
        self.minimap = None
        self.connections = None
        self.vehicles = None
        self.layers = None

        self.evolution = None
        self.presenter = None
        self.core = None

    def load_system(self, system):
        """
        Load the system from a YAML file
        """
        with open(system, 'r') as f:
            system = yaml.load(f)

        self.minimap = system['minimap']
        self.connections = system['connections']

        self.vehicles = system.get('vehicles', 40)

        self.core = Core(self.minimap, self.connections, self.vehicles)

        hidden_layers = layers = system.get('layers', [])
        side_neurons = len(self.core.junction_queues)
        self.layers = [side_neurons] + hidden_layers + [side_neurons]

    def present(self):
        """
        Called when the user wants to run the simulation with GUI
        """
        self.presenter = Presenter(self.connections, self.minimap, (900, 900))
        self.presenter.main_loop(self.core)

    def validate(self):
        pass

    def develop(self):
        """
        Called when the user wants to train the AI for a given system from YAML
        """
        try:
            self.evolution = Evolution(self.layers)

            for _ in range(GENERATIONS):
                self.__train()
                print('')

        finally:
            self.core.reset(self.evolution.get_nn(self.evolution.best_fit))
            self.present()

    def __train(self):
        """
        Evaluate the population of current generation and breed them
        """
        for index, individual in enumerate(self.evolution.queue):
            self.evolution.rated(individual, self.__rate(individual))

            if index % 5 == 0:
                print('.', end='')
                sys.stdout.flush()

        self.evolution.breed()

    def __rate(self, individual):
        """
        Evaluate how good the AI was
        """
        self.core.reset(self.evolution.get_nn(individual))

        stucked = 0
        for _ in range(TEST_STEPS):
            self.core.step()

            for link in self.core.links:
                stucked += link.stucked

            for ap in self.core.access_points:
                if ap.inactive:
                    stucked += ap.to_generate
        return stucked
