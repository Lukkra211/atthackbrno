import pygame

length = int(os.environment.get('length'), 3)
size = (length, length)

class Presenter:
    def __init__(self):
        pass

    @staticmethod
    def _init_window():
        pygame.init()
        pygame.display.set_caption("something")

        screen = pygame.display.set_mode((200, 200))
        screen.fill(255, 255, 255)
        pygame.display.flip()

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

    @staticmethod
    def _draw_cell(x, y, color):
        px = x * length
        py = y * length

        rectangle = pygame.rect((px, py), size)
        pygame.draw.rect(pygame.display.get_surface(), color, rectangle)

    def _process_connection(self):
        pass

    def _get_source_info(self):
        pass

    def _calculate_start(self):
        pass




