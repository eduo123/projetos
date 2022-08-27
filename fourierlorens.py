


import pygame


import random

import numpy as np
import math
from math import cos,sin
pygame.init()
azul = (0,0,250)
win = pygame.display.set_mode((1000,1200))



win.fill((45,45,45))
pontos=[]
desenhar = True
pygame.display.update()
while (desenhar==True):

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
             pygame.quit()
             #sys.exit()
        if pygame.key.get_pressed()[pygame.K_a]:
            desenhar = False
        if (pygame.mouse.get_pressed()[0]):
             posicaoagora = pygame.mouse.get_pos()
             pontos.append(posicaoagora)
             print(pontos)

    for j in range(0,len(pontos)-1):
        pygame.draw.line(win,(190,190,190),pontos[j],pontos[j+1],3)
        
        
    pygame.display.update()
    win.fill((45,45,45))


x = [j[0] for j in pontos]
y = [j[1] for j in pontos]
t = len(x)


def int_exp(f,freq):
    f=f
    freq=freq
    L=len(f)
    versor = complex(0,0)
    soma = complex(0,0)
    for j in range(0,L):
        
        versor = complex(math.cos(2*freq*j*math.pi/L),-math.sin(2*freq*j*math.pi/L))
        soma+=versor*f[j]/L
    return soma

    

c = zip(x,y)
print('cCCC', c)




tempo=0
x_draw=0
y_draw=0


            
    

R = list(zip(x,y))
RC = [complex(a[0],a[1]) for a in R]
print('RC', RC)

def distancia(p1,p2):

    return(math.sqrt((p1[0]-p2[0])**2+(p1[1]-p2[1])**2))
coefzero = int_exp(RC,0)

coefspos = [int_exp(RC,n) for n in range(1,1000)]
coefsneg = [int_exp(RC,n*(-1)) for n in range(1,1000)]
running = True
total = 2
print('coefs', coefspos,'coefsneg',coefsneg)


while (running):
    win.fill((40,40,40))
    
    #print(coeficientescomplexos)
    
    #desenhar_fourier(coefs_x,coefs_y)
    rp = [0,0]
    rp2=[0,0]
    n = len(coefspos)
    path =[[0,0]]
    r = complex(0,0)
    for t in range(0,100000):
        r = complex(0,0)
        r+=coefzero
        for c in range(1,total):
            versor = complex(math.cos(0.2*t*c*2*math.pi/(len(RC))),math.sin(0.2*t*c*2*math.pi/(len(RC))))
            versor2 = complex(math.cos(0.2*t*c*2*math.pi/(len(RC))),-math.sin(0.2*t*2*c*math.pi/(len(RC))))
            #print(versor)
            
            rp[0]=int(r.real)
            rp[1] = int(r.imag)
            rp2[0]=int(r.real)
            rp2[1] = int(r.imag)
            r+=coefspos[c-1]*versor
            
            rp[0]=int(r.real)
            rp[1] = int(r.imag)
            pygame.draw.line(win,(200,0,255),rp,rp2,1)
            
            pygame.draw.circle(win,(250,250,250),rp,int(distancia(rp,rp2)),2)
            
            #win.fill((20,20,20))
            rp2[0]=int(r.real)
            rp2[1] = int(r.imag)
            r+=coefsneg[c-1]*versor2
            rp[0]=int(r.real)
            rp[1] = int(r.imag)
            pygame.draw.line(win,(200,0,255),rp,rp2,1)
            pygame.draw.circle(win,(250,250,250),rp,int(distancia(rp,rp2)),2)
            for event in pygame.event.get():
                if event.type==pygame.KEYDOWN:
                    total+=1

            
            



            
            
        rp[0]=int(r.real)
        rp[1] = int(r.imag)
        if (t<10*len(RC)):
            path.append(rp)
        path[t%(10*len(RC))]=[rp[0],rp[1]]
        #print(len(path))
        for t in path:
            pygame.draw.circle(win,(240,240,40),t,1)
        
        
        
        
        pygame.display.update()
        win.fill((45,45,45))
        #win.fill((20,20,20))
    for event in pygame.event.get():
        if event.type==pygame.KEYDOWN:
            total+=1

        



        










                                

                    
