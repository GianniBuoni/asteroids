import pygame
import sys
from constants import *
from asteroid import Asteroid
from asteroidfield import AsteroidField
from player import Player
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    
    # group stufffff!
    asteroids = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    updatables = pygame.sprite.Group()
    
    # asteroids
    Asteroid.containers = (asteroids, drawables, updatables)
    AsteroidField.containers = (updatables)
    asteroid_field = AsteroidField()

    # player
    Player.containers = (drawables, updatables)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # shots
    Shot.containers = (drawables, shots, updatables)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")

        for updatable in updatables:
            updatable.update(dt)
            
        for asteroid in asteroids:
            if asteroid.collides(player):
                print("GAME OVER, MAN! GAME OVER!")
                sys.exit()
            for shot in shots:
                if asteroid.collides(shot):
                    asteroid.kill()
                    shot.kill()

        for drawable in drawables:
            drawable.draw(screen)

        pygame.display.flip()

        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
