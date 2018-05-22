#Exercicio 3

'''
3 - Escreva um programa que recebe um número e:
Caso ele seja múltiplo de 3 e múltiplo de 5,
imprima True. Senão, imprima False.
'''

numero = int(input('Digite um numero: '))
if (numero % 3 == 0) and (numero % 5 == 0):
    print(True)
else:
    print(False)
    
        