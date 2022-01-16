import pygame
from pygame.surface import Surface
from local_modules import BaseModule


class DrawPolygon(BaseModule.BaseModule):

    def __init__(self, screen: Surface):
        super().__init__(screen)
        self.timer_interval = 0
        self.color = (0, 148, 220)
        self.line_size = 2

        self.points = []

    def get_most_left_distance(self):
        most_left = None
        for point in self.points:
            if most_left is None or point[0] < most_left:
                most_left = point[0]

        return most_left

    def get_most_up_distance(self):
        most_up = None
        for point in self.points:
            if most_up is None or point[1] < most_up:
                most_up = point[1]

        return most_up

    def handle_input_mouse(self, event: pygame.event):
        if event.button == pygame.BUTTON_LEFT:
            self.points.append(pygame.mouse.get_pos())
        print(self.points)

    def draw(self):
        if len(self.points) >= 2:
            pygame.draw.polygon(self._screen, self.color, self.points, self.line_size)