# Exercicio 1: Ao final da execução da função abaixo,
# Qual o número de execuções em função de n?
'''
    1 + n + n² + n² + 1
    2n² + n + 2
'''
# Qual a complexidade usando a notação O()?
'''
    O(n²)
'''
def funcao1(n):
    s = 0                               # 1
    for i in range(n):                  # n
        for j in range(n):              # n²
            s = s + 1                   # n²
    return s                            # 1

# Exercicio 2: Ao final da execução da função abaixo,
# Qual o número de execuções em função de n?
'''
    1 + n + n² + n³ + n³ + 1
    2n³ + n² + n + 2
'''
# Qual a complexidade usando a notação O()?
'''
    O(n³)
'''
def funcao2(n):
    s = 0                               # 1
    for i in range(n):                  # n
        for j in range(n):              # n²
            for k in range(n):          # n³
                s = s + 1               # n³
    return s                            # 1

# Exercicio 3: Considerando a função abaixo e responda as questões:
# a) se a = 10 e b = 100, quantas vezes as linhas marcadas são executadas?
'''
    linha1 = a² = 10² 100
    linha2 = b = 100
'''
# b) se a = 20 e b = 10, quantas vezes as linhas marcadas são executadas?
'''
    linha1 = a² = 20² = 400
    linha2 = b = 10
'''
# c) se a = 100 e b = 10, quantas vezes as linhas marcadas são executadas?
'''
    linha1 = a² = 100² = 10000
    linha2 = b = 10
'''
# d) Qual a complexidade usando a notação O()?
'''
    1 + n + n² + n² + n + n + 1
    2n² + 2n + n + 2
    n²
    O(n²)
'''
def funcao3(a, b):
    cont = 0                                        # 1
    for i in range(a):                              # n
        for j in range(a):                          # n²
            cont = cont + 1     # linha 1           # n²
    for i in range(b):                              # n
        cont = cont + 1         # linha 2           # n
    return cont                                     # 1

# Exercicio 4: Considerando a função abaixo e responda as questões:
# a) se a lista tem tamanho 1000, quantas vezes as linhas marcadas são executadas?
"""
    1000²
"""
# b) se a lista tem tamanho 2000, quantas vezes as linhas marcadas são executadas?
"""
    2000²
"""
# c) se a lista tem tamanho 4000, quantas vezes as linhas marcadas são executadas?
"""
    4000²
"""
# d) Qual a complexidade usando a notação O()?
"""
    1 + n + 2n²
    2n²

    O(n²)
"""

def funcao4(lista):
    i = 0                                           # 1
    for e1 in lista:                                # n
        for e2 in lista:                            # n²
            i = i+1         # linha 1               # n²


# Exercicio 5: Considerando a função abaixo e responda as questões:
# a) se a lista tem tamanho 1000, quantas vezes as linhas marcadas são executadas?
"""
    1000
"""
# b) se a lista tem tamanho 2000, quantas vezes as linhas marcadas são executadas?
"""
    2000
"""
# c) se a lista tem tamanho 4000, quantas vezes as linhas marcadas são executadas?
"""
    4000
"""
# d) Qual a complexidade usando a notação O()?
"""
    1 + 2n
    2n

    O(n)
"""

def funcao5(lista):
    i = 0                                           # 1
    for e in lista:                                 # n
        i = i+1             # linha 1               # n

# Exercicio 6: Considerando a função abaixo e responda as questões:
# a) se a lista tem tamanho 1000, quantas vezes as linhas marcadas são executadas?
"""
    linha 1 = 1000
    linha 2 = n² = 1000²
"""
# b) se a lista tem tamanho 2000, quantas vezes as linhas marcadas são executadas?
"""
    linha 1 = 2000
    linha 2 = n² = 2000²
"""
# c) se a lista tem tamanho 4000, quantas vezes as linhas marcadas são executadas?
"""
    linha 1 = 4000
    linha 2 = n² = 4000²
"""
# d) Qual a complexidade usando a notação O()?
"""
    1 + 3n + 2n²

    O(n²)
"""

def funcao6(lista):
    i = 0                                           # 1
    for e in lista:                                 # n
        i = i+1             # linha 1               # n
    for e1 in lista:                                # n
        for e2 in lista:                            # n²
            i = i+1         # linha 2               # n²

# Exercicio 7:
# Escreva uma função que recebe uma lista de tamanho n e troca de posição seu maior e seu menor elementos.
# Você não pode usar outro vetor como auxiliar e não deve utilizar funções prontas do python.
# A função deve ter complexidade O(n).

def troca(lista):
    maior = lista[0] # 1
    menor = lista[0] # 1
    indice_maior = 0 # 1
    indice_menor = 0 # 1
    for i in range(len(lista)):                 # n
        if lista[i] > maior:                    # n
            maior = lista[i]                    # n
            indice_maior = i                    # n
        if lista[i] < menor:                    # n
            menor = lista[i]                    # n 
            indice_menor = i                    # n
    lista[indice_maior] = menor                 # 1
    lista[indice_menor] = maior                 # 1

lista = [1, 3, 4, 90, 5]
troca(lista)
print(lista)

# Exercicio 8:
# Escreva uma função para inverter a ordem dos elementos de uma lista de tamanho n.
# Você não pode usar outro vetor como auxiliar e não deve utilizar funções prontas do python.
# A função deve ter complexidade O(n).

def inverte(lista):
    a = len(lista) - 1                  # a = n-1......... 0
    for i in range(len(lista)//2):      # a = 0........... n-1
        auxiliar = lista[i]
        lista[i] = lista[a]
        lista[a] = auxiliar
        a -= 1
lista = [1, 2, 3, 4, 5, 6]
inverte(lista)
print(lista)
