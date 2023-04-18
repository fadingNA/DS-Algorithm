import pygame
from settings import *


class Tile(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(groups)
        self.image = pygame.image.load('../../../Downloads/1 - level/graphics/tilemap/ground.png').convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
