import random

import pygame

import config as c
from ball import Ball
from brick import Brick
from game import Game
from paddle import Paddle


class Breakout(Game):
    def __init__(self):
        Game.__init__(self, 'Breakout', c.screen_width, c.screen_height, c.screen_color, c.frame_rate)
        self.bricks = self.create_bricks()
        self.paddle = self.create_paddle()
        self.ball = self.create_ball()
        self.score = 0

    def create_ball(self):
        speed = (random.randint(-3, 3), 5)
        ball = Ball(c.screen_width // 2,
                    c.screen_height // 2,
                    c.ball_radius,
                    c.ball_color,
                    speed)
        self.objects.append(ball)
        return ball

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
        return paddle

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
        return bricks

    def handle_ball_collisions(self):
        def intersect(obj, ball):
            return obj.bounds.inflate(ball.diameter, ball.diameter).collidepoint(*ball.center)

        s = self.ball.speed
        if intersect(self.paddle, self.ball):
            self.ball.speed = (s[0], -s[1])

        # Hit floor
        if self.ball.top > c.screen_height:
            self.game_over = True

        # Hit ceiling
        if self.ball.top < 0:
            self.ball.speed = (s[0], -s[1])

        # Hit wall
        if self.ball.left < 0 or self.ball.right > c.screen_width:
            self.ball.speed = (-s[0], s[1])

        # Hit brick
        for brick in self.bricks:
            if intersect(brick, self.ball):
                self.bricks.remove(brick)
                self.objects.remove(brick)
                self.score += 1
                self.ball.speed = (s[0], -s[1])


    def update(self):
        self.handle_ball_collisions()
        super().update()


def main():
    Breakout().run()


if __name__ == '__main__':
    main()
