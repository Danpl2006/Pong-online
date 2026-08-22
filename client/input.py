import pygame


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


def menu_input(event, menu_options, menu_selected, game_state):
    if event.key == pygame.K_DOWN:
        if menu_selected < len(menu_options) - 1:
            menu_selected += 1

    elif event.key == pygame.K_UP:
        if menu_selected > 0:
            menu_selected -= 1

    elif event.key == pygame.K_RETURN:
        if menu_options[menu_selected] == "Local Game":
            game_state = "playing"
        elif menu_options[menu_selected] == "Multiplayer":
            print("in develop")  # заглушка
        elif menu_options[menu_selected] == "Settings":
            print("in develop")
        elif menu_options[menu_selected] == "Exit":
            game_state = "exit"

    return menu_selected, game_state
