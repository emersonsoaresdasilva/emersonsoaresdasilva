'''
Crie uma função que receba como parâmetros um valor real x, um vetor de reais v
e o tamanho n de v.
A função deverá devolver como resposta True, caso encontre x em v, ou False caso
contrário.
Observações: O vetor está ordenado.
Restrições:
(I) não pode usar in ou not in;
(II) os itens do vetor devem ser percorridos um a um;
'''

from time import time #Retornar um valor em segundos, desde a data 01 / 01 / 1970 até agora.

#------------------------------------
#         FUNÇÃO VERSÃO FOR
#------------------------------------
def busca_for(x, v, n):
    for i in range(n):
        if v[i] == x:
            return True
    return False

#------------------------------------
#         FUNÇÃO VERSÃO WHILE
#------------------------------------
def busca_while(x, v, n):
    i = 0
    while i < n:
        if v[i] == x:
            return True
        i += 1
    return False

#------------------------------------
#        FUNÇÃO [Versão 01]
#------------------------------------
def busca_v1(x, v, n):
    i = 0
    while i < n and v[i] != x:
        i += 1
    return i < n
#------------------------------------
#        FUNÇÃO [Versão 02]
#------------------------------------
def busca_v2(x, v, n): #Funciona somente em vetores ordenados!
    i = 0
    while i < n and v[i] < x:
        i += 1
    return i < n

#------------------------------------
#  FUNÇÃO [Versão 03] - 0 segundos!
#------------------------------------
def busca_v3(x, v, n): #Funciona somente em vetores ordenados!
    p = 0
    u = n - 1
    while p <= u:
        m = (p + u) // 2 #Guarda o índice do item do meio do vetor.
        if x == v[m]:
            return True
        elif x < v[m]:
            u = m - 1
        else:
            p = m + 1
    return False

#     0  1  2  3  4  5  6  7  8  9 10
v = [21,27,43,55,57,61,78,88,89,92,94] # n = 11
#     p              m              u

#     0  1  2  3  4  5  6  7  8  9 10
#v = [21,27,43,55,57,61,78,88,89,92,94] # n = 11
#     p            u  m  p           u


n = 100000000
v = list(range(n))
x = n*2

inicio = time()
busca_v1(x, v, len(v))
tempo_busca1 = time() - inicio
print('Tempo de busca 01: %.3F segundos'% tempo_busca1)

inicio = time()
busca_v2(x, v, len(v))
tempo_busca2 = time() - inicio
print('Tempo de busca 02: %.3F segundos'% tempo_busca2)

inicio = time()
busca_v3(x, v, len(v))
tempo_busca3 = time() - inicio
print('Tempo de busca 03: %.3F segundos'% tempo_busca3)

