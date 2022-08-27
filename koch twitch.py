
import pygame
import numpy as np
import math
import random
from math import cos, sin
win = pygame.display.set_mode((1400,800))

win.fill([20,20,20])

import time
pygame.display.update()

running = True

triangulo = [[700,100],[100,700],[1300,700]]
n = 7


poligono = [np.array([700+400*math.cos(2*j/n*math.pi),400+400*math.sin(2*j/n*math.pi)]) for j in range(0,n)]
#



















print(poligono[0])





for ponto in poligono:
    pygame.draw.circle(win, (250,250,250), ponto, 5)
pygame.display.update()


segmentos = np.array([[poligono[j%n],poligono[(j+1)%n]] for j in range(len(poligono))])


def koch(seg):
        vetor = (seg[1]-seg[0])
        vetor = vetor/np.linalg.norm(vetor)
        theta = np.deg2rad(random.choice([-90]))
        rot = np.array([[cos(theta), -sin(theta)], [sin(theta), cos(theta)]])
        normal = np.dot(rot ,vetor)
        ponto1 = seg[0]+vetor*np.linalg.norm(seg[1]-seg[0])/3
        ponto2 = seg[0]+2*vetor*np.linalg.norm(seg[1]-seg[0])/3
        #ponto3 = seg[0]+0.5*vetor*np.linalg.norm(seg[1]-seg[0])+1.73/2*normal*np.linalg.norm(seg[1]-seg[0])/3
        ponto3 = seg[0]+0.5*vetor*np.linalg.norm(seg[1]-seg[0])+1.73/2*normal*np.linalg.norm(seg[1]-seg[0])/3
        #ponto4 = seg[0]+(2/3)*vetor*np.linalg.norm(seg[1]-seg[0])-2/2*normal*np.linalg.norm(seg[1]-seg[0])/3
    
        return seg[0],ponto1,ponto3,ponto2,seg[1]
    


pontos = []
for seg in segmentos:
#    print(koch(seg))
    pontos.append(koch(seg))
    pygame.draw.line(win,(250,250,250),seg[0],seg[1],1)
pygame.display.update()
pygame.time.wait(2500)
[print(j, pontos[j]) for j in range(len(pontos))]


for j in pontos:
    for m in j:
        pygame.draw.circle(win,(100,10,100),m,10)
        pygame.display.update()
        
[pygame.draw.line(win,(200,20,200),ponto[j],ponto[j+1]) for j in range(0,4) for ponto in pontos]
pygame.display.update()
#pygame.time.wait(2500)
contador = 200
while running:
    contador+=2
    #print('t',contador)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
          running = False
    if running == False:
      pygame.quit()
    win.fill((20,20,20))
    gerações = 4

    
    z = contador/200
    ponto = [np.array([700+300*cos(2*w/z*math.pi),400+300*sin(2*w/z*math.pi)]) for w in range(int(z)+1)]
    #[pygame.draw.circle(win,(200,200,200), ponto, 1) for ponto in ponto]
    #[pygame.draw.line(win,(200,200,200),ponto[j%len(ponto)],ponto[(j+1)%len(ponto)]) for j in range(len(ponto))]
    #pygame.display.update()
    
    #pygame.time.wait(20)
    #win.fill((20,20,20))

    
    segmentos = np.array([[ponto[j%len(ponto)],ponto[(j+1)%len(ponto)]] for j in range(len(ponto))])
    pontos = []
    for seg in segmentos:
#    print(koch(seg))
        pontos.append(koch(seg))
    for t in range(gerações):
        #print(t,len(pontos))
        segmentos = []
        for j in range(0,len(pontos)):
            for m in range(0,len(pontos[j])-1):
                segmentos.append([pontos[j][m],pontos[j][m+1]])
        pontos = []
        for seg in segmentos:
    #    print(koch(seg))
            pontos.append(koch(seg))
        
        if (t==gerações-1):
            [pygame.draw.line(win,(250,100,250),ponto[j],ponto[j+1]) for j in range(0,4) for ponto in pontos]
            pygame.display.update()
            #running = False
            #print('deu')
    #pygame.time.wait(2500)
                             
                            
    
