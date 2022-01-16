import pygame
import config
from local_modules.BaseModule import BaseModule
from local_modules.DrawPolygon import DrawPolygon
from local_modules.MousePosition import MousePosition
from local_modules.PolygonMover import PolygonMover
from local_modules.TextBottom import TextBottom


class PolygonDrawer:

    def __init__(self):
        self.screen = None  # type: pygame.Surface or None
        self.screen_rect = None  # type: pygame.Rect or None
        self.game_is_running = True
        self.last_event = None
        self.time_passed = 0
        self.all_modules = []  # type: list[BaseModule]

    def import_modules(self):
        mouse_position = MousePosition(self.screen)
        mouse_position.timer_interval = 0.25
        mouse_position.font_size = 30
        mouse_position.position = (self.screen_rect.width - 100, self.screen_rect.height - 30)
        mouse_position.calculate()
        self.all_modules.append(mouse_position)

        draw_polygon = DrawPolygon(self.screen)
        self.all_modules.append(draw_polygon)

        polygon_mover = PolygonMover(self.screen, draw_polygon)
        self.all_modules.append(polygon_mover)

        controls_help = TextBottom(self.screen, [
            'Controls:',
            'Draw: Left Mouse Button (2 points required, filled 3 points)',
            'TAB: toggle line / filled',
            'Move: Arrow keys | Rotate: Q / E | Snap Left: A | Snap Up: W',
            'Undo: ctrl+z | Save Json: 1 | Save Python list: 2 '
        ])
        self.all_modules.append(controls_help)

    def run_game(self):
        pygame.init()
        pygame.display.set_caption("Polygon Drawer")

        self.screen = pygame.display.set_mode((config.SCREEN_WIDTH, config.SCREEN_HEIGHT), pygame.RESIZABLE)
        self.screen_rect = self.screen.get_rect()

        clock = pygame.time.Clock()

        self.import_modules()

        self.game_is_running = True

        while self.game_is_running:
            # limit frame speed
            self.time_passed = clock.tick(60)

            self.screen_rect = self.screen.get_rect()

            mouse_position = self.all_modules[0]
            mouse_position.position = (self.screen_rect.width - 100, self.screen_rect.height - 30)

            self.screen.fill(config.BACKGROUND_COLOR, self.screen_rect)

            keys = pygame.key.get_pressed()
            for module in self.all_modules:
                module.handle_input_keyboard_pressed(keys)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_is_running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.game_is_running = False
                    else:
                        for module in self.all_modules:
                            module.handle_input_keyboard(event)

                elif event.type == pygame.MOUSEBUTTONUP:
                    for module in self.all_modules:
                        module.handle_input_mouse(event)
                #else:
                    #print(event.type)

            for module in self.all_modules:
                module.timer()
                module.draw()

            # final draw
            pygame.display.flip()
