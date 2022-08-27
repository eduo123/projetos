
def collatvida(a):

    a0 = a
    durou = 0
    while (a>=a0):
        if (a%2==0):
            a = a/2
            durou+=1
        else:
            a = (3*a+1)/2
            durou+=1
    return (durou)

vidamaxima=1
for j in range (3,100000000):
    
    
    vidaagora = collatvida(j)
    if (vidaagora>vidamaxima):
        print (j,vidaagora)
        vidamaxima = vidaagora

        
        
    
    
