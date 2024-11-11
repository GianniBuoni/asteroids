import pygame
from lib.constants import SCREEN_WIDTH, SCREEN_HEIGHT

# game initialization
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Asteroids")
clock = pygame.time.Clock()
running = True

# game loop
while running:
    dt = clock.tick(60) / 1000
    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # draw
    screen.fill("grey9")
    # update
    pygame.display.update()
