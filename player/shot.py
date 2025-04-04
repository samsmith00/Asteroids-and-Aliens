import pygame
from circleShape import CircleShape
from assets.constants import BULLET_RECT_SIZE, SHOT_RADIUS, SCREEN_WIDTH, SCREEN_HEIGHT

powerup_colors = {
        "default": "#FFFFFF",
        "S": "#57b9ff",
        "FS": "#EE4B2B", 
        "P": "#228B22",
    }

class Shot(CircleShape):
    def __init__(self, x, y, radius, rotation, origin):
        super().__init__(x, y, radius)
        
        self.rotation = rotation
        self.origin = origin
        self.color = powerup_colors["default"] if self.origin == "Player" else powerup_colors["FS"]
        
    def rectangle_bullet(self): 
        forward = pygame.Vector2(0, -1).rotate(self.rotation) * BULLET_RECT_SIZE[1] / 2 
        side = pygame.Vector2(0, 1).rotate(self.rotation + 90) * BULLET_RECT_SIZE[0] / 2
        
        a = self.position + forward - side
        b = self.position + forward + side
        c = self.position - forward + side
        d = self.position - forward - side
        
        return [a,b,c,d]
       
    def draw(self, screen):
        if self.origin == "Player":
            pygame.draw.polygon(screen, self.color, points=self.rectangle_bullet())
        else: 
            pygame.draw.circle(screen, self.color, self.position, SHOT_RADIUS)
   
    def update(self, dt):
        self.position += self.velocity * dt
        if self.position.x > SCREEN_WIDTH or self.position.y > SCREEN_HEIGHT: 
            self.kill()
        
    
    
