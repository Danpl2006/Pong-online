import pygame
from settings import SETTING_ROWS


def handle_input(keys, paddle_left, paddle_right):
    if keys[pygame.K_w]:
        paddle_left.move_up()
    elif keys[pygame.K_s]:
        paddle_left.move_down()
    else:
        paddle_left.stop_y()

    if keys[pygame.K_a]:
        paddle_left.move_left()
    elif keys[pygame.K_d]:
        paddle_left.move_right()
    else:
        paddle_left.stop_x()

    if keys[pygame.K_UP]:
        paddle_right.move_up()
    elif keys[pygame.K_DOWN]:
        paddle_right.move_down()
    else:
        paddle_right.stop_y()

    if keys[pygame.K_RIGHT]:
        paddle_right.move_right()
    elif keys[pygame.K_LEFT]:
        paddle_right.move_left()
    else:
        paddle_right.stop_x()


def navigate_menu(event, menu):
    if event.key == pygame.K_DOWN:
        menu.move_down()
    elif event.key == pygame.K_UP:
        menu.move_up()


def is_back(event, menu):
    return event.key == pygame.K_ESCAPE or (
                event.key == pygame.K_RETURN and menu.current == "Back")


def menu_input(event, menu, game_state):
    navigate_menu(event, menu)

    if event.key == pygame.K_RETURN:
        if menu.current == "Local Game with Friend":
            game_state = "playing"
        elif menu.current == "Local Game with Computer":
            game_state = "side_select"
        elif menu.current == "Multiplayer":
            print("in develop")
        elif menu.current == "Settings":
            game_state = "settings"
        elif menu.current == "Exit":
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