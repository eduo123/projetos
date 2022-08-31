import pandas

data=pandas.read_csv("br-sem-acentos.txt")
#print(data)


df = pandas.DataFrame(data)
lista = df.values.tolist()
#print(len(lista))
#print(lista[10][0],len(lista[10]))
lista5 = [palavrinha[0] for palavrinha in lista if len(palavrinha[0])==5]

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
print(palavra, minhapalavra)