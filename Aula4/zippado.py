def zippado(*listas):
    while True:
        if [] in listas:
            break
        result = []
        for x in listas:
            result.append(x.pop(0))
        yield result
        