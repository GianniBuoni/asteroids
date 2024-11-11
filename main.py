import pygame
from lib.constants import SCREEN_WIDTH, SCREEN_HEIGHT
from lib.groups import all_sprites
from lib.player import Player

# game initialization
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Asteroids")
clock = pygame.time.Clock()
running = True

player = Player(all_sprites)

# game loop
while running:
    dt = clock.tick(60) / 1000
    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # update sprites
    all_sprites.update(dt)

    # draw sprites
    screen.fill("grey9")
    all_sprites.draw(screen)

    # update display
    pygame.display.update()
