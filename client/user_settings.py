import json
from dataclasses import dataclass
from settings import RESOLUTIONS, COLORS, MIN_CONTRAST, SETTING_ROWS, \
    CONFIG_PATH
from color_utils import contrast_ratio


@dataclass
class UserSettings:
    resolution_index: int = 0
    bg_color_index: int = 0
    paddle_color_index: int = 1
    ball_color_index: int = 1
    text_color_index: int = 1

    @property
    def bg_color(self):
        return COLORS[self.bg_color_index][1]

    @property
    def paddle_color(self):
        return COLORS[self.paddle_color_index][1]

    @property
    def ball_color(self):
        return COLORS[self.ball_color_index][1]

    @property
    def text_color(self):
        return COLORS[self.text_color_index][1]

    @property
    def resolution(self):
        return RESOLUTIONS[self.resolution_index][1]

    def cycle(self, field, options, step):
        for attempt in range(1, len(options) + 1):
            index = (getattr(self, field) + step * attempt) % len(options)
            if self.is_allowed(field, options[index][1]):
                setattr(self, field, index)
                return

    def label(self, field, options):
        return options[getattr(self, field)][0]

    def is_allowed(self, field, color):
        if field == "resolution_index":
            return True
        if field == "bg_color_index":
            others = [self.paddle_color, self.ball_color, self.text_color]
            return all(
                contrast_ratio(color, other) >= MIN_CONTRAST
                for other in others
            )
        return contrast_ratio(color, self.bg_color) >= MIN_CONTRAST

    def save(self):
        data = {
            field: self.label(field, options)
            for field, options in SETTING_ROWS.values()
        }
        CONFIG_PATH.parent.mkdir(parents=True, exist_ok=True)
        CONFIG_PATH.write_text(json.dumps(data, indent=4), encoding="utf-8")

    @classmethod
    def load(cls):
        settings = cls()
        try:
            data = json.loads(CONFIG_PATH.read_text(encoding="utf-8"))
        except (FileNotFoundError, json.JSONDecodeError):
            return settings

        for field, options in SETTING_ROWS.values():
            names = [name for name, _ in options]
            if data.get(field) in names:
                setattr(settings, field, names.index(data[field]))

        return settings
