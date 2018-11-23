import yaml

from automata import Core
from genetics import Evolution

TEST_STEPS = 500
GENERATIONS = 100


class Controller:
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
        system: path to system (yaml)
        """
        with open(system, 'r') as f:
            system = yaml.load(f)

        self.minimap = system['minimap']
        self.connections = system['connections']

        self.vehicles = system.get('vehicles', 40)
        self.layers = system.get('layers', [])

        self.core = Core(self.minimap, self.connections, self.vehicles)

    def present(self):
        self.presenter = Presenter(self.connections, self.minimap, self.core)
        self.presenter.main_loop()

    def validate(self):
        pass

    def develop(self):
        self.evolution = Evolution(self.layers)

        for _ in range(GENERATIONS):
            self.__train()

    def __train(self):
        for individual in self.evolution.queue:
            self.evolution.rated(individual, self.__rate(individual))
            print('hello')

        self.evolution.breed()

    def __rate(self, individual):
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
