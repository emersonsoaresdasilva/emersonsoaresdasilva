#-----------------------------
#          FUNÇÕES
#-----------------------------
def exibe(v, n):
    for i in range(n):
        print(v[i], end=' ')
    print()

def troca(v, i, j):
    temp = v[i]
    v[i] = v[j]
    v[j] = temp

def empurra(v, n):
    i = 0
    while i < n - 1:
        if v[i] > v[i+1]:
            troca(v, i, i+1)
        i += 1

def empurra_for(v, n):
    for i in range(n-1): #[0...n-1[
        if v[i] > v[i+1]:
            troca(v, i, i+1)
        i += 1

def bubble_sort(v, n): #Faz o mesmo papel do .sort()
    tamanho = n
    while tamanho > 1:
        empurra(v, tamanho)
        tamanho -= 1
'''      
#     0  1   2  3  4  5  6
v = [23,-77,96,45,15,21,13] #Tamanho do vetor: 7
#     i, i+1

exibe(v, 7)
empurra(v, 7)
exibe(v, 7)
'''
