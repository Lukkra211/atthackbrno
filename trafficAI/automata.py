from numpy import random
from itertools import chain


class Link:
    pass


class LinkPoint:
    pass


class Point:
    pass


class AccessPoint:
    pass


class JunctionPoint:
    pass


class Core:

    TYPES = {a: AccessPoint,
             j: JunctionPoint,
             l: LinkPoint,
        }

    def __init__(self, minimap: list, connections: list, vehicles: int):

        self.vehicles = vehicles
        self.access_points = []
        self.junction_points = []
        self.junction_queues = []
        self.points = {}

        self.nn = False
        self.__process(minimap, connections)

    def __process(self, minimap, connections):
        for code in chain.from_iterable(minimap):
            if not code:
                continue

            point = Point(code = code)
            self.points.appent(point)

            if code[0] == "a":
                point.callback = self.spawn
                self.access_points.append(point)

            if code[0] == "j":
                self.junction_points.append(point)

    def __exec_nn(self):
        pass

    def reset(self, nn):
        pass

    def spawn_vehicle(self):
        pass

    def create_links(self, code1, code2):
        pass

    def finalize(self):
        pass

    def step(self):
        pass
