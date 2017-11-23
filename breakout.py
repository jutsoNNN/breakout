import random

import pygame
from pygame.rect import Rect

import config as c
from ball import Ball
from brick import Brick
from game import Game
from paddle import Paddle
from text_label import TextLabel


class Breakout(Game):
    def __init__(self):
        Game.__init__(self, 'Breakout', c.screen_width, c.screen_height, c.screen_color, c.frame_rate)
        self.score = 0
        self.lives = c.initial_lives
        self.create_bricks()
        self.create_paddle()
        self.create_ball()
        self.create_labels()

    def create_labels(self):
        self.score_label = TextLabel(c.score_offset,
                                     c.status_offset_y,
                                     lambda: f'SCORE: {self.score}',
                                     c.BLUE,
                                     c.font_name,
                                     c.font_size)
        self.objects.append(self.score_label)
        self.lives_label = TextLabel(c.lives_offset,
                                    c.status_offset_y,
                                    lambda: f'LIVES: {self.lives}',
                                    c.BLUE,
                                    c.font_name,
                                    c.font_size)
        self.objects.append(self.lives_label)

    def create_ball(self):
        speed = (random.randint(-3, 3), 5)
        self.ball = Ball(c.screen_width // 2,
                         c.screen_height // 2,
                         c.ball_radius,
                         c.ball_color,
                         speed)
        self.objects.append(self.ball)

    def create_paddle(self):
        paddle = Paddle((c.screen_width - c.paddle_width) // 2,
                        c.screen_height - c.paddle_height * 2,
                        c.paddle_width,
                        c.paddle_height,
                        c.paddle_color,
                        c.paddle_speed)
        self.objects.append(paddle)
        self.keydown_handlers[pygame.K_LEFT].append(paddle.handle)
        self.keydown_handlers[pygame.K_RIGHT].append(paddle.handle)
        self.keyup_handlers[pygame.K_LEFT].append(paddle.handle)
        self.keyup_handlers[pygame.K_RIGHT].append(paddle.handle)
        self.paddle = paddle

    def create_bricks(self):
        w = c.brick_width
        h = c.brick_height
        brick_count = c.screen_width // (w + 1)
        offset_x = (c.screen_width - brick_count * (w + 1)) // 2

        bricks = []
        for row in range(c.row_count):
            for col in range(brick_count):
                brick = Brick(offset_x + col * (w + 1),
                              c.offset_y + row * (h + 1),
                              w,
                              h,
                              c.RED)
                self.objects.append(brick)
                bricks.append(brick)
        self.bricks = bricks

    def handle_ball_collisions(self):
        def intersect(obj, ball):
            edges = dict(left=Rect(obj.left, obj.top, 1, obj.height),
                         right=Rect(obj.right, obj.top, 1, obj.height),
                         top=Rect(obj.left, obj.top, obj.width, 1),
                         bottom=Rect(obj.left, obj.bottom, obj.width, 1))
            collisions = set(edge for edge, rect in edges.items() if ball.bounds.colliderect(rect))
            if not collisions:
                return None

            if len(collisions) == 1:
                return list(collisions)[0]

            if 'top' in collisions:
                if ball.centery >= obj.top:
                    return 'top'
                if ball.centerx < obj.left:
                    return 'left'
                else:
                    return 'right'

            if 'bottom' in collisions:
                if ball.centery >= obj.bottom:
                    return 'bottom'
                if ball.centerx < obj.left:
                    return 'left'
                else:
                    return 'right'

        s = self.ball.speed
        edge = intersect(self.paddle, self.ball)
        if edge == 'top':
            self.ball.speed = (s[0], -s[1])
        elif edge in ('left', 'right'):
            self.ball.speed = (-s[0], s[1])

        # Hit floor
        if self.ball.top > c.screen_height:
            self.lives -= 1
            if self.lives == 0:
                self.game_over = True
            else:
                self.create_ball()

        # Hit ceiling
        if self.ball.top < 0:
            self.ball.speed = (s[0], -s[1])

        # Hit wall
        if self.ball.left < 0 or self.ball.right > c.screen_width:
            self.ball.speed = (-s[0], s[1])

        # Hit brick
        for brick in self.bricks:
            edge = intersect(brick, self.ball)
            if not edge:
                continue
            self.bricks.remove(brick)
            self.objects.remove(brick)
            self.score += 1

            if edge in ('top', 'bottom'):
                self.ball.speed = (s[0], -s[1])
            else:
                self.ball.speed = (-s[0], s[1])

    def update(self):
        self.handle_ball_collisions()
        super().update()


def main():
    Breakout().run()


if __name__ == '__main__':
    main()
