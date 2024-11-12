import pygame
from os.path import join
from lib.constants import SCREEN_WIDTH, SCREEN_HEIGHT, ASTEROID_SPAWN_RATE
from lib.player import Player
from lib.groups import all_sprites

# global
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
running = True
score = 0

# imports
player = Player(all_sprites)
asteroid_surface = pygame.image.load(join("assets", "meteor.png")).convert_alpha()

# events
asteroid_event = pygame.event.custom_type()
pygame.time.set_timer(asteroid_event, ASTEROID_SPAWN_RATE)

def display_score(score):
    font = pygame.font.Font(join("assets", "Oxanium-Bold.ttf"), 42)
    text_surface = font.render(score, True, (240, 240, 240))
    text_rect = text_surface.get_frect(
        midbottom = (SCREEN_WIDTH / 2, SCREEN_HEIGHT - 50)
    )

    screen.blit(text_surface, text_rect)
    pygame.draw.rect(screen, (240, 240, 240), text_rect.inflate(40,20).move(0,-8), 5, 10)
