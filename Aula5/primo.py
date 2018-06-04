#é primo?

def primo(n):
    '''retorna True se n é primo, False otherwise'''
    for k in range(2, int(n/2)):
        if n % k == 0:
            return False
    return True

n = int(input('diga o numero: '))
print(primo(n))
          