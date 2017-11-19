class GameObject:
    def __init__(self, x, y, w, h, speed=(0,0)):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.speed = speed

    @property
    def bounds(self):
        return self.x, self.y, self.w, self.h

    @property
    def left(self):
        return self.x

    @property
    def right(self):
        return self.x + self.w

    @property
    def top(self):
        return self.y

    @property
    def bottom(self):
        return self.y + self.h

    def draw(self, surface):
        pass

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def update(self):
        """"""
        if self.speed == [0, 0]:
            return

        self.move(*self.speed)
