import pygame
import random

class Player:
    def __init__(self):
        self.x = 50
        self.y = 200
        self.rect = pygame.Rect(self.x,self.y,20,20)
        self.color = (random.randint(100,255),random.randint(100,255),random.randint(100,255))
    #Game related functions
    def draw(self,widow):
        pygame.draw.rect(widow,self.color,self.rect)