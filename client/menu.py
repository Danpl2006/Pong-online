from dataclasses import dataclass


@dataclass
class Menu:
    options: list[str]
    selected: int = 0

    def move_down(self):
        if self.selected < len(self.options) - 1:
            self.selected += 1

    def move_up(self):
        if self.selected > 0:
            self.selected -= 1

    @property
    def current(self):
        return self.options[self.selected]

