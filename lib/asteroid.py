#pyright: reportOptionalMemberAccess=false

import pygame
from random import uniform
from lib.constants import ASTEROID_SPEED

class Asteroid(pygame.sprite.Sprite):
    def __init__(self, surface, pos, groups) -> None:
        super().__init__(groups)
        self.image = surface
        self.rect = self.image.get_frect(
            center = pos
        )
        self.kill_timer = 3.00
        self.direction = pygame.Vector2(uniform(-0.5, 0.5), 1)

    def update(self, dt):
        self.kill_timer -= dt
        if self.kill_timer < 0:
            self.kill()

        self.rect.center += self.direction * ASTEROID_SPEED * dt
