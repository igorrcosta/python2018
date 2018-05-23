#Exercicio 7

'''
7 - Para esse exercício, vamos usar a
função str.split (que já vem no python!):
 
str.split(s,sep) - Recorta a string s em todas
as ocorrencias de sep e retorna a lista com os pedaços.
Se sep não for especificado, recorta a string
nos espaços.
Exemplo:
>>> palavra = ’AB BC CD’
>>> str.split(palavra)
[’AB’, ’BC’, ’CD’]
>>> palavra2 = ’AXBXCXD’
>>> str.split(palavra2,’X’)
[’A’, ’B’, ’C’, ’D’]

Usando essa função, faça um programa que recebe
uma frase e retorna o numero de palavras.
Exemplo:

>>> conta_palavras('Vamos contar quantas palavras tem nessa frase')
7
>>> conta_palavras('Como vai?')
2
'''

def conta_palavras(frase):
    picotada = str.split(frase)
    return len(picotada)
