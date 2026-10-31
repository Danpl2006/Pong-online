import pygame
from settings import *
from i18n import tr


def draw(screen, paddle_left, paddle_right,
         ball, score_left, score_right, font,
         game_state, user_settings, language):
    pygame.draw.rect(screen, user_settings.paddle_color,
                     (paddle_left.x, paddle_left.y, paddle_left.width,
                      paddle_left.height))
    pygame.draw.rect(screen, user_settings.paddle_color,
                     (paddle_right.x, paddle_right.y, paddle_right.width,
                      paddle_right.height))

    if game_state == "playing" or game_state in MENU_STATES:
        pygame.draw.circle(screen, user_settings.ball_color,
                           (ball.x + ball.size // 2, ball.y + ball.size // 2),
                           ball.size // 2)

    if game_state == "score_display":
        text_left = font.render(str(score_left), True,
                                user_settings.text_color)
        text_right = font.render(str(score_right), True,
                                 user_settings.text_color)
        screen.blit(text_left, ((WIDTH / 2) - 170, 50))
        screen.blit(text_right, ((WIDTH / 2) + 150, 50))

    if game_state == "game_over":
        if score_left >= WINNING_SCORE:
            text_left_win = font.render(tr("win.left", language), True,
                                        user_settings.text_color)
            screen.blit(text_left_win,
                        (WIDTH // 2 - text_left_win.get_width() // 2, 200))
        elif score_right >= WINNING_SCORE:
            text_right_win = font.render(tr("win.right", language), True,
                                         user_settings.text_color)
            screen.blit(text_right_win,
                        (WIDTH // 2 - text_right_win.get_width() // 2, 200))


def draw_menu(screen, font, menu, user_settings, language):
    row_height = 90
    start_y = (HEIGHT - len(menu.options) * row_height) // 2
    for index, option in enumerate(menu.options):
        y = start_y + index * row_height
        label = tr(option, language)
        if option in SETTING_ROWS:
            field, options = SETTING_ROWS[option]
            value = tr(user_settings.label(field, options), language)
            label = f"{label}: < {value} >"

        if index == menu.selected:
            text_local = font.render(label, True, user_settings.bg_color)
            pygame.draw.rect(screen, user_settings.text_color,
                             (WIDTH / 2 - text_local.get_width() // 2 - 10,
                              y - 5, text_local.get_width() + 20,
                              text_local.get_height() + 10))
            screen.blit(text_local,
                        (WIDTH / 2 - text_local.get_width() // 2, y))
        else:
            text = font.render(label, True, user_settings.text_color)
            screen.blit(text, (WIDTH / 2 - text.get_width() // 2, y))
