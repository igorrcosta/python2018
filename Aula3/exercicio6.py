#Exercicio6
'''
6 - Escreva uma função que receba uma string e um caracter
e retorne quantas vezes aquele caracter aparece na string.
Ex:
>>> conta_caracter('arara', 'a')
3
>>> conta_caracter('python', 'i')
0
'''

def conta_caracter(palavra, letra):
    soma_letras = 0
    for l in palavra:
        #print(l, palavra, soma_letras)
        if letra == l:
            soma_letras = soma_letras + 1
    return soma_letras