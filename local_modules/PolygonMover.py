import pygame
from pygame.surface import Surface
from local_modules import BaseModule, DrawPolygon, Helper


class PolygonMover(BaseModule.BaseModule):

    def __init__(self, screen: Surface, polygon_object: DrawPolygon.DrawPolygon):
        super().__init__(screen)
        self.timer_interval = 0
        self.polygon_object = polygon_object  # type: DrawPolygon.DrawPolygon

        self.controls_move = {
            pygame.K_LEFT: self.move_left,
            pygame.K_RIGHT: self.move_right,
            pygame.K_UP: self.move_up,
            pygame.K_DOWN: self.move_down
        }

        self.controls_rotate = {
            pygame.K_q: self.rotate_left,
            pygame.K_e: self.rotate_right
        }

        self.controls_snap = {
            pygame.K_a: self.snap_left,
            pygame.K_w: self.snap_up,
        }

    def handle_input_keyboard(self, event: pygame.event):
        if event.mod & pygame.KMOD_LCTRL and event.key == pygame.K_z:
            if self.polygon_object.points:
                self.polygon_object.points.pop()

        if event.key in self.controls_snap:
            self.controls_snap[event.key]()

    def handle_input_keyboard_pressed(self, keys):
        for key in self.controls_move:
            if keys[key]:
                self.controls_move[key]()

        for key in self.controls_rotate:
            if keys[key]:
                self.controls_rotate[key]()

    def snap_left(self):
        smallest_distance = self.polygon_object.get_most_left_distance()
        for i in range(len(self.polygon_object.points)):
            self.polygon_object.points[i] = (
                self.polygon_object.points[i][0] - smallest_distance, self.polygon_object.points[i][1]
            )

    def snap_up(self):
        smallest_distance = self.polygon_object.get_most_up_distance()
        for i in range(len(self.polygon_object.points)):
            self.polygon_object.points[i] = (
                self.polygon_object.points[i][0], self.polygon_object.points[i][1] - smallest_distance
            )


    def move_left(self):
        for i in range(len(self.polygon_object.points)):
            self.polygon_object.points[i] = (self.polygon_object.points[i][0] - 1, self.polygon_object.points[i][1])

    def move_right(self):
        for i in range(len(self.polygon_object.points)):
            self.polygon_object.points[i] = (self.polygon_object.points[i][0] + 1, self.polygon_object.points[i][1])

    def move_up(self):
        for i in range(len(self.polygon_object.points)):
            self.polygon_object.points[i] = (self.polygon_object.points[i][0], self.polygon_object.points[i][1] - 1)

    def move_down(self):
        for i in range(len(self.polygon_object.points)):
            self.polygon_object.points[i] = (self.polygon_object.points[i][0], self.polygon_object.points[i][1] + 1)

    def rotate_left(self):
        self.polygon_object.points = Helper.rotate_polygon(self.polygon_object.points, 1)

    def rotate_right(self):
        self.polygon_object.points = Helper.rotate_polygon(self.polygon_object.points, -1)
