import pygame
from settings import *

def draw(screen, paddle_left, paddle_right
         , ball, score_left, score_right, font, game_state):
    pygame.draw.rect(screen, (255,255,255), (paddle_left.x, paddle_left.y, paddle_left.width, paddle_left.height))
    pygame.draw.rect(screen, (255, 255, 255), (paddle_right.x, paddle_right.y, paddle_right.width, paddle_right.height))

    if game_state == "playing" or game_state == "menu":
        pygame.draw.circle(screen, (255, 255, 255),
        (ball.x + ball.size // 2, ball.y + ball.size // 2), ball.size // 2)

    if game_state == "score_display":
        text_left = font.render(str(score_left), True, (255, 255, 255))
        text_right = font.render(str(score_right), True, (255, 255, 255))
        screen.blit(text_left, ((WIDTH / 2) - 170, 50))
        screen.blit(text_right, ((WIDTH / 2) + 150, 50))

    if game_state == "game_over":
        if score_left >= WINNING_SCORE:
            text_left_win = font.render("LEFT PLAYER WIN!", True, (255, 255, 255))
            screen.blit(text_left_win, (WIDTH // 2 - text_left_win.get_width() // 2, 200))
        elif score_right>= WINNING_SCORE:
            text_right_win = font.render("RIGHT PLAYER WIN!", True, (255, 255, 255))
            screen.blit(text_right_win, (WIDTH // 2 - text_right_win.get_width() // 2, 200))


def draw_menu(screen, font, menu_options, menu_selected):
    for index, option in enumerate(menu_options):
        y = 200 + index * 90
        if index == menu_selected:
            text_local = font.render(str(option), True, BG_COLOR)
            pygame.draw.rect(screen, TEXT_COLOR, (WIDTH / 2 - text_local.get_width() // 2 - 10, y - 5, text_local.get_width() + 20, text_local.get_height() + 10))
            screen.blit(text_local, (WIDTH / 2 - text_local.get_width() // 2, y))
        else:
            text= font.render(str(option), True, TEXT_COLOR)
            screen.blit(text, (WIDTH / 2 - text.get_width() // 2, y))