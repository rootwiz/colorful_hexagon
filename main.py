import pygame
from pygame.locals import *
import sys
import random
import time
from Color import Color
from Hexagon import Hexagon
from HexMap import HexMap

# screen size
S_HIGHT = 500
S_WIDTH = 500

def debug(hexmap):
    hexmap.hexagons[hexmap.vertex_index[(4, 4)]].color = Color.INACTIVE_COLOR
    hexmap.hexagons[hexmap.vertex_index[(4, 4)]].active = False
    hexmap.hexagons[hexmap.vertex_index[(4, 5)]].color = Color.INACTIVE_COLOR
    hexmap.hexagons[hexmap.vertex_index[(4, 5)]].active = False
    hexmap.hexagons[hexmap.vertex_index[(5, 6)]].color = Color.INACTIVE_COLOR
    hexmap.hexagons[hexmap.vertex_index[(5, 6)]].active = False
    hexmap.hexagons[hexmap.vertex_index[(4, 6)]].color = Color.INACTIVE_COLOR
    hexmap.hexagons[hexmap.vertex_index[(4, 6)]].active = False
    hexmap.hexagons[hexmap.vertex_index[(3, 3)]].color = Color.INACTIVE_COLOR
    hexmap.hexagons[hexmap.vertex_index[(3, 3)]].active = False

    time.sleep(1)
    hexmap.draw()

def main():
    pygame.init()
    hexmap = HexMap(8)
    hexmap.draw()
    pygame.display.update()
    #debug(hexmap)

    while True:
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                click_x, click_y = event.pos
                print("clicked", event.pos)
                hex_coor = hexmap.cpos_to_ipos(click_x, click_y)
                hexmap.hexagons[hexmap.vertex_index[hex_coor]].color = Color.INACTIVE_COLOR
                hexmap.hexagons[hexmap.vertex_index[hex_coor]].active = False
                hexmap.judge_all(hex_coor[0], hex_coor[1])

            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()

if __name__ == '__main__':
    main()
