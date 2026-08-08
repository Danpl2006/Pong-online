import pygame


def draw(screen, paddle_left, paddle_right, ball):
    pygame.draw.rect(screen, (255,255,255), (paddle_left.x, paddle_left.y, paddle_left.width, paddle_left.height))
    pygame.draw.rect(screen, (255, 255, 255), (paddle_right.x, paddle_right.y, paddle_right.width, paddle_right.height))
    pygame.draw.circle(screen, (255, 255, 255), (ball.x + ball.size // 2, ball.y + ball.size // 2), ball.size // 2)