import numpy

LINK_LEN = 30
EMPTY_CELL = 0
FULL_CELL = 1

class Link:
    def __init__(self, source: 'Point', destination: 'Point'):
        self.code = '{}-{}'.format(source.code, destination.code)
        self.reverse_code = '{}-{}'.format(destination.code, source.code)
        self.source = source
        self.destination = destination
        self.queue = LINK_LEN * [0]
        self.stucked = 0
        self.inactive = False

    def step(self):
        self.stucked = 0
        self.inactive = True
        skip = False

        for i in range(LINK_LEN - 1):
            if skip or self.queue[i] == EMPTY_CELL:
                skip = False
                continue
            if self.queue[i + 1] == FULL_CELL:
                    self.stucked += 1
            else:
                skip = True
                self.inactive = False
                self.queue[i] = 0
                self.queue[i + 1] = 1

        if self.queue[-1] == FULL_CELL:
            if self.destination._redirect(self):
                self.queue[-1] = 0
                self.inactive = False
            else:
                self.stucked += 1

    def reset(self):
        self.queue = [0] * LINK_LEN
        self.stucked = 0

    def generate(self, empty_cells=1):
        empty = self.si_empty(empty_cells)
        if empty:
            self.queue[0] = 1
            self.inactive = False
        return empty

    def _redirect(self, *_):
        return self.generate()

    def si_empty(self, span: int = 1):
        return not any(self.queue[:span])


class LinkPoint:
    pass


class Point:
        pass


class AccessPoint:
    pass


class JunctionPoint:
    pass


class Core:
    pass
