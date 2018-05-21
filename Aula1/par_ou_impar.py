'''Receba um numero e retorne True se for par
ou False se for ímpar'''

a = input('Digite um número: ')
a = int(a) # Transforma str em int
if a % 2 == 0: # Testa se é par!
    print(True)
else: # Se não foi par...
    print(False)
