


import pygame
import random
import math

import numpy as np

from numpy import save
from numpy import load

def detmin(a2,b2):
    valor = a2[0]*b2[1]-a2[1]*b2[0]
    #print(valor)
    return (valor)

def sigmoid(x):
    #return (1/(1+math.e**(0-x)))
    return (math.tanh(x))

valores = np.ones((5,5))
valores*=2

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


o = [1,2,3]
on = np.array(o)
#print (valores)
contador = 1
inputs = np.ones(5)
valores = np.ones((5,5))
pesos = np.random.rand(5,5,5)
#print (len(valores))
#print(len(pesos))
def flow(i,v,p):
    v2=v
    for j in range (len(p)):
        if (j==0):
            v[j]=i
        else:
            v2[j] = sigmoid(np.matmul(v2[j-1],p[j-1]).sum())
           
             
    return (v2[len(v)-1])

#
        

vidamax = 0
pesosmelhores =[]
    
k=0
premio = np.random.rand(2)


parede=[]

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
screen = pygame.display.set_mode((600, 800), 0, 32)
screen.fill(BLACK)
def girar(vetor,angulo):
    c,s = np.cos(angulo),np.sin(angulo)
    R = np.array(((c,-s),(s,c)))
    vetor2 = np.matmul(vetor,R).tolist()
    #print('vetor2', vetor2)
    return (vetor2)


def laser(posi,velo, angulo,pesoangulo,paredes):
    step = 1.0
    pos2 = np.array(posi)
    velo2 = np.array(girar(np.array(velo),angulo))
    pos3 = pos2+0.4*pesoangulo*velo2
    
    bateu = False
    #pygame.draw.line(screen,(0,200,200),pos2.astype(int).tolist(),pos3.astype(int).tolist(),1)
  #  print('pos2', pos2)
   # print('velo2', velo2)
    
    dist = 0
    
    w = 0
    t =0
    
    while(bateu == False and t<5):
        for j in paredes:
    #        print([pos2.tolist(), pos3.tolist()], 'aqui')
            
            if cruzou([pos2.tolist(), pos3.tolist()], j):
                bateu=True
                dist=t
        
                
        pos3 +=0.4*velo2
        pos2+=0.4*velo2
    
        t+=1

    pygame.draw.line(screen,(0,100,200), posi,pos3,1)   
    if (bateu== True):
        return (dist/5)
    if (t==5):
        return (dist/5)
            #print(pos3,pos2,velo2)
        
            
mortes = []
    
            
angulosmelhores = []

          
tamanhosmelhores = []
    

    

    
class carro:
    pos = [10,10]
    def __init__(self, pos, velo,paredes):
        self.pos = np.array(pos)
        self.velo = np.array(velo)
        self.paredes = paredes
        self.volante = 0
        self.olhos = np.array((0,0,0,0,0))
        self.pos_inicial = self.pos
        self.velo_inicial = self.velo
        self.pesosolhos = 5*np.random.rand(5)

        self.valores = np.ones((5,5))
        self.pesos = 6*np.random.rand(5,5,5)-3
        self.vida = 0
        self.angulos = 6*np.random.rand(5)-3
        self.cor = (250,250,250)
        self.angolho = zip(self.angulos.tolist(),self.pesosolhos.tolist())

    def andar(self):
        self.pos = self.pos+0.4*self.velo
        self.vida+=1
        #print('pos',self.pos)
    def virar(self):
        #print('velo', self.velo)
        self.velo = np.array(girar(self.velo,self.volante))
        #print('velo', self.velo)
    def desenhar(self):
        #print( self.pos.astype(int).tolist(), (self.pos-self.velo).astype(int))#
        
        pygame.draw.line(screen,self.cor, self.pos.astype(int).tolist(), (self.pos-self.velo).astype(int).tolist(), 1)
    def ver(self):
        self.angolho = list(zip(self.angulos.tolist(),self.pesosolhos))
        
        self.olhos =[laser(self.pos,self.velo, p[0],p[1], self.paredes) for p in self.angolho]
        #print('olhos', self.olhos)
        

    def decidir(self):
        #print('ovp:', self.olhos, self.valores, self.pesos)
        self.volante = flow(self.olhos,self.valores,self.pesos)[0]-0.5
        #print('volante', self.volante)

    def checarcolisão(self):
        global vidamax
        global pesosmelhores
        global mortes
        global angulosmelhores
        global tamanhosmelhores
        self.corpo = [self.pos, self.pos-self.velo]

        if (self.vida>2*(vidamax+100)):
            pesosmelhores.append(self.pesos)
            angulosmelhores.append(self.angulos)
            tamanhosmelhores.append(self.pesosolhos)
            
            
        for m in self.paredes:
            if cruzou(self.corpo,m):
                if (self.vida>vidamax):
                    vidamax = self.vida
                    print(vidamax)
                    mortes.append(self.pos)
                    pesosmelhores.append(self.pesos)
                    angulosmelhores.append(self.angulos)
                    tamanhosmelhores.append(self.pesosolhos)
                self.pos = self.pos_inicial
                self.velo = self.velo_inicial
                a = random.random()

                if (a>=0.8):
                    self.pesos = 4*np.random.rand(5,5,5)-2
                    self.angulos = 6*np.random.rand(5)-3
                    self.pesosolhos = 6*np.random.rand(5)
                    #print(self.pesos)
                else:
                    self.pesos = pesosmelhores[len(pesosmelhores)-1]
                    #+0.5*(0.5-np.random.rand(5,5,5))
                    self.angulos = angulosmelhores[len(angulosmelhores)-1]
                    #+0.1*(0.5-np.random.rand(5))
                    self.pesosolhos = tamanhosmelhores[len(tamanhosmelhores)-1]
                    #+0.1*(0.5-np.random.rand(5))
                    #print(pesosmelhores)
                if (a<=0.79):
                    self.pesos =pesosmelhores[len(pesosmelhores)-1]+0.7*(-0.5+np.random.rand(5,5,5))
                    self.angulos = angulosmelhores[len(angulosmelhores)-1]+0.7*(-0.5+np.random.rand(5))
                    self.pesosolhos = tamanhosmelhores[len(tamanhosmelhores)-1]+0.7*(-0.5+np.random.rand(5))
                if(a<=0.3):
                    self.pesos+=3*(-0.5+np.random.rand(5,5,5))
                    self.angulos+=3*(-0.5+np.random.rand(5))
                    self.pesosolhos+=3*(-0.5+np.random.rand(5))
                self.vida=0            
                    
                
        
                
        

        
abrirsalvo=1

if abrirsalvo ==1:
    parede = load('paredes.npy').tolist()
    

minhalista = []

TOTAL = 10

for c in range (0,TOTAL):
    d = carro([200.0,200.0],[14.0,0.0],parede)
    
    minhalista.append(d)
  


while True:
    
    
    if(k==0):
           while (k==0):
                if (abrirsalvo==1):
                    parede = load('paredes.npy').tolist()
                    print(parede)
                    k=1
                else:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            sys.exit()
                        if event.type == pygame.MOUSEBUTTONUP:
                            posicaoagora = pygame.mouse.get_pos()
                            if (contador>1):
                                parede.append([posicaoantiga,posicaoagora])

                            posicaoantiga = posicaoagora
                            contador +=1
                        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                            contador =1
                            #print (contador)
                        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                            save('paredes.npy', np.array(parede))
                            k = 1
                            
                        for a in parede:
                            pygame.draw.line(screen, (0,0,100),a[0],a[1],1)
                            
                    pygame.draw.line(screen, WHITE, (100,100),(200,200),1)
                    
                    pygame.display.update()

    
    if (k==1):
        
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
        tempomedio =0
        
        for j in mortes:
            pygame.draw.circle(screen,(0,0,0),j.astype(int).tolist(),4)
        for a in parede:
            pygame.draw.line(screen,(0,0,250),a[0],a[1],2)
            #print('desenhei')
        screen.fill((20,20,20))
        for j in minhalista:
            j.desenhar()
            j.andar()
            j.ver()
            j.decidir()
            j.virar()
            j.checarcolisão()
            #print(j.olhos)

            
        
    
        pygame.display.update()
        #screen.fill(BLACK)
        






       
