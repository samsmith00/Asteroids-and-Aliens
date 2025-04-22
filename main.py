import pygame
import time
import os
from pygame import mixer
from assets.constants import SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN
from player.player import Player
from asteroid.asteroid import Asteroid
from asteroid.astroid_field import AsteroidField
from player.shot import Shot
from game_over_screens.game_over import game_over
from powerups.powerups import PowerUps
from powerups.spawn_powerups_rand_pos import Spawn_Powerups_Rand_Pos
from powerups.spawn_powerups_fall import Spawn_Powerups_fall
from timer import Timer
from enemy.enemy import Enemy
from enemy.spawn_enemy import Spawn_Enemy
from score import ScoreBoard
sound_path = os.path.join("assets", "background_music.mp3") # For music sometime, stops all other sounds though


def run_game(death_count): 
    pygame.init()
    
    screen = SCREEN
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.LayeredUpdates()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    powerups = pygame.sprite.Group()
    enemies = pygame.sprite.Group()


    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()
    
    Shot.containers = (shots, updatable, drawable)

    Player.containers = (updatable, drawable)
    
    PowerUps.containers = (powerups, drawable, updatable)
    Spawn_Powerups_Rand_Pos.containers = updatable
    Spawn_Powerups_fall.containers = updatable
    #spawn_powerups_rand = Spawn_Powerups_Rand_Pos()
    spawn_powerups_fall = Spawn_Powerups_fall()
    
    Timer.containers = (updatable, drawable)
    timer = Timer()
    drawable.change_layer(timer, 5)
    
    Enemy.containers = (enemies, updatable, drawable)
    Spawn_Enemy.containers = updatable
    
    ScoreBoard.containers = (updatable, drawable)
    score_board = ScoreBoard()
    drawable.change_layer(score_board, 5)
    
    
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    spawn_enemy = Spawn_Enemy(player)


    dt = 0
    
    active_powerups_status = {
        "S": False,
        "FS": False,
        "P": False
    }
    active_powerups = {}
    
    
    while True: 
        
        dt = clock.tick(60) / 1000
        
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                return False, death_count
    
        updatable.update(dt)
        
        current_time = time.time()
        
        for powerup, start_time in list(active_powerups.items()):
            if current_time - start_time >= 10:
                active_powerups.pop(powerup)
                active_powerups_status[powerup] = False
                player.powerup_color("default")
            
                if powerup == "FS":
                    player.faster_shooting(False)
                    
        
        for asteroid in asteroids:
            if asteroid.is_colliding(player):
                if active_powerups_status["S"]: 
                    continue
                else: 
                    if game_over(death_count):
                        death_count += 1
                        return  True, death_count
                    return False, death_count
        
            for bullet in shots: 
                if bullet.is_colliding(asteroid) and bullet.origin == "Player":
                    size = asteroid.split()
                    score_board.change_score(size)
                # Remove to make bullets pass through astroids
                    if active_powerups_status["P"]: 
                        continue
                    else: 
                        bullet.kill()  
                        
        for enemy in enemies:
            if enemy.is_colliding(player): 
                if active_powerups_status["S"]: 
                    continue
                else: 
                    if game_over(death_count):
                        death_count += 1
                        return  True, death_count
                    return False, death_count
            for bullet in shots: 
                if bullet.is_colliding(enemy) and bullet.origin == "Player": 
                    enemy.destroy() 
                    score_board.change_score(points="ufo")
                    if active_powerups_status["P"]: 
                        continue
                    else: 
                        bullet.kill() 
                if bullet.is_colliding(player) and bullet.origin != "Player": 
                    if active_powerups_status["S"]: 
                        continue    
                    else: 
                        if game_over(death_count):
                            death_count += 1
                            return True, death_count
                        return False, death_count
              
               
        for powerup in powerups: 
            if powerup.is_colliding(player): 
                timer.start(10)
                powerup.despawn()
                p_up = powerup.get_powerup()
                
                active_powerups[p_up] = time.time()
                
                active_powerups_status[p_up] = True
                player.powerup_color(p_up) 

                if p_up == "FS":
                    player.faster_shooting(active_powerups_status[p_up])
                    
                           
        screen.fill("black")
        for obj in drawable: 
            obj.draw(screen)
            
        pygame.display.flip()


def main(): 
    death_count = 0
    while True: 
        restart, death_count = run_game(death_count)
        if not restart: 
            break
   
    pygame.quit()     
        
        
        

if __name__ == "__main__": 
    main()