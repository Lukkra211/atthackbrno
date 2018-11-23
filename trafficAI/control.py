import yaml


class Controller:
    def __init__(self):
        self.minimap = None
        self.connections = None
        self.vehicles = None
        self.layers = None

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
        pass

    def __train(self):
        pass

    def __rate(self):
        pass
