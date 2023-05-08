from sys import exit
import pygame

pygame.init()

screen = pygame.display.set_mode((800,400))
pygame.display.set_caption("Runner")
clock = pygame.time.Clock()

test_font = pygame.font.Font("sprites/font/Pixeltype.ttf",50)


sky_surface = pygame.image.load("sprites/background/Sky.png").convert()
ground_surface = pygame.image.load("sprites/background/ground.png").convert()
text_surface = test_font.render("My game",False,"Black")
text_rect = text_surface.get_rect(center=(400,50))

snail_surface = pygame.image.load("sprites/graphics/snail/snail1.png").convert_alpha()
snail_rect = snail_surface.get_rect(midbottom=(600,305))

player_surface = pygame.image.load("sprites/graphics/Player/player_stand.png").convert_alpha()
player_rect = player_surface.get_rect(midbottom=(50,305))

while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        '''if event.type == pygame.MOUSEBUTTONDOWN:
            print(event.pos)
            '''
        if event.type == pygame.MOUSEBUTTONDOWN:
            if player_rect.collidepoint(event.pos):
                print(event.pos)
    
    screen.blit(sky_surface,(0,0))
    screen.blit(ground_surface,(0,300))
    screen.blit(text_surface,text_rect)
    screen.blit(snail_surface,snail_rect)
    screen.blit(player_surface,player_rect)
    
    snail_rect.left-=3
    
    if snail_rect.left < -80: snail_rect.left = 810
    
    '''if player_rect.colliderect(snail_rect):
        print("col")'''
    
    '''mouse_pos = pygame.mouse.get_pos()
    
    if player_rect.collidepoint(mouse_pos):
        print(pygame.mouse.get_pressed())'''
    
    # draw all elements anad update everything 
    pygame.display.update()
    clock.tick(60)