import pygame
import math

def blit_rotate_center(window, image, top_left, angle):

    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center=image.get_rect(topleft=top_left).center)
    window.blit(rotated_image, new_rect.topleft)

class Car:

    def __init__(self, max_vel, rotation_vel):
        self.img = self.IMG
        self.max_vel = max_vel
        self.vel = 0
        self.rotation_vel = rotation_vel
        self.angle = 0
        self.x, self.y = self.START_POS
        self.accel = 0.05


    def rotate(self, left = False, right = False):

        if left:
            self.angle += self.rotation_vel
        elif right:
            self.angle -= self.rotation_vel

    def draw(self, window):
        blit_rotate_center(window, self.img, (self.x, self.y), self.angle)

    def move_forward(self):
        self.vel = min(self.vel + self.accel, self.max_vel)
        self.move()

    def move_backward(self):
        self.vel = max(self.vel - self.accel, -self.max_vel/2)
        self.move()

    def move(self):
        radians = math.radians(self.angle)
        vert_vel = math.cos(radians) * self.vel
        horz_vel = math.sin(radians) * self.vel
        self.y -= vert_vel
        self.x -= horz_vel

    def reduce(self):
        self.vel = max(self.vel - self.accel / 2, 0)
        self.move()

    def collide(self, mask, x=0, y=0):
        car_mask = pygame.mask.from_surface(self.img)
        offset = (int(self.x - x), int(self.y - y))
        collision = mask.overlap(car_mask, offset)
        return collision

    def reset(self):
        self.x, self.y = self.START_POS



