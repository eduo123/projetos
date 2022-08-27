
letras = ['A','B','C','D']

contador = 0
combinação =[]
for j in letras:

    for m in letras:
        if (m!=j):
            for l in letras:
                if(l!=j and l!=m):
                    combinação = [j,m,l]
                    contador+=1
                    print(combinação,contador)
                    #for p in letras:
                     #   if (p!=j and p!=m and p!=l):
                      #      combinação = [j,m,l,p]
                       #     contador+=1
                        #    print (combinação,contador)
                    
