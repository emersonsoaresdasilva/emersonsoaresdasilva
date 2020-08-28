'''Crie um programa que use uma função que receba como parâmetro um lista
de números inteiros. A função deverá retornar o menor item da lista.

Obs.: A lista deverá ser preenchida pelo usuário no programa principal.
Restrições.: Não use a função min,max, append e insert.

A função deverá ser construída por você.
O preenchimento da lista termina quando o usuário digitar o valor -1.
Há garantia que haverá no máximo 10 itens.
'''
#========================================
#    FUNÇÃO MÍNIMO DE UMA LISTA (WHILE)
#========================================

def minimo_while(lista, tamanho):
    minimo = lista[0] #Recebendo o primeiro item da lista.
    i = 1 #Recebendo 1 porque o item 0 já foi usado anteriormente.
    while indice < tamanho:
        if lista[indice]:
            minimo = lista[indice]
        indice += 1
    return minimo #Menor item da lista.

#=======================================
#    FUNÇÃO MÍNIMO DE UMA LISTA (FOR)
#========================================

def minimo_for(lista, tamanho):
    minimo = lista[0] #Recebendo o primeiro item da lista.
    for i in range(1, tamanho):
        if lista[i] < minimo:
            minimo = lista[i]
    return minimo #Menor item da lista.

#=======================================
#          PROGRAMA PRINCIPAL
#========================================

lista = 10 * [0] #Criando lista com tamanho exato.
indice = 0
x = int(input('Valor: ')) #X[indice] = int(input())

while x != -1:
    lista[indice] = x #Armazenando X na lista manualmente, sem append/insert.
    indice += 1 #Servindo para contar quantos itens foram contados.
    x = int(input('Valor: '))
print('Valor mínimo:',minimo_for(lista,indice)) #Chamando a função para mostrar o mínimo.
    
