import pygame
import random
import math
pygame.init()

contador = 1

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
azul = (20,20,250)
screen = pygame.display.set_mode((600, 600), 0, 32)
screen.fill(BLACK)
pygame.display.update()
circles = []
vermelho =(250,20,20)
verde = (20,250,20)
cores = [azul,verde,vermelho]

velocidades = []
for j in range (0,20):
    circles.append([random.randrange(50,450),random.randrange(50,450)])
    velocidades.append([1*(random.random()-0.500),1*(random.random()-0.500)])


def posint(a):
    b = [int(a[0]),int(a[1])]
    return b
pensamento = []
passado = pensamento

conexoes = []
a=[]
for j in range (0, 10):
    a=[]
    for w in range (0,10):
        a.append(random.randint(0,1))
    conexoes.append(a)
print(conexoes)
def conclusao (a,b):
    velocidadenova = []
    
    for j in range(0,len(a)):
        return
pesos = []


for j in range(0,10000):
    pesos.append[(random.randint(-1000,1000)/1000,random.randint(-1000,1000)/1000)]


while True:
    pensamento = conclusao(circles,pesos)
    for j in  range (0,len(circles)):
        
        pygame.draw.circle(screen,cores[j%3] , posint(circles[j]),20)
        circles[j][0] = circles[j][0]+velocidades[j][0]
        circles[j][0] = pensamento[j][0]
        
        circles[j][1] = circles[j][1]+velocidades[j][1]

        if (circles[j][0]<0):
            circles[j][0]=circles[j][0]+450
        if (circles[j][0]>500):
            circles[j][0]=circles[j][0]-450
        
        #print([1*(random.random()-0.500),1*(random.random()-0.500)])
        velocidades[j]=[5*(random.randrange(0,10000, 1)/10000-0.500),5*(random.randrange(0,10000, 1)/10000-0.500)]

        




    pygame.display.update()
    screen.fill(BLACK)
        
        






