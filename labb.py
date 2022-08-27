
import pygame

import pygame
import random

import numpy as np
import math
from math import cos,sin
pygame.init()
azul = (0,0,250)
win = pygame.display.set_mode((1000,1000))
win.fill((20,20,20))



v1 = 2.4090
v2 = 0
m1 = 43.6165*0.001
m2 = 43.5518*0.001
x1 = 400
x2 = 800

deltat = 0.5
k = 0
dados = [32.5,33.45,33.65,33.80,33.15,34.20,34.95,35.10,35.25,38.50,32.10,32.75,33.65,35.55,36.35,32.15,33.40,34.70,34.85,35.10]
for j in dados:
    pygame.draw.circle(win, (200,200,200), [int(10*j), 400],2)
pygame.display.update()
#while True:
    #pygame.draw.circle(win,(100,100,100), [int(x1),400], 10)
    #pygame.draw.circle(win,(100,100,100), [int(x2),400], 10)
    #x1 += v1*deltat
    #x2+=v2*deltat
    #pygame.display.update()
    #win.fill((20,20,20))

    #if ((x2-x1)<(20) and k == 0):
     #   k = 1
        
    #    v2 = 2*m1/(m1+m2)*v1
     #   v1 = (m1-m2)*v1/(m1+m2)

