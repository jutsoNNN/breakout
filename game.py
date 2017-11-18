import pygame
import config


class Game:
    def __init__(self):
        self.game_over = False
        self.objects = []


    def Run(self):
        while not self.game_over:
