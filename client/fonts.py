import pygame
import os

def get_font(language: str, size: int = 100) -> pygame.font.Font:
    """
    Возвращает шрифт, который поддерживает переданный язык.
    По умолчанию используется NotoSans (покрывает латиницу, кириллицу и греческий),
    для CJK-языков — отдельные Noto Serif CJK, для хинди — Devanagari-шрифт.
    """
    # 1. Специальные шрифты для языков со своей письменностью
    special_fonts = {
        "zh": "NotoSerifCJKsc-Regular.otf",   # Китайский (упрощённый)
        "ja": "NotoSerifCJKjp-Regular.otf",   # Японский
        "ko": "NotoSerifCJKkr-Regular.otf",   # Корейский
        "hi": "NotoSansDevanagari-Regular.ttf",  # Хинди (деванагари)
    }

    # 2. Если языка нет в словаре (en, ru, es, de, fr, it, pl, cs, sr, tr,
    #    fi, no, sv, da, nl, pt, hu, el), метод .get() вернёт NotoSans.
    #    NotoSans-Regular.ttf покрывает латиницу, кириллицу и греческий алфавит.
    font_file = special_fonts.get(language, "NotoSans-Regular.ttf")

    # 3. Формируем правильный путь (os.path.join сам поставит нужный слэш / или \)
    font_path = os.path.join("assets", "fonts", font_file)

    # 4. Пытаемся загрузить шрифт
    try:
        return pygame.font.Font(font_path, size)
    except FileNotFoundError:
        # Если файл шрифта случайно удален, игра не упадет, а выдаст системный шрифт
        print(f"ОШИБКА: Шрифт не найден по пути {font_path}. Используется стандартный.")
        return pygame.font.Font(None, size)