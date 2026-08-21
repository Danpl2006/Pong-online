import pygame
from settings import *
from entities import Paddle, Ball
from render import  draw
from input import handle_input
from collisions import check_paddle_collision

# Инициализация pygame и шрифтов
pygame.init()
pygame.font.init()

# Размер Экрана
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Заголовок экрана
pygame.display.set_caption("Pong-online")

# Ограничитель кадров
clock = pygame.time.Clock()

font = pygame.font.Font(None, 86)
# Экземпляры классов
paddle_left = Paddle(0, HEIGHT // 2 - PADDLE_HEIGHT // 2, 0, PADDLE_ZONE)
paddle_right = Paddle(WIDTH - PADDLE_WIDTH,HEIGHT // 2 - PADDLE_HEIGHT // 2, WIDTH - PADDLE_ZONE, WIDTH - PADDLE_WIDTH)
ball = Ball(WIDTH // 2,HEIGHT // 2)

# Переменные для счета
score_left = 0
score_right = 0
pending_goal = None
# "playing" — обычная игра, мяч летает.
# "score_display" — показываем счёт.
# "waiting_respawn" — пауза после исчезновения счёта, ждём перед появлением мяча.
game_state = "playing"
state_timer = 0

# Главный цикл игры
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    handle_input(keys, paddle_left, paddle_right)

    screen.fill(BG_COLOR)
    paddle_left.update()
    paddle_right.update()

    if game_state == "playing":
        check_paddle_collision(ball, paddle_left)
        check_paddle_collision(ball, paddle_right)
        goal = ball.update()

        if  goal == "left":
            pending_goal = "left"
            game_state = "score_display"
            state_timer = pygame.time.get_ticks()
        elif goal == "right":
            pending_goal = "right"
            game_state = "score_display"
            state_timer = pygame.time.get_ticks()

    if game_state == "score_display":
        elapsed = pygame.time.get_ticks() - state_timer
        if elapsed > 700 and  pending_goal == "left":
            score_left += 1
            if score_left >= WINNING_SCORE:
                game_state = "game_over"
            pending_goal = None
        elif elapsed > 700 and pending_goal == "right":
            score_right += 1
            if score_right >= WINNING_SCORE:
                game_state = "game_over"
            pending_goal = None

        if elapsed > 2500 and game_state != "game_over":
            game_state = "waiting_respawn"
            state_timer = pygame.time.get_ticks()

    if game_state == "waiting_respawn":
        elapsed = pygame.time.get_ticks() - state_timer
        if elapsed > 750:
            game_state = "playing"
            ball.reset()

    draw(screen, paddle_left, paddle_right, ball,
         score_left, score_right, font, game_state)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()

