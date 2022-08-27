import pygame
import random
import math
pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
screen = pygame.display.set_mode((800, 800), 0, 32)
screen.fill(BLACK)

centro = [250,250]



def collat(numero):
    number = numero
    lista = []
    #print('passei',numero)

    lista.append(number)

    while (number!=1):
        if (number%2 ==0):
            number*=0.5
        else:
            number = (3*number+1)/2
        lista.append(number)
        #print(lista)
    return (lista)

k = True
fator = 1.0
while k:
    a = []
    
    for b in range(10,100):
        a = collat(b)
        #print (len(a),a,b)
        for j in range(0,len(a)-1):
            #print('passeisim')
            #if (j%2 ==0):
                #pygame.draw.line(screen,(200,0,200),[5*j,int(fator*.008*a[j])],[5*(j+1),int(fator*.008*a[j+1])],1)
            #else:
                #pygame.draw.line(screen,(0,200,250),[5*j,int(fator*.008*a[j])],[5*(j+1),int(fator*.008*a[j+1])],1)

            pygame.draw.circle(screen,(0,0,250),[int(5*j),int(fator*.008*a[j])],1)
    pygame.display.update()
    fator*=1.001
    screen.fill(BLACK)
    print (fator)
    

    
