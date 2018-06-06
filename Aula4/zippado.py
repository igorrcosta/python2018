def zippado(*listas):
    '''Essa função reimplementa a funcao zip do python de forma tosca'''
    while True:
        if [] in listas:
            break
        result = []
        for x in listas:
            result.append(x.pop(0))
        yield result
        
for x in zippado([1,2,3,4], [3,4,5,6]):
    print(x)
