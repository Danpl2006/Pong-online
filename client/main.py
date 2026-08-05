import pygame

from settings import *

# Инициализация
pygame.init()

# Размер Экрана
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Заголовок экрана
pygame.display.set_caption("Pong-online")

# Ограничитель кадров
clock = pygame.time.Clock()

# Главный цикл игры
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    screen.fill(BG_COLOR)
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()

