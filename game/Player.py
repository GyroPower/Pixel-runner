from typing import Any
import pygame

class player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        player_frame_1 = pygame.image.load("sprites/graphics/Player/player_walk_1.png").convert_alpha()
        player_frame_2 = pygame.image.load("sprites/graphics/Player/player_walk_2.png").convert_alpha() 
        self.player_list_anim = [player_frame_1,player_frame_2]
        self.player_jump_anim = pygame.image.load("sprites/graphics/Player/jump.png").convert_alpha()
        self.player_anim_index = 0
        self.image = self.player_list_anim[self.player_anim_index]
        self.rect = self.image.get_rect(midbottom=(50,300))
        self.gravity = 0
        self.jump_sound = pygame.mixer.Sound("sound/jump.mp3")
        self.jump_sound.set_volume(0.1)
    
    def player_input(self):
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_SPACE] and self.rect.bottom >= 300:
            self.gravity = -20
            self.jump_sound.play()
    
    def apply_gravity(self):
        self.gravity +=1
        
        self.rect.y += self.gravity
        
        if self.rect.bottom >= 300:
            self.rect.bottom = 300 
    
    def update(self):
        self.player_input()
        self.apply_gravity()
        self.player_anim()
        
    def player_anim(self):
        
        if self.rect.bottom < 300: self.image = self.player_jump_anim
        else: 
            self.player_anim_index += 0.1 
            if self.player_anim_index >= len(self.player_list_anim): self.player_anim_index=0 
            self.image = self.player_list_anim[int(self.player_anim_index)] 
            

class player_test(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        player_frame_1 = pygame.image.load("sprites/graphics/Player/player_walk_1.png").convert_alpha()
        player_frame_2 = pygame.image.load("sprites/graphics/Player/player_walk_2.png").convert_alpha() 
        self.player_list_anim = [player_frame_1,player_frame_2]
        self.player_jump_anim = pygame.image.load("sprites/graphics/Player/jump.png").convert_alpha()
        self.player_anim_index = 0
        self.image = self.player_list_anim[self.player_anim_index]
        self.rect = self.image.get_rect(midbottom=(50,300))
        
        self.move_speed = 200
        self.direction = 1
        self.rotation = 0
        self.pos = pygame.math.Vector2(self.rect.topleft)
        
    def player_move(self,dt):
        self.pos.x +=  self.direction * self.move_speed * dt
        self.rect.x = round(self.pos.x)
        if self.rect.x > 1280 or self.rect.x < 0:
            self.direction *=-1
    
    def player_rotate(self,dt):
        self.rotation += 50 * dt 
        self.image = pygame.transform.rotozoom(self.image,self.rotation,1)
    
    def update(self,dt):
        self.player_move(dt)
        self.player_anim(dt)
        self.player_rotate(dt)
       
        
    def player_anim(self,dt):
        
        self.player_anim_index += 10 * dt
        if self.player_anim_index >= len(self.player_list_anim): self.player_anim_index=0 
        self.image = self.player_list_anim[int(self.player_anim_index)] 
       
    