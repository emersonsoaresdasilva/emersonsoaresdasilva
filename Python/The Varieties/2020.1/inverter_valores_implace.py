'''
Crie uma função que receba como parâmetro um vetor V e o seu tamanho N.
A função deverá criar um vetor auxiliar com os itens de V em sequência
contrária.
A função deverá retornar auxiliar.
'''
def preenche(v, n):
    for i in range(n):
        v[i] = int(input('Vetor[%d]: ' % i))

def exibe(v, n):
    for i in range(n):
        print(v[i], end=' ')
    print()

def inverte(v, n):
    w = n * [0]
    j = n - 1
    for i in range(n):
        w[j] = v[i]
        j -= 1
    return w

n = 5
v = n * [0]
preenche(v, n)
exibe(v, n)
w = inverte(v, n)
exibe(w, n)
