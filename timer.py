import pygame
from assets.constants import SCREEN_WIDTH, SCREEN_HEIGHT



class Timer(pygame.sprite.Sprite): 
    def __init__(self):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.start_time = 0
        self.font = pygame.font.SysFont("Arial", 45)
        self.time_elapsed = 0
        self.color = "red"
        self.active = False
        self.x = SCREEN_WIDTH / 1.07
        self.y = SCREEN_HEIGHT / 9
        self.rect = pygame.Rect(self.x, self.y, 20, 15)
        
    
    def start(self, duration=10): 
        self.start_time = duration
        self.active = True
        
    def draw(self, screen): 
        if self.active:
            text_surface = self.font.render(str(self.start_time), True, self.color)
            screen.blit(text_surface , (self.x,self.y))
            pygame.draw.rect(screen, self.color, ((self.x-45), self.y - 10, 110, 70), 2)
            
    
    def update(self, dt): 
        if not self.active: 
            return
        
        self.time_elapsed += dt
        
        if self.time_elapsed >= 1: 
            self.start_time -= 1
            self.time_elapsed = 0
            
        if self.start_time <= 0: 
            self.active = False
                
            