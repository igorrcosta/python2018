# OOP

class Pessoa():
    def __init__(self, nome):
        self.nome = nome
        
    def saudacao(self):
        print('olá! Meu nome é', self.nome)
        
    def mudanca(self, novo_nome):
        self.nome = novo_nome
        
    def __repr__(self):
        return 'hahaha'
    
        
v = Pessoa('vinicius')

