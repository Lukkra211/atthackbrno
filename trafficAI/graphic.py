import pygame
import sys
import os

access = [[0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, ],
          [0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, ],
          [1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, ],
          [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, ],
          [1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, ],
          [1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, ],
          [1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, ],
          [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, ],
          [1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, ],
          [0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, ],
          [0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, ]]

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

minimap = [['a01', 'j01', 'a02'],
           ['a03', 'j05', 'a07'],
           ['a08', 'l10', 'a12']]
connections = ['a01 - j01']

check = 1
for i in range(len(minimap)):
    for j in range(len(minimap[i])):
        if len(minimap[i]) > check:
            check = len(minimap[i])

# print(minimap[0][2])
cell_empty = 0
cell_filled = 1
black = (0, 0, 0)
white = (255, 255, 255)
cell_colors = {cell_filled: black, cell_empty: white}

length = 4
size = (length, length)
screensize = (((len(minimap)*41*4)-120), ((check*41*4)-120))
print(screensize)
# print(screensize[0],screensize[1])

"""import minimap from somewhere"""

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
                x, y = Presenter._minimap_to_grid(
                    self.minimap[indexRow][indexColm])
                Presenter._draw_object(x, y,
                                       OBJECTS[self.minimap[indexRow][indexColm][0]])
                self.point_location[self.minimap[indexRow]
                                    [indexColm]] = (indexColm, indexRow)

        for connection in self.connections:
            sorce, dest = connection.split(" - ")

            self._process_connection(source=sorce, destination=dest)

    def main_loop(self):
        pass

    def _redraw_links(self):
        pass

    @staticmethod
    def _minimap_to_grid(pos_name):
        for k in range(len(minimap)):
            for l in range(len(minimap[k])):
                #print(minimap[i][j],"-",j * 41, i * 41)
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
        pygame.display.update()

    def _process_connection(self, source, destination):
        """ Draw connections between the points"""
        colm, row, vect = self._get_source_info(source, destination)
        shift_x, shift_y = self._calculate_start(colm, row, vect)
        print(shift_x,shift_y)

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
        pygame.display.flip()

    def _get_source_info(self, code1, code2):
        """ Get info of the """
        source = self.point_location[code1]
        dest = self.point_location[code2]

        dest, source = source, dest
        print(dest, source)
        vector = (source[0] - dest[0], source[1] - dest[1])
        if vector not in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
            exit(1)
        return source[0], source[1], vector

    def _calculate_start(self, colm, row, vector):
        start_x, start_y = Presenter._minimap_to_grid(self.minimap[row][colm])
        # xy
        if vector == (0, 1):
            # up
            start_x += 2
            start_y -= 1
        elif vector == (0, -1):
            # down
            start_x += 8
            start_y += 11
        elif vector == (-1, 0):
            # left
            start_x -= 1
            start_y += 10
        elif vector == (1, 0):
            # right
            start_x += 11
            start_y += 2
        return (start_x, start_y)


Presenter(connections, minimap, None, screensize)

input()
