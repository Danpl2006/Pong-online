import pygame
import os

os.environ["SDL_VIDEO_CENTERED"] = "1"

def create_window(resolution):
    return pygame.display.set_mode(resolution, pygame.SCALED, vsync=1)

def recreate_window(resolution):
    pygame.display.quit()
    pygame.display.init()
    return create_window(resolution)
