
def colat(a):
    c = a
    conta = 0
    while (c!=1):
        if (c%2==0):
            c = c/2

            conta+=1
        else:
            c = (3*c+1)/2

            conta+=1
    return ([c,conta])

maxi = 0


for f in range (3,10000):
    print (f, colat(f))
    if (colat(f)[1]>maxi):
        print('max aqui')
        maxi = colat(f)[1]

