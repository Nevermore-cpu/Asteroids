import random
from constants import ASTEROID_MIN_RADIUS

def split_asteroid(asteroid):
    """
    Split an asteroid into two smaller pieces moving in different directions.
    
    Args:
        asteroid: The asteroid to split
        
    Returns:
        list: List of new asteroids, or empty list if asteroid is too small
    """
    # Only split if the asteroid is large enough
    if asteroid.radius <= ASTEROID_MIN_RADIUS * 2:
        return []  # Too small to split further
        
    # Calculate new radius for child asteroids
    new_radius = asteroid.radius - ASTEROID_MIN_RADIUS
    
    # Generate random angle between 20 and 50 degrees
    random_angle = random.uniform(20, 50)
    
    # Create two new velocity vectors by rotating the original velocity
    velocity1 = asteroid.velocity.rotate(random_angle)
    velocity2 = asteroid.velocity.rotate(-random_angle)
    
    # Speed up the new asteroids a bit
    velocity1 *= 1.2
    velocity2 *= 1.2
    
    # Create two new asteroids at the current position
    asteroid1 = Asteroid(asteroid.position.x, asteroid.position.y, new_radius)
    asteroid1.velocity = velocity1
    
    asteroid2 = Asteroid(asteroid.position.x, asteroid.position.y, new_radius)
    asteroid2.velocity = velocity2
    
    # Return the new asteroids
    return [asteroid1, asteroid2]