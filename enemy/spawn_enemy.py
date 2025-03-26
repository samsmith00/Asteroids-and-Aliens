import pygame
import random
import math
from enemy.enemy import Enemy
from assets.constants import SCREEN_WIDTH, SCREEN_HEIGHT,ENEMY_RADIUS, ENEMY_SPAWN_TIMES 
import player
class Spawn_Enemy(pygame.sprite.Sprite): 
    edges = [
        [
            pygame.Vector2(1,0),
            lambda y: pygame.Vector2(-ENEMY_RADIUS, y * SCREEN_HEIGHT),
        ], 
        [
            pygame.Vector2(-1, 0), 
            lambda y: pygame.Vector2(SCREEN_WIDTH + ENEMY_RADIUS, y * SCREEN_HEIGHT)
        ],
        [
            pygame.Vector2(0, 1),
            lambda x: pygame.Vector2(x * SCREEN_WIDTH, -ENEMY_RADIUS)
        ],
        [
            pygame.Vector2(0,-1),
            lambda x: pygame.Vector2(x * SCREEN_WIDTH, SCREEN_HEIGHT + ENEMY_RADIUS)
        ]
    ]
    
    def __init__(self, player):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.spawn_timer = 0
        self.player = player
        # self.is_enemy = False
        
    def spawn(self, spawn_position, velocity, target_position):
        enemy = Enemy(spawn_position.x, spawn_position.y, ENEMY_RADIUS, velocity, target_position, self.player)
        enemy.velocity = velocity
        ENEMY_DESTROYED = False
        
            
    def calc_spawn_angle(self, spawn_pos, target_pos):
        dx = target_pos[0] - spawn_pos[0]
        dy = target_pos[1] - spawn_pos[1]
        return math.atan2(dy, dx)

            
        
    def update(self, dt): 
        self.spawn_timer += dt 
        
        spawn_time = random.choices(ENEMY_SPAWN_TIMES, weights=[2, 1, 2, 1, 1, 1])[0]

        if self.spawn_timer >= spawn_time: #not self.is_enemy
            self.spawn_timer = 0
            edge = random.choice(self.edges)
            speed = random.randint(180, 300)
            velocity = edge[0] * speed
            spawn_position = edge[1](random.uniform(0,1))
            
            start_x = SCREEN_WIDTH/22
            start_y = SCREEN_HEIGHT/13
            
            target_x_pos = random.uniform(int(start_x), int(SCREEN_WIDTH - start_x))
            target_y_pos = random.uniform(int(start_y), int(SCREEN_HEIGHT - start_y))
            target = pygame.Vector2(target_x_pos, target_y_pos)
            
            angle = self.calc_spawn_angle(spawn_position, target)
            velocity = pygame.Vector2(math.cos(angle), math.sin(angle)) * speed
            
            self.spawn(spawn_position, velocity, target)
        
        
        