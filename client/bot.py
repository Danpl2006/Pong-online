from dataclasses import dataclass
from settings import *
from collisions import check_paddle_collision
from input import control_paddle, WASD, ARROWS


@dataclass(frozen=True)
class BotProfile:
    reaction_zone: int
    move_x: bool
    speed_factor: float = 1.0
    engage_zone: int = 0
    release_zone: int = 0


MENU_BOT = BotProfile(reaction_zone=BOT_REACTION_ZONE, move_x=False)
GAME_BOT = BotProfile(reaction_zone=WIDTH, move_x=True,
                      speed_factor=BOT_SPEED_FACTOR,
                      engage_zone=BOT_ENGAGE_ZONE,
                      release_zone=BOT_RELEASE_ZONE)


def bot_input(paddle, ball, side, profile):
    center_paddle = paddle.y + paddle.height // 2
    center_ball = ball.y + ball.size // 2

    if side == "left":
        if ball.x >= profile.reaction_zone:
            paddle.stop_y()
            return

    elif side == "right":
        if ball.x <= WIDTH - profile.reaction_zone:
            paddle.stop_y()
            return

    if center_ball < center_paddle:
        paddle.dy = -PADDLE_SPEED * profile.speed_factor
    elif center_ball > center_paddle:
        paddle.dy = PADDLE_SPEED * profile.speed_factor
    else:
        paddle.stop_y()

    if profile.move_x:
        if side == "left":
            distance = ball.x
            near_x, far_x = paddle.max_x, paddle.min_x
        else:
            distance = WIDTH - (ball.x + ball.size)
            near_x, far_x = paddle.min_x, paddle.max_x

        currently_forward = abs(paddle.x - near_x) < abs(paddle.x - far_x)
        if currently_forward:
            moving_forward = distance < profile.release_zone
        else:
            moving_forward = distance < profile.engage_zone
        target_x = near_x if moving_forward else far_x

        step = PADDLE_SPEED * profile.speed_factor
        if paddle.x < target_x:
            paddle.dx = min(step, target_x - paddle.x)
        elif paddle.x > target_x:
            paddle.dx = -min(step, paddle.x - target_x)
        else:
            paddle.dx = 0


def update_menu_background(paddle_left, paddle_right, ball):
    bot_input(paddle_left, ball, "left", MENU_BOT)
    bot_input(paddle_right, ball, "right", MENU_BOT)
    paddle_left.update()
    paddle_right.update()
    check_paddle_collision(ball, paddle_left)
    check_paddle_collision(ball, paddle_right)
    goal = ball.update()
    if goal is not None:
        ball.reset()


def freeze_paddle(paddle):
    paddle.stop_y()
    paddle.stop_x()


def vs_computer_controls(keys, paddle_left, paddle_right, ball, player_side,
                         game_state):
    if player_side == "left":
        human, bot, bot_side = paddle_left, paddle_right, "right"
    else:
        human, bot, bot_side = paddle_right, paddle_left, "left"

    control_paddle(keys, human, WASD, ARROWS)
    if game_state == "playing":
        bot_input(bot, ball, bot_side, GAME_BOT)
    else:
        freeze_paddle(bot)
