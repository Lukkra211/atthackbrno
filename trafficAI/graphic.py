import pygame

COLORS = [(0, 0, 0), (255, 255, 255), (0, 0, 0), (0, 0, 0)]
LINK = [1, 0, 3, 0, 2, 0, 1]
OBJECTS = {}


class Presenter:
    def __init__(self, connections, minimap, core):
        self.connections = connections
        self.core = core
        self.minimap = minimap
        self._process()
        self.point_location = {}

    def _init_window(self):
        pass

    def _process(self):
        for indexRow in range(len(self.minimap)):
            for indexColm in range(len(self.minimap[indexRow])):
                self._draw_object(indexRow, indexColm,
                                  OBJECTS[self.minimap[indexRow][indexColm][0]])
                self.point_location[self.minimap[indexRow]
                                    [indexColm]] = (indexRow, indexColm)

        for row in self.connections:
            for connection in row:
                sorce, dest = connection.split(" - ")
                self._process_connection(source=sorce, destination=dest)

    def main_loop(self):
        pass

    def _redraw_links(self):
        pass

    def _minimap_to_grid(self, code):
        pass

    def _draw_object(self):
        pass

    def _draw_cell(self):
        pass

    def _process_connection(self, source, destination):
        """ Draw connections between the points"""
        colm, row, vect = self._get_source_info(source, destination)
        shift_x, shift_y = self._calculate_start(colm, row, vect)

        forward = '{}-{}'.format(source, destination)
        backwards = '{}-{}'.format(destination, source)

        for index in range(30):
            for i in range(len(LINK)):
                if vect == (0, -1):
                    # up
                    self._draw_cell(shift_x+i, shift_y -
                                    index, COLORS[LINK[colm]])
                elif vect == (0, 1):
                    # down
                    self._draw_cell(shift_x-i, shift_y +
                                    index, COLORS[LINK[colm]])
                elif vect == (1, 0):
                    # left
                    self._draw_cell(shift_x-index, shift_y +
                                    i, COLORS[LINK[colm]])
                elif vect == (-1, 0):
                    # right
                    self._draw_cell(shift_x+index, shift_y +
                                    i, COLORS[LINK[colm]])
        pygame.display.flip()

    def _get_source_info(self, code1, code2):
        """ Get info of the """
        source = self.point_location[code1]
        dest = self.point_location[code2]

        vector = (source[0] - dest[0], source[1] - dest[1])
        if vector not in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
            exit(1)
        return source[0], source[1], vector

    def _calculate_start(self, colm, row, vector):
        start_x, start_y = self._minimap_to_grid(row, colm)
        # xy
        if vector == (0, -1):
            # up
            start_x += 2
            start_y -= 1
        elif vector == (0, 1):
            # down
            start_x += 10
            start_y += 11
        elif vector == (1, 0):
            # left
            start_x -= 1
            start_y += 10
        elif vector == (-1, 0):
            # right
            start_x += 11
            start_y += 1
        return (start_x, start_y)
