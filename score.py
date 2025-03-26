import pygame
from assets.constants import POINT_VALUES

class ScoreBoard(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(self.containers) 

        self.x, self.y = 10, 10 
        self.width, self.height = 200, 75 
        self.color = "#00CED1"

        self.font = pygame.font.SysFont("Arial", 45)
        self.text = "Score: "  
        self.score = 0
        
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height) 

    def draw(self, screen): 
        """Draws the scoreboard with text and border"""
        text_surface = self.font.render(self.text, True, self.color)
        score = self.font.render(str(self.score), True, self.color)
        screen.blit(text_surface, (self.x + 10, self.y + 10)) 
        screen.blit(score, (self.x + 150, self.y + 10)) 
        
    def change_score(self, points): 
        self.score += POINT_VALUES[points]
