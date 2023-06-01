import pygame.draw

from CarSummary import Car
from Assets import COMP_CAR1

class carcomputer(Car):
    IMG = COMP_CAR1
    START_POS = (200, 170)

    def __init__(self, max_vel, rotation_vel, path=[]):
        super().__init__(max_vel, rotation_vel)
        self.path = path
        self.current_point = 0
        self.vel = max_vel

    def draw_points(self, window):
        for point in self.path:
            pygame.draw.circle(window, (255, 0, 0), point, 5)


comp_c = carcomputer(2, 2)
