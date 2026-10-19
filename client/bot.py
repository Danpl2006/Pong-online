"""

"""

from settings import WIDTH, BOT_REACTION_ZONE
from collisions import check_paddle_collision


def bot_input(paddle, ball, side):
    center_paddle = paddle.y + paddle.height // 2
    center_ball = ball.y + ball.size // 2

    if side == "left":
        if ball.x >= BOT_REACTION_ZONE:
            paddle.stop_y()
            return

    elif side == "right":
        if ball.x <= WIDTH - BOT_REACTION_ZONE:
            paddle.stop_y()
            return

    if center_ball < center_paddle:
        paddle.move_up()
    elif center_ball > center_paddle:
        paddle.move_down()
    else:
        paddle.stop_y()


def update_menu_background(paddle_left, paddle_right, ball):
    bot_input(paddle_left, ball, "left")
    bot_input(paddle_right, ball, "right")
    paddle_left.update()
    paddle_right.update()
    check_paddle_collision(ball, paddle_left)
    check_paddle_collision(ball, paddle_right)
    goal = ball.update()
    if goal is not None:
        ball.reset()
