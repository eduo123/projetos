import pandas 
data=pandas.read_csv("br-sem-acentos.txt")
#print(data)
import matplotlib.pyplot as plt

df = pandas.DataFrame(data)
lista = df.values.tolist()
#print(len(lista))
#print(lista[10][0],len(lista[10]))
lista5 = [palavrinha[0].lower() for palavrinha in lista if len(palavrinha[0])==5]

print (len(lista5))


def contar_consoantes(palavra):
    cont = 0
    for j in palavra:
        if j not in 'AEIOUaeiou':
            cont+=1
    return cont
minhapalavra = [palavra for palavra in lista5 if 't' in palavra if 'a' in palavra if 'e' in palavra if 'o' in palavra if 'a'==palavra[0]]

#palavra = [palavra for palavra in lista5 if "e" in palavra if "a" in palavra if "r" in palavra]
palavra = [palavra for palavra in lista5 if contar_consoantes(palavra)==4]
#print(len(palavra))
#print (palavra)
print(minhapalavra)
contador = 0

print(contador)
letras =[]
contadores = []
for letra in 'abcdefghijklmnopqrstuvwxyz':
    letras.append(letra)
    contador = 0
    for palavra in lista5:
        if (palavra.count(letra)>0):
            contador+=1
    contadores.append(contador)        
    print(letra,contador, contador/len(lista5), len(lista5),len(lista))


df = pandas.DataFrame({'Letras': letras, 'Quantidades': contadores}, index=letras)
#df['Letras'] = letras
#df['Quantidade']= contadores
print(df)
df.plot.pie( x='Letras',y='Quantidades',legend=False)
#plt.legend(loc="lower right")


#plt.subplots_adjust(left=0.0, bottom=0.1, right=0.45)
#plt.legend(pie[0],labels, bbox_to_anchor=(1,0.5), loc="center right", fontsize=10, bbox_transform=plt.gcf().transFigure)
#df['Letra','Quantidade'].plot.bar()
#df['Frequência'] = df[]
plt.show()