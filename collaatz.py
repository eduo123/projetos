import math


def condição0(a):
    if ((a+1)%2==0):
        return True
    else:
        return False

def condição1(a):

    if ((a*3-1)%4==0):
        return True
    else:
        return False
def condição2(a):
    if ((a*9+5)%16==0):
        return True
    else:
        return False
def condição3(a):
    if ((a*27+23)%32==0):
        return True
    else:
        return False

contador0 = 0
contador1 = 0
contador2 = 0
contador3 = 0
contador4 = 0
for k in range(1,1000):
    if condição0(k)==False:
        contador0+=1
        if condição1(k)==False:
            contador1+=1
            if condição2(k)==False:
                contador2+=1
                if condição3(k)==False:
                    contador3+=1

print (contador0,contador1, contador2, contador3,contador4)
