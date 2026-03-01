import pygame
import random
import config

class Player:
    def __init__(self):
        #Bird
        self.x = 50
        self.y = 200
        self.rect = pygame.Rect(self.x,self.y,20,20)
        self.color = (random.randint(100,255),random.randint(100,255),random.randint(100,255))
        self.vel=0
        self.flap = False
        self.alive = True

        #AI
        self.decision=None


    #Game related functions
    def draw(self,widow):
        pygame.draw.rect(widow,self.color,self.rect)

    def ground_collision(self,ground):
        return pygame.Rect.colliderect(self.rect,ground)

    def sky_collision(self):
        return bool(self.rect.y<30)

    def pipe_collision(self):
        for p in config.pips:
            return pygame.Rect.colliderect(self.rect,p.top_rect) or \
                   pygame.Rect.colliderect(self.rect,p.bottom_rect)

    def update(self,ground):
        if not (self.ground_collision(ground) or self.pipe_collision()):
            #gravity
            self.vel+= 0.25
            self.rect.y += self.vel
            if self.vel>5:
                self.vel=5
        else:
            self.vel=0
            self.alive = False
            self.flap = False

    def bird_flap(self):
        if not self.flap and not self.sky_collision():
            self.flap = True
            self.vel=-5
        if self.vel >=3:
            self.flap = False

    # AI shenanigans
    def think(self):
        self.decision= random.uniform(0,1)
        if self.decision>.73:
            self.bird_flap()

