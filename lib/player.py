import pygame
from os.path import join
from lib.constants import *
from lib.constants import PLAYER_SPEED, SCREEN_WIDTH, SCREEN_HEIGHT

class Player(pygame.sprite.Sprite):
    def __init__(self, groups) -> None:
        super().__init__(groups)

        self.image = pygame.image.load(
            join("assets",'player.png')
        ).convert_alpha()

        self.rect = self.image.get_frect(
            center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT/2)
        )

        self.direction = pygame.Vector2()

    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.direction.x = int(keys[pygame.K_RIGHT]) - int(keys[pygame.K_LEFT])
        self.direction.y = int(keys[pygame.K_DOWN]) - int(keys[pygame.K_UP])
        self.direction = self.direction.normalize() if self.direction else self.direction

        self.rect.center += self.direction * PLAYER_SPEED * dt #type:ignore
