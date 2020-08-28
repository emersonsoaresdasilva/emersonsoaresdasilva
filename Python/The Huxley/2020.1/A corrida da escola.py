def converter(lista):
    for indice in range(len(lista)):
        lista[indice] = int(lista[indice])
    return lista

def soma(lista):
    soma = 0
    for indice in range(len(lista)):
        soma += lista[indice]
    return soma

N, M = input().split()

N = int(N)
M = int(M)
menor = 1000000 * 101

for i in range(1, N+1): #Iniciando o i em 1.
    voltas = input().split()
    voltas = converter(voltas)
    total = sum(voltas)
    if total < menor:
        menor = total
        competidor = i
print(competidor)