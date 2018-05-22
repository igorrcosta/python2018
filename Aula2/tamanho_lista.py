#exercicio listas 1

'''
Escreva uma função que recebe uma lista
e retorna o tamanho dela.
'''

def tamanho_lista(lista):
    tamanho = 0
    for item in lista:
        tamanho = tamanho + 1
    return tamanho


tamanho = tamanho_lista([5,4,3,2,5,4,3])