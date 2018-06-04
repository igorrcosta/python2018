from collections import Counter

def leitura_letras():
    with open('exemplo.txt', 'r', encoding='utf-8') as arquivo:
        dic_letras = Counter() #{'a':2, 'b':1}
        for linha in arquivo:
            for caracter in linha:
                dic_letras[caracter] += 1
    return dic_letras

def escrita_alfabetica(dic_letras):
    with open('saida.txt', 'w', encoding='utf-8') as saida:
        lista_caracteres = sorted(dic_letras.keys())
        for caracter in lista_caracteres:
            valor = str(dic_letras[caracter])
            linha_saida = str.join('\t', [caracter, valor])
            saida.write(linha_saida)
            saida.write('\n')
            
def escrita_frequencia(dic_letras):
    with open('saida.txt', 'w', encoding='utf-8') as saida:
        lista_frequencia = dic_letras.most_common() #[('a', 41), ('e', 31), ('c', 20)]
        for caracter, frequencia in lista_frequencia: #pega os dois elementos da tupla
            valor = str(frequencia) #transforma o numero da frequencia em string
            linha_saida = str.join('\t', [caracter, valor]) #junta com um tab como separador
            saida.write(linha_saida) #escreve a linha no arquivo
            saida.write('\n') #escreve o enter depois da linha

def main():
    resultado = leitura_letras()
    escrita_frequencia(resultado)

main()

#Arquivo novo . txt:
'''
a   31
b   3
c   5
'''