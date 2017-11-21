import pygame

from game_object import GameObject


class Brick(GameObject):
    def __init__(self, x, y, w, h, color):
        GameObject.__init__(self, x, y, w, h)
        self.width = w
        self.height = h
        self.color = color

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.bounds)