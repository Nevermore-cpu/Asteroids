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
    
    # Calculate new radius for child asteroids
        new_radius = self.radius - ASTEROID_MIN_RADIUS
    
    # Generate random angle between 20 and 50 degrees
        random_angle = random.uniform(20, 50)
    
    # Create two new velocity vectors by rotating the original velocity
        velocity1 = self.velocity.rotate(random_angle)
        velocity2 = self.velocity.rotate(-random_angle)
    
    # Speed up the new asteroids a bit
        velocity1 *= 1.2
        velocity2 *= 1.2
    
    # Create two new asteroids at the current position and add them to groups
        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid1.velocity = velocity1
        for group in self.groups():
            group.add(asteroid1)
    
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2.velocity = velocity2
        for group in self.groups():
            group.add(asteroid2)
