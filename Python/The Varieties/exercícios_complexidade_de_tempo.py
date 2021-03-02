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
2n³ + 2n² + 2
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
a = 100
b = 100
'''
# b) se a = 20 e b = 10, quantas vezes as linhas marcadas são executadas?
'''
a = 400
b = 10
'''
# c) se a = 100 e b = 10, quantas vezes as linhas marcadas são executadas?
'''
a = 1000
b = 10
'''
# d) Qual a complexidade usando a notação O()?
'''
1 + n + n² + n² + n + n + 1
2n² + 3n + 2

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
1.000.000
"""
# b) se a lista tem tamanho 2000, quantas vezes as linhas marcadas são executadas?
"""
2.000.000
"""
# c) se a lista tem tamanho 4000, quantas vezes as linhas marcadas são executadas?
"""
4.000.000
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
1 + n + n
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
linha 2 = 1.000.000
"""
# b) se a lista tem tamanho 2000, quantas vezes as linhas marcadas são executadas?
"""
linha 1 = 2000
linha 2 = 4.000.000
"""
# c) se a lista tem tamanho 4000, quantas vezes as linhas marcadas são executadas?
"""
linha 1 = 4000
linha 2 = 16.000.000
"""
# d) Qual a complexidade usando a notação O()?
"""
1 + n + n + n + n² + n²
2n² + 3n + 1

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

def funcao7(lista):
    pass


# Exercicio 8:
# Escreva uma função para inverter a ordem dos elementos de uma lista de tamanho n.
# Você não pode usar outro vetor como auxiliar e não deve utilizar funções prontas do python.
# A função deve ter complexidade O(n).

def funcao8(lista):
    pass
