import pygame
from os.path import join
from random import randint
from lib.asteroid import Asteroid
from lib.groups import all_sprites, asteroid_sprites, shot_sprites
from lib.player import Player
from lib.constants import SCREEN_WIDTH, SCREEN_HEIGHT, ASTEROID_SPAWN_RATE

# game initialization
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Asteroids")
clock = pygame.time.Clock()
running = True

# sprites
asteroid_surface = pygame.image.load(join("assets", "meteor.png")).convert_alpha()
player = Player(all_sprites)

# events
asteroid_event = pygame.event.custom_type()
pygame.time.set_timer(asteroid_event, ASTEROID_SPAWN_RATE)

# game loop
while running:
    dt = clock.tick(60) / 1000
    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == asteroid_event:
            rand_x = randint(0, SCREEN_WIDTH)
            rand_y = randint(-100, 0)
            Asteroid(asteroid_surface, (rand_x, rand_y), (all_sprites, asteroid_sprites))

    for shot in shot_sprites:
        if pygame.sprite.spritecollide(shot, asteroid_sprites, True):
            shot.kill()

    if pygame.sprite.spritecollide(player, asteroid_sprites, False):
        print("GAME OVER MAN, GAME OVER!")
        running = False

    # update sprites
    all_sprites.update(dt)

    # draw sprites
    screen.fill("grey9")
    all_sprites.draw(screen)

    # update display
    pygame.display.update()
