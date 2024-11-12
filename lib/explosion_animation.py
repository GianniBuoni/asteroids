import pygame

from lib.constants import EXPLOSION_SPEED

class ExpolsionAnimation(pygame.sprite.Sprite):
    def __init__(self, frames, position, groups) -> None:
        super().__init__(groups)
        self.frames = frames
        self.frames_index = 0
        self.image = self.frames[self.frames_index]
        self.rect = self.image.get_frect(
            center = position
        )

    def update(self, dt):
        self.frames_index += EXPLOSION_SPEED * dt
        if self.frames_index > len(self.frames) - 1:
            self.kill()
        self.image = self.frames[int(self.frames_index)]
