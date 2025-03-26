import pygame
import time
from circleShape import CircleShape
from assets.constants import SCREEN_WIDTH, SCREEN_HEIGHT

lookup = {
    "Faster Shooting": "FS",
    "Piercing": "P", 
    "Shield": "S", 
    }

class PowerUps(CircleShape): 
    def __init__(self, x, y, radius, powerup_type):
        super().__init__(x, y, radius)
        
        self.type = powerup_type   
        self.text_font = pygame.font.SysFont("Arial", 25)     
        self.time_elapsed = 0
        self.countdown = 0
        self.countdown_text = 10

    def draw_text(self, screen, text, font, x, y, color): 
        img = font.render(text, True, color)
        screen.blit(img, (x, y))
    
    def draw(self, screen):
        self.text_font = pygame.font.SysFont("Arial", 21 if lookup[self.type] == "FS" else 25)

        x_pos = self.position.x - (13 if lookup[self.type] == "FS" else 8)
        y_pos = self.position.y - (12 if lookup[self.type] == "FS" else 13)
            
        pygame.draw.circle(screen, (255,215,0), self.position, self.radius, 2)
        self.draw_text(screen, lookup[self.type], self.text_font, x_pos, y_pos, color=(255, 215, 0))
    
    def update(self, dt): 
        self.time_elapsed += dt
        if self.time_elapsed > 5: 
            self.despawn()
    
    def despawn(self): 
        self.kill()
        
    def get_powerup(self): 
        return lookup[self.type]
    
    def get_powerup_countdown_corrdinates(self): 
        x = SCREEN_WIDTH/2 + SCREEN_WIDTH/4
        y = SCREEN_HEIGHT/2 + SCREEN_HEIGHT/4
        
        return (x,y)
    
        
        
        


        
        
        
        