import pygame
import os
from circleShape import CircleShape
from assets.constants import SCREEN_WIDTH, SCREEN_HEIGHT


class PowerUps(CircleShape): 
    def __init__(self, x, y, radius, powerup_type, origin):
        super().__init__(x, y, radius)
        self.x = x
        
        self.type = powerup_type   
        self.text_font = pygame.font.SysFont("Arial", 25)     
        self.time_elapsed = 0
        self.countdown = 0
        self.countdown_text = 10
        
        self.rand_or_fall = origin
        
        self.lookup = {
            "Faster Shooting": "FS",
            "Piercing": "P", 
            "Shield": "S", 
            }

        self.image_lookup = {
            "FS": os.path.join("assets", "faster_shooting.png"), 
            "P": os.path.join("assets", "piercing.png"), 
            "S": os.path.join("assets", "shield.png")
        }
        
        self.image_path = self.image_lookup[self.lookup[powerup_type]]
        self.image = pygame.image.load(self.image_path).convert_alpha()
        
        print(self.rand_or_fall)
        print(self.image_path)
        print(self.image)
        
    def draw_text(self, screen, text, font, x, y, color): 
        img = font.render(text, True, color)
        screen.blit(img, (x, y))
    
    def draw(self, screen):
        if self.rand_or_fall == "rand": 
            self.text_font = pygame.font.SysFont("Arial", 21 if self.lookup[self.type] == "FS" else 25)

            x_pos = self.position.x - (13 if self.lookup[self.type] == "FS" else 8)
            y_pos = self.position.y - (12 if self.lookup[self.type] == "FS" else 13)
                
            pygame.draw.circle(screen, (255,215,0), self.position, self.radius, 2)
            self.draw_text(screen, self.lookup[self.type], self.text_font, x_pos, y_pos, color=(255, 215, 0))
        else:
            pygame.draw.circle(screen, (255, 215, 0), self.position, self.radius, 0)
            image = pygame.transform.scale(self.image, (int(self.radius * 1.5), int(self.radius * 1.5)))
            image_rect = image.get_rect(center=self.position)
            screen.blit(image, image_rect)
            
    def update(self, dt): 
        self.time_elapsed += dt
        if self.rand_or_fall == "rand":
            if self.time_elapsed > 5: 
                self.despawn()
        else: 
            if self.time_elapsed >= 1:
                self.position.y += 2
        
        if self.position.y > SCREEN_HEIGHT: 
            self.despawn()
                
    
    def despawn(self): 
        self.kill()
        
    def get_powerup(self): 
        return self.lookup[self.type]
    
    def get_powerup_countdown_corrdinates(self): 
        x = SCREEN_WIDTH/2 + SCREEN_WIDTH/4
        y = SCREEN_HEIGHT/2 + SCREEN_HEIGHT/4
        
        return (x,y)
    
        
        
        


        
        
        
        