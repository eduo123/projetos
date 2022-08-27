def comprime(a):
    
    b = a[0]
    listacomprimida = []
    contaqui = 0
    for j in range(0,len(a)):
        if(a[j]==b):
            contaqui+=1
        else:
            
            listacomprimida.append(contaqui)
            contaqui=1
            b=a[j]
        if (j==len(a)-1):
             listacomprimida.append(contaqui)
    return (listacomprimida)
            

def colatlist(a):
    lista = []
    b = a
    while (b!=1):
        if (b%2==0):
            b=b/2
            lista.append(0)
        else:
            b = (3*b+1)/2
            lista.append(1)
    return (lista)

def emstring(a):
    c = ''
    for j in a:
        c = c+str(j)
    return (c)
            



for i in range (3,20):
    #print (i,colatlist(i))
    print(i, emstring(comprime(colatlist(i))))
