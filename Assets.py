import pygame

def scale_image(img, factor):
    size = round(img.get_width() * factor), round(img.get_height()*factor)
    return pygame.transform.scale(img, size)


WATER = scale_image(pygame.image.load("images/Слой 3.png"), 50)
TRACK = scale_image(pygame.image.load("images/TRACK2.png"), 0.9)
TRACK_BORDER = scale_image(pygame.image.load("images/BORDER2.png"), 0.9)
finish = scale_image(pygame.image.load("images/finish.png"), 0.8)
PLAYER_CAR = scale_image (pygame.image.load("images/white-car.png"), 0.4)
COMP_CAR1 = scale_image (pygame.image.load("images/red-car.png"), 0.4)
TRACK_BORDER_MASK = pygame.mask.from_surface(TRACK_BORDER)
finish_pos = (220, 160)
finish_mask = pygame.mask.from_surface((finish))