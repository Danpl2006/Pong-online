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

MIN_CONTRAST = 3.0

# Опции доступные в настройках
RESOLUTIONS = [
    ("1280x720", (1280, 720)),
    ("1600x900", (1600, 900)),
    ("1920x1080", (1920, 1080))
]

COLORS = [("Black", (0, 0, 0)),
          ("White", (255, 255, 255)),
          ("Red", (255, 0, 0)),
          ("Green", (0, 255, 0)),
          ("Blue", (80, 120, 255)),
          ("Yellow", (255, 255, 0))
          ]

SETTING_ROWS = {
    "Resolution": ("resolution_index", RESOLUTIONS),
    "Background": ("bg_color_index", COLORS),
    "Paddles": ("paddle_color_index", COLORS),
    "Ball": ("ball_color_index", COLORS),
    "Text": ("text_color_index", COLORS)
}

# Состояния меню
MENU_STATES = ("menu", "settings", "side_select")
