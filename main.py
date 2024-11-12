import pygame
from random import randint

from lib.asteroid import Asteroid
from lib.groups import all_sprites, asteroid_sprites, shot_sprites
from lib.variables import (
    asteroid_event, asteroid_surface, clock,
    display_score,player, running, screen, score
)
from lib.constants import SCREEN_WIDTH

# game initialization
pygame.init()
pygame.display.set_caption("Asteroids")

# event loop
while running:
    dt = clock.tick(60) / 1000
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == asteroid_event:
            rand_x = randint(0, SCREEN_WIDTH)
            rand_y = randint(-100, 0)
            Asteroid(asteroid_surface, (rand_x, rand_y), (all_sprites, asteroid_sprites))

    for shot in shot_sprites:
        if pygame.sprite.spritecollide(shot, asteroid_sprites, True):
            score += 1
            shot.kill()

    if pygame.sprite.spritecollide(player, asteroid_sprites, False, pygame.sprite.collide_mask):
        print(f"GAME OVER MAN, GAME OVER!\nSCORE: {score}")
        running = False

    # update sprites
    all_sprites.update(dt)

    # draw sprites
    screen.fill("#322e3f")
    all_sprites.draw(screen)
    display_score(str(score))

    # update display
    pygame.display.update()
