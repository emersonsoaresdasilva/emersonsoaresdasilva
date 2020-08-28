'''
Crie uma função que receba como parâmetros um valor inteiro X, um vetor de
inteiros V e o tamanho de N de V.
A função deverá retornar o índice da primeira ocorrência de X em V, ou -1
caso X não esteja em V.

Restrições; Funções/métodos built-in
Permitidos: range()
'''


def indice(x, v, n):
    for i in range(n): #[0..n[
        if v[i]==x:
            return i
    return -1

v = [50,78,31,20,10,-4,0,6,8,10]
ind = indice(10, v, 8)
if ind != -1:
    print('Item encontrado! Indice:',ind)
else:
    print('Item não foi encontrado')
    
