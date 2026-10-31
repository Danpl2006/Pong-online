"""
Глобальные настройки игры Pong:
- размеры экрана
- параметры объектов
- игровые константы
- цветовые параметры
"""

from pathlib import Path

CONFIG_PATH = Path.home() / ".pong_online" / "config.json"

# Screen size
WIDTH = 1280
HEIGHT = 720

# Ball  parameters
BALL_SPEED = 8
BALL_SIZE = 20

# Paddle parameters
PADDLE_WIDTH = 20
PADDLE_HEIGHT = 150
PADDLE_SPEED = 8
PADDLE_ZONE = 250  # Конечная граница движения по X от начального

# Параметры бота
BOT_REACTION_ZONE = 500  # Зона реакции ракетки на движение мяча

# Максимальный счет
WINNING_SCORE = 10

# Кадры в секунду
FPS = 60

MIN_CONTRAST = 2.0

# Опции доступные в настройках
RESOLUTIONS = [
    ("1280x720", (1280, 720)),
    ("1600x900", (1600, 900)),
    ("1920x1080", (1920, 1080))
]

COLORS = [
    ("color.black", (0, 0, 0)),
    ("color.white", (255, 255, 255)),
    ("color.red", (255, 0, 0)),
    ("color.green", (0, 255, 0)),
    ("color.blue", (80, 120, 255)),
    ("color.yellow", (255, 255, 0)),
]

LANGUAGES = [
    ("lang.en", "en"),
    ("lang.ru", "ru"),
    ("lang.de", "de"),
    ("lang.es", "es"),
]

SETTING_ROWS = {
    "settings.resolution": ("resolution_index", RESOLUTIONS),
    "settings.background": ("bg_color_index", COLORS),
    "settings.paddles": ("paddle_color_index", COLORS),
    "settings.ball": ("ball_color_index", COLORS),
    "settings.text": ("text_color_index", COLORS),
    "settings.language": ("language_index", LANGUAGES),
}

DEFAULT_LANGUAGE = "ru"

# Состояния меню
MENU_STATES = ("menu", "settings", "side_select")

BOT_SPEED_FACTOR = 1.0
BOT_ENGAGE_ZONE = int(WIDTH * 0.4)
BOT_RELEASE_ZONE = int(WIDTH * 0.6)
