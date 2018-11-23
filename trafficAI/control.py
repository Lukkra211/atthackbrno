import yaml


class Controller:
    def __init__(self):
        self.minimap = None
        self.connections = None
        self.vehicles = None
        self.layers = None

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


    def present(self):
        pass

    def validate(self):
        pass

    def develop(self):
        pass

    def __train(self):
        pass

    def __rate(self):
        pass
