import pygame

import pygame
import random

import numpy as np
import math
from math import cos,sin
pygame.init()
azul = (0,0,250)
win = pygame.display.set_mode((1000,1000))



win.fill((0,0,0))


pygame.display.update()






def collat_draw(n,pos,velo1):
    posi = pos
    velo = velo1
    theta = np.deg2rad(1.2)

    rot = np.array([[cos(theta), -sin(theta)], [sin(theta), cos(theta)]])
    c = n
    angulo = 0.2
    
    #velo = np.array([2,-2])
    cor = random.randint(0,250)
    cor2 = random.randint(0,250)
    cor3 = random.randint(0,2)
    while(c!=1):
        #theta=-theta
        
        if (c%2==0):
            rot = np.array([[cos(-theta), -sin(-theta)], [sin(-theta), cos(-theta)]])
            velo = np.dot(rot,velo)
            posf = posi+velo
            pygame.draw.line(win,(cor,cor3,cor2),posi, posf,1)
            c = c/2
            
            posi = posf
        else:
            rot = np.array([[cos(theta), -sin(theta)], [sin(theta), cos(theta)]])
            velo = np.dot(rot,velo)
            posf = posi+velo
            pygame.draw.line(win,(cor,cor3,cor2),posi, posf,1)
            c = (3*c+1)/2
            posi=posf
            
    if (c==1):
        return ('pronto')

total = 7
ang = np.deg2rad(360/total)
rotaqui= np.array([[cos(ang), -sin(ang)], [sin(ang), cos(ang)]])
veloaqui = np.array([-1,0.2])
for j in range(200000000,1100000000):
    veloaqui = np.array([1,0.2])
    for raios in range(0,total):
        veloaqui = np.dot(veloaqui,rotaqui)
        collat_draw(total*j+raios,np.array([400,400]), veloaqui)
    
    
    
    pygame.display.update()
    #win.fill((0,0,0))



    
