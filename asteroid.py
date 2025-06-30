import pygame
import random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def split(self):
        self.kill()
        if self.radius == ASTEROID_MIN_RADIUS:
            return
        
        new_angle = random.uniform(20, 50)
        asteroid1_angle = self.velocity.rotate(new_angle)
        asteroid2_angle = self.velocity.rotate(-new_angle)
        asteroid_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid1 = Asteroid(self.position.x, self.position.y, asteroid_radius)
        asteroid1.velocity = asteroid1_angle * 1.2
        asteroid2 = Asteroid(self.position.x, self.position.y, asteroid_radius)
        asteroid2.velocity = asteroid2_angle * 1.2
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
        
    def update(self, dt):
        self.position += self.velocity * dt