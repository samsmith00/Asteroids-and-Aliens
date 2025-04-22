import pygame
import math
import os
import random
from pygame import mixer
from circleShape import CircleShape
from player.shot import Shot
from assets.constants import ENEMY_WAIT_TIME, ENEMY_SHOT_COUNT, SHOT_RADIUS, PLAYER_SHOOT_SPEED, SCREEN_WIDTH, SCREEN_HEIGHT
image_path = os.path.join("assets", "enemy.png")
sound_path = os.path.join("assets", "ufo_explosion.mp3")



class Enemy(CircleShape): 
    mixer.init()
    
    def __init__(self, x, y, radius, velocity, target_position, player):
        super().__init__(x, y, radius)
        
        self.player = player
        
        self.velocity = velocity
        self.target_position = target_position
        self.counter = 0
        
        self.image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (83,83))
        
        self.out_angle = random.randint(0, 365)
        self.out_velocity = random.randint(300, 450)
        self.at_rest = False
        
        self.shot_count = 0
        self.distance = (self.position - self.target_position).length() - radius
        self.moving_shots = random.choice(ENEMY_SHOT_COUNT)
        self.stationary_shots = random.choice(ENEMY_SHOT_COUNT) - 4
        self.moving_shot_points = sorted([random.uniform(0, self.distance) for _ in range(self.moving_shots)], reverse=True)
        
        self.ufo_explosion = mixer.Sound(sound_path)
        self.ufo_explosion.set_volume(1)

    def draw(self, screen): 
        ufo = self.image.get_rect(center=self.position)
        screen.blit(self.image, ufo)
    
    def update(self, dt): 
        current_pos = (self.position - self.target_position).length()
        if current_pos > 3:
            self.position += self.velocity * dt
            self.attack(current_pos, self.at_rest)
        else: 
            self.counter += dt
            self.at_rest = True
            self.position = self.target_position
            self.velocity = pygame.Vector2(0,0)
            if self.counter > 0.5 and self.stationary_shots > 0: 
                self.attack(at_rest = self.at_rest)
                self.counter = 0
                self.stationary_shots -= 1
            
        if self.stationary_shots < 1 and self.at_rest:
            self.at_rest = False
            self.move_out(dt)
            
        
    def move_out(self, dt): 
        # THIS MAKES "JITTER" PHYSICS, COULD BE COOL
        # out_angle = random.randint(0, 365)
        # speed = random.randint(100, 250)
        self.at_rest = False
        self.velocity = pygame.Vector2(1,1) * self.out_velocity
        self.velocity = self.velocity.rotate(self.out_angle)
        self.position += self.velocity * dt
        
        if self.position.x < -2 or self.position.x > SCREEN_WIDTH: 
            self.kill()
        if self.position.y < -2 or self.position.y > SCREEN_HEIGHT: 
            self.kill()
    
    def attack(self, current_pos=None, at_rest=None): 
        if not at_rest: 
            if self.moving_shot_points and abs(current_pos - self.moving_shot_points[0]) <= 5: 
                self.shoot()
                self.moving_shot_points.pop(0)
        else: 
            self.shoot()
            
        
            
        
    def calc_shot(self): 
        player_x, player_y = self.player.get_position()
        shot_angle = math.atan2(player_y - self.position.y, player_x - self.position.x)
        return shot_angle
    
   
        
    def shoot(self): 
        angle_rad = self.calc_shot()
        direction = pygame.Vector2(math.cos(angle_rad), math.sin(angle_rad))
        shot = Shot(self.position.x, self.position.y, SHOT_RADIUS, rotation=0, origin="Enemy")
        shot.velocity = direction * PLAYER_SHOOT_SPEED
        
    
    def destroy(self): 
        self.ufo_explosion.play()
        self.kill()
