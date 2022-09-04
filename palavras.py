import pandas

data=pandas.read_csv("br-sem-acentos.txt")
#print(data)


df = pandas.DataFrame(data)
lista = df.values.tolist()
#print(len(lista))
#print(lista[10][0],len(lista[10]))
lista5 = [palavrinha[0] for palavrinha in lista if len(palavrinha[0])==7]

print (len(lista5))


def contar_consoantes(palavra):
    cont = 0
    for j in palavra:
        if j not in 'AEIOUaeiou':
            cont+=1
    return cont
minhapalavra = [palavra for palavra in lista5 if 'a' in palavra  if 'n' in palavra if 's' in palavra if 'd' in palavra if 'u' in palavra if 'i'==palavra[5] ]
minhapalavra2 = [palavra for palavra in lista5 if 'g' in palavra if 'e' in palavra if 'd' in palavra if 'a' in palavra if 'g'==palavra[0] if 'a'!=palavra[1] if 't'!=palavra[0] ]
#palavra = [palavra for palavra in lista5 if "e" in palavra if "a" in palavra if "r" in palavra]
palavra = [palavra for palavra in lista5 if contar_consoantes(palavra)==4]
#print(len(palavra))
#print (palavra)
print( minhapalavra,palavra)