#Exercicio1
'''
1 - Escreva um programa que receba uma palavra e:
'''
palavra = input('Digite uma palavra: ')
#a) Imprima a primeira e a última letra.
print(palavra[0], palavra[-1])
#b) Imprima a terceira letra.
print(palavra[2])
#c) Imprima a palavra invertida (de trás para frente).
print(palavra[::-1])
#d) Imprima a frase "Essa palavra começa com A" 
#caso a palavra comece com A ou a (maiúsculo ou minúsculo)
if palavra[0] == 'A' or palavra[0] == 'a':
    print('Essa palavra começa com A')
