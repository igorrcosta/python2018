def f(x):
    '''Essa funçao retorna o
    quadrado do argumento
    '''
    return x**2

g = lambda x: x**2

print(g(2))

map(lambda x:x**2, [1,2,3,4,5])

for x in range(1,6):
    print(x**2)
