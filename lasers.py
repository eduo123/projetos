
import pygame

import pygame
import random

import numpy as np
import math
from math import cos,sin
pygame.init()
azul = (0,0,250)
win = pygame.display.set_mode((1000,1000))

def detmin(a2,b2):
    valor = a2[0]*b2[1]-a2[1]*b2[0]
    return (valor)


def cruzou ( seg1, seg2):
  #  print(seg1,seg2)
    a = np.array(seg1)
    b = np.array(seg2)
    c = False
    if (all(a[0]==b[0]) or all(a[0]==b[1]) or all(a[1]==b[0]) or all(a[1]==b[1])):
        c = True
    AB = [seg1[1][0]-seg1[0][0],seg1[1][1]-seg1[0][1]]
    AC = [seg2[0][0]-seg1[0][0],seg2[0][1]-seg1[0][1]]
    AD = [seg2[1][0]-seg1[0][0],seg2[1][1]-seg1[0][1]]
    CD = [seg2[1][0]-seg2[0][0],seg2[1][1]-seg2[0][1]]
    CA = [seg1[0][0]-seg2[0][0],seg1[0][1]-seg2[0][1]]
    CB = [seg1[1][0]-seg2[0][0],seg1[1][1]-seg2[0][1]]
    
    
    if detmin(AB,AC)*detmin(AB,AD)<0 and detmin(CD, CA)*detmin(CD,CB)<0 or c:
        return True
    else:
        return False



class laser:
    def __init__(self, pos, velo):
        self.corpo = np.array([pos for j in range (30)])
        self.velo = velo
        self.cor = (200,0,200)
        
    def andar(self):
        for j in range (0,len(self.corpo)):
            
            if (j==len(self.corpo)-1):
                self.corpo[len(self.corpo)-j-1] = self.corpo[len(self.corpo)-j-1]+self.velo
            else:
                self.corpo[len(self.corpo)-j-1]=self.corpo[len(self.corpo)-j-2]
    def checar_colisão(self, paredes):
        for j in paredes:
            vetorseg = np.array(j[0])-np.array(j[1])
            #print(j,[self.corpo[0],self.corpo[1]])
            if (cruzou(j,[(self.corpo[0]+2*self.velo).astype(list),(self.corpo[0]-0*self.velo).astype(list)]) ):
                self.cor = np.array([random.randrange(0,250),random.randrange(0,250),random.randrange(0,250)])
                #self.velo = -1*self.velo
                vetorvelo = self.velo/np.linalg.norm(self.velo)
                vetorseg = np.array(j[0])-np.array(j[1])
                vetorseg = vetorseg/np.linalg.norm(vetorseg)
                #print(vetorvelo,vetorseg)
                theta = -1*np.arccos(np.dot(vetorvelo,vetorseg))
                
                rot = np.array([[cos(theta), -sin(theta)], [sin(theta), cos(theta)]])
                if (np.linalg.norm(vetorseg+vetorvelo)**2>=np.linalg.norm(vetorseg)**2+np.linalg.norm(vetorvelo)**2):
                    vetorseg = 2*np.dot(vetorvelo,vetorseg)*vetorseg
                    self.velo = vetorseg-vetorvelo
                else:
                    
                    vetorseg = -2*np.dot(vetorvelo,vetorseg)*vetorseg
                    self.velo = -vetorseg-vetorvelo
                    
                    
                self.velo = 5*self.velo/np.linalg.norm(self.velo)
                self.corpo[0] = self.corpo[1]+3*self.velo
                self.corpo[1] = self.corpo[1]+2*self.velo
            

    def desenhar(self):
        for j in range(len(self.corpo)):
            pygame.draw.circle(win, self.cor,self.corpo[j].astype(int), 5-j/20)
        
        
paredes = [[[800,0],[800,800]],[[0,0],[0,800]]]
eixox = 400
eixoy = 200
tamanho = 0
for t in range (1,tamanho+1):
    
    paredes.append([[400+eixox*cos(t/tamanho*2*math.pi),400+eixoy*sin(t/tamanho*2*math.pi)],[400+eixox*cos(((t+1)/tamanho)*2*math.pi),400+eixoy*sin(((t+1)/tamanho)*2*math.pi)]])

lasers = [laser(np.array([400,400]),np.array([5*sin(0.01*j*math.pi*2/10),5*cos(0.01*j*math.pi*2/10)])) for j in range (0,10)]

running = False
contador=1
while (running == False):
    for j in paredes:
        pygame.draw.line(win,(200,200,200), j[0],j[1],1)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONUP:
            posicaoagora = pygame.mouse.get_pos()
            if (contador>1):
                paredes.append([posicaoantiga,posicaoagora])
            contador+=1
            posicaoantiga = posicaoagora
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            contador =1
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = True

contador = 0
while running:
    contador+=1
    for a in paredes:
        pygame.draw.line(win, (0,0,100),a[0],a[1],1)
    
    for jasers in lasers:                        
        jasers.andar()
        jasers.checar_colisão(paredes)
        jasers.desenhar()
    if (contador%1==0):
        pygame.display.update()
    #win.fill((20,20,20))
    


        
        
