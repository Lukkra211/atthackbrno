import pygame
import time
from automata import Core

access = [[0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, ],
          [1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, ],
          [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, ],
          [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, ],
          [1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, ],
          [1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, ],
          [1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, ],
          [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, ],
          [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, ],
          [1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, ],
          [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, ]]

junction = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, ],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, ],
            [1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, ],
            [1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, ],
            [1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, ],
            [1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, ],
            [1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, ],
            [1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, ],
            [1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, ],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, ],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, ]]

link = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
        [0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, ],
        [0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, ],
        [0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, ],
        [0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, ],
        [0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, ],
        [0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, ],
        [0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, ],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ]]

minimap = [['a01', 'l04', 'a02'],
           ['a03', '', 'a04']]
connections = ['a03-a01', 'a01-l04', 'l04-a02', 'a02-a04']
connectionsForCore = []

for connection in connections:
    connectionsForCore.append(connection.split("-"))

check = 1

for i in range(len(minimap)):
    for j in range(len(minimap[i])):
        if len(minimap[i]) > check:
            check = len(minimap[i])


black = (0, 0, 0)
white = (255, 255, 255)

cell_empty = 0
cell_filled = 1
cell_colors = {cell_filled: black, cell_empty: white}

length = 4
size = (length, length)

screensize = ((check*164)-120, (len(minimap)*164)-120)

COLORS = [white, black, white, white]
LINK = [1, 0, 3, 0, 2, 0, 1]
OBJECTS = {"j": junction, "l": link, "a": access}


class Presenter:
    def __init__(self, connections, minimap, core, screensize):
        """This class will visualize the map and cars"""
        self._init_window(screensize)
        self.connections = connections
        self.core = core
        self.minimap = minimap
        self.point_location = {}
        self.link_vector = {}
        self._process()

    @staticmethod
    def _init_window(screensize):
        pygame.init()
        pygame.display.set_caption("Traffic Controled By Neural Network")

        screen = pygame.display.set_mode(screensize)
        screen.fill((255, 255, 255))

    def _process(self):
        for indexRow in range(len(self.minimap)):
            for indexColm in range(len(self.minimap[indexRow])):
                if not self.minimap[indexRow][indexColm]:
                    continue
                x, y = Presenter._minimap_to_grid(
                    self.minimap[indexRow][indexColm])
                Presenter._draw_object(x, y,
                                       OBJECTS[self.minimap[indexRow][indexColm][0]])
                self.point_location[self.minimap[indexRow]
                                    [indexColm]] = (indexColm, indexRow)

        for connection in self.connections:
            sorce, dest = connection.split("-")
            self._process_connection(source=sorce, destination=dest)

    def main_loop(self, core):
        while True:
            core.step()

            self._redraw_links(core)
            pygame.display.flip()
            time.sleep(0.2)

    def _redraw_links(self, core):
        for link in core.links:
            x, y, vec = self.link_vector[link.code]

            for index, cell in enumerate(link.queue):
                Presenter._draw_cell(
                    x + (index * vec[0]), y + (index * vec[1]), COLORS[cell])

    def _minimap_to_grid(pos_name):
        for k in range(len(minimap)):
            for l in range(len(minimap[k])):
                if pos_name == minimap[k][l]:
                    cordx = l*41
                    cordy = k*41
                    return cordx, cordy

    @staticmethod
    def _draw_object(horizontal, vertical, array):
        for hor_s, row in enumerate(array):
            for ver_s, cell in enumerate(row):
                hor = horizontal + hor_s
                ver = vertical + ver_s
                Presenter._draw_cell(hor, ver, cell_colors[cell])

    @staticmethod
    def _draw_cell(x, y, color):
        px = x * length
        py = y * length

        rectangle = pygame.Rect((px, py), size)
        pygame.draw.rect(pygame.display.get_surface(), color, rectangle)

    def _process_connection(self, source, destination):
        """ Draw connections between the points"""
        colm, row, vect = self._get_source_info(source, destination)
        shift_x, shift_y = self._calculate_start(colm, row, vect)

        forward = '{}-{}'.format(source, destination)
        backwards = '{}-{}'.format(destination, source)

        for index in range(30):
            for i in range(len(LINK)):
                if vect == (0, 1):
                    # up
                    Presenter._draw_cell(shift_x+i, shift_y -
                                         index, COLORS[LINK[i]])
                elif vect == (0, -1):
                    # down
                    Presenter._draw_cell(shift_x-i, shift_y +
                                         index, COLORS[LINK[i]])
                elif vect == (-1, 0):
                    # left
                    Presenter._draw_cell(shift_x-index, shift_y +
                                         i, COLORS[LINK[i]])
                elif vect == (1, 0):
                    # right
                    Presenter._draw_cell(shift_x+index, shift_y +
                                         i, COLORS[LINK[i]])

    def _get_source_info(self, code1, code2):
        """ Get info of the """
        source = self.point_location[code1]
        dest = self.point_location[code2]

        dest, source = source, dest
        vector = (source[0] - dest[0], dest[1] - source[1])
        if vector not in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
            print("Can't connect")
            exit(1)
        return dest[0], dest[1], vector

    def _calculate_start(self, colm, row, vector):
        code = self.minimap[row][colm]
        x, y = Presenter._minimap_to_grid(code)
        # xy
        if vector == (0, 1):
            # up
            x += 2
            y -= 1

            start_x = x + 2
            start_y = y
            vec = (0, -1)
            end_x = start_x + 2
            end_y = y - 29
            destcode = self.minimap[row-1][colm]

        elif vector == (0, -1):
            # down
            x += 8
            y += 11

            start_x = x - 2
            start_y = y
            vec = (0, 1)
            end_x = start_x - 2
            end_y = y + 30
            destcode = self.minimap[row+1][colm]

        elif vector == (-1, 0):
            # left
            x -= 1
            y += 2

            start_x = x
            start_y = y + 4
            vec = (-1, 0)
            end_x = x - 29
            end_y = start_y - 2
            destcode = self.minimap[row][colm-1]

        elif vector == (1, 0):
            # right
            x += 11
            y += 2

            start_x = x
            start_y = y+2
            end_x = x + 29
            end_y = start_y + 2
            vec = (1, 0)
            destcode = self.minimap[row][colm+1]

        forward_str = code + "-" + destcode
        backward_str = destcode + "-" + code

        self.link_vector[forward_str] = (start_x, start_y, vec)
        self.link_vector[backward_str] = (end_x, end_y, (-vec[0], -vec[1]))
        return (x, y)


def main():
    core = Core(minimap, connectionsForCore, 5)
    core.spawn_vehicle()
    presenter = Presenter(connections, minimap, core, screensize)
    presenter.main_loop(core)

    input()


if __name__ == "__main__":
    main()
