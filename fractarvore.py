import pygame
import random
import math


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
screen = pygame.display.set_mode((1000, 900), 0, 32)
screen.fill((0,0,0))

linhas = []
escala = 1.0
contador =0
def girar(vetor,graus):
    graus = graus*math.pi/180
    
    meuvetor = [vetor[0]*math.cos(graus)+vetor[1]*math.sin(graus), -vetor[0]*math.sin(graus)+vetor[1]*math.cos(graus)]
    modulo =(meuvetor[0]**2+meuvetor[1]**2)**(-1/2)
    meuvetor[0] *= modulo
    meuvetor[1] *= modulo
    return(meuvetor)


linhas.append([[345,450],[500,450]])
linhasiniciais = linhas

def desenhartriangulo(ponto1,ponto2,angulo):
    ponto1[1]=ponto1[1]+100
    ponto2[1] = ponto2[1]+100
    pontomedio = [(ponto1[0]+ponto2[0])/2,(ponto1[1]+ponto2[1])/2]
    vetorraio = [ponto2[0]-pontomedio[0],ponto2[1]-pontomedio[1]]
    vetorraiogirado = girar(vetorraio,angulo)
    vetorraiogirado2 = girar(vetorraio,angulo)
    ponto12 = [ponto1[0]+2*vetorraiogirado2[0],ponto1[1]+2*vetorraiogirado2[1]]
    ponto22 = [ponto2[0]+2*vetorraiogirado2[0],ponto2[1]+2*vetorraiogirado2[1]]
    a = len(linhas)
    #print(a)
    
    cor = [250,0,15*math.log(a+1,2)]
    #cor = [random.randint(0,250),random.randint(0,250),random.randint(0,250)]
    
    pygame.draw.line(screen,cor,ponto1,ponto12,1)
    #pygame.time.wait(5+int(1000/maximo))
    pygame.display.update()
    pygame.draw.line(screen,cor,ponto2,ponto22,20)
    #pygame.time.wait(5+int(1000/maximo))
    pygame.display.update()
    pontomedio = [(ponto12[0]+ponto22[0])/2,(ponto12[1]+ponto22[1])/2]
    pygame.draw.line(screen,cor,ponto12,ponto22,1)
    #pygame.time.wait(5+int(1000/maximo))
    pygame.display.update()
    pontofinal =[pontomedio[0]+vetorraiogirado[0],pontomedio[1]+vetorraiogirado[1]]
    linhas.append([ponto12,pontofinal])
    linhas.append([pontofinal,ponto22])
    
    pygame.draw.line(screen,cor,ponto12,pontofinal,1)
    #pygame.time.wait(5+int(5000/maximo))
    pygame.display.update()
    
    pygame.draw.line(screen,cor,ponto22,pontofinal,1)
    ##print('passei')
    #pygame.time.wait(1+int(1000/maximo))
    pygame.display.update()




ang = 90
linhas2=[]
run = True
maximo = 1
K=0
contador = 0
valendo = False
#pygame.draw.line(screen,(230,230,230),(200,600),(600,600),1)
while run:
    #pygame.draw.line(screen,(230,230,230),(escala*200,escala*600),(escala*600,escala*600),1)
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
                #maximo*=10

            valendo = True
    
    pygame.display.update()
    linhas2 = linhas
    linhas = []
    maximo*=3
    contador+=1
    #print(contador)
    events = pygame.event.get()
    if (True):
            if len(linhas2)<maximo:
                
                for j in linhas2:
                        desenhartriangulo(j[0],j[1],ang)
                        #ang+=180
                        #contador+=1
                       # if (contador%4==0):
                        #    ang+=180
                        #ang = random.randrange(0,360)

            else:
                linhas = linhas[:-1]

    #print(len(linhas))
    pygame.display.update()
    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                ang+=1
                linhas = linhasiniciais
                linhas2 = linhas
                #print(ang)
                screen.fill(BLACK)
            
            #if event.key == pygame.K_RIGHT:
                #ang-=1
                #linhas = linhasiniciais
                #linhas2 = linhas
                ##print(ang)
                #screen.fill(BLACK)
            if event.key == pygame.K_UP:
                #maximo*=10
                valendo = True
                
            if event.key == pygame.K_DOWN:
                maximo*=.50
            
                
            

            

    

    
    

