from collections import Counter

with open('exemplo.txt', 'r', encoding='utf-8') as arquivo:
    dic_letras = Counter() #{'a':2, 'b':1}
    for linha in arquivo:
        for caracter in linha:
            dic_letras[caracter] += 1
#print(dic_letras)
with open('saida.txt', 'w', encoding='utf-8') as saida:
    lista_caracteres = sorted(dic_letras.keys())
    for caracter in lista_caracteres:
        valor = str(dic_letras[caracter])
        linha_saida = str.join('\t', [caracter, valor])
        saida.write(linha_saida)
        saida.write('\n')

#Arquivo novo . txt:
'''
a   31
b   3
c   5
'''
        #implementacao 2:
        #try:
            #dic_letras[caracter] += 1
        #except KeyError:
            #dic_letras[caracter] = 1