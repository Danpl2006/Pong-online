
def check_paddle_collision(ball, paddle):
    if (ball.x < paddle.x + paddle.width
        and ball.x + ball.size > paddle.x
        and ball.y < paddle.y + paddle.height
        and ball.y + ball.size > paddle.y):
        ball.dx = -ball.dx
