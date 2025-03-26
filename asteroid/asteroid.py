import pygame
import random
import os
from pygame import mixer
from circleShape import CircleShape
from assets.constants import ASTEROID_MIN_RADIUS
image_path = os.path.join("assets", "asteroid.png")
sound_path = os.path.join("assets", "asteroid_explosion.wav")
mixer.init()

size_lookup = {
    ASTEROID_MIN_RADIUS * 3: (150, 150),
    ASTEROID_MIN_RADIUS * 2: (100, 100),
    20: (60, 60)
}


class Asteroid(CircleShape): 
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.size = radius
        self.image = pygame.image.load(image_path).convert_alpha()
        self.explosion_sound = mixer.Sound(sound_path)
        #self.image = pygame.transform.scale(self.image, (150,150)) #150 for large, 100 for medium, 60 for small
        
    def draw(self, screen):
        self.image = pygame.transform.scale(self.image, size_lookup[self.size])
        asteroid = self.image.get_rect(center=self.position)
        screen.blit(self.image, asteroid)

    def update(self, dt):
        self.position += self.velocity * dt
        
    def split(self):
        self.kill()
        self.explosion_sound.play()
        
        if self.radius <= ASTEROID_MIN_RADIUS: 
            return self.size
        
        split_angle = random.uniform(20, 50)
        vect_one = self.velocity.rotate(split_angle)
        vect_two = self.velocity.rotate(-split_angle)
        
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        
        new_asteroid_one = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid_one.velocity = vect_one * 1.6
        
        new_asteroid_two = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid_two.velocity = vect_two * 1.6
        
        return self.size