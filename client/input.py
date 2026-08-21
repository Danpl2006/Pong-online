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