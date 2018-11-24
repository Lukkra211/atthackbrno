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

juncgrrr = [[2, 2, 1, 1, 1, 1, 1, 1, 1, 3, 3, ],
            [2, 2, 1, 1, 1, 1, 1, 1, 1, 3, 3, ],
            [1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, ],
            [1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, ],
            [1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, ],
            [1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, ],
            [1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, ],
            [1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, ],
            [1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, ],
            [3, 3, 1, 1, 1, 1, 1, 1, 1, 3, 3, ],
            [3, 3, 1, 1, 1, 1, 1, 1, 1, 3, 3, ]]

juncrgrr = [[3, 3, 1, 1, 1, 1, 1, 1, 1, 2, 2, ],
            [3, 3, 1, 1, 1, 1, 1, 1, 1, 2, 2, ],
            [1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, ],
            [1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, ],
            [1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, ],
            [1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, ],
            [1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, ],
            [1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, ],
            [1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, ],
            [3, 3, 1, 1, 1, 1, 1, 1, 1, 3, 3, ],
            [3, 3, 1, 1, 1, 1, 1, 1, 1, 3, 3, ]]

juncrrgr = [[3, 3, 1, 1, 1, 1, 1, 1, 1, 3, 3, ],
            [3, 3, 1, 1, 1, 1, 1, 1, 1, 3, 3, ],
            [1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, ],
            [1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, ],
            [1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, ],
            [1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, ],
            [1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, ],
            [1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, ],
            [1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, ],
            [2, 2, 1, 1, 1, 1, 1, 1, 1, 3, 3, ],
            [2, 2, 1, 1, 1, 1, 1, 1, 1, 3, 3, ]]

juncrrrg = [[3, 3, 1, 1, 1, 1, 1, 1, 1, 3, 3, ],
            [3, 3, 1, 1, 1, 1, 1, 1, 1, 3, 3, ],
            [1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, ],
            [1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, ],
            [1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, ],
            [1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, ],
            [1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, ],
            [1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, ],
            [1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, ],
            [3, 3, 1, 1, 1, 1, 1, 1, 1, 2, 2, ],
            [3, 3, 1, 1, 1, 1, 1, 1, 1, 2, 2, ]]

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

black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)

cell_empty = 0
cell_filled = 1
cell_green = 2
cell_red = 3
cell_colors = {cell_filled: black, cell_empty: white, cell_green: green, cell_red: red}

length = 4
size = (length, length)

COLORS = [white, black, white, white]
LINK = [1, 0, 3, 0, 2, 0, 1]
OBJECTS = {"j": junction, "l": link, "a": access}


class Presenter:
    def __init__(self, connections, minimap, screensize):
        """This class will innit the functionality"""
        self._init_window(screensize)
        self.connections = connections
        self.minimap = minimap
        self.point_location = {}
        self.link_vector = {}
        self._process()

    @staticmethod
    def _init_window(screensize):
        """ This class will innit pygame a set background to white"""
        pygame.init()
        pygame.display.set_caption("Traffic Controlled By Neural Network")

        screen = pygame.display.set_mode(screensize)
        screen.fill((255, 255, 255))

    def _process(self):
        """Take minimap and connections and send then to draw"""
        for indexRow in range(len(self.minimap)):
            for indexColm in range(len(self.minimap[indexRow])):
                if not self.minimap[indexRow][indexColm]:
                    continue
                x, y = self._minimap_to_grid(self.minimap[indexRow][indexColm])
                obj = OBJECTS[self.minimap[indexRow][indexColm][0]]
                if(obj == junction):
                    side = "left"
                    if(side == "up"):
                        Presenter._draw_object(x, y, juncrgrr)
                    elif(side == "down"):
                        Presenter._draw_object(x, y, juncrrgr)
                    elif(side == "left"):
                        Presenter._draw_object(x, y, juncgrrr)
                    elif(side == "righ"):
                        Presenter._draw_object(x, y, juncrrrg)
                else:
                    Presenter._draw_object(x, y, obj)
                self.point_location[self.minimap[indexRow]
                                    [indexColm]] = (indexColm, indexRow)

        for source, dest in self.connections:
            self._process_connection(source=source, destination=dest)

    def main_loop(self, core):
        """Main loopupdates of display"""
        while True:
            core.step()
            self._redraw_links(core)
            pygame.display.flip()
            time.sleep(0.02)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit(0)

    def _redraw_links(self, core):
        """Redraw links will draw the cars"""
        for link in core.links:
            x, y, vec = self.link_vector[link.code]

            for index, cell in enumerate(link.queue):
                if cell == link.queue[index-1] and cell == 1:
                    Presenter._draw_cell(
                        x + (index * vec[0]), y + (index * vec[1]), red)

                else:
                    Presenter._draw_cell(
                        x + (index * vec[0]), y + (index * vec[1]), COLORS[cell])

    def _minimap_to_grid(self, pos_name):
        """ geting grid coordinates from name of the object"""
        for k in range(len(self.minimap)):
            for l in range(len(self.minimap[k])):
                if pos_name == self.minimap[k][l]:
                    cordx = l*41
                    cordy = k*41
                    return cordx, cordy

    @staticmethod
    def _draw_object(horizontal, vertical, array):
        """This will draw an object"""
        for hor_s, row in enumerate(array):
            for ver_s, cell in enumerate(row):
                hor = horizontal + hor_s
                ver = vertical + ver_s
                Presenter._draw_cell(hor, ver, cell_colors[cell])

    @staticmethod
    def _draw_cell(x, y, color):
        """This will draw a single cell to the screen"""
        px = x * length
        py = y * length

        rectangle = pygame.Rect((px, py), size)
        pygame.draw.rect(pygame.display.get_surface(), color, rectangle)

    def _process_connection(self, source, destination):
        """ Draw connections between the points"""
        colm, row, vect = self._get_source_info(source, destination)
        shift_x, shift_y = self._calculate_start(colm, row, vect)

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
        """ Get info of the objects"""
        source = self.point_location[code1]
        dest = self.point_location[code2]

        dest, source = source, dest
        vector = (source[0] - dest[0], dest[1] - source[1])
        if vector not in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
            print("Can't connect")
            exit(1)
        return dest[0], dest[1], vector

    def _calculate_start(self, colm, row, vector):
        """This will claculate start point of the links"""
        code = self.minimap[row][colm]
        x, y = self._minimap_to_grid(code)
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
            end_y = y + 29
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

        return x, y
