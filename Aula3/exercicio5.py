#Exercicio 5

'''5 - Escreva uma função que receba uma string e um número 
e retorne uma string igual a s, exceto
pelo caracter da posição i, 
que deve ser substituı́do pelo caracter x. Ex:
>>> troca_letra(‘bola’,1)
‘bxla’
>>> troca_letra(‘programando’,5)
‘progrxmando’
'''

def troca_letra(palavra, indice):
    return palavra[:indice] + 'x' + palavra[indice + 1:]