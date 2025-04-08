import pygame
import random
from assets.constants import SCREEN_WIDTH, SCREEN_HEIGHT, POWERUPS_RADIUS, POWERUPS_TYPE
from powerups.powerups import PowerUps



class Spawn_Powerups_fall(pygame.sprite.Sprite): 

    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self, self.containers)
        
        self.speed = 5
        
        self.type = random.choice(POWERUPS_TYPE)
        self.elapsed_time = 0
        self.spawn_time = random.randint(1,3)
        
        self.edge = [
            pygame.Vector2(0, -1), 
            (random.uniform(POWERUPS_RADIUS, SCREEN_WIDTH - POWERUPS_RADIUS), -POWERUPS_RADIUS)
    ]
    
    
    def spawn(self, powerup_type): 
        PowerUps(self.edge[1][0], self.edge[1][1], POWERUPS_RADIUS, powerup_type, "fall")
        
    def change_powerup(self): 
        self.spawn_time = random.randint(15, 30)
        self.elapsed_time = 0
        self.type = random.choice(POWERUPS_TYPE)
        
    def update(self, dt): 
        self.elapsed_time += dt 
        
        if self.elapsed_time >= self.spawn_time: 
            self.spawn(self.type)
            
            self.change_powerup()