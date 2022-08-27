import pygame
import numpy as np
import math
import random
from math import cos, sin
win = pygame.display.set_mode((1400,800))

win.fill([20,20,20])



def mand(zz):
    z = zz
    c = zz
    #c = 0.1+0.1j
    count = 0
    if (np.absolute(z)<0.01):
            return 0
    else:
        for t in range(0,100):
            count+=1
            a = np.real(z)
            b = np.imag(z)
            
            z =z**2+c
            if (np.absolute(z)>=10):
                return count/100
            if (np.absolute(z)<=0.001):
                return count/100
            if (t==100-1):
                return count/100
import time
pygame.display.update()

running = True

teste = mand(1+1.5j)
print(teste)
mands = []
mands = [mand((x-50)/2+(y-50)/2*(0+1j)) for x in range(0,100) for y in range(0,100)]
for x in range(-1000,400):
    for y in range(-500,400):
        v = complex(x/800,y/800)
        v0 = complex(0,0)
        v = v+v0
        l = mand(v)
        
        cor = 250*l
        pygame.draw.circle(win,(cor,cor,cor),[x+1000,y+500],2)
    if (x%80==0):
        pygame.display.update()
pygame.display.update()

#[print(mands[k]) for k in range(len(mands))]
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if running == False:
        pygame.quit()
        




teste = mand(1+1.5j)
print(teste)

            
        
        
    
