import random

def exibe(v, n):
    for i in range(n):
        print(v[i], end=' ')
    print()

def aleatorio(i, f): #Wrapper!
    return random.randint(i, f)

def preencher(v, n):
    for i in range(n):
        v[i] = aleatorio(10, 99)


n = 10
v = n * [0]
preencher(v, n)
exibe(v, n)
