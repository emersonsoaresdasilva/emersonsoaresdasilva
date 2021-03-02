#--------------------------------------------
#https://wiki.python.org/moin/TimeComplexity
#--------------------------------------------
#                Algoritmo 01
#           O(1) - Tempo constante
#--------------------------------------------
x = 1                               # 1
y = 3                               # 1
z = 4                               # 1
lista = [1,2,3,4,..., 1000000]      # 1

#--------------------------------------------
#               Algoritmo 02
#           O(1) - Tempo constante
#--------------------------------------------
lista = [2,3,4,5,6,7,..., 10000]    # 1
x = lista[999]                      # 1

#--------------------------------------------
#               Algoritmo 03
#           O(1) - Tempo constante
#--------------------------------------------
print(lista[1])                     # 1

#--------------------------------------------
#               Algoritmo 04
#       O(n) - Tempo de execução, depende
#           do tamanho da lista
#--------------------------------------------
lista = [1,2,3,... n]
x = 10
print(lista, x)                     # n

#--------------------------------------------

#--------------------------------------------
# Algoritmo 05.
# O(1) - Tempo constante.
lista[1] = 10                       # 1
lista.append(30)                    # 1

#--------------------------------------------
#               Algoritmo 06
#       O(n) - Tempo de execução, depende
#           do tamanho da lista
#--------------------------------------------
lista.insert(0, 100)
# Uma única instrução, por exemplo, "insert()" pode mudar todo o tempo de execução.

def teste(n):
    lista = list(range(n))          # 1
    lista.append(100)               # 1
    lista.insert(0, 100)            # n
    
#--------------------------------------------
#               Algoritmo 07
#       O(n) - Tempo de execução, depende
#           do tamanho da lista
#--------------------------------------------

i = 0                               # 1
while i < len(lista):               # n
    print(lista[i])                 # n
    i += 1                          # n

#--------------------------------------------
#               Algoritmo 08
#           O(1) - Tempo constante
#--------------------------------------------
tamanho_da_lista = 5

i = len(lista)                      # 1
while i < len(lista):               # 1 - O while nunca será executado.
    print(lista[i])                 # 0
    i += 1                          # 0

#--------------------------------------------
#               Algoritmo 09
#       O(n) - Tempo de execução, depende
#           do tamanho da lista
#--------------------------------------------
x = 0                               # 1
for i in range(3):                  # n
    x += 1                          # n

#--------------------------------------------
#               Algoritmo 10
#       O(n) - Tempo de execução, depende
#           do tamanho da lista
#--------------------------------------------
n = len(lista)                      # 1
x = 0                               # 1
for i in range(5, n):               # n-5
    x += 1                          # n-5
'''
1 + 1 + n-5 + n-5
2 + 2*(n-5)
2n -10 + 2
4n - 8
'''
O(n)

#--------------------------------------------
#               Algoritmo 11
#       O(n²) - Loop dentro do outro.
#--------------------------------------------
for i in range(n):                  # n
    for j in range(n):              # n * n --> n²
        x = 1                       # n * n --> n²
'''
n + n² + n²
2n² + n
2n²
n²
'''
O(n²)

#--------------------------------------------
#               Algoritmo 12
#       O(n²) - Loop dentro do outro.
#--------------------------------------------
i = 0                               # 1
while i < len(lista):               # n
    print(lista)                    # n * n --> n² | Acessa cada índice da lista para exibir, mesma coisa que um for.
    i += 1                          # n
'''
1 + 2n + n²
n²
'''
O(n²)

#--------------------------------------------
#               Algoritmo 13
#       O(n²) - Loop dentro do outro.
#--------------------------------------------
i = 0                               # 1
for i in range(n):                  # n
    for j in range(n):              # n * n     --> n²
        for k in range(n):          # n * n * n --> n³
            i += 1                  # n * n * n --> n³
'''
1 + n + n² + 2n³
2n³
n³
'''
O(n³)
