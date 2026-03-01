import pygame
import random
import config
import brain

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
        self.lifespan=0

        #AI
        self.decision=None
        self.vision=[0.5,1,0.5]
        self.inputs=3
        self.fitness=0
        self.brain=brain.Brain(self.inputs)
        self.brain.generate_net()

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
            #increment lifespan
            self.lifespan+=1
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
    @staticmethod
    def closest_pipe():
        for p in config.pips:
            if not p.passed:
                return p



    # AI shenanigans

    def look(self):
        if config.pips:

            #line to top pipe
            self.vision[0]=max(0,self.rect.center[1]-self.closest_pipe().top_rect.bottom) / 500

            #line to mid-pipe
            self.vision[1]=max(0,self.closest_pipe().x - self.rect.center[0]) / 500

            #line to bottom pipe
            self.vision[2]=max(0,self.closest_pipe().bottom_rect.top-self.rect.center[1]) / 500

            # Draw line for visuals
            #top line
            pygame.draw.line(config.window, self.color, self.rect.center,
                             (self.rect.center[0], config.pips[0].top_rect.bottom),2)
            #mid-line
            pygame.draw.line(config.window, self.color, self.rect.center,(config.pips[0].x,self.rect.center[1]),2)

            #bottom line
            pygame.draw.line(config.window, self.color, self.rect.center,
                             (self.rect.center[0], config.pips[0].bottom_rect.top),2)

    def think(self):
        self.decision=self.brain.feed_forward(self.vision)
        if self.decision>.73:
            self.bird_flap()



    def calculate_fitness(self):
        self.fitness=self.lifespan

    def clone(self):
        clone=Player()
        clone.fitness=self.fitness
        clone.brain=self.brain.clone()
        clone.brain.generate_net()
        return clone