# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0

    #Groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    #Containers
    AsteroidField.containers = (updatable,)
    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable, drawable)
    Shot.containers = (shots, updatable, drawable)

    #Entities
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    asteroid_field = AsteroidField()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill('#16161D')
                
        dt = clock.tick() / 1000
        for item in updatable:
            item.update(dt)

        for asteroid in asteroids:
            has_collided = asteroid.check_collision(player)
            if has_collided:
                sys.exit()

        for asteroid in asteroids:
            for shot in shots:
                has_been_shot = asteroid.check_collision(shot)
                if has_been_shot:
                    shot.kill()
                    asteroid.split()
        

        for item in drawable:
            item.draw(screen)

        pygame.display.flip()

if __name__ == "__main__":
        main()
