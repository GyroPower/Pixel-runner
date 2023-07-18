from sys import exit
import time
import pygame
from random import randint,choice 

from Player import player
from Obstacle import obstacle


def display_score():
    current_time= (pygame.time.get_ticks() - start_time)//1000 
    score_surf = test_font.render("Score: "+str(current_time),False,(64,64,64))
    score_rect = score_surf.get_rect(center=(400,50))
    screen.blit(score_surf,score_rect)
    
    return current_time

def collision():
    if pygame.sprite.spritecollide(Player.sprite,obstacles_group,False):
        obstacles_group.empty()
        return False 
    return True  

             
pygame.init()

bg_music = pygame.mixer.Sound("sound/music.wav")
bg_music.set_volume(0.1)
bg_music.play(loops=-1)
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption("Pixel Runner")
clock = pygame.time.Clock()

game_active = False
start_time = 0
test_font = pygame.font.Font("sprites/font/Pixeltype.ttf",50)

# dead = 0
max_score = 0

sky_surface = pygame.image.load("sprites/background/Sky.png").convert()
ground_surface = pygame.image.load("sprites/background/ground.png").convert()

title_surf = test_font.render("Pixel Runner",False,(64,64,64))
title_rect = title_surf.get_rect(center=(400,50))

start_surf = test_font.render("Press space to run",False,(64,64,64))
start_rect = start_surf.get_rect(center=(400,300))

#Obstacles
obstacles_group = pygame.sprite.Group()


#player
Player = pygame.sprite.GroupSingle()
Player.add(player())

player_icon = pygame.transform.rotozoom(pygame.image.load("sprites/graphics/Player/player_stand.png").convert_alpha(),0,2)
player_icon_rect = player_icon.get_rect(midbottom=(400,250))

player_gravity = 0

#timers 

obstacle_timer = pygame.USEREVENT +1
pygame.time.set_timer(obstacle_timer,1500)


prev_time = time.time()
while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        if game_active:
                    
            if event.type == obstacle_timer:
                    
                obstacles_group.add(obstacle(choice(["fly","snail","snail","snail"])))
                    
        else:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_active = True             
                    start_time = pygame.time.get_ticks()
        
                
    if game_active:
                  
        screen.blit(sky_surface,(0,0))
        screen.blit(ground_surface,(0,300))
        
        max_score = display_score()
        
        Player.draw(screen)
        Player.update()
        
        obstacles_group.draw(screen)
        obstacles_group.update()
        
        game_active = collision()
        
        
    else:
        screen.fill("#c0e8ec")

        if max_score > 0:
            score_surf = test_font.render("Score: "+str(max_score),False,(64,64,64))
            score_rect = score_surf.get_rect(center=(400,350))
            screen.blit(score_surf,score_rect)
        
        # player_rect.bottom = 300
        
        screen.blit(title_surf,title_rect)
        
        screen.blit(player_icon,player_icon_rect)
        
        screen.blit(start_surf,start_rect)
        
        
    # draw all elements anad update everything 
    pygame.display.update()
    clock.tick(60)