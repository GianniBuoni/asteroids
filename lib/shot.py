# pyright: reportOptionalMemberAccess = false

import pygame
from lib.constants import SHOT_SPEED

class Shot(pygame.sprite.Sprite):
    def __init__(self, surface, pos, groups) -> None:
        super().__init__(groups)
        self.image = surface
        self.rect = self.image.get_frect(
            midbottom = pos
        )

    def update(self, dt) -> None:
        self.rect.top -= SHOT_SPEED * dt
        if self.rect.bottom < 0:
            self.kill()
