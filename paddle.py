import pygame

import config as c
from game_object import GameObject


class Paddle(GameObject):
    def __init__(self, x, y, w, h, color, offset):
        GameObject.__init__(self, x, y, w, h)
        self.width = w
        self.height = h
        self.color = color
        self.offset = offset
        self.left_down = False
        self.right_down = False

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.bounds)

    def handle(self, key):
        if key == pygame.K_LEFT:
            self.left_down = not self.left_down
        else:
            self.right_down = not self.right_down

    def update(self):
        if self.left_down:
            dx = -(min(self.offset, self.left))
        elif self.right_down:
            dx = min(self.offset, c.screen_width - self.right)
        else:
            return

        self.move(dx, 0)