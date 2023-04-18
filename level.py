import pygame
from settings import *
from tile import Tile
from player import Player

class Level:
    def __init__(self):
        # get the display surface
        self.display_surface = pygame.display.get_surface()
        #sprite group setup
        self.visible_spirtes = pygame.sprite.Group()
        self.obstacble_sprites = pygame.sprite.Group()

        # sprite setpup
        self.create_map()

    def create_map(self):
        for row_index, row in enumerate(WORLD_MAP):
            for col_inde, col in enumerate(row):
                x = col_index * TILESIZE
                y = row_index * TILESIZE
                if col == 'x':
                    Tile((x,y), [self.visible_spirtes,self.obstacble_sprites])
                if col == 'p':
                    Player((x,y), [self.visible_spirtes])

    def run(self):
        # update and draw the game
        self.visible_spirtes.draw(self.display_surface)