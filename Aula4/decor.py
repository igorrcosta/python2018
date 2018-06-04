   
def decor(fun):
    def nova():
        print('pre')
        fun()
        print('pos')
    return nova

@decor
def teste():
    print('teste')

teste()