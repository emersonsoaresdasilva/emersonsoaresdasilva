'''
Crie uma função que receba como parâmetros um valor real x, um vetor de reais v
e o tamanho n de v.
A função deverá devolver como resposta True, caso encontre x em v, ou False caso
contrário.
Restrições:
(I) não pode usar in ou not in;
(II) os itens do vetor devem ser percorridos um a um;
'''

def busca(x, v, n):
    for i in range(n):
        if v[i] == x:
            return True
    return False

def busca(x, v, n):
    i = 0
    while i < n:
        if v[i] == x:
            return True
        i += 1
    return False

def busca(x, v, n):
    i = 0
    while i < n and v[i] != x:
        i += 1
    return i < n

v = [56.0,78.0,-1.0,10.0,59.0]
x = busca(59, v, 5)
if x == True:
    print('Achou!')
else:
    print('Não achou!')
