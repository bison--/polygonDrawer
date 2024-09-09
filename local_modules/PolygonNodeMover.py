from abc import ABC

import pygame
from pygame.surface import Surface
from local_modules import BaseModule, DrawPolygon, Helper


class PolygonNodeMover(BaseModule.BaseModule, ABC):

    def __init__(self, screen: Surface, polygon_object: DrawPolygon.DrawPolygon):
        super().__init__(screen)
        self.timer_interval = 0
        self.polygon_object = polygon_object  # type: DrawPolygon.DrawPolygon
        self.selected_node_index = None
        self.color = (255, 0, 0)
        self.size = 2
        self.press_mode = True
        self.text_object = None

        self.controls_move = {
            pygame.K_j: self.move_left,
            pygame.K_l: self.move_right,
            pygame.K_i: self.move_up,
            pygame.K_k: self.move_down
        }

    def has_node(self):
        return self.selected_node_index is not None

    def get_node_pos(self):
        return self.polygon_object.points[self.selected_node_index]

    def set_node_pos(self, x, y):
        self.polygon_object.points[self.selected_node_index] = (x, y)

    def deselect_node(self):
        self.selected_node_index = None
        if self.text_object is not None:
            self.text_object.set_text("")

    def draw(self):
        if self.has_node():
            pygame.draw.circle(self._screen, self.color, self.get_node_pos(), self.size)
            if self.text_object is not None:
                self.text_object.set_text(str(self.get_node_pos()))

    def handle_input_mouse(self, event):
        if event.button == pygame.BUTTON_RIGHT:
            if self.has_node():
                self.deselect_node()
                return

            mouse_position = pygame.mouse.get_pos()
            closest_index = None
            closest_distance = None
            index = 0
            for point in self.polygon_object.points:
                temp_distance = Helper.calculate_distance(mouse_position, point)
                if closest_index is None or temp_distance < closest_distance:
                    closest_distance = temp_distance
                    closest_index = index

                index += 1

            if closest_index is not None:
                self.selected_node_index = closest_index

    def handle_input_keyboard(self, event: pygame.event):
        if event.key == pygame.K_u:
            self.press_mode = not self.press_mode

        if not self.press_mode and event.key in self.controls_move:
            self.controls_move[event.key]()

        if not self.has_node():
            return

        if event.mod & pygame.KMOD_LCTRL:
            pass

    def handle_input_keyboard_pressed(self, keys):
        if not self.has_node():
            return

        if not self.press_mode:
            return

        for key in self.controls_move:
            if keys[key]:
                self.controls_move[key]()

    def move_left(self):
        node_pos = self.get_node_pos()
        self.set_node_pos(node_pos[0] - 1, node_pos[1])

    def move_right(self):
        node_pos = self.get_node_pos()
        self.set_node_pos(node_pos[0] + 1, node_pos[1])

    def move_up(self):
        node_pos = self.get_node_pos()
        self.set_node_pos(node_pos[0], node_pos[1] - 1)

    def move_down(self):
        node_pos = self.get_node_pos()
        self.set_node_pos(node_pos[0], node_pos[1] + 1)
