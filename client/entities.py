from settings import *
import random


class Paddle:

    """Класс ракетки..."""
    def __init__(self, x, y,):
        self.x = x
        self.y = y
        self.width = PADDLE_WIDTH
        self.height = PADDLE_HEIGHT
        self.speed = PADDLE_SPEED
        self.dy = 0

    def move_up(self):
        self.dy = -self.speed

    def move_down(self):
        self.dy = self.speed

    def stop(self):
        self.dy = 0

    def update(self):
        self.y += self.dy
        if self.y < 0:
            self.y = 0
        elif self.y > HEIGHT - self.height:
            self.y = HEIGHT - self.height

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
