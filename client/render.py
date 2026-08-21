import pygame
from settings import *

def draw(screen, paddle_left, paddle_right
         , ball, score_left, score_right, font, game_state):
    pygame.draw.rect(screen, (255,255,255), (paddle_left.x, paddle_left.y, paddle_left.width, paddle_left.height))
    pygame.draw.rect(screen, (255, 255, 255), (paddle_right.x, paddle_right.y, paddle_right.width, paddle_right.height))
    if game_state == "playing":
        pygame.draw.circle(screen, (255, 255, 255),
        (ball.x + ball.size // 2, ball.y + ball.size // 2), ball.size // 2)
    if game_state == "score_display":
        text_left = font.render(str(score_left), True, (255, 255, 255))
        text_right = font.render(str(score_right), True, (255, 255, 255))
        screen.blit(text_left, ((WIDTH / 2) - 170, 230))
        screen.blit(text_right, ((WIDTH / 2) + 150, 230))
    if game_state == "game_over":
        if score_left >= WINNING_SCORE:
            text_left_win = font.render("LEFT PLAYER WIN!", True, (255, 255, 255))
            screen.blit(text_left_win, (WIDTH // 2 - text_left_win.get_width() // 2, 200))
        elif score_right>= WINNING_SCORE:
            text_right_win = font.render("RIGHT PLAYER WIN!", True, (255, 255, 255))
            screen.blit(text_right_win, (WIDTH // 2 - text_right_win.get_width() // 2, 200))
