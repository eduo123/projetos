vetor = [0,0,0]


def colat(a,b):
    c = a
   
    for d in range(0,3):
        if (c%2==0):
            c = c/2
            vetor[d]=1
        else:
            c = (3*c+1)/2
            vetor[d]=-1
    return c

count = 0
for j in range(2,3):
    count = 0
    for a in range (2000,4000):
        f = colat(a,j)
        print(vetor)
        if (a<colat(a,j)):
            count+=1
            #print (vetor)
            #print(a,colat(a,j),j)
    #print (count)
    print (j, count)
