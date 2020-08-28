'''
Crie uma função que receba como parâmetro um vetor V e o seu tamanho N.
A função deverá INVERTER a sequência de itens de v, sem usar um vetor auxiliar.
'''
def preenche(v, n):
    for i in range(n):
        v[i] = int(input('Vetor[%d]: ' % i))

def exibe(v, n):
    for i in range(n):
        print(v[i], end=' ')
    print()

def troca(v, i, j): #trocando i com j
    temp = v[i] #temp não tem nada, mas recebeu v[i].
    v[i] = v[j] #v[i] recebeu v[j].
    v[j] = temp #v[j] recebeu valor de v[i], ta feito a troca.

def troca2(v, i, j):
    v[i], v[j] = v[j], v[i]

def inverte(v, n):
    i = 0
    j = n - 1
    while i < j:
        troca(v, i, j)
        i += 1
        j -= 1
    
v = [10,20,30,40,50,60]
troca(v, 1, 5)
exibe(v, 6)
