import pygame
import random
import numpy as np
import math
pygame.init()
azul = (0,0,250)
win = pygame.display.set_mode((1200,1200))







centro = [400,400]
raio  =10000

n=5




def sierrandom(pontos):

    posi = [0,0]
    posi2=[0,0]
    posi = pontos[0]

    for j in range (0,1000):
        posi2 = random.choice(pontos)
        posi = [int((posi[0]+posi2[0])/2), int((posi[1]+posi2[1])/2)]
        pygame.draw.circle(win,(0,200,200),posi,0)
        
        
    

while True:
    for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        n+=1
                        win.fill((0,0,0))
                        print(n)
                    
                    if event.type == pygame.MOUSEBUTTONUP:
                        press = 0
    vertices =[]

    def desenharpoligono(N):
        pos = [0,0]
        pos2 = [0,0]
        for a in range(0,N):
            pos = [400+raio*math.cos(2*a*math.pi/N ),400+raio*math.sin(2*a*math.pi/(N) )]
            vertices.append(pos)
            pos2 = [400+raio*math.cos(2*(a+1)*math.pi/(N) ),400+raio*math.sin(2*(a+1)*math.pi/(N) )]
            pygame.draw.line(win,(250,0,250),pos,pos2,4)
                    
    #desenharpoligono(n)
    #pygame.display.update()                


    def desenharcaminho(pontos, sentido):
        pos1=[0,0]
        pos2 = [0,0]
        tot = len(pontos)
        for f in pontos:
            pos1[0]+=f[0]
            pos1[1]+=f[1]

        pos1[0] = pos1[0]/tot
        pos1[1] = pos1[1]/tot
        posI = pos1
        k = 0
        for a in pontos:
            pos1 = posI

            for d in range(0,10000):
                pos2 = [(pos1[0]+pontos[(d+k)%tot][0])/2,(pos1[1]+pontos[(d+k)%tot][1])/2]
                pygame.draw.line(win,(150,150,250),pos1,pos2,1)
                pos1 = pos2

            k+=1
        k=0
        for a in pontos:
            pos1 = posI

            for d in range(0,10000):
                pos2 = [(pos1[0]+pontos[(100-d-k)%tot][0])/2,(pos1[1]+pontos[(100-d-k)%tot][1])/2]
                pygame.draw.line(win,(0,250,250),pos1,pos2,1)
                pos1 = pos2

            k+=1
        pos = [0,0]
        pos2 = [0,0]
    for a in range(0,n):
        pos = [600+raio*math.cos(2*a*math.pi/n ),600+raio*math.sin(2*a*math.pi/(n) )]
        vertices.append(pos)
        pos2 = [600+raio*math.cos(2*(a+1)*math.pi/(n) ),600+raio*math.sin(2*(a+1)*math.pi/(n) )]
        pygame.draw.line(win,(250,0,250),pos,pos2,4)

    desenharcaminho(vertices,2)
    #sierrandom(vertices)
    pygame.display.update()
    #win.fill((0,0,0))
