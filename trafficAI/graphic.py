import pygame
import sys
import os

access =   [[0,0,1,1,1,1,1,1,1,0,0,],
            [0,1,1,0,0,0,0,0,1,1,0,],
            [1,1,0,0,0,0,0,0,0,1,1,],
            [1,0,0,0,0,1,0,0,0,0,1,],
            [1,0,0,0,1,1,1,0,0,0,1,],
            [1,0,0,1,1,1,1,1,0,0,1,],
            [1,0,0,0,1,1,1,0,0,0,1,],
            [1,0,0,0,0,1,0,0,0,0,1,],
            [1,1,0,0,0,0,0,0,0,1,1,],
            [0,1,1,0,0,0,0,0,1,1,0,],
            [0,0,1,1,1,1,1,1,1,0,0,]]

junction = [[1,1,1,1,1,1,1,1,1,1,1,],
            [1,1,1,1,1,1,1,1,1,1,1,],
            [1,1,1,1,1,1,1,1,1,1,1,],
            [1,1,1,0,0,0,0,0,1,1,1,],
            [1,1,1,0,1,1,1,0,1,1,1,],
            [1,1,1,0,1,1,1,0,1,1,1,],
            [1,1,1,0,1,1,1,0,1,1,1,],
            [1,1,1,0,0,0,0,0,1,1,1,],
            [1,1,1,1,1,1,1,1,1,1,1,],
            [1,1,1,1,1,1,1,1,1,1,1,],
            [1,1,1,1,1,1,1,1,1,1,1,]]

link     = [[0,0,0,0,0,0,0,0,0,0,0,],
            [0,0,0,0,0,0,0,0,0,0,0,],
            [0,0,1,1,1,1,1,1,1,0,0,],
            [0,0,1,0,0,0,0,0,1,0,0,],
            [0,0,1,0,0,1,0,0,1,0,0,],
            [0,0,1,0,1,1,1,0,1,0,0,],
            [0,0,1,0,0,1,0,0,1,0,0,],
            [0,0,1,0,0,0,0,0,1,0,0,],
            [0,0,1,1,1,1,1,1,1,0,0,],
            [0,0,0,0,0,0,0,0,0,0,0,],
            [0,0,0,0,0,0,0,0,0,0,0,]]

minimap =  [['a01', 'j01', 'a02'],
            ['a03', 'j05', 'a07'],
            ['a08', 'j10', 'a12']]

check = 1
for i in range(len(minimap)):
    for j in range(len(minimap[i])):
        if len(minimap[i]) > check:
            check = len(minimap[i])

#print(minimap[0][2])
cell_empty = 0
cell_filled = 1
black = (0,0,0)
white = (255,255,255)
cell_colors = {cell_filled: black,cell_empty: white}

length = 4
size = (length, length)
screensize = (((len(minimap)*41)-30), ((check*41)-30))
#print(screensize[0],screensize[1])

"""import minimap from somewhere"""

class Presenter:
    def __init__(self):
        pass

    @staticmethod
    def _init_window(screensize):
        pygame.init()
        pygame.display.set_caption("something")

        screen = pygame.display.set_mode(screensize)
        screen.fill((255, 255, 255))

    def process(self):
        pass

    def main_loop(self):
        pass

    def _redraw_links(self):
        pass

    @staticmethod
    def _minimap_to_grid(pos_name):
        for i in range(len(minimap)):
            for j in range(len(minimap[i])):
                #print(minimap[i][j],"-",j * 41, i * 41)
                if pos_name == minimap[i][j]:
                    cordx = j*41
                    cordy = i*41
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

    def _process_connection(self):
        pass

    def _get_source_info(self):
        pass

    def _calculate_start(self):
        pass


#Presenter._init_window(screensize)
Presenter._minimap_to_grid('j10')
#Presenter._draw_object(0, 0, access)
input()

