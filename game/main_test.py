import pygame 
import sys, time 

from Player import player_test

pygame.init()


screen = pygame.display.set_mode((1280,720))

clock = pygame.time.Clock()


Player = pygame.sprite.GroupSingle()

Player.add(player_test())

previous_time = time.time()

while True:
    
    dt = time.time() - previous_time
    previous_time = time.time()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    screen.fill("white")
    
    Player.draw(screen)
    
    Player.update(dt)
    
    pygame.display.update()
    
    clock.tick(1000)
    
