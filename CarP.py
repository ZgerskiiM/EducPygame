import pygame
from CarSummary import Car
from Assets import PLAYER_CAR



class carplayer(Car):
    IMG = PLAYER_CAR
    START_POS = (200, 180)


    def bounce(self):
        self.vel = -self.vel
        self.move()










play_c = carplayer(2, 2)