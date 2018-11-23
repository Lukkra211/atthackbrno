import pygame


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

        src, dest, vect = self._get_source_info(source, dest)
        

    def _get_source_info(self, code1, code2):
        source = self.point_location[code1]
        dest = self.point_location[code2]

        vector = (source[0] - dest[0], source[1] - dest[1])
        if vector not in [(0,1),(1,0),(-1,0),(0,-1)]:
            raise RuntimeError("Unexpected direction")
        return source[0], source[1], vector

    def _calculate_start(self):
        pass
