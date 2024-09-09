import time
from abc import abstractmethod

from pygame.surface import Surface


class BaseModule:

    def __init__(self, screen: Surface):
        self._screen = screen
        self.timer_interval = 1.1
        self.__next_calculation_time = time.time()

    def timer(self):
        if self.__next_calculation_time <= time.time():
            self.__next_calculation_time = time.time() + self.timer_interval
            self.execute_timer()

    @abstractmethod
    def calculate(self):
        pass

    @abstractmethod
    def execute_timer(self):
        pass

    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def handle_input_keyboard(self, event):
        pass

    @abstractmethod
    def handle_input_keyboard_pressed(self, event):
        pass

    @abstractmethod
    def handle_input_mouse(self, event):
        pass
