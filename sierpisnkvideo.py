

import pygame
import numpy as np
import random
screen = pygame.display.set_mode((1400,800))

screen.fill([40,40,40])


pygame.display.update()




triangulo = np.array([[700,100],[100,700],[1300,700]])

for ponto in triangulo:
    pygame.draw.circle(screen, (0,0,250), ponto, 3)
pygame.display.update()

ponto = (triangulo[0]+triangulo[1]+triangulo[2])/3

pygame.draw.circle(screen,(250,0,0), ponto,3)
pygame.display.update()


for c in range (0,100000):
    numero = random.randrange(0,3)

    ponto = (ponto+triangulo[numero])/2
    cor =[100+random.randrange(0,150) for n in range (0,3)]
    pygame.draw.circle(screen,cor, ponto, 1)
    pygame.display.update()


