from abc import ABC

import pygame
from pygame.surface import Surface
from local_modules import BaseModule


class TextBottom(BaseModule.BaseModule, ABC):

    def __init__(self, screen: Surface, text_lines: list):
        super().__init__(screen)

        self.text_lines: list = text_lines
        self.text_lines_reversed = []

        self.font_size = 30
        self.color = (245, 101, 44)  # orange
        self.position = (10, 10)

        self.font = None  # type: pygame.font or None
        self.__real_position = None  # type: tuple or None
        self.text_size = (0, 0)

        self.calculate()

    def set_text(self, text: list or str):
        if type(text) is list:
            self.text_lines = text
        elif type(text) is str:
            self.text_lines.clear()
            self.text_lines.append(text)

        self.calculate()

    def get_text_size(self):
        max_width = 0
        max_height = 0

        for line in self.text_lines:
            size = self.font.size(line)
            max_width += size[0]
            max_height += size[1]

        return max_width, max_height

    def calculate(self):
        self.font = pygame.font.SysFont("MS Comic Sans,Comic Neue", self.font_size)
        self.text_size = self.get_text_size()
        self.text_lines_reversed = self.text_lines.copy()
        self.text_lines_reversed.reverse()

    def draw(self):
        self._render_text()

    def _render_text(self):
        line_counter = 1
        for line in self.text_lines_reversed:
            size = self.font.size(line)

            self._screen.blit(
                self.font.render(line, True, self.color),
                (self.position[0], (self._screen.get_rect().height - (size[1] * line_counter)) - self.position[1])
            )

            line_counter += 1
