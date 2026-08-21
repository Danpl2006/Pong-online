def check_paddle_collision(ball,
                           paddle):
    if (ball.x < paddle.x + paddle.width
        and ball.x + ball.size > paddle.x
        and ball.y < paddle.y + paddle.height
        and ball.y + ball.size > paddle.y):

        overlap_left = ball.x + ball.size - paddle.x
        overlap_right = paddle.x + paddle.width - ball.x
        overlap_top = ball.y + ball.size - paddle.y
        overlap_bottom = paddle.y + paddle.height - ball.y
        min_overlap = min(overlap_left, overlap_right,
                          overlap_top, overlap_bottom)

        if min_overlap == overlap_left:
            ball.dx = -ball.dx
            ball.x = paddle.x - ball.size
        elif min_overlap == overlap_right:
            ball.dx = -ball.dx
            ball.x = paddle.x + paddle.width
        elif min_overlap == overlap_top:
            ball.dy = -ball.dy
            ball.y = paddle.y - ball.size
        else:
            ball.dy = -ball.dy
            ball.y = paddle.y + paddle.height