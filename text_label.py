import pygame

import config as c
from game_object import GameObject

class TextLabel:
    def __init__(self, x, y, text_func, color, font_name, font_size):
        self.pos = (x, y)
        self.text_func = text_func
        self.color = color
        self.font = pygame.font.SysFont(font_name, font_size)

    def draw(self, surface):
        text_surface = self.font.render(self.text_func(), False, self.color)
        surface.blit(text_surface, self.pos)

    def update(self):
        pass
