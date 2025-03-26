import pygame
from pygame import mixer
import os
from assets.constants import SCREEN, SCREEN_WIDTH, SCREEN_HEIGHT, GAME_OVER_TEXT, PLAY_AGAIN_TEXT, QUIT_TEXT
img_path = os.path.join("assets", "scary_face.png")
evil_scream = os.path.join("assets", "scary_sound.mp3")
evil_laugh = os.path.join("assets", "evil_laugh.mp3")

pygame.init()
mixer.init()

text_font = pygame.font.SysFont("Arial", 40)
screen = SCREEN

scary_face = pygame.image.load(img_path).convert_alpha()
scary_face = pygame.transform.scale(scary_face, (900, 700))
scary_rect = scary_face.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2))


scream_sound = mixer.Sound(evil_scream)
laugh_sound = mixer.Sound(evil_laugh)

mixer.music.set_volume(0.7) 

def fade(): 
    for alpha in range(255, 0, -1):
        screen.fill((0,0,0))
        scary_face.set_alpha(alpha)
        screen.blit(scary_face, scary_rect.topleft)
        pygame.display.flip()
        pygame.time.delay(10)
         
        

def draw_text_helper(text, font, x, y):
    img = font.render(text, True, "red")
    text_rect = img.get_rect(center=(x,y))
    screen.blit(img, text_rect.topleft)
    
def draw_text(): 
    draw_text_helper(GAME_OVER_TEXT, text_font, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 100)
    draw_text_helper(PLAY_AGAIN_TEXT, text_font, SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    draw_text_helper(QUIT_TEXT, text_font, SCREEN_WIDTH/2, SCREEN_HEIGHT/2 + 70)
    


def game_over(death_count): 
    if death_count < 1:
        screen.fill(color=(0,0,0))
        # scream_sound.play()
        laugh_sound.play()
        fade()
        draw_text()
    else: 
        screen.fill(color=(0,0,0)) # normal red color=(139,0,0)
        draw_text()
        scary_face.set_alpha(50)
        screen.blit(scary_face, scary_rect.topleft)
        laugh_sound.play()
   
    pygame.display.flip()
    
    waiting = True
    while waiting: 
        keys = pygame.key.get_pressed()
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                return False
            if keys[pygame.K_q]:
                laugh_sound.stop()
                scream_sound.stop()
                return False
            if keys[pygame.K_r]:
                laugh_sound.stop()
                scream_sound.stop()
                waiting = False
                return True
                    
                    
        
        
