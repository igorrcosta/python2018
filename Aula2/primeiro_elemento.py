#Exercicio lista 2

'''
Funcao que recebe duas listas
e retorna true se e somente se
elas começarem com o mesmo elemento
'''

def mesmo_inicio(lista1, lista2):
    if lista1[0] == lista2[0]:
        return True
    return False

'''
Agora vamos usar essa funcao para
testar varias listas!
'''

def funcao_principal():
    print(mesmo_inicio([1,2,3], [4,6,6]))
    print(mesmo_inicio([2], [4]))
    print(mesmo_inicio(['oi', 0], ['oi', 1]))
    nomes1 = ['Abimeleque','Sinforoso']
    nomes2 = ['João', 'Maria']
    teste = mesmo_inicio(nomes1, nomes2)
    print(teste)