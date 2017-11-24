import pygame
import sys

from collections import defaultdict


class Game:
    def __init__(self, caption, width, height, back_image, frame_rate):
        self.back_image = back_image
        self.frame_rate = frame_rate
        self.game_over = False
        self.objects = []
        pygame.init()
        pygame.font.init()
        self.surface = pygame.display.set_mode((width, height))
        pygame.display.set_caption(caption)
        self.clock = pygame.time.Clock()
        self.keydown_handlers = defaultdict(list)
        self.keyup_handlers = defaultdict(list)

    def update(self):
        for o in self.objects:
            o.update()

    def draw(self):
        for o in self.objects:
            o.draw(self.surface)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                for handler in self.keydown_handlers[event.key]:
                    handler(event.key)
            elif event.type == pygame.KEYUP:
                for handler in self.keydown_handlers[event.key]:
                    handler(event.key)

    def run(self):
        bg = pygame.image.load(self.back_image)
        while not self.game_over:
            self.surface.blit(bg, (0, 0))
            #self.surface.fill(self.back_color)

            self.handle_events()
            self.update()
            self.draw()

            pygame.display.update()
            self.clock.tick(self.frame_rate)
