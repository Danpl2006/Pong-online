from dataclasses import dataclass
import pygame
from settings import SETTING_ROWS


@dataclass(frozen=True)
class KeyScheme:
    up: int
    down: int
    left: int
    right: int


WASD = KeyScheme(pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d)
ARROWS = KeyScheme(pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT)


def control_paddle(keys, paddle, *schemes):
    up = any(keys[scheme.up] for scheme in schemes)
    down = any(keys[scheme.down] for scheme in schemes)
    left = any(keys[scheme.left] for scheme in schemes)
    right = any(keys[scheme.right] for scheme in schemes)

    if up:
        paddle.move_up()
    elif down:
        paddle.move_down()
    else:
        paddle.stop_y()

    if left:
        paddle.move_left()
    elif right:
        paddle.move_right()
    else:
        paddle.stop_x()


def handle_input(keys, paddle_left, paddle_right):
    control_paddle(keys, paddle_left, WASD)
    control_paddle(keys, paddle_right, ARROWS)


def navigate_menu(event, menu):
    if event.key == pygame.K_DOWN:
        menu.move_down()
    elif event.key == pygame.K_UP:
        menu.move_up()


def is_back(event, menu):
    return event.key == pygame.K_ESCAPE or (
            event.key == pygame.K_RETURN and menu.current == "back")


def menu_input(event, menu, game_state):
    navigate_menu(event, menu)

    if event.key == pygame.K_RETURN:
        if menu.current == "menu.local_friend":
            game_state = "playing"
        elif menu.current == "menu.local_computer":
            game_state = "side_select"
        elif menu.current == "menu.multiplayer":
            print("in develop")
        elif menu.current == "menu.settings":
            game_state = "settings"
        elif menu.current == "menu.exit":
            game_state = "exit"

    return game_state


def settings_input(event, menu, game_state, user_settings):
    navigate_menu(event, menu)
    if is_back(event, menu):
        game_state = "menu"

    elif (event.key in (pygame.K_LEFT, pygame.K_RIGHT)
          and menu.current in SETTING_ROWS):
        step = 1 if event.key == pygame.K_RIGHT else -1
        field, options = SETTING_ROWS[menu.current]
        user_settings.cycle(field, options, step)

    return game_state


def side_select_input(event, menu, game_state):
    navigate_menu(event, menu)
    if is_back(event, menu):
        game_state = "menu"
    elif event.key == pygame.K_RETURN:
        game_state = "playing"

    return game_state
