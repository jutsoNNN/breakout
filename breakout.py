import random

import pygame
import config as c
from game import Game
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

        if self.x < 0 or self.right > c.screen_width:
            print(dx)
        self.move(dx, 0)


class Ball(GameObject):
    def __init__(self, x, y, r, color, speed):
        GameObject.__init__(self, x, y, r * 2, r * 2, speed)
        self.radius = r
        self.color = color

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (self.x, self.y), self.radius)


class Brick(GameObject):
    def __init__(self, x, y, w, h, color):
        GameObject.__init__(self, x, y, w, h)
        self.width = w
        self.height = h
        self.color = color

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.bounds)


class Breakout(Game):
    def __init__(self):
        Game.__init__(self, c.screen_width, c.screen_height, c.screen_color, c.frame_rate)
        self.bricks = self.create_bricks()
        self.paddle = self.create_paddle()
        self.ball = self.create_ball()

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

    def update(self):
        def intersect(paddle, ball):
            if ball.bottom < paddle.top:
                return False
            if ball.right < paddle.left:
                return False
            if ball.left > paddle.right:
                return False
            return True

        if intersect(self.paddle, self.ball):
            s = self.ball.speed
            self.ball.speed = (s[0], s[1] * -1)
        super().update()


def main():
    Breakout().run()


if __name__ == '__main__':
    main()
