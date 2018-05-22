#Exercicio 2

'''
2 - Escreva um programa que recebe dois números (a e b):
Se os dois números forem iguais, imprima o número.
Senão, imprima o maior dividido pelo menor.
'''

a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))

if a == b:
    print(a)
else:
    if a > b:
        print(a/b)
    elif b > a:
        print(b/a)