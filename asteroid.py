import pygame
from constants import ASTEROID_MIN_RADIUS
from circleshape import CircleShape
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        print("Splitting asteroid")
        print(self.radius)
        if self.radius == ASTEROID_MIN_RADIUS:
            return
        asteroid_angle = random.uniform(20, 50)
        rotated_velocity_1 = self.velocity.rotate(asteroid_angle)
        rotated_velocity_2 = self.velocity.rotate(-asteroid_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        Asteroid(self.position.x, self.position.y, new_radius).velocity = rotated_velocity_1
        Asteroid(self.position.x, self.position.y, new_radius).velocity = rotated_velocity_2


