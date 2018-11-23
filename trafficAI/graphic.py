import pygame

COLORS = [(0, 0, 0), (255, 255, 255), (0, 0, 0), (0, 0, 0)]
LINK = [1, 0, 3, 0, 2, 0, 1]


class Presenter:
    def __init__(self):
        pass

    def _init_window(self):
        pass

    def _process(self):
        pass

    def main_loop(self):
        pass

    def _redraw_links(self):
        pass

    def _minimap_to_grid(self):
        pass

    def _draw_object(self):
        pass

    def _draw_cell(self):
        pass

    def _process_connection(self, source, destination):

        colm, row, vect = self._get_source_info(source, destination)
        x, y, step = self._calculate_start(colm, row, vect)

        forward = '{}-{}'.format(source, destination)
        backwards = '{}-{}'.format(destination, source)

        for index in range(30):
            shift_x = x
            shift_y = y

            for colm in [1, 0, 3, 0, 2, 0, 1]:
                self._draw_cell(shift_x+index, shift_y+index, COLORS[colm])

    def _get_source_info(self, code1, code2):
        source = self.point_location[code1]
        dest = self.point_location[code2]

        vector = (source[0] - dest[0], source[1] - dest[1])
        if vector not in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
            raise RuntimeError("Unexpected direction")
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
