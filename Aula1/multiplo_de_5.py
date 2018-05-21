'''Receba um número e retorne ele ao quadrado se
for multiplo de 5. Se não for, impria ele dividido por 2'''

numero = int(input('Digite um numero: '))
if numero % 5 == 0: #Testa se o numero é multiplo de 5
    print(numero**2) #Imprime o numero ao quadrado
else:
    print(numero/2) #Imprime a metade do numero