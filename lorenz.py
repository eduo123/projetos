


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
deltat = 0.0001
p = np.array([0,1,1.05])
p2=p
xnovo=400
ynovo=400
znovo=400
alfa=10
beta = 28.0
gama= 8.0/3.0
#print (p2)

for m in range(100000000):
    xnovo=deltat*float(alfa*(p[1]-p[0]))
    ynovo=deltat*float((p[0]*(beta-p[2])-p[1]))
    znovo=deltat*float((p[0]*p[1]-gama*p[2]))
 #   print('novo', [xnovo,ynovo,znovo])
    
    p2=  p2+ np.array([xnovo,ynovo,znovo])
    #print (p2)
    #print(p[0],p[1],[p2[0],p2[1]])
    cor = (int(100*math.sin(m/1000)+100),100*int(math.sin(m/1000)*math.cos(m/1000)),int(100*math.cos(m/1000)+100))
    
    pygame.draw.line(win,cor, [10*p[2]+400,10*p[0]+400],[int(10*p2[2])+400,int(10*p2[0]+400)],1)
    #pygame.draw.line(win,(200,0,200), [10*p[1]+400,10*p[0]+400],[int(10*p2[1])+400,int(10*p2[0]+400)],1)
    #pygame.draw.line(win,(200,0,0), [10*p[2]+400,10*p[1]+400],[int(10*p2[2])+400,int(10*p2[1]+400)],1)
    if (m%10000==0):
        pygame.display.update()
    p = p2
    if (m==100000-1):
        print('acabei')
    if (m%100==0):
        pygame.display.update()
        #win.fill((0,0,0))
        
    
    

pygame.display.update()



