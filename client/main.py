import pygame
from settings import *
from entities import Paddle, Ball
from render import draw, draw_menu
from input import handle_input, menu_input, settings_input, side_select_input
from collisions import check_paddle_collision
from bot import update_menu_background, vs_computer_controls
from user_settings import UserSettings
from menu import Menu
from display import create_window, recreate_window


pygame.init()
pygame.font.init()

user_settings = UserSettings.load()

# Размер Экрана
screen = create_window(user_settings.resolution)

applied_resolution = user_settings.resolution
game_surface = pygame.Surface((WIDTH, HEIGHT))

pygame.display.set_caption("Pong-online")

clock = pygame.time.Clock()

font = pygame.font.Font(None, 100)

# Экземпляры классов
paddle_left = Paddle(0, HEIGHT // 2 - PADDLE_HEIGHT // 2, 0, PADDLE_ZONE)
paddle_right = Paddle(WIDTH - PADDLE_WIDTH, HEIGHT // 2 - PADDLE_HEIGHT // 2,
                      WIDTH - PADDLE_ZONE, WIDTH - PADDLE_WIDTH)

ball = Ball(WIDTH // 2, HEIGHT // 2)

# Переменные для счета
score_left = 0
score_right = 0
pending_goal = None


game_state = "menu"
state_timer = 0
game_mode = "local"
player_side = "left"

main_menu = Menu(["menu.local_friend", "menu.local_computer",
                  "menu.multiplayer", "menu.settings", "menu.exit"])
settings_menu = Menu(list(SETTING_ROWS) + ["back"])
side_menu = Menu(["side.left", "side.right", "back"])

# Главный цикл игры
running = True
while running:
    previous_state = game_state

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN and game_state == "menu":
            game_state = menu_input(event, main_menu, game_state)

        elif event.type == pygame.KEYDOWN and game_state == "settings":
            game_state = settings_input(event, settings_menu, game_state,
                                        user_settings)
        elif event.type == pygame.KEYDOWN and game_state == "side_select":
            game_state = side_select_input(event, side_menu, game_state)

        if (event.type == pygame.KEYDOWN and
                event.key == pygame.K_ESCAPE and
                game_state not in MENU_STATES):
            paddle_left.reset()
            paddle_right.reset()
            ball.reset()
            game_state = "menu"

    if previous_state in MENU_STATES and game_state == "playing":
        paddle_left.reset()
        paddle_right.reset()
        ball.reset()
        score_left = 0
        score_right = 0
        game_mode = "vs_computer" if previous_state == "side_select" else "local"
        if previous_state == "side_select":
            player_side = "left" if side_menu.current == "side.left" else "right"

    if previous_state == "settings" and game_state != "settings":
        user_settings.save()

    if game_state == "exit":
        running = False

    if user_settings.resolution != applied_resolution:
        screen = recreate_window(user_settings.resolution)
        applied_resolution = user_settings.resolution

    game_surface.fill(user_settings.bg_color)
    keys = pygame.key.get_pressed()

    if game_state in MENU_STATES:
        update_menu_background(paddle_left, paddle_right, ball)
    else:
        if game_mode == "local":
            handle_input(keys, paddle_left, paddle_right)
        else:
            vs_computer_controls(keys, paddle_left, paddle_right, ball,
                                 player_side, game_state)
        paddle_left.update()
        paddle_right.update()

    if game_state == "playing":

        check_paddle_collision(ball, paddle_left)
        check_paddle_collision(ball, paddle_right)
        goal = ball.update()

        if goal == "left":
            pending_goal = "left"
            game_state = "score_display"
            state_timer = pygame.time.get_ticks()
        elif goal == "right":
            pending_goal = "right"
            game_state = "score_display"
            state_timer = pygame.time.get_ticks()

    if game_state == "score_display":
        elapsed = pygame.time.get_ticks() - state_timer
        if elapsed > 700 and pending_goal == "left":
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

    draw(game_surface, paddle_left, paddle_right, ball,
         score_left, score_right, font, game_state, user_settings, user_settings.language)

    if game_state == "menu":
        draw_menu(game_surface, font, main_menu, user_settings, user_settings.language)
    elif game_state == "settings":
        draw_menu(game_surface, font, settings_menu, user_settings, user_settings.language)
    elif game_state == "side_select":
        draw_menu(game_surface, font, side_menu, user_settings, user_settings.language)

    scaled_surface = pygame.transform.smoothscale(game_surface,
                                                  screen.get_size())
    screen.blit(scaled_surface, (0, 0))

    pygame.display.flip()
    clock.tick(FPS)

user_settings.save()
pygame.quit()
