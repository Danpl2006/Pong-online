import pygame


def handle_input(keys, paddle_left, paddle_right):
    if keys[pygame.K_w]:
        paddle_left.move_up()
    elif keys[pygame.K_s]:
        paddle_left.move_down()
    else:
        paddle_left.stop()

    if keys[pygame.K_UP]:
        paddle_right.move_up()
    elif keys[pygame.K_DOWN]:
        paddle_right.move_down()
    else:
        paddle_right.stop()