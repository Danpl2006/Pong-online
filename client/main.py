import pygame
from settings import *
from entities import Paddle, Ball
from render import  draw
from input import handle_input
from collisions import check_paddle_collision

# Инициализация
pygame.init()

# Размер Экрана
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Заголовок экрана
pygame.display.set_caption("Pong-online")

# Ограничитель кадров
clock = pygame.time.Clock()

# Экземпляры классов
paddle_left = Paddle(0, HEIGHT // 2 - PADDLE_HEIGHT // 2)
paddle_right = Paddle(WIDTH - PADDLE_WIDTH,HEIGHT // 2 - PADDLE_HEIGHT // 2)
ball = Ball(WIDTH // 2,HEIGHT // 2)

# Главный цикл игры
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    handle_input(keys, paddle_left, paddle_right)

    screen.fill(BG_COLOR)
    paddle_left.update()
    paddle_right.update()
    check_paddle_collision(ball, paddle_left)
    check_paddle_collision(ball, paddle_right)
    ball.update()


    draw(screen, paddle_left, paddle_right, ball)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()

