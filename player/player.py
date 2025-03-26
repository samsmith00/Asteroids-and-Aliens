import pygame
import os
from pygame import mixer
from circleShape import CircleShape
from player.shot import Shot
from assets.constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOOT_SPEED, SHOOT_COOLDOWN
image_path = os.path.join("assets", "player_ship.png")
sound_path = os.path.join("assets", "lazer1.mp3")

mixer.init()


powerup_colors = {
        "default": "#FFFFFF",
        "S": "#57b9ff",
        "FS": "#EE4B2B", 
        "P": "#228B22",
    }

class Player(CircleShape): 
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)   
        
        self.rotation = 0
        self.timer = 0
        self.shooting_val = 0
        self.shoot_cooldown = SHOOT_COOLDOWN
        self.color = powerup_colors["default"]
        self.og_img = pygame.image.load(image_path).convert_alpha()
        self.og_img = pygame.transform.scale(self.og_img, (50,50))
        self.img = self.og_img
        self.powerup_active = False
        
        self.lazer_sound = mixer.Sound(sound_path)
        
    def triangle(self):
        forward = pygame.Vector2(0, -1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        
        return [a, b, c] 
    
    def bullet_spawn_point(self): 
        forward = pygame.Vector2(0, -1).rotate(self.rotation)
        bullet_point = self.position + forward * (self.radius + 7)
    
        return bullet_point
    
    def draw(self, screen): 
        #ygame.draw.polygon(screen, color=pygame.Color(self.color), points=self.triangle(), width=0)
        # self.image = pygame.transform.rotate(self.rotation)
        self.img = pygame.transform.rotate(self.og_img, -self.rotation)
        player = self.img.get_rect(center=self.position)
        screen.blit(self.img, player)
        if self.powerup_active: 
            pygame.draw.circle(screen, self.color, self.position, self.radius, 5)
        
    def rotate(self, dt): 
        self.rotation += PLAYER_TURN_SPEED * dt
    
    def move(self, dt):
        forward = pygame.Vector2(0, -1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
        

    def shoot(self):
        shot = Shot(self.bullet_spawn_point()[0], self.bullet_spawn_point()[1], self.radius, self.rotation, origin="Player")
        shot.velocity = pygame.Vector2(0,-1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
        self.timer = self.shoot_cooldown
        
    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.timer -= dt

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
            
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]: 
            self.move(-dt)
         
        # Change this to make shooting faster    
        if keys[pygame.K_SPACE]:
            if self.timer <= self.shooting_val:
                self.shoot()
                self.lazer_sound.play()


    def powerup_color(self, powerup="default"): 
        self.color = powerup_colors[powerup]
        self.powerup_active = True
        if powerup == "default":
            self.powerup_active = False
        
    
    def faster_shooting(self, active):             
        if active: 
            self.shoot_cooldown = 0.1
        else:
            self.shoot_cooldown = SHOOT_COOLDOWN
            
    def get_position(self): 
        return self.position