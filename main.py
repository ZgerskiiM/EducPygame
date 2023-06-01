import pygame
import time
from CarP import play_c
from Assets import TRACK, WATER, \
    finish, TRACK_BORDER, TRACK_BORDER_MASK, finish_pos, finish_mask
from Moving import player_move
pygame.init()




width, height = TRACK.get_width(), TRACK.get_height()
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Гонки")


FPS = 60

MAIN_FONT = pygame.font.SysFont("arial", 38)

def blit_text_center(win, font, text):
    render = font.render(text, 1, (200, 200, 200))
    win.blit(render, (win.get_width()/2 - render.get_width() /
                      2, win.get_height()/2 - render.get_height()/2))

class GameInfo:
    LEVELS = 10
    LEVEL_TIME = 5

    def __init__(self, level=1):
        self.level = level
        self.started = False
        self.level_start_time = 0

    def next_level(self):
        self.level += 1
        self.started = False

    def reset(self):
        self.level = 1
        self.started = False
        self.level_start_time = 0

    def game_finished(self):
        return self.level > self.LEVELS

    def start_level(self):
        self.started = True
        self.level_start_time = pygame.time.get_ticks()

    def get_level_time(self):
        if not self.started:
            return 0
        elapsed_time = pygame.time.get_ticks() - self.level_start_time
        remaining_time = self.LEVEL_TIME * 1000 - elapsed_time
        if remaining_time <= 0:
            return -1  # уровень окончен
        return round(remaining_time / 1000)




def draw(window, images, play_c, game_info):
    for img, pos in images:
        window.blit(img, pos)

    level_text = MAIN_FONT.render(
        f"Level {game_info.level}", 1, (255, 255, 255))
    window.blit(level_text, (640, height - level_text.get_height() - 40))

    time_text = MAIN_FONT.render(
        f"Time: {game_info.get_level_time()}s", 1, (255, 255, 255))
    window.blit(time_text, (640, height - time_text.get_height() - 0))

    play_c.draw(window)
    pygame.display.update()

run = True
clock = pygame.time.Clock()
images = [(WATER, (0, 0)), (TRACK, (0,0)), (finish, finish_pos), (TRACK_BORDER, (0,0))]
game_info = GameInfo()

while run:
    clock.tick(FPS)

    draw(window, images, play_c, game_info)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break


    player_move(play_c)

    if play_c.collide(TRACK_BORDER_MASK) != None:
        play_c.bounce()

    finish_collision_collide = play_c.collide(finish_mask, *finish_pos)
    if finish_collision_collide != None:
        if finish_collision_collide [1] == 0:
            play_c.bounce()
        else:
            game_info.next_level()
            play_c.reset()


    if game_info.game_finished():
        blit_text_center(window, MAIN_FONT, "You won the game!")
        pygame.time.wait(5000)
        game_info.reset()
        play_c.reset()




pygame.quit()





