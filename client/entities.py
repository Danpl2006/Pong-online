from settings import *
import random


class Paddle:
    """Класс ракетки..."""
    def __init__(self, x, y, min_x, max_x):
        self.x = x
        self.y = y
        self.start_x = x  # запоминаем стартовое значение отдельно
        self.start_y = y
        self.min_x = min_x
        self.max_x = max_x
        self.width = PADDLE_WIDTH
        self.height = PADDLE_HEIGHT
        self.speed = PADDLE_SPEED
        self.dy = 0
        self.dx = 0

    def move_up(self):
        self.dy = -self.speed

    def move_down(self):
        self.dy = self.speed

    def move_left(self):
        self.dx = -self.speed

    def move_right(self):
        self.dx = self.speed

    def stop_y(self):
        self.dy = 0

    def stop_x(self):
        self.dx = 0

    def update(self):
        self.y += self.dy
        self.x += self.dx
        if self.y < 0:
            self.y = 0
        elif self.y > HEIGHT - self.height:
            self.y = HEIGHT - self.height

        if self.x < self.min_x:
            self.x = self.min_x
        elif self.x > self.max_x:
            self.x = self.max_x

    def reset(self):
        self.__init__(self.start_x, self.start_y, self.min_x, self.max_x)


class Ball:
    """Класс мячика..."""
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = BALL_SIZE
        self.dx = BALL_SPEED * random.choice([-1, 1])
        self.dy = BALL_SPEED * random.choice([-1, 1])


    def update(self):
        self.x += self.dx
        self.y += self.dy
        if self.y < 0:
            self.dy = -self.dy
        elif self.y + self.size > HEIGHT:
            self.dy = -self.dy

        if self.x + self.size > WIDTH:
            return "left" # забил левый игрок
        elif self.x < 0:
            return "right" # забил правый игрок
        else:
            return None


    def reset(self):
        self.__init__(WIDTH // 2,HEIGHT // 2)
