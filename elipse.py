#elipse

import pygame
import numpy as np
import math
from numpy import linalg
from math import sin, cos
import time
pygame.init()
azul = (0,0,250)
win = pygame.display.set_mode((1400,800))

win.fill([20,20,20])
pygame.display.update()

A = 400
E = 0.7
B = (A**2*(1-E**2))**0.5

foco1 = np.array([A*E,0])
foco2 = np.array([-A*E,0])
AA = 800
delta = np.array([700,400])
pygame.draw.circle(win,azul, (foco1+delta).astype(int),3)
pygame.draw.circle(win,azul, (foco2+delta).astype(int),3)
win.fill((40,40,40))
pygame.display.update()

pontos = []
ponto = np.array([0,0])
t=0
desenhando = True
pygame.display.update()
time.sleep(2)
while(desenhando):
    ponto = np.array([A*math.cos(t/400),B*math.sin(t/400)])
    ponto = ponto+ delta
    pontos.append(ponto)
    pygame.draw.circle(win,(200,0,200), foco1+delta,3)
    pygame.draw.circle(win,(200,0,200), foco2+delta,3)
    pygame.draw.circle(win,(200,200,200),ponto.astype(int),2)
    pygame.draw.line(win,(100,0,200),ponto.astype(int),(foco1+delta).astype(int),2)
    pygame.draw.line(win,(100,0,200),ponto.astype(int),(foco2+delta).astype(int),2)
    for j in pontos:
        pygame.draw.circle(win,(200,200,200),j,2)
    pygame.display.update()
    win.fill((40,40,40))
    d = np.linalg.norm(ponto-foco1)+np.linalg.norm(ponto-foco2)
    #print(d)
    t+=2
    if (t/400)>=2*math.pi:
        desenhando = False

win.fill((40,40,40))

pygame.draw.circle(win,azul, foco1,3)
pygame.draw.circle(win,azul, foco2,3)
for j in pontos:
    pygame.draw.circle(win,(200,200,200),j,2)
pygame.display.update()
p1 = np.array(foco1)
p2 =np.array(foco1)
v1 = np.array([2**(-0.5),2**(-0.5)])
def laser(p1,v1,A,B,m2):
    #y = m*(x-p1[0])+p1[1]
    m = v1[1]/v1[0]
    
    aq = -(B**2/A**2)-m**2
    bq = 2*m**2*p1[0]-2*m*p1[1]
    cq = B**2-(m**2)*(p1[0]**2)+2*m*p1[0]*p1[1]-p1[1]**2
    xq1 = (-bq-((bq**2-4*aq*cq)**0.5))/(2*aq)
    #print((-B**2+(B*xq1/A)**2))
    #yq1 = (B**2*(1-xq1**2/(A**2)))**0.5
    
    xq2 = (-bq+((bq**2-4*aq*cq)**0.5))/(2*aq)
    yq1 = m*xq1-m*p1[0]+p1[1]
    yq2 = m*xq2-m*p1[0]+p1[1]

    
    
    
    return([np.array([xq1,yq1]),np.array([xq2,yq2])])

def girar(vetor,angulo):
    rot = np.array([[math.cos(angulo),-math.sin(angulo)],[math.sin(angulo),math.cos(angulo)]])
    return (np.dot(rot,vetor))

t = 0
p1 = np.array([0,0])
running = False
while(running):
    v1 = girar(np.array([0.6,0.8]),t)
    t+=0.001
    
    for l in pontos:
        pygame.draw.circle(win,(200,200,200),l,3)
    for m in range(100):
        
        pygame.draw.circle(win,azul, foco1+delta,3)
        pygame.draw.circle(win,azul, foco2+delta,3)
        if (v1[0]>0):
            p2 = laser(p1,v1,A,B,m)[0]
        else:
            p2 = laser(p1,v1,A,B,m)[1]
        
        
        #pygame.display.update()
        #print(p1,p2)
        
        #print(p1,p2)
        n1 = np.array([-2/A**2*p2[0],-2/B**2*p2[1]])
        n1 = n1/np.linalg.norm(n1)
        
        
        v1 =v1-2*np.dot(n1,v1)*n1
    
        pygame.draw.line(win,(200,20,20),(p1+delta).astype(int),(p2+delta).astype(int),2)    
        #v1 = v1/np.linalg.norm(v1)
        p1 = np.array(p2)
            
        
    p1 = np.array([100,0])
    p2 = p1
   
    pygame.display.update()
    win.fill((40,40,40))



def path(P1,V1,AA,BB,comprimento):
    pontos = []
    v1 = V1
    p1 = P1
    A = AA
    B = BB
    p2 =p1
    pontos.append(p1)
    for j in range(0,comprimento):
        if (v1[0]>0):
            p2 = laser(p1,v1,A,B,1)[0]
        else:
            p2 = laser(p1,v1,A,B,1)[1]    
        pontos.append(p2)
        n1 = np.array([-2/A**2*p2[0],-2/B**2*p2[1]])
        n1 = n1/np.linalg.norm(n1)
        
        
        v1 =v1-2*np.dot(n1,v1)*n1
        p1 = np.array(p2)
    return(pontos)


qtd = 8
os_lasers = []
p1 = np.array(foco1)
#for j in range(0,qtd):
 #   v1 = girar(np.array([2**(-0.5),2**(-0.5)]),j/qtd*2*math.pi+0.001)
  #  os_lasers.append(path(p1,v1,A,B,2))
    

#for m in os_lasers:
    #print('m',m)

 #   for c in range(0,len(m)-1):
  #      pontoi = np.array(m[c])
        #print(pontoi)
   #     pontof = np.array(m[c+1])
    #    pygame.draw.line(win,(200,20,200), (pontoi+delta).astype(int),(pontof+delta).astype(int),3)
    
    
pygame.display.update()

class bolinha:
    def __init__(self, pos, velo,A,B,cor):
        self.pos = pos
        self.velo = velo
        self.cor = cor
        self.A = A
        self.B = B
        self.caminho = path(self.pos,self.velo,A,B,100)
        self.colisoes = 0

    def andar(self):
        self.pos =self.pos+ 0.43*self.velo
        #print(self.velo)
        if (np.linalg.norm((self.pos-self.caminho[self.colisoes+1]))<=3.7):
            self.colisoes+=1
            #print('colidiu')
            self.velo = self.caminho[self.colisoes+1]-self.caminho[self.colisoes]
            self.velo = self.velo/(np.linalg.norm(self.velo))
        pygame.draw.circle(win,self.cor,(self.pos+delta).astype(int),3)
    def desenharcaminho(self):
        for m in range(len(self.caminho)-1):
            pygame.draw.line(win,self.cor,(self.caminho[m]+delta).astype(int),(self.caminho[m+1]+delta).astype(int),3)
bolinhas = []
qtd = 500
for j in range(qtd):
    v1 = girar(np.array([2**(-0.5),2**(-0.5)]),math.pi/4+0*j/qtd*2*math.pi/100+0.01)
    p1 = (foco1+foco2)/2+ math.sin(j/qtd*2*math.pi)*(np.array([-400,0]))
    #p1 = foco1+(np.array([-200,0]))
    #p1 = foco1
    #p1 = (2.7*foco1)/2
    #p1 = p1+np.array([-250,10])
    cor = (int(j/qtd*250),0,250-int(j/qtd*250))
    bolinhas.append(bolinha(p1,v1, A,B,cor))
while True:
    for l in pontos:
        pygame.draw.circle(win,(200,0,200),l,3)
    for m in bolinhas:
        for l in pontos:
            pygame.draw.circle(win,(200,0,200),l,3)    
        #m.andar()
        m.desenharcaminho()
        pygame.display.update()
        win.fill((40,40,40))
        time.sleep(0.05)
        
    
    pygame.display.update()
    win.fill((40,40,40))
        




    
    





