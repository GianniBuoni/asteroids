#pyright: reportOptionalMemberAccess=false

import pygame
from random import uniform, randint

class Asteroid(pygame.sprite.Sprite):
    def __init__(self, surface, pos, groups) -> None:
        super().__init__(groups)
        self.original_surfce = surface
        self.image = surface
        self.rect = self.image.get_frect(
            center = pos
        )
        self.kill_timer = 3.00

        # asteroid movement
        self.speed = randint(400, 500)
        self.direction = pygame.Vector2(uniform(-0.5, 0.5), 1)
        self.rotation = 0
        self.rotation_speed = randint(40, 50)

    def update(self, dt):
        self.kill_timer -= dt
        if self.kill_timer < 0:
            self.kill()

        # update rect center position
        self.rect.center += self.direction * self.speed * dt

        # update self rotation
        self.rotation += self.rotation_speed * dt
        self.image = pygame.transform.rotozoom(self.original_surfce, self.rotation, 1)
        self.rect = self.image.get_frect(
            center = self.rect.center
        )
