def monkey_trouble(macaco_a, macaco_b):
    #a = True e b = True, retorna True
    #a = False e b = False, retorna True
    # todos os outros casos, retorna False
    if macaco_a == macaco_b:
        return True
    else:
        return False
    
def funcao_principal():
    print('Confusao!')