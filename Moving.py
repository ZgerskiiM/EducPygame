import pygame



def player_move(play_c):
    keys = pygame.key.get_pressed()
    moved = False

    if keys[pygame.K_a]:
        play_c.rotate(left=True)
    if keys[pygame.K_d]:
        play_c.rotate(right=True)
    if keys[pygame.K_w]:
        moved = True
        play_c.move_forward()
    if keys[pygame.K_s]:
        moved = True
        play_c.move_backward()
    if not moved:
        play_c.reduce()

