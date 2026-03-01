import pygame
import components
win_width = 550
win_height = 720
window=pygame.display.set_mode((win_width,win_height))
pygame.display.set_caption("my flappy bird")
ground = components.Ground(win_width)
population_size=10
components.Pipes.width=15
components.Pipes.opening=100
pips = []
