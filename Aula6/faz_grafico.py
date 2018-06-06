#Aula 7
#faz_grafico.py

from matplotlib import pyplot 

'''Esse programa cria graficos usando o matplotlib'''

def faz_grafico(lista_numeros):
    fig1, ax1 = pyplot.subplots()
    ax1.set_title('Basic Plot')
    ax1.boxplot(lista_numeros)
    pyplot.show()