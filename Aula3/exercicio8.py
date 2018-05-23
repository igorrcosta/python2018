#Exercicio 8
''' Faça uma funcao que recebe uma lista de strings
e retorna as palavras concatenadas com ' oi ' entre elas.
Exemplo:
concatena(['palavra1', 'palavra2'])
'palavra1 oi palavra2'
'''
def concatena(lista):
    return str.join(' oi ', lista)