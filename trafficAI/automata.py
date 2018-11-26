"""
Cellular automata simulating traffic
"""

# IMPORTS
from numpy import random
import itertools
from itertools import chain


# CONSTANTS
LINK_LEN = 30
EMPTY_CELL = 0
FULL_CELL = 1

# ====================
# Transport structures
# ====================


class Link:
    """
    One directional link between two traffic points

    When two connections are pointing to LinkPoint, the self.destination is
    actually another ``Link`` instead of ``Point`` object. Thats why the Link
    objects requires ``_redirect`` method to imitate point behaviour.

    Params:
        source: traffic point that puts vehicles on the link
        destination: traffic point that receives the vehicles from this link

    Args:
        queue: line on which the vehicles are placed and moved forward

    """
    def __init__(self, source: 'Point', destination: 'Point'):
        self.code = '{}-{}'.format(source.code, destination.code)
        self.reverse_code = '{}-{}'.format(destination.code, source.code)
        self.destination = destination
        self.source = source
        self.queue = LINK_LEN * [0]
        self.stucked = 0
        self.inactive = False

    def step(self) -> None:
        """
        Moves cars forward, or forwards them to the destination point
        """

        self.stucked = 0
        self.inactive = True
        skip = False

        for i in range(LINK_LEN - 1):
            if skip or self.queue[i] == EMPTY_CELL:
                # on the checked cell there isn't a vehicle or there is one but
                # it is the one moved forward in previous step
                skip = False
                continue
            if self.queue[i + 1] == FULL_CELL:
                # the vehicle is blocked by the one forward
                self.stucked += 1
            else:
                # ahead of the vehicle is an empty spot. Move the vehicle there
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

    def reset(self) -> None:
        """
        Set the link to the initial state
        """
        self.queue = [0] * LINK_LEN
        self.stucked = 0

    def generate(self, empty_cells=1) -> bool:
        """
        Spawn new vehicle on the road

        Returns:
            (bool): True if generated successfully, False otherwise

        """
        empty = self.is_empty(empty_cells)
        if empty:
            self.queue[0] = 1
            self.inactive = False
        return empty

    def _redirect(self, *_) -> bool:
        """
        If theres a space for a vehicle, generate it

        Returns:
            (bool): True if redirected successfully, False otherwise

        """
        return self.generate()

    def is_empty(self, span: int = 1) -> bool:
        """
        Return true if selected number of spaces are empty, false otherwise

        Params:
            span: how much space should be empty

        """

        return not any(self.queue[:span])


class LinkPoint:
    """
    Point that is actually doing pretty much nothing besides connecting the
    links to each other. The links are actually not connected to the LinkPoint
    but to the other link in the way.

    Params:
        code: name of the traffic point

    Args:
        incoming: list of incoming links
        outcoming: list of outcoming links
        register: number of registered links, should be exactly 4

    """
    def __init__(self, code: str):
        self.code = code
        self.incomming = []
        self.outcomming = []
        self.register = 0

    def register_links(self, incomming: Link, outcomming: Link) -> None:
        self.incomming.append(incomming)
        self.outcomming.append(outcomming)
        self.register += 2

    def lock(self) -> None:
        try:
            self.incomming[0].destination = self.outcomming[1]
            self.incomming[1].destination = self.outcomming[0]
        except IndexError as e:
            raise RuntimeError(e, self)

        if self.register != 4:
            raise RuntimeError('LinkPoint got links instead of 4')


# ==================
# Logical structures
# ==================


class Point:
    """
    Parent of all points that take cares about the logic of the cars.
    """

    def __init__(self, code):
        self.code = code
        self.incomming_cicle = None
        self.outcomming_cicle = None
        self.incomming = []
        self.outcomming = []

    def register_links(self, incomming: Link, outcomming: Link) -> None:
        """
        To notify the point, that there's a link to it.
        """
        self.incomming.append(incomming)
        self.outcomming.append(outcomming)

    def lock(self) -> None:
        """
        Prepare the point for its function. All data should be already in place
        """
        self.incomming_cicle = itertools.cycle(self.incomming)
        self.outcomming_cicle = itertools.cycle(self.outcomming)

    def _redirect(self, link) -> bool:
        """
        The method tries to process the incomming vehicle

        Params:
            link: the link which wants one of its vehicle to be processed by
                the point, so link can forget the vehicle

        Returns:
            (bool): True if generated successfully, False otherwise

        """
        raise RuntimeError('Method not implement yet')


class AccessPoint(Point):
    """
    Class that symbolize the border of our traffic area
    """

    def __init__(self, code):
        super().__init__(code)
        self.callback = None
        self.to_generate = 0
        self.inactive = False
        self.skip = False

    def _redirect(self, link) -> bool:
        """
        There is no redirection here. The vehicle just dissapears since it gets
        out of the traffic map. It is assumed that traffic beyond the system is
        perfect, therefore the point cannot be blocked. The controller have to
        be notified thought so new vehicle will be spawned to balance the total
        number of vehicles.
        """
        self.callback()
        return True

    def generate(self) -> None:
        """
        Increase the counter of vehicles, that should be spawned
        """
        self.to_generate += 1

    def step(self) -> None:
        """
        Try to generate vehicle
        """

        if self.skip or self.to_generate == 0:
            self.skip = False
            return
        self.inactive = False

        for _ in range(len(self.outcomming)):
            possible_link = next(self.outcomming_cicle)
            if possible_link.generate():
                self.to_generate -= 1
                self.skip = True
                return
        self.inactive = True

    def reset(self) -> None:
        """
        Set the point to the initial state
        """

        self.to_generate = 0
        self.inactive = False
        self.skip = False


class JunctionPoint(Point):
    """
    Junction which may connect more than two connections. At the time only one
    incoming link isn't blocked.

    Args:
        open: maps outcoming links to boolean which determine if the link is
            closed. If true, vehicles pass, otherwise they are blocked.

    """
    def __init__(self, code):
        super().__init__(self)
        self.code = code

    def _redirect(self, link) -> bool:

        # if self.open[link.code]:
        if True:  # self.links
            for _ in range(len(self.outcomming)):
                possible_link = next(self.outcomming_cicle)
                if possible_link.code != link.reverse_code and possible_link._redirect():
                    return True
                else:
                    continue
        else:
            return False


class Core:
    """
    Initialize, connects and finally control traffic objects

    Note:
        The ID belonging to traffic point is called 'code'. The code is string
        containing one letter and number. The letter specifies type of traffic
        point

        Traffic point character identificator:
            a - Access point
            j - Junction point
            l - Link point

        It's important do distinguish the link, which is one-way queue from one
        traffic point to the another, and connection, which is made of two
        links in order to provide two-directional flow.

    Params:
        TYPES Dict[str, Point]: mapps character identifier to the
            initialization method of the related class

        junction_points List[JunctionPoint]: list of junctions
        junction_queues Link[Link]: list of links that heads to JunctionPoints
        access_points List[AccessPoint]: list of points generating vehicles
        points Dict[str, Point]: list of all points, access points included
        links List[Link]: list of all links between points

        nn Callable[[List[List[int]]], List[int]]=None: represents the
            neural network
        vehicles int: number of vehicles in the system simultaneously
        step int: counter of steps
        vehicles: number of vehicles in the system simultaneously


    """

    def __init__(self, minimap: list, connections: list, vehicles: int):

        self.TYPES = {"a": AccessPoint,
                      "j": JunctionPoint,
                      "l": LinkPoint,
                      }
        self.vehicles = vehicles
        self.access_points = []
        self.junction_points = []
        self.junction_queues = []
        self.points = {}
        self.links = []

        self.nn = False
        self.step_no = 0
        self.__process(minimap, connections)

    def __process(self, minimap, connections) -> None:
        """
        Process given minimap and links between the points

        Args:
            minimap: 2D map of traffic points
            connections: connections between traffic points


        """

        for code in chain.from_iterable(minimap):
            if not code:
                continue

            point = self.TYPES[code[0]](code=code)
            self.points[code] = point

            if code[0] == "a":
                point.callback = self.spawn_vehicle
                self.access_points.append(point)

            if code[0] == "j":
                self.junction_points.append(point)

        for connection in connections:
            self.create_links(*connection)
        self.finalize()

    def reset(self, nn=None) -> None:
        """
        Set the system to the initial state

        Since the reset is used mainly for the training of different
        NN, the method can also be used to inject the nn

        Args:
            nn: neural network to be used

        """
        self.nn = nn
        for link in self.links:
            link.reset()
        for point in self.access_points:
            point.reset()

    def spawn_vehicle(self) -> None:
        """
        Spawn one vehicle to the map

        This function is called at the __init__ of the controler and also by
        access points as a callback when vehicle arrived to it.
        """
        random.choice(self.access_points).generate()

    def create_links(self, code1: str, code2: str) -> None:
        """
        Create links between given points

        Two contradictory links are created. These links are registered to each
        traffic point and added to list of links.

        Links that heads into JunctionPoints are added to
        ``self.junction_queues``

        Args:
            code1: The code of first traffic point
            code2: The code of second traffic point

        """
        point1 = self.points[code1]
        point2 = self.points[code2]
        link1 = Link(source=point1, destination=point2)
        link2 = Link(source=point2, destination=point1)

        self.links.extend((link1, link2))
        if code1[0] == "j":
            self.junction_queues.append(point2)
        if code2[0] == "j":
            self.junction_queues.append(point1)

        point1.register_links(incomming=link2, outcomming=link1)
        point2.register_links(incomming=link1, outcomming=link2)

    def finalize(self) -> None:
        """
        Make final initialization which need all data to be set

        The junctions and links are sorted by code. Because they are related to
        the neural network, they need to stay in the same order. By sorting
        these objects, even when the YAML file changes in a way, that does not
        change the simulation environment, e. g. swapping names in the
        connection definition, the network will still work.

        Also tells traffic points that they can perform their final
        initialization since they finally have all data needed.
        """

        self.links.sort(key=lambda link: link.code)
        self.access_points.sort(key=lambda point: point.code)
        for point in self.points.values():
            point.lock()

        for _ in range(self.vehicles):
            self.spawn_vehicle()

    def step(self) -> None:
        """
        Perform one step

        Every ``EVALUATE_STEP`` the nn will process the data
        """
        for link in self.links:
            link.step()

        for access_point in self.access_points:
            access_point.step()
