import pygame
import random
import math
pygame.init()
contador = 1

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
screen = pygame.display.set_mode((600, 800), 0, 32)
screen.fill(WHITE)
clock = pygame.time.Clock()
p1 =[100,100]
p2 =[500,100]
p3= [500,500]
posicaoantiga = [0,0]


tempoglobal  = 0

posicaoagora = [0,0]
k=0
p4=[100,500]
parede =[]
pontostodos = []
minhalista = []
pygame.draw.circle(screen,BLACK,(200,200),2)
def detmin(a2,b2):
    valor = a2[0]*b2[1]-a2[1]*b2[0]
    return (valor)





def cruzou ( seg1, seg2):

  
    AB = [seg1[1][0]-seg1[0][0],seg1[1][1]-seg1[0][1]]
    AC = [seg2[0][0]-seg1[0][0],seg2[0][1]-seg1[0][1]]
    AD = [seg2[1][0]-seg1[0][0],seg2[1][1]-seg1[0][1]]
    CD = [seg2[1][0]-seg2[0][0],seg2[1][1]-seg2[0][1]]
    CA = [seg1[0][0]-seg2[0][0],seg1[0][1]-seg2[0][1]]
    CB = [seg1[1][0]-seg2[0][0],seg1[1][1]-seg2[0][1]]
    if detmin(AB,AC)*detmin(AB,AD)<0 and detmin(CD, CA)*detmin(CD,CB)<0:
        return True
    else:
        return False
class carro:
    pos = [10,10]
    def __init__(self, pos, velo,paredes):
        self.pos = pos
        self.velo = velo
        self.visao = [5,5,5,5,5,5,5]
        self.paredes = paredes
        self.olho0 = [self.pos[0]+5*self.velo[0],self.pos[1]+5*self.velo[1]]
        self.velo1 = [self.velo[0]*math.cos(.25)+self.velo[1]*math.sin(.25),-self.velo[0]*math.sin(.25)+self.velo[1]*math.cos(.25)]
        self.pesos = [[[0,0,0,0,0,0]*5]*5]*5
        self.velo2 = [self.velo[0]*math.cos(-.25)+self.velo[1]*math.sin(-.25),-self.velo[0]*math.sin(-.25)+self.velo[1]*math.cos(-.25)]
        self.velo3 = [self.velo[0]*math.cos(0.75)+self.velo[1]*math.sin(0.75),-self.velo[0]*math.sin(0.75)+self.velo[1]*math.cos(0.75)]
        self.velo4 = [self.velo[0]*math.cos(-0.75)+self.velo[1]*math.sin(-0.75),-self.velo[0]*math.sin(-0.75)+self.velo[1]*math.cos(-0.75)]
        self.olho1 = [self.pos[0]+5*self.velo1[0],self.pos[1]+5*self.velo1[1]]
        self.olho2 = [self.pos[0]+5*self.velo2[0],self.pos[1]+5*self.velo2[1]]
        self.olho3 = [self.pos[0]+5*self.velo3[0],self.pos[1]+5*self.velo3[1]]
        self.olho4 = [self.pos[0]+5*self.velo4[0],self.pos[1]+5*self.velo4[1]]
        self.olhos = [self.olho0,self.olho1,self.olho2,self.olho3,self.olho4]
        self.pos = [self.pos[0]+self.velo[0]/2,self.pos[1]+self.velo[1]/2]
        self.pesos = [[[0,0,0,0,0]*5]*5]*5
        self.pesosfora = [[0,0,0,0,0]*5]*5
        self.pesosfora2 = [[0,0,0,0,0]*5]*2
        self.contador = 0
        self.tamanho = [0,0,0,0,0]
        self.outaqui = 0
        self.outtotal = 0
        self.outtotal2 = 0
        self.outtotal3 = [0,0]
        self.viraresquerda = True
        self.virardireita = True
        self.tempodevida = 0
        self.angulos = [0,0,0,0,0]





        for k in range (0,5):
            self.angulos[k] =1.5*random.random()-.75
            self.tamanho[k] = 5*random.random()
            for z in range(0,2):
                self.pesosfora2[z][k]=6*random.random()-3
            for j in range (0,5):
                self.pesosfora[k][j] = 6*random.random()-3
                for w in range(0,5):
                    self.pesos[k][j][w] = 6*random.random()-3

    
    def checarvisao(self):
        self.olho0 = [self.pos[0]+self.tamanho[0]*self.velo[0],self.pos[1]+self.tamanho[0]*self.velo[1]]
        self.velo1 = [self.velo[0]*math.cos(self.angulos[0])+self.velo[1]*math.sin(self.angulos[0]),-self.velo[0]*math.sin(self.angulos[0])+self.velo[1]*math.cos(self.angulos[0])]
        
        self.velo2 = [self.velo[0]*math.cos(self.angulos[1])+self.velo[1]*math.sin(self.angulos[1]),-self.velo[0]*math.sin(self.angulos[1])+self.velo[1]*math.cos(self.angulos[1])]
        self.velo3 = [self.velo[0]*math.cos(self.angulos[2])+self.velo[1]*math.sin(self.angulos[2]),-self.velo[0]*math.sin(self.angulos[2])+self.velo[1]*math.cos(self.angulos[2])]
        self.velo4 = [self.velo[0]*math.cos(self.angulos[3])+self.velo[1]*math.sin(self.angulos[3]),-self.velo[0]*math.sin(self.angulos[3])+self.velo[1]*math.cos(self.angulos[3])]
        self.olho1 = [self.pos[0]+self.tamanho[1]*self.velo1[0],self.pos[1]+self.tamanho[1]*self.velo1[1]]
        self.olho2 = [self.pos[0]+self.tamanho[2]*self.velo2[0],self.pos[1]+self.tamanho[2]*self.velo2[1]]
        self.olho3 = [self.pos[0]+self.tamanho[3]*self.velo3[0],self.pos[1]+self.tamanho[3]*self.velo3[1]]
        self.olho4 = [self.pos[0]+self.tamanho[4]*self.velo4[0],self.pos[1]+self.tamanho[4]*self.velo4[1]]
        self.olhos = [self.olho0,self.olho1,self.olho2,self.olho3,self.olho4]
        for b in range (0,5):
            for f in range (0,len(self.paredes)):
                if (cruzou([self.pos,self.olhos[b]], self.paredes[f])== True):
                    self.visao[b] = 1
                    break
                else:
                    self.visao[b] = 0
            if (self.visao[b] ==1):
                pygame.draw.line(screen,(0,100,100),self.pos,self.olhos[b],1)
            if (self.visao[b] ==0):
                pygame.draw.line(screen,(100,0,100),self.pos,self.olhos[b],1)


    def andar(self):
        global carromelhor
        global pontostodos
        
        self.pos = [self.pos[0]+self.velo[0]/2,self.pos[1]+self.velo[1]/2]
        self.tempodevida += 5

        if (self.tempodevida > 60 and self.tempodevida> 2*carromelhor.tempodevida+40):
            carromelhor.tempodevida = self.tempodevida
            
            centro = [int(self.pos[0]),int(self.pos[1])]
            pontostodos.append(centro)
            for k in range (0,5):
                carromelhor.angulos[k] = self.angulos[k]
                carromelhor.tamanho[k] = self.tamanho[k]
                for z in range(0,2):
                    carromelhor.pesosfora2[z][k]=self.pesosfora2[z][k]
                    for j in range (0,5):
                        carromelhor.pesosfora[k][j] = self.pesosfora[k][j]
                        for w in range(0,5):
                            carromelhor.pesos[k][j][w] = self.pesos[k][j][w]
            print('mudouandando')
    def mutacao(self):
        
        for k in range (0,5):
            self.aleaqui = random.random()
            if (self.aleaqui > 0.9):
                o = random.random()
                self.angulos[k] +=0.5*o-0.25
                #print('mutei')
            if (self.aleaqui > 0.9):
                o = random.random()
                self.tamanho[k] +=1*o-0.5
                #print('mutei')
   
            for z in range(0,2):
                self.ale = random.random()
                if (self.ale>0.9):
                    o = random.random()
                    self.pesosfora2[z][k]+=6*o-3
                    #print('mutei')
              
            for j in range (0,5):
                self.ale2 = random.random()
                if (self.ale2>0.9):
                    o = random.random()
                    self.pesosfora[k][j] +=6*o-3
                    #print('mutei')
                for w in range(0,5):
                    self.ale3 = random.random()
                    if (self.ale3>0.9):
                        o = random.random()
                        self.pesos[k][j][w] +=6*o-3
                        #print('mutei')
                
    def decidir(self):

        for k in range (0,2):
            if (k==0):
                self.outtotal3[0] = 0
                self.outtotal3[1] = 0
            for a in range(0,5):

                for b in range(0,5):
                    if (b==0):
                        self.outtotal2 = 0
                    for c in range(0,5):
                        if (c ==0):
                            self.outtotal =0
                        self.outaqui = self.pesos[a][b][c]*self.visao[c]
                        
                        self.outtotal += self.outaqui
                       
                        if (c == 4):
                            self.outtotal = 1/(1+math.exp(-self.outtotal))
                    self.outtotal2 += self.outtotal*self.pesosfora[a][b]
                    
                    if (b ==4):
                        self.outtotal2 = 1/(1+math.exp(-self.outtotal2))
                self.outtotal3[k] += self.outtotal2*self.pesosfora2[k][a]
            
                
                if (a==4):
                    for h in range (0,2):
                        self.outtotal3[h] = 1/(1+math.exp(-self.outtotal3[h]))
          
        if (self.outtotal3[0]<0.65):
            self.viraresquerda = True
        else:
            self.viraresquerda = False
        
        if (self.outtotal3[1]>0.65):
            self.virardireita = True
        else:
            self.virardireita = False
                
                            
            
                    
            

    
    

    def virar(self):



        


 
        a = 0.3
        b = -1*a
        if (self.viraresquerda== True and self.virardireita ==False):
            self.velo = [self.velo[0]*math.cos(a)+self.velo[1]*math.sin(a),-self.velo[0]*math.sin(a)+self.velo[1]*math.cos(a)]
        if (self.virardireita == True and self.viraresquerda == False):
            self.velo = [self.velo[0]*math.cos(b)+self.velo[1]*math.sin(b),-self.velo[0]*math.sin(b)+self.velo[1]*math.cos(b)]
    def checarcolisao(self):
        global carromelhor
        global pontostodos

        corpo = [self.pos,[self.pos[0]-self.velo[0],self.pos[1]-self.velo[1]]]
        for f in range (0,len(self.paredes)):
            if (cruzou(corpo,self.paredes[f])==True):
                if (self.tempodevida > carromelhor.tempodevida):
                    carromelhor.tempodevida = self.tempodevida
                    carromelhor.pesos = self.pesos
                    carromelhor.pesosfora = self.pesosfora
                    carromelhor.pesosfora2 = self.pesosfora2
                    
                    
                    for w in range(0,5):
                        carromelhor.angulos[w] = self.angulos[w]
                        carromelhor.tamanho[w] = self.tamanho[w]
                    
                    
                    #print(carromelhor.tempodevida,self.tempodevida)
                

                    centro = [int(self.pos[0]),int(self.pos[1])]
                    pontostodos.append(centro)
                    pygame.draw.circle(screen,(20,20,20),centro,5)
                    
                

                    
                self.aleatorio = random.random()
                if(self.aleatorio >0.1 and self.pesos[1][1][1] != carromelhor.pesos[1][1][1]):
                    for k in range (0,5):
                        self.tamanho[k] = 5*random.random()
                        self.angulos[k] = 1.5*random.random()-0.75
                        for z in range(0,2):
                            self.pesosfora2[z][k]=6*random.random()-3
                            for j in range (0,5):
                                self.pesosfora[k][j] = 6*random.random()-3
                                for w in range(0,5):
                                    self.pesos[k][j][w] = 6*random.random()-3
                
                else:
                    for k in range (0,5):
                        self.angulos[k] = (self.angulos[k]+carromelhor.angulos[k])/2
                        self.tamanho[k] = (self.tamanho[k]+carromelhor.tamanho[k])/2
                        for z in range(0,2):
                            self.pesosfora2[z][k]= (self.pesosfora2[z][k]+carromelhor.pesosfora2[z][k])/2
                            for j in range (0,5):
                                self.pesosfora[k][j] =(self.pesosfora[k][j]+carromelhor.pesosfora[k][j])/2
                                for w in range(0,5):
                                    self.pesos[k][j][w] = (self.pesos[k][j][w]+carromelhor.pesos[k][j][w])/2
                    #self.mutacao()
                if (self.pesos[2][1][1] != carromelhor.pesos[2][1][1]):
                    self.mutacao()
                #if (self.pesos[2][1][1] == carromelhor.pesos[2][1][1]):

                    #print('sou o melhor', self)
                #print(carromelhor.pesos[1][1][1])
                self.tempodevida = 0   
                self.pos = [200,200]
                self.velo = [10,10]
                #self.mutacao()
                
                break
                #for k in range (0,5):
                    #for z in range(0,2):
                        #self.pesosfora2[z][k]=6*random.random()-3
                        #for j in range (0,5):
                            #self.pesosfora[k][j] = 6*random.random()-3
                            #for w in range(0,5):
                                #self.pesos[k][j][w] = 6*random.random()-3
                #self.mutacao()
            
carromelhor = carro([200,200],[10,10],parede)


for c in range (0,30):
    d = carro([200,200],[10,10],parede)
    minhalista.append(d)



while True:
    
    if(k==0):
           while (k==0):
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
                        print (contador)
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                        k = 1
                        
                    for a in parede:
                        pygame.draw.line(screen, (0,0,100),a[0],a[1],1)
                        
                pygame.draw.line(screen, BLACK, (100,100),(200,200),1)
                pygame.display.update()


    if (k==1):
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
        tempomedio =0
        
        for b in range(0,30):

            posi1 = minhalista[b].pos
            minhalista[b].checarvisao()
            minhalista[b].decidir()
            minhalista[b].virar()
            minhalista[b].andar()
    
         
            posi2 = minhalista[b].pos
            minhalista[b].checarcolisao()
            tempomedio+=minhalista[b].tempodevida
            
            pygame.draw.line(screen, BLACK, posi1,posi2,1)
            
        for l in pontostodos:
            pygame.draw.circle(screen,(20,20,20),l,5)
        for a in parede:
            pygame.draw.line(screen,(0,0,100),a[0],a[1],1)
        tempomediodevida = tempomedio/100
    
        pygame.display.update()
        screen.fill(WHITE)
        



