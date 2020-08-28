# Escreva a funcao media_pares_impares(lista) abaixo:
def media_pares_impares(lista):
    soma_pares = 0
    soma_impares = 0
    qtd_pares = 0
    qtd_impares = 0
    for i in range(len(lista)):
        if lista[i] % 2 == 0:
            soma_pares += lista[i]
            qtd_pares += 1
        else:
            soma_impares += lista[i]
            qtd_impares += 1
    print(soma_pares/qtd_pares)
    print(soma_impares/qtd_impares)
    

# Programa principal (ja implementado, voce nao precisa se preocupar com o codigo partir deste ponto)
'''
lista = eval(input())
media_pares_impares(lista)
'''
