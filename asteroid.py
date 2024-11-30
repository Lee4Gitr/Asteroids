import pygame
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        theta = random.uniform(20, 50)
        
        velocity = self.velocity.rotate(theta)

        asteroid_size = self.radius - ASTEROID_MIN_RADIUS

        # Refactor this to spawn n number of children, depending on a constant,
        # and at an evenly divided angle theta.
        for i in range(0, 2):
            escape_angle_modifier = 1 if i % 2 == 0 else - 1
            asteroid = Asteroid(self.position.x, self.position.y, asteroid_size)
            asteroid.velocity = velocity * escape_angle_modifier * 1.2 
