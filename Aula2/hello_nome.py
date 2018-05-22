#>>> hello_nome('Igor')
# Olá, Igor!
# >>> hello_nome('Jeferson')
# Olá, Jeferson!

def hello_nome(nome):
    print('Olá, ' + nome + '!')
    
def pergunta_idade(nome, idade = 30):
    print('Olá, ' + nome + '!')
    if idade > 80:
        print('Nossa...', nome)
        print('Idade de respeito!')
    else:
        print('Você é muito jovem')