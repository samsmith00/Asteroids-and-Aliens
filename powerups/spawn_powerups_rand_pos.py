import pygame
import random
from assets.constants import SCREEN_WIDTH, SCREEN_HEIGHT, POWERUPS_RADIUS, POWERUPS_TYPE
from powerups.powerups import PowerUps



class Spawn_Powerups_Rand_Pos(pygame.sprite.Sprite): 
    def __init__(self):
        pygame.sprite.Sprite.__init__(self, self.containers)
        
        self.elapsed_time = 0
        self.spawn_time = random.randint(1, 3)
        
        self.x_spawn_location = random.randrange(POWERUPS_RADIUS, SCREEN_WIDTH - POWERUPS_RADIUS)
        self.y_spawn_location = random.randrange(POWERUPS_RADIUS, SCREEN_HEIGHT - POWERUPS_RADIUS)
        self.type = random.choice(POWERUPS_TYPE)
    
    def spawn(self, position, radius, powerup_type): 
        powerup = PowerUps(position[0], position[1], radius, powerup_type, "rand")
    
    def change_powerup(self): 
        self.spawn_time = random.randint(10, 15)
        self.elapsed_time = 0
        self.x_spawn_location = random.randrange(POWERUPS_RADIUS, SCREEN_WIDTH - POWERUPS_RADIUS)
        self.y_spawn_location = random.randrange(POWERUPS_RADIUS, SCREEN_HEIGHT - POWERUPS_RADIUS)
        self.type = random.choice(POWERUPS_TYPE)
    #  
    def update(self, dt): 
        self.elapsed_time += dt
        
        if self.elapsed_time >= self.spawn_time: 
            self.spawn((self.x_spawn_location, self.y_spawn_location), POWERUPS_RADIUS, self.type)

            self.change_powerup()
        