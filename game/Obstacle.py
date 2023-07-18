import pygame 
from random import randint

class obstacle(pygame.sprite.Sprite):
    
    def __init__(self,type):
        super().__init__() 
        
        if type == "fly": 
            fly_frame_1 = pygame.image.load("sprites/graphics/fly/Fly1.png").convert_alpha()
            fly_frame_2 = pygame.image.load("sprites/graphics/fly/Fly2.png").convert_alpha()
            self.frames = [fly_frame_1,fly_frame_2]
            y_pos = 210
        elif type == "snail":
            #snail
            snail_frame_1 = pygame.image.load("sprites/graphics/snail/snail1.png").convert_alpha()
            snail_frmae_2 = pygame.image.load("sprites/graphics/snail/snail2.png").convert_alpha()
            self.frames = [snail_frame_1,snail_frmae_2]
            y_pos = 300
        self.obstacle_index = 0 
        
        self.image = self.frames[self.obstacle_index]
        self.rect = self.image.get_rect(midbottom=(randint(900,1200),y_pos))
        
    def obs_animation(self):
        self.obstacle_index +=0.1
        if self.obstacle_index >= len(self.frames): self.obstacle_index = 0
            
        self.image = self.frames[int(self.obstacle_index)]
        self.rect.x -=5
            
    def update(self):
        self.obs_animation()
        self.destroy()
        
    def destroy(self):
        if self.rect.x <= -100:
            self.kill()
        
            