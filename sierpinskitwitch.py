
import pygame
import numpy as np
import math
import random

win = pygame.display.set_mode((1400,800))

win.fill([20,20,20])


pygame.display.update()

running = True

triangulo = [[700,100],[100,700],[1300,700]]
n = 3

poligono = [np.array([700+500*math.cos(2*j/n*math.pi),400+500*math.sin(2*j/n*math.pi)]) for j in range(0,n)]
for ponto in poligono:
    pygame.draw.circle(win, (250,250,250), ponto, 5)
pygame.display.update()

ponto = np.array([700,400])
for j in range(1000000):
    numero = random.randrange(0,n)
    ponto = (ponto+poligono[numero])/2
    pygame.draw.circle(win,(250,0,250), ponto, 1)
    if (j%1000==0):
        pygame.display.update()
    


while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    if running == False:
      pygame.quit()
      



