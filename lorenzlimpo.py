


import pygame

import pygame
import random

import numpy as np
import math
from math import cos,sin
pygame.init()
azul = (0,0,250)
win = pygame.display.set_mode((1000,1000))

def girarvetorx(vetor,angulo):

    return ([vetor[0]*math.cos(angulo)-vetor[1]*math.sin(angulo),vetor[0]*math.sin(angulo)+vetor[1]*math.cos(angulo),vetor[2]])



win.fill((0,0,0))

pontos = [[10+0.01*random.random(),10+0.01*random.random(),10+0.01*random.random()] for j in range (0,45)]
#pontos = [[20*random.random(),20*random.random(),20*random.random()] for j in range (0,50)]

#cor = (int(100*math.sin(m/1000)+100),100*int(math.sin(m/1000)*math.cos(m/1000)),int(100*math.cos(m/1000)+100))

pontosiniciais = [j for j in pontos]

#cor = []
#for m in range(0,len(pontos)):
#    cor.append([int(100*math.sin(2*math.pi*m/len(pontos))+100),100*int(2*math.sin(2*math.pi*m/len(pontos))*math.cos(2*math.pi*m/len(pontos))),int(100*math.cos(2*math.pi*m/len(pontos))+100)])
#cor = [[250,0,0],[0,0,250]]
pontos2 =pontos


cor = [[int(250*random.random()),int(20*random.random()),int(250*random.random())] for p in pontos]

k=0
#for j in range(len(cor)):
   #k = random.random()
   #if k>0.5:
       #cor[j] = [0,0,0]
   #else:
#       cor[j] = [250,250,250]
       
    

#cor = [[random.choice([0,0,0,0,255]),random.choice([0,0,0,0,0,255]),random.choice([0,0,0,0,0,255])] for p in pontos]
print(pontos)


sigma = 10
rho=30
beta =8/3
dt = 0.01

def lorents(ponto,sigma,rho,beta,dt):
    x = ponto[0]
    y = ponto[1]
    z = ponto[2]
    dx = dt*sigma*(y-x)
    dy = dt*(x*(rho-z)-y)
    dz = dt*(x*y-beta*z)
    

    return [x+dx,y+dy,z+dz]
pontostotais = []
#for j in pontos:
#    print(lorents(j,sigma,rho,beta,dt))
#desenhar = [0,0]

girarpontos = [[0,0,0] for m in pontos]

angulo =0 
for l in range(0,1):
    angulo+=0.05
    
    for k in range (0,20000):
        pygame.display.update()
        for m in range(len(pontos)):
            
            #angulo+=0.01
            desenhar = [int(15*girarvetorx(pontos[m],angulo)[0])+400,int(15*girarvetorx(pontos[m],angulo)[2])+100]
            desenhar[1]=800-desenhar[1]
            pygame.draw.circle(win,cor[m],desenhar,1)
            pontos[m] = lorents(pontos[m],sigma,rho,beta,dt)
            #pygame.display.update()
        
        #pontostotais.append([pontos])

    pygame.display.update()
    win.fill((0,0,0))
    for j in range(0,len(pontos)):
        pontos[j]=pontosiniciais[j]
    #print(pontos[j])
    
    
        
            
        
 



    
        

    
