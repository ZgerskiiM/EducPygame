from pygame import *


init()

ARIAL = font.SysFont('arial', 35)

class Menu:
    def __init__(self):
        self.option_surface = []
        self.callback = []
        self.current_option = 0

    def append_option(self, option, callback):
        self.option_surface.append(ARIAL.render(option, True, (255, 255, 255)))
        self.callback.append(callback)

    def switch(self, direction):
        self.current_option = max(0, min(self.current_option + direction, len(self.option_surface) -1))


    def select(self):
        self.callback[self.current_option]

    def draw(self, surf, x, y, opttion_y):
        for i, opttion in enumerate(self.option_surface):
            opttion_rect = opttion.get_rect()
            opttion_rect.topleft = (x, y + i * opttion_y)
            if i == self.current_option:
                draw.rect(surf, (0, 100, 0), opttion_rect)
            surf.blit(opttion, opttion_rect)






